# 🗪 Ollama Chatbot (Real-Time Streaming using Flask)

A fast and modern **real-time chatbot web app** built using local **Ollama LLaMA models**.
It supports live streaming replies using SSE (Server-Sent Events) and shows Ollama live status in the footer.

Type any message, and the chatbot responds stream-by-stream, just like ChatGPT typing in real time.

---

## 🖥 Features

- Real-time streaming chat powered by Ollama LLaMA

- SSE-based live typing effect

- Clean Flask backend

- Responsive chat UI (index.html)

- Footer shows Ollama server status

- Fully offline, runs locally (no API keys needed)  

---

## 🚀 Requirements

- Python 3.10+

- Flask

- requests

- Ollama installed on your system

- Any LLaMA model installed **(default: llama3.2)**

---

## ⚙️ Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/document-summarizer.git
cd document-summarizer
```
2. **Create a virtual environment (recommended)**
```bash
python -m venv venv

# Linux/macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```
3. **Install dependencies**
```bash
pip install -r requirements.txt
```
4. **Ensure Ollama LLaMA is running locally:**
```bash
ollama run llama3.2
```
Check that your model is running at http://localhost:11434
## 📝 Usage

1. **Run the Flask app**
```bash
python app.py
```
2. **Open your browser and go to:**

     http://127.0.0.1:5000/

3. **Start chatting:**



- Type your message

- Receive streaming responses

- Footer automatically shows Ollama live status


## 🧠 How It Works
- /chat endpoint streams responses using Server-Sent Events

- Backend sends each chunk live to the frontend

- Ollama LLaMA model generates text locally

- No cloud, no external APIs, fully private

## 🗂 File Structure

```
ollama-chatbot/
│
├── app.py                 # Main Flask application
├── templates/
│   └── index.html         # Chat UI
├── README.md              # This File
└── requirements.txt       # Dependencies

```
## ⚠️ Notes

- Ensure Ollama is running before opening the chat

- Works only with models installed in Ollama

- SSE response requires modern browsers

## 👨‍💻 Author

Pratik Pawar  
Data Analyst | Flask & AI Projects |
