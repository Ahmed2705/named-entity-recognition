import spacy
import pandas as pd
def load_conll_data(filepath):
    sentences = []
    sentence = []

    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()


            if not line:
                if sentence:
                    sentences.append(sentence)
                    sentence = []
                continue

            parts = line.split()
            if len(parts) >= 2:
                word, tag = parts[0], parts[-1]
                sentence.append((word, tag))

    if sentence:
        sentences.append(sentence)

    return sentences


train_data = load_conll_data("train.txt")
valid_data = load_conll_data("valid.txt")
test_data = load_conll_data("test.txt")

print(f"Loaded {len(train_data)} training sentences.")
print(f"Loaded {len(valid_data)} validation sentences.")
print(f"Loaded {len(test_data)} test sentences.\n")

train_texts = [" ".join([word for word, tag in sent]) for sent in train_data]
valid_texts = [" ".join([word for word, tag in sent]) for sent in valid_data]
test_texts = [" ".join([word for word, tag in sent]) for sent in test_data]

print("Example from training set:")
print(train_texts[0])
print("-" * 60)

print("Loading spaCy English model...")
nlp = spacy.load("en_core_web_sm")
print("spaCy model loaded successfully!\n")

ruler = nlp.add_pipe("entity_ruler", before="ner")

patterns = [
    {"label": "ORG", "pattern": "StarLink"},
    {"label": "PRODUCT", "pattern": "CyberTruck"},
    {"label": "ORG", "pattern": "Tesla"},
    {"label": "PERSON", "pattern": "Elon Musk"},
]
ruler.add_patterns(patterns)

print("Added custom rule-based patterns.\n")

print("Running NER on sample sentences...\n")
results = []

for text in train_texts[:10]:
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    results.append({"text": text, "entities": entities})

    print(f"Text: {text}")
    print(f"Entities: {entities}")
    print("-" * 80)


df = pd.DataFrame(results)
df.to_csv("ner_output.csv", index=False)
print("\nResults saved to 'ner_output.csv'")

print("\nNER Pipeline Completed Successfully!")
