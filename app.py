from flask import Flask, render_template, request
from modules.intent_detector import get_intent
from services import smart_gpt

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    user_input = ""
    response = ""
    intent = ""
    confidence = 0

    if request.method == "POST":
        user_input = request.form["user_input"]
        intent, confidence = get_intent(user_input)

        if confidence >= 0.6:
            response = f"(Intent: {intent}) — This feature is coming soon."
        else:
            response = smart_gpt(user_input)

    return render_template("index.html", user_input=user_input, response=response)

if __name__ == "__main__":
    app.run(debug=True)

