from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle

app = Flask(__name__)
CORS(app)

# Load model and tokenizer
model = load_model("model/model.h5")
with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

max_seq_len = model.input_shape[1]

# Create reverse lookup dict once
reverse_word_index = {index: word for word, index in tokenizer.word_index.items()}
reverse_word_index[0] = "<OOV>"  # Add this to handle unknown predictions

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    seed_text = data.get("text", "").strip().lower()

    if not seed_text:
        return jsonify({"error": "No input text provided."}), 400

    try:
        token_list = tokenizer.texts_to_sequences([seed_text])[0]
        token_list = pad_sequences([token_list], maxlen=max_seq_len - 1, padding="pre")

        prediction = model.predict(token_list)
        predicted_index = np.argmax(prediction, axis=-1)[0]
        predicted_word = reverse_word_index.get(predicted_index, "<unk>")

        print(f"Seed Text: {seed_text}")
        print(f"Token List: {token_list}")
        print(f"Predicted Index: {predicted_index}")
        print(f"Predicted Word: {predicted_word}")

        return jsonify({"next_word": predicted_word})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
