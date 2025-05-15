# AnimateText: Transforming Text to Visual Expressions <img src="https://img.icons8.com/emoji/48/performing-arts.png" alt="Icon" width="24" height="24">

<p align="center">
  <img src="AnimateText_Banner.png" alt="AnimateText Banner" style="width:70%; height:auto;">
</p>

[![Python Version](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square)](https://www.python.org/)
[![Dataset](https://img.shields.io/badge/Dataset-Labeled%20CSV-orange?style=flat-square)]()
[![NLP](https://img.shields.io/badge/NLP-Text%20Classification-lightgrey?style=flat-square)]()
[![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)]()
[![License](https://img.shields.io/badge/License-MIT-lightgrey?style=flat-square)]()

---

An intelligent sentiment and emotion recognition system built in Python that classifies emotional tone from input text and maps it to a corresponding emotional category such as joy, anger, fear, sadness, surprise, and neutrality.

---

## ✨ Features

- 🎭 **Emotion Detection**: Detects and classifies emotional tone from raw input text
- 📊 **Dataset Driven**: Supports CSV-based emotion-tagged sentence files
- 🧠 **Expandable**: Ideal for building ML models or integrating into Flask APIs
- 🖼️ **Visual Layer Ready**: Lays the foundation for animating expressions based on detected emotion

---

## 🛠 Tech Stack

| Component        | Technology       |
|------------------|------------------|
| Programming      | Python 3.8+       |
| Data Processing  | Pandas, CSV       |
| Optional API     | Flask             |
| Development IDE  | VS Code / Jupyter |

---

## 📋 Prerequisites

- Python ≥ 3.8 installed
- Run `pip install pandas flask` to get dependencies
- (Optional) Flask for API integration

---

## 📁 Data Structure

| Filename               | Emotion Label       |
|------------------------|---------------------|
| `joy_sentences.csv`     | Joy                 |
| `sadness_sentences.csv` | Sadness             |
| `anger_sentences.csv`   | Anger               |
| `fear_sentences.csv`    | Fear                |
| `surprise_sentences.csv`| Surprise            |
| `neutral_sentences.csv` | Neutral             |
| `tgif-v1.0.tsv`         | External (optional) |

---

## 🚀 Example Code

```python
import pandas as pd

df = pd.read_csv("surprise_sentences.csv")
print(df.sample(3))

## Acknowledgements 😇

- 💡 Open-source contributors and dataset curators for providing emotion-labeled sentence corpora  
- 🧠 Python and Pandas communities for enabling seamless text and data processing  
- 🎨 Creative AI pioneers for inspiring emotion-to-visual expression research  
- 🔧 Flask developers and the open Python ecosystem for API extensibility  
- ❤️ The open-source community for fostering innovation and collaboration
