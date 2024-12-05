# Tweet Financial Sentiment Analysis

This repository hosts a sentiment classification web application leveraging a fine-tuned BERT model. It predicts sentiment for input text and classifies it into three categories:

- **Bearish**
- **Bullish**
- **Neutral**

The application is deployed using Docker and hosted on Hugging Face Spaces.

---

## Key Features

- **State-of-the-art NLP**: Fine-tuned BERT model ensures high accuracy in sentiment analysis.
- **User-Friendly Interface**: Built with Flask, styled with custom CSS for a seamless experience.
- **Scalability**: Dockerized deployment for ease of use across environments.
- **Accessibility**: Hosted on Hugging Face Spaces, accessible from anywhere.

---

## Live Demo

Experience the application live at:
➡️ [Hugging Face Space](https://huggingface.co/spaces/Aditya-K-23/Twitter-Financial-Sentiment-Analyst)

---

## Getting Started

### Local Setup

Follow these steps to run the application locally:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/bert-sentiment-classifier.git
   cd bert-sentiment-classifier
   ```

2. **Install Dependencies**

   Ensure Python 3.9+ and Docker are installed on your system.

   - Create a virtual environment:

     ```bash
     python -m venv venv
     source venv/bin/activate  # For Linux/macOS
     venv\Scripts\activate  # For Windows
     ```

   - Install the required libraries:

     ```bash
     pip install -r requirements.txt
     ```

   - Start the Flask app:

     ```bash
     python app.py
     ```

3. **Access the Application**

   Open your browser and navigate to: [http://127.0.0.1:8080](http://127.0.0.1:8080).

---

### Docker Setup

Run the application using Docker:

1. **Build the Docker Image**

   ```bash
   docker build -t bert-sentiment-classifier .
   ```

2. **Run the Docker Container**

   ```bash
   docker run -p 8080:8080 bert-sentiment-classifier
   ```

3. **Access the Application**

   Visit: [http://127.0.0.1:8080](http://127.0.0.1:8080) in your browser.

---

## Model Details

The fine-tuned BERT model (based on `bert-base-uncased`) classifies sentiment into:

- **LABEL_0**: Bearish
- **LABEL_1**: Bullish
- **LABEL_2**: Neutral

These technical labels are mapped to human-readable sentiments in the web application.

---

## REST API

The application also provides a REST API for programmatic access to predictions.

### Endpoint

```http
POST /predict
```

### Example Request

```json
{
  "text": "The market is volatile, and stocks are dropping."
}
```

### Example Response

```json
{
  "predicted_class": "LABEL_0",
  "sentiment": "Bearish"
}
```

---

## Deployment on Hugging Face Spaces

To replicate the deployment:

1. **Create a New Space**

   Set the runtime to `Docker`.

2. **Push the Code**

   ```bash
   git add .
   git commit -m "Initial commit"
   git push
   ```

3. **Build and Deploy**

   The Docker image will automatically build and deploy.

---

## Contributing

Contributions are encouraged!

- **Report Issues**: Open an issue if you encounter bugs or have feature requests.
- **Submit Pull Requests**: Enhance the application with your ideas.
