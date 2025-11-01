# 🧠 Named Entity Recognition (NER) using spaCy & Streamlit

This project implements a **Named Entity Recognition (NER)** pipeline using **spaCy**, one of the most powerful Natural Language Processing libraries in Python.
It can automatically identify key information in text — such as **people, organizations, locations, dates, and products** — and display them interactively using a **Streamlit-based web app**.

The goal of this project is to demonstrate how to process raw text, extract named entities, and visualize them in a clean, intuitive interface suitable for both research and real-world applications.

---

## 📚 Table of Contents

1. [✨ Overview](#-overview)
2. [🚀 Features](#-features)
3. [📂 Project Structure](#-project-structure)
4. [⚙️ Installation](#%EF%B8%8F-installation)
5. [🧠 Usage](#-usage)
6. [💬 Example Input & Output](#-example-input--output)
7. [🏷️ Entity Label Reference](#%EF%B8%8F-entity-label-reference)
8. [📈 Dataset Information](#-dataset-information)
9. [🎨 Streamlit GUI Overview](#-streamlit-gui-overview)
10. [🧩 Future Improvements](#-future-improvements)
11. [🤝 Contributing](#-contributing)
12. [📜 License](#-license)
13. [👨‍💻 Author](#-author)

---

## ✨ Overview

**Named Entity Recognition (NER)** is a crucial task in Natural Language Processing (NLP).
It involves identifying real-world objects in text — like names of people, organizations, locations, times, quantities, and more — and classifying them into predefined categories.

In this project:

* We use **spaCy** to perform entity recognition.
* We add **custom rule-based patterns** using spaCy’s `EntityRuler`.
* We visualize the output interactively through a **Streamlit** web interface.

This project combines **machine learning**, **linguistic rules**, and **data visualization** in one complete pipeline.

---

## 🚀 Features

✅ Parses CoNLL-style text datasets (`train.txt`, `valid.txt`, `test.txt`)
✅ Uses pre-trained `en_core_web_sm` spaCy model
✅ Adds **custom rule-based entities** (e.g., StarLink, CyberTruck, Tesla, Elon Musk)
✅ Exports detected entities into a CSV file (`ner_output.csv`)
✅ Includes a **beautiful Streamlit GUI** for interactive entity recognition
✅ Clean, minimal, and responsive design for easy testing

---

## 📂 Project Structure

```
NLP-Task4/
├── main.py              # Core NER script for processing and exporting results
├── app.py               # Streamlit GUI for interactive entity recognition
├── train.txt            # Training dataset (CoNLL format)
├── valid.txt            # Validation dataset
├── test.txt             # Testing dataset
├── ner_output.csv       # Output of recognized entities
├── requirements.txt     # Required Python packages
└── README.md            # Project documentation
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Ahmed2705/named-entity-recognition.git
cd named-entity-recognition
```

### 2️⃣ (Optional) Create a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate     # On Windows
source venv/bin/activate  # On macOS/Linux
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

---

## 🧠 Usage

### ▶️ Run the Main Script

```bash
python main.py
```

This will:

* Load your dataset
* Run the NER pipeline
* Display recognized entities
* Save them to a CSV file (`ner_output.csv`)

### 🖥️ Launch the Streamlit Web App

```bash
streamlit run predict.py
```

Then open the provided local URL (usually `http://localhost:8501`) in your browser.
You can now input any sentence and instantly visualize all detected entities in a clean, interactive way.

---

## 💬 Example Input & Output

**Input:**

> Apple Inc. was founded by Steve Jobs and Steve Wozniak in California in 1976.

**Output:**

| Entity        | Label  |
| ------------- | ------ |
| Apple Inc.    | ORG    |
| Steve Jobs    | PERSON |
| Steve Wozniak | PERSON |
| California    | GPE    |
| 1976          | DATE   |

---

## 🏷️ Entity Label Reference

| Label       | Description                                          |
| ----------- | ---------------------------------------------------- |
| PERSON      | Names of people, including fictional characters      |
| ORG         | Companies, agencies, institutions                    |
| GPE         | Geopolitical entities (countries, cities, states)    |
| LOC         | Non-political locations (mountains, rivers, regions) |
| PRODUCT     | Product names                                        |
| EVENT       | Named events (wars, sports, conferences)             |
| WORK_OF_ART | Titles of creative works (books, songs, movies)      |
| LANGUAGE    | Names of languages                                   |
| DATE        | Absolute or relative dates/times                     |
| TIME        | Times smaller than a day                             |
| MONEY       | Monetary values                                      |
| PERCENT     | Percentage expressions                               |
| CARDINAL    | Numerals that are not ordinal                        |
| ORDINAL     | “First”, “second”, etc.                              |

---

## 📈 Dataset Information

This project is compatible with **CoNLL-style datasets**, where each line represents:

```
Word  POS-tag  Chunk-tag  Entity-tag
```

Example:

```
Elon  NNP  B-NP  B-PERSON
Musk  NNP  I-NP  I-PERSON
founded  VBD  B-VP  O
OpenAI  NNP  B-NP  B-ORG
```

Each sentence is separated by a blank line.
This format allows the model to learn which words correspond to named entities.

---

## 🎨 Streamlit GUI Overview

The Streamlit interface provides:

* A **clean input box** for typing or pasting text
* An automatic display of detected entities with their labels
* A responsive design suitable for desktop and mobile
* Real-time NLP inference using the spaCy model

It’s perfect for demonstrations, NLP testing, or showcasing projects interactively.

---

## 🧩 Future Improvements

* Train a custom NER model using the provided dataset instead of using spaCy’s pre-trained model
* Add precision, recall, and F1-score evaluation metrics
* Visualize entities directly on the text using color-coded highlights
* Deploy the Streamlit app publicly using **Streamlit Cloud**, **Hugging Face Spaces**, or **Render**

---

## 🤝 Contributing

Contributions are welcome!
If you’d like to improve the interface, enhance the model, or expand the dataset, feel free to:

1. Fork this repository
2. Create a new branch (`feature-improvement`)
3. Commit your changes
4. Open a Pull Request

---

## 📜 License

This project is open-source and available under the **MIT License**.
You are free to use, modify, and distribute it with attribution.

