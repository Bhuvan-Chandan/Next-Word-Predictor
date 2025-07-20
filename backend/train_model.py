import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
#from sklearn.model_selection import train_test_split
import pickle

# Exit early if model already exists
if os.path.exists("model/model.h5"):
    print("⚠️ Model already exists. Delete it manually to retrain.")
    exit()

  

# Load dataset
with open("data/sentences.csv", "r", encoding="utf-8") as f:
    lines = f.readlines()

    # Print a few lines to debug
print("Sample lines from dataset:")
print(lines[:5])  

# Use a smaller dataset for now
#lines = lines[:10000]

# Extract English sentences
texts = [
    parts[2].strip().lower()
    for line in lines
    if (parts := line.strip().split("\t")) and len(parts) > 2 and parts[1] == "eng"
][:50000]

import re
texts = [re.sub(r"[^\w\s']","",text) for text in texts]


print(f"Total cleaned sentences: {len(texts)}")
if not texts:
    print("❌ No valid English sentences found.")
    exit()



# Tokenize
tokenizer = Tokenizer(num_words=5000, oov_token="<OOV>")
tokenizer.fit_on_texts(texts)

# Save tokenizer
with open("tokenizer.pkl", "wb") as f:
    pickle.dump(tokenizer, f)

# Create input sequences
input_sequences = []
for line in texts:
    token_list = tokenizer.texts_to_sequences([line])[0]
    for i in range(1, len(token_list)):
        n_gram_seq = token_list[:i+1]
        input_sequences.append(n_gram_seq)

# Pad sequences
max_seq_len = max(len(seq) for seq in input_sequences)
input_sequences = pad_sequences(input_sequences, maxlen=max_seq_len, padding='pre')

# Separate features and labels
input_sequences = np.array(input_sequences)
X = input_sequences[:, :-1]
y = input_sequences[:, -1]  # Use integer labels directly

# Model
model = Sequential()
model.add(Embedding(5000, 100, input_length=max_seq_len - 1))
model.add(LSTM(150))
model.add(Dense(5000, activation='softmax'))

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train
model.fit(X, y, epochs=30, batch_size=128, verbose=1)

# Save model
os.makedirs("model", exist_ok=True)
model.save("model/model.h5")
print("✅ Training completed and model saved as model/model.h5")
