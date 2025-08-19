@Summary...........

# 🎳 Bowling Score Calculator

A simple web application to calculate bowling scores.  
Built with **Flask (Python)** for the backend and **HTML/JavaScript** for the frontend.

---

## 🚀 Features
- Input bowling scores frame by frame (10 frames).
- Handles strikes, spares, and open frames.
- Calculates the total score based on official bowling rules.
- Simple and lightweight Flask app.

---

## 📂 Project Structure

ScoreCalculator/
│── app.py # Flask backend
│── templates/
│ └── index.html # Frontend UI
│── static/ # (optional) for CSS/JS later
│── README.md # Project documentation



---

## ⚡ Installation & Run

1. Clone the repository:
   ```bash
   git clone https://github.com/sowmyabusinayani/ScoreCalculator.git
   cd ScoreCalculator

2. Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows


3. Install dependencies:

pip install flask


4. Run the app:

python app.py


5. Open in your browser:

http://127.0.0.1:5000

🔮 Future Enhancements

🎨 Add CSS styling for a better UI.

🖱 Auto-disable second input on strikes.

📊 Show per-frame scores as well as total.

💾 Save games in a database (SQLite/Postgres).

🌍 Deploy to Heroku/Render for public access.

🛠 Tech Stack

Backend: Python (Flask)

Frontend: HTML, JavaScript

🤝 Contributing
Pull requests are welcome. For major changes, open an issue first to discuss.

📜 License
MIT © 2025 Sowmya Businayani