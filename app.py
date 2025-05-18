from flask import Flask, request, render_template, jsonify
from model_loader import load_model

app = Flask(__name__)
model, tokenizer = load_model()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]

    inputs = tokenizer(user_input, return_tensors="pt").to(model.device)
    outputs = model.generate(**inputs, max_new_tokens=150, do_sample=True, temperature=0.9, top_p=0.95)
    reply = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return jsonify({"reply": reply.strip()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
