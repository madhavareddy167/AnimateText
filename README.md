<p align="center">
  <img src="A_2D_digital_graphic_banner_image_for_%22EmotionSpar.png" alt="AnimateText Banner" width="800"/>
</p>

<h1 align="center">🎨 AnimateText</h1>

<p align="center">
  Transforming text to visual expressions using emotion-aware intelligence.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.8+-blue?style=flat-square&logo=python">
  <img src="https://img.shields.io/badge/status-active-brightgreen?style=flat-square">
  <img src="https://img.shields.io/badge/license-MIT-lightgrey?style=flat-square">
  <img src="https://img.shields.io/badge/dataset-emotion--labeled%20CSV-orange?style=flat-square">
</p>

---

## ✨ Features

- 🧠 **Emotion Detection** – Classifies text into Joy, Sadness, Anger, Surprise, Fear, or Neutral
- 🎥 **Text-to-Visual Flow** – Converts emotional text into expressive output (foundation ready for animation layer)
- 📊 **Dataset-Driven** – Works with real labeled CSV files to learn emotional intent
- 🔌 **ML/API Ready** – Can be extended into ML models or deployed as a Flask API

---

## 🛠 Tech Stack

| Layer         | Technology          |
|---------------|---------------------|
| Backend       | Python 3.8+         |
| Data Handling | Pandas, CSV         |
| Dataset       | Emotion CSVs, TGIF  |
| (Optional) API| Flask               |
| Tools         | VS Code, Jupyter    |

---

## 📁 Dataset Files

| File Name              | Description                   |
|------------------------|-------------------------------|
| `joy_sentences.csv`      | Sentences labeled as Joy      |
| `sadness_sentences.csv`  | Sentences labeled as Sadness  |
| `anger_sentences.csv`    | Sentences labeled as Anger    |
| `fear_sentences.csv`     | Sentences labeled as Fear     |
| `surprise_sentences.csv` | Sentences labeled as Surprise |
| `neutral_sentences.csv`  | Sentences labeled as Neutral  |
| `tgif-v1.0.tsv`          | TGIF dataset (optional)       |

---

## 🚀 Example Usage

```python
import pandas as pd

df = pd.read_csv("joy_sentences.csv")
print(df.sample(5))
