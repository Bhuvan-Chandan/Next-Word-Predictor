# 🧠 Next-Word Prediction Language Learning Tool

This is a full-stack AI-powered web application that predicts the **next word** in a sentence. It helps users learn English in an interactive and engaging way.

- 🔤 Built using a **deep learning model** trained on English sentence data.
- ⚙️ Backend built with **Flask + TensorFlow**
- 🌐 Frontend built with **React** (with dark mode, animations, and mobile responsiveness)

---

## 📁 Project Structure

```
Next-Word Prediction Language Learning Tool/
│
├── backend/
│   ├── .venv/                   # Python virtual environment
│   ├── data/
│   │   └── sentences.csv        # Dataset (ignored in git)
│   ├── model/
│   │   └── model.h5             # Trained Keras model (ignored in git)
│   ├── app.py                   # Flask backend
│   ├── train_model.py           # Script to train model
│   └── tokenizer.pkl            # Tokenizer saved after training
│
├── frontend/
│   ├── node_modules/            # Dependencies (ignored in git)
│   ├── public/                  # Public assets
│   ├── src/
│   │   ├── components/
│   │   │   └── Predictor.jsx    # Main prediction component
│   │   ├── App.js               # Main React component
│   │   ├── App.css              # Styling with animations
│   │   └── index.js             # React entry point
│   ├── package.json             # NPM metadata
│   └── .gitignore               # Node-related ignore rules
│
└── README.md
```

---

## 🚀 Features

- 🧠 **Next-Word Prediction** using a deep learning model
- 🌙 **Dark Mode Toggle**
- 📱 **Mobile Responsive UI**

---

## 🧑‍💻 Getting Started

### 1️⃣ Clone the repo

```bash
git clone https://github.com/your-username/next-word-prediction-app.git
cd next-word-prediction-app
```

---

### 2️⃣ Setup the Backend

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate          # (Use source .venv/bin/activate on Mac/Linux)
pip install -r requirements.txt
```

#### ✅ Train the model (optional if already trained):

```bash
python train_model.py
```

#### ▶️ Run the Flask server:

```bash
python app.py
```

This starts the backend at: `http://127.0.0.1:5000`

---

### 3️⃣ Setup the Frontend

```bash
cd frontend
npm install
npm start
```

Open your browser at: `http://localhost:3000`

---

## 🔄 Example Usage

- Type a sentence like:  
  `how are you`  
  Click **"Predict Next Word"**  
  → App responds with: `doing`

---

## 📦 Dependencies

### Backend

- Flask
- TensorFlow / Keras
- NumPy
- Pickle (for tokenizer)

### Frontend

- React
- Axios
- CSS Animations

---

## 🙈 .gitignore Summary

### In `/backend/.gitignore`
```
.venv/
model/
data/
__pycache__/
*.pyc
```

### In `/frontend/.gitignore`
```
node_modules/
build/
.env
```

---

## 🧠 Model Training (Optional)

If you want better predictions:

- Train on a **larger dataset** (100k+ lines)
- Add dropout or validation split
- Save checkpoints every few epochs
- Clean dataset for grammar/length

---


---

## 🌐 Deployment (Optional)

- Host Flask backend: **Render / Railway / Heroku**
- Host React frontend: **Vercel / Netlify / GitHub Pages**
- Add CORS config in `app.py` for production domains

---

## 🧑‍🏫 Ideal For

- Language learning tools
- Typing practice enhancements
- AI + frontend projects
- Student portfolio demos

---

## 🙋‍♂️ Author

Built by Bhuvan Chandan N A 

GitHub: https://github.com/bhuvan726

---