from flask import Flask, render_template, request, jsonify
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Load the sentence-transformers model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load emotion DataFrames and embeddings
# emotion_dfs = pd.read_pickle("emotion_dfs/emotion_dfs.pkl")
emotion_embeddings = {}
emotions = ['anger', 'neutral', 'joy', 'fear', 'surprise', 'sadness']

import pandas as pd

# Define the list of CSV filenames (replace these with your actual filenames)
csv_files = [
    "anger_sentences.csv",  # Replace with the actual file name
    "neutral_sentences.csv",  # Replace with the actual file name
    "joy_sentences.csv",  # Replace with the actual file name
    "fear_sentences.csv",  # Replace with the actual file name
    "surprise_sentences.csv",  # Replace with the actual file name
    "sadness_sentences.csv"  # Replace with the actual file name
]

# Dictionary to store separate DataFrames for each emotion
emotion_dfs = {}

# Loop through the files and load them into separate DataFrames
for file in csv_files:
    # Extract the emotion name from the file name (assumes the format is <emotion>_sentences.csv)
    emotion_name = file.split('_')[0]

    # Load the CSV file into a DataFrame
    df = pd.read_csv(file)

    # Add a new column 'emotion' to the DataFrame with the emotion name
    df['emotion'] = emotion_name

    # Store the DataFrame in the dictionary with the emotion name as the key
    emotion_dfs[emotion_name] = df

for emotion in emotions:
    try:
        embeddings = np.load(f"emotion_dfs/{emotion}_embeddings.npy")
        emotion_embeddings[emotion] = embeddings
    except FileNotFoundError:
        print(f"Error: {emotion}_embeddings.npy not found.")

# Load the TGIF dataset
tgif_df = pd.read_csv('tgif-v1.0.tsv', sep='\t')
tgif_df.rename(columns={tgif_df.columns[0]: 'link', tgif_df.columns[1]: 'sentence'}, inplace=True)

def find_most_similar_sentence(emotion, query_sentence):
    query_embedding = model.encode([query_sentence])
    emotion_embedding = emotion_embeddings[emotion]
    similarities = cosine_similarity(query_embedding, emotion_embedding)
    
    most_similar_idx = similarities.argmax()
    best_sentence = emotion_dfs[emotion]['Sentence'].iloc[most_similar_idx]
    best_score = similarities[0][most_similar_idx]

    # Normalize the sentence to avoid issues with small variations
    best_sentence_normalized = best_sentence.strip().lower()
    query_sentence_normalized = query_sentence.strip().lower()

    print(f"Normalized query: '{query_sentence_normalized}'")
    print(f"Normalized best sentence: '{best_sentence_normalized}'")

    return best_sentence, best_score

@app.route("/")  # @app.route is a decorator used in web frameworks like flask to bind URL to specific function 
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    query_sentence = request.form.get("user_input")
    response = {"error": "No matching emotion found.", "gif_url": ""}

    try:
        best_emotion = None
        best_sentence = None
        best_score = 0.0

        for emotion in emotions:
            similar_sentence, score = find_most_similar_sentence(emotion, query_sentence)
            
            # Debugging print to check the sentences being compared
            print(f"Comparing '{query_sentence}' to '{similar_sentence}' with score {score}")
            
            # Only update if the new score is higher
            if score > best_score:
                best_emotion = emotion
                best_sentence = similar_sentence
                best_score = score

        if best_sentence:
            # Convert score to native float
            best_score = float(best_score)

            # Debugging print to check the best sentence and score
            print(f"Best sentence: '{best_sentence}' with score: {best_score}")

            # Find the GIF link from the TGIF dataset
            matching_row = tgif_df[tgif_df['sentence'].str.strip().str.lower() == best_sentence.strip().lower()]
            if not matching_row.empty:
                gif_url = matching_row['link'].values[0]
                response = {
                    "emotion": best_emotion,
                    "sentence": best_sentence,
                    "gif_url": gif_url,
                    "score": best_score
                }
            else:
                response["error"] = "No matching GIF found for the sentence."

    except Exception as e:
        response["error"] = str(e)

    return jsonify(response)

if __name__== "__main__":
    app.run(debug=True) 