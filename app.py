from flask import Flask, request, jsonify
from transformers import BertTokenizer, BertForSequenceClassification
import torch

# Paths to model and tokenizer
MODEL_PATH = "./saved_model"
model = BertForSequenceClassification.from_pretrained(MODEL_PATH)  # No from_safetensors argument needed
tokenizer = BertTokenizer.from_pretrained(MODEL_PATH)

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        if "text" not in data:
            return jsonify({"error": "No text provided"}), 400

        # Tokenize input text
        inputs = tokenizer(
            data["text"],
            return_tensors="pt",
            max_length=128,
            truncation=True,
            padding="max_length"
        )

        # Perform inference
        model.eval()
        with torch.no_grad():
            outputs = model(**inputs)
            logits = outputs.logits
            predicted_class = logits.argmax(dim=-1).item()

        return jsonify({"predicted_class": predicted_class})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
