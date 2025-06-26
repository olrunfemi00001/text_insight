from flask import Flask, request, jsonify
import spacy
from textblob import TextBlob
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

nlp = spacy.load("en_core_web_sm")

app = Flask(__name__)

def summarize_text(text, sentence_count=2):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentence_count)
    return " ".join([str(sentence) for sentence in summary])

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "Text is required"}), 400

    # Sentiment
    sentiment = TextBlob(text).sentiment.polarity
    sentiment_label = "Positive" if sentiment > 0 else "Negative" if sentiment < 0 else "Neutral"

    # Entities
    doc = nlp(text)
    entities = list(set([ent.text for ent in doc.ents]))

    # Summary
    summary = summarize_text(text)

    # Keywords (nouns and proper nouns)
    keywords = list(set([token.text for token in doc if token.pos_ in ["NOUN", "PROPN"] and not token.is_stop]))

    return jsonify({
        "sentiment": sentiment_label,
        "entities": entities,
        "summary": summary,
        "keywords": keywords
    })

if __name__ == '__main__':
    app.run(debug=True)
