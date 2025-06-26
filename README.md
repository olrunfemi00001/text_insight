# Text Insight API

**Text Insight API** is a lightweight and intelligent Flask-based NLP API that analyzes raw text input and returns:
- Sentiment (Positive, Negative, Neutral)
- Named Entities (e.g., people, organizations, locations)
- Summary of the input text
- Extracted Keywords

This API is ideal for projects that require basic Natural Language Processing capabilities via RESTful endpoints.

---

## Live Demo
(Add your live URL here after deployment, e.g. https://text-insight.onrender.com/analyze)

---

## Features

- Sentiment Analysis using TextBlob  
- Named Entity Recognition (NER) with spaCy  
- Text Summarization using Sumy (LSA-based)  
- Keyword Extraction from nouns and proper nouns  
- REST API built with Flask  
- Easy to deploy and integrate

---

## Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/text-insight-api.git
   cd text-insight-api
````

2. Set up your virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the server:

   ```bash
   python app.py
   ```

---

## API Usage

### Endpoint:

```
POST /analyze
```

### Request Body (JSON):

```json
{
  "text": "Elon Musk announced a new SpaceX launch from Texas next month."
}
```

### Example Response:

```json
{
  "sentiment": "Neutral",
  "entities": ["Elon Musk", "SpaceX", "Texas", "next month"],
  "summary": "Elon Musk announced a new SpaceX launch from Texas next month.",
  "keywords": ["Elon Musk", "SpaceX", "Texas", "launch"]
}
```

---

## Dependencies

* Flask
* spaCy
* TextBlob
* Sumy
* Gunicorn (for deployment)
* en\_core\_web\_sm (spaCy model)

---

## Use Cases

* Chatbots and Virtual Assistants
* Text Monitoring and Moderation
* Social Media Analysis
* News Aggregation and Summarization
* Internal Company Tools

---

## Deployment

### Render (Recommended):

* Connect your GitHub repo
* Set Build Command: `pip install -r requirements.txt`
* Set Start Command: `gunicorn app:app`
* Add a `Procfile`:

  ```
  web: gunicorn app:app
  ```

---

## Author

**Daniel Olorunfemi**

* GitHub: [@olrunfemi00001](https://github.com/olrunfemi00001)
* LinkedIn: [Daniel Olorunfemi](https://www.linkedin.com/in/daniel-olorunfemi-500700295/)
* Email: [olorunfemidaniel53@gmail.com](mailto:olorunfemidaniel53@gmail.com)

---

## License

This project is open-source and free to use under the MIT License.

```

---

Let me know when you're ready to upload it to your GitHub repository or if you'd like help customizing it further.
```
