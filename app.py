from flask import Flask, request, render_template, Response
import requests
import json
import time

app = Flask(__name__)

OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2"

def stream_ollama(prompt):
    """Stream bot response via SSE."""
    response = requests.post(
        OLLAMA_API_URL,
        json={"model": MODEL, "prompt": prompt},
        stream=True
    )

    for line in response.iter_lines():
        if line:
            try:
                data = json.loads(line.decode("utf-8"))
                if "response" in data:
                    yield f"data: {data['response']}\n\n"
                    time.sleep(0.01)
            except json.JSONDecodeError:
                continue
    yield "data: [DONE]\n\n"

def check_ollama_status() -> str:
    """Check if Ollama is running."""
    try:
        test_prompt = {"model": MODEL, "prompt": "Hello"}
        response = requests.post(OLLAMA_API_URL, json=test_prompt, timeout=2)
        if response.ok:
            return "Powered by Ollama LLaMA ✅"
        else:
            return "Powered by Ollama LLaMA ⚠️ (not responding)"
    except Exception:
        return "Powered by Ollama LLaMA ⚠️ (not running)"

@app.route("/")
def index():
    status = check_ollama_status()
    return render_template("index.html", ollama_status=status)

@app.route("/chat")
def chat():
    user_input = request.args.get("user_input", "")
    if not user_input:
        return "No input provided", 400
    return Response(stream_ollama(user_input), mimetype="text/event-stream")

if __name__ == "__main__":
    app.run(debug=True)
