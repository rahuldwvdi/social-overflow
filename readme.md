# 🚀 Social Overflow

<p align="center">
A <b>multi-agent AI debate platform</b> where AI agents discuss complex questions and produce structured reasoning.
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-backend-green)
![Ollama](https://img.shields.io/badge/Ollama-local%20LLM-purple)
![License](https://img.shields.io/badge/license-MIT-orange)

</p>

---

# 🧠 Concept

Most AI apps work like this:

```
User → AI → Answer
```

**Social Overflow works differently:**

```
User Question
      ↓
🤖 Multiple AI Agents respond
      ↓
⚔️ Agents challenge reasoning
      ↓
🏆 Critic Agent selects best argument
```

Instead of one answer, the system produces **multiple perspectives and structured reasoning**.


# ✨ Features

```

- 🤖 Multi-Agent AI System  
- 🧠 Different reasoning perspectives  
- ⚔️ AI argument critiques  
- 🏆 Critic agent evaluation  
- 💾 Debate memory with SQLite  
- 🌐 Clean web interface  
- ⚡ Runs completely locally with Ollama  

---

# 🏗 System Architecture

```
Frontend (HTML / CSS / JS)
        ↓
FastAPI Backend
        ↓
Debate Engine
        ↓
AI Agents
        ↓
Critique Engine
        ↓
Critic Agent
        ↓
SQLite Memory
        ↓
Ollama Local Model
```


# ⚙️ Tech Stack

```

| Technology | Purpose |
|-----------|--------|
| Python | Backend logic |
| FastAPI | API framework |
| Ollama | Local LLM runtime |
| SQLite | Debate storage |
| HTML / CSS / JS | Web interface |

---

# 🚀 Getting Started

## 1️⃣ Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/social-overflow.git
cd social-overflow
```

## 2️⃣ Install dependencies

```bash
pip install fastapi uvicorn requests
```

---

## 3️⃣ Install Ollama

Download Ollama:

```
https://ollama.com
```

Run a model:

```bash
ollama run tinyllama
```

---

## 4️⃣ Start the server

```bash
uvicorn main:app --reload
```

---

## 5️⃣ Open the app

Open in browser:

```
http://localhost:8000
```

Ask a question and watch **AI agents debate**.

---

# 🧪 Example Question

```
Will AI replace software engineers?
```

Agents respond from different perspectives:

```
Engineer Agent
Research Agent
Startup Agent
Security Agent
Philosophy Agent
```

Then the **Critic Agent selects the best argument**.

```
PS : use advanced models like Llama 4 / 3.3 / 3.2, Mistral Small 3 / 3.2, Gemma 3 depending upon your hardware
```