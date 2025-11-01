import spacy
import streamlit as st
from spacy import displacy

st.set_page_config(page_title="NER Visualizer", page_icon="🧠", layout="wide")

st.markdown("""
    <style>
        .main {
            background-color: #0e1117;
            color: #ffffff;
            font-family: 'Segoe UI', sans-serif;
        }
        .title {
            text-align: center;
            font-size: 40px;
            font-weight: 700;
            margin-bottom: 0;
        }
        .subtitle {
            text-align: center;
            color: #9aa0a6;
            font-size: 18px;
            margin-bottom: 40px;
        }
        .stTextArea textarea {
            background-color: #1e1e1e !important;
            color: #ffffff !important;
            font-size: 16px !important;
            border-radius: 10px;
        }
        .entity {
            background-color: #1e293b;
            padding: 8px 12px;
            border-radius: 10px;
            margin: 4px 0;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='title'>🧠 Named Entity Recognition</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Highlighting people, organizations, locations, and more</p>", unsafe_allow_html=True)

nlp = spacy.load("en_core_web_sm")
ruler = nlp.add_pipe("entity_ruler", before="ner")
patterns = [
    {"label": "ORG", "pattern": "OpenAI"},
    {"label": "PRODUCT", "pattern": "ChatGPT"},
    {"label": "ORG", "pattern": "Tesla"},
    {"label": "PERSON", "pattern": "Elon Musk"},
]
ruler.add_patterns(patterns)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    text = st.text_area("✍️ Enter your text below", "", height=180)

center_button = st.columns([2.7, 1, 2.7])[1]
with center_button:
    analyze = st.button("🔍 Analyze Text", use_container_width=True)

if analyze:
    if text.strip() == "":
        st.warning("Please enter some text to analyze.")
    else:
        doc = nlp(text)
        html = displacy.render(doc, style="ent", page=False)
        st.markdown("<hr>", unsafe_allow_html=True)
        st.subheader("🧩 Entities Highlighted in Text")
        st.markdown(f"<div style='background-color:#111;border-radius:10px;padding:15px;'>{html}</div>", unsafe_allow_html=True)

        if not doc.ents:
            st.warning("No entities found in the text.")
        else:
            st.markdown("<br>", unsafe_allow_html=True)
            st.subheader("📋 Extracted Entities")
            for ent in doc.ents:
                st.markdown(f"<div class='entity'>✨ <b>{ent.text}</b> → <code>{ent.label_}</code></div>", unsafe_allow_html=True)
