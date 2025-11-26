@Summary...........

# Bowling Score Calculator

A web-based bowling score calculator built using **Python (Flask)** for the backend
and **HTML + JavaScript** for the frontend.

This project demonstrates how to implement business logic, handle user input,
and connect frontend interaction with backend processing in a web application.
---

##  Features
- Input scores for all 10 frames of a bowling game  
- Handles strikes, spares, and open frames based on official bowling rules  
- Automatically calculates final score  
- User-friendly web interface  
- Lightweight Flask-based backend  

---

## Tech Stack

- **Backend:** Python (Flask)  
- **Frontend:** HTML, JavaScript  
- **Tools:** Git, GitHub

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

## What This Project Demonstrates

- Implementing real-world logic (bowling rules) in code
- Handling front-end user input in a structured way
- Building a simple web application using Flask
- Connecting UI events with backend computation
- Organizing a mini full-stack project

## Future Enhancements

- Add CSS styling for a better UI.

- Auto-disable second input on strikes.

- Display individual frame scores.

- Save games in a database (SQLite/Postgres).

- Deploy to Heroku/Render for public access.


## Contributing
Pull requests are welcome. For major changes, open an issue first to discuss.

## License
MIT © 2025 Sowmya Businayani
