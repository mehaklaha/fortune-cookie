import random
from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

FORTUNES = [
    "A bug fixed today saves three tomorrow.",
    "Your next commit will be your best one.",
    "Someone will soon say 'it works on my machine'.",
    "A great opportunity hides inside a merge conflict.",
    "You will drink chai and solve the problem.",
    "Today is a good day to deploy. (Not Friday, though.)",
]

PAGE = """
<!doctype html>
<html>
<head>
  <title>Fortune Cookie</title>
  <style>
    body { font-family: Arial; background:#fff4d6; text-align:center; padding-top:80px; }
    .card { display:inline-block; background:white; padding:40px; border-radius:16px;
            box-shadow:0 4px 12px rgba(0,0,0,.15); max-width:420px; }
    button { padding:10px 20px; border:none; border-radius:8px; background:#e07b00;
             color:white; font-size:16px; cursor:pointer; }
  </style>
</head>
<body>
  <div class="card">
    <h1>🥠 Your Fortune</h1>
    <p style="font-size:20px">{{ fortune }}</p>
    <button onclick="location.reload()">Another one</button>
  </div>
</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(PAGE, fortune=random.choice(FORTUNES))


@app.route("/api/fortune")
def api_fortune():
    return jsonify({"fortune": random.choice(FORTUNES)})


@app.route("/health")
def health():
    return jsonify(status="ok")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
