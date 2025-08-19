from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


def calculate_bowling_score(rolls: list[int]):
    """
    rolls: flat list of ints (0–10), including any bonus rolls in the 10th frame.
    Returns {"total": int} or {"error": "..."} if input is insufficient.
    """
    try:
        score = 0
        i = 0
        for frame in range(10):
            # make sure we have enough rolls to read
            if i >= len(rolls):
                return {"error": "Not enough rolls provided."}

            # Strike
            if rolls[i] == 10:
                if i + 2 >= len(rolls):
                    return {"error": "Strike needs two bonus rolls."}
                score += 10 + rolls[i + 1] + rolls[i + 2]
                i += 1
            else:
                if i + 1 >= len(rolls):
                    return {"error": "Frame missing second roll."}
                r1, r2 = rolls[i], rolls[i + 1]
                if r1 + r2 == 10:  # Spare
                    if i + 2 >= len(rolls):
                        return {"error": "Spare needs one bonus roll."}
                    score += 10 + rolls[i + 2]
                else:             # Open frame
                    score += r1 + r2
                i += 2

        return {"total": score}
    except Exception:
        return {"error": "Invalid input."}


@app.route("/")
def home():
    # serves templates/index.html
    return render_template("index.html")


@app.route("/score", methods=["POST"])
def score():
    data = request.get_json(silent=True) or {}
    rolls = data.get("rolls", [])
    result = calculate_bowling_score(rolls)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
