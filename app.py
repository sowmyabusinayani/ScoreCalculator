from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


def calculate_bowling_score(rolls):
    # validate
    if not isinstance(rolls, list):
        return {"error": "rolls must be a list"}
    try:
        rolls = [int(r) for r in rolls]
    except Exception:
        return {"error": "rolls must be integers"}
    if any(r < 0 or r > 10 for r in rolls):
        return {"error": "each roll must be between 0 and 10"}

    total = 0
    i = 0
    frames = []

    # Frames 1–9
    for frame in range(1, 10):
        if i >= len(rolls):
            return {"error": "Not enough rolls provided."}

        # Strike
        if rolls[i] == 10:
            if i + 2 >= len(rolls):
                return {"error": "Strike needs two bonus rolls."}
            frame_score = 10 + rolls[i+1] + rolls[i+2]
            frames.append({"frame": frame, "type": "strike",
                          "rolls": [10], "score": frame_score})
            total += frame_score
            i += 1
        else:
            if i + 1 >= len(rolls):
                return {"error": "Frame missing second roll."}
            r1, r2 = rolls[i], rolls[i+1]
            if r1 + r2 > 10:
                return {"error": f"Invalid frame {frame}: pins exceed 10."}
            if r1 + r2 == 10:  # spare
                if i + 2 >= len(rolls):
                    return {"error": "Spare needs one bonus roll."}
                frame_score = 10 + rolls[i+2]
                frames.append({"frame": frame, "type": "spare",
                              "rolls": [r1, r2], "score": frame_score})
                total += frame_score
                i += 2
            else:  # open
                frame_score = r1 + r2
                frames.append({"frame": frame, "type": "open",
                              "rolls": [r1, r2], "score": frame_score})
                total += frame_score
                i += 2

    # Frame 10
    if i >= len(rolls):
        return {"error": "Not enough rolls for 10th frame."}

    r1 = rolls[i]
    if r1 == 10:
        if i + 2 >= len(rolls):
            return {"error": "10th-frame strike needs two bonus rolls."}
        r2, r3 = rolls[i+1], rolls[i+2]
        if r2 != 10 and r2 + r3 > 10:
            return {"error": "Invalid 10th frame bonus rolls."}
        frame_score = 10 + r2 + r3
        frames.append({"frame": 10, "type": "strike", "rolls": [
                      10, r2, r3], "score": frame_score})
        i += 3
    else:
        if i + 1 >= len(rolls):
            return {"error": "10th frame missing second roll."}
        r2 = rolls[i+1]
        if r1 + r2 > 10:
            return {"error": "Invalid 10th frame: pins exceed 10."}
        if r1 + r2 == 10:
            if i + 2 >= len(rolls):
                return {"error": "10th-frame spare needs one bonus roll."}
            r3 = rolls[i+2]
            frame_score = 10 + r3
            frames.append({"frame": 10, "type": "spare", "rolls": [
                          r1, r2, r3], "score": frame_score})
            i += 3
        else:
            frame_score = r1 + r2
            frames.append({"frame": 10, "type": "open", "rolls": [
                          r1, r2], "score": frame_score})
            i += 2

    total += frame_score

    if i != len(rolls):
        return {"error": "Too many rolls provided."}

    return {"total": total, "frames": frames}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/score", methods=["POST"])
def score():
    data = request.get_json(silent=True) or {}
    rolls = data.get("rolls", [])
    result = calculate_bowling_score(rolls)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
