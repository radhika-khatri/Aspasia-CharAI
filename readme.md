# Aspasia-CharAI

An interactive AI-powered philosophical chatbot that brings **Aspasia of Miletus** — the renowned classical Athenian philosopher, rhetorician, and intellectual — to life through a beautifully crafted conversational interface. Engage in Socratic dialogue on topics like love, justice, education, and women's power.

## Demo

<iframe width="560" height="315" src="https://www.youtube.com/embed/dV2FjZSD4_I?si=jV5fprNpVEAk2I5h" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

[![Watch the Demo](https://img.youtube.com/vi/dV2FjZSD4_I/maxresdefault.jpg)](https://youtu.be/dV2FjZSD4_I)

## Features

- **Socratic Teaching Style** — Aspasia asks probing questions rather than giving direct answers, encouraging deeper thinking
- **Local LLM Powered** — Runs entirely on your machine using Ollama with the Mistral model — no API keys or cloud dependency
- **Immersive UI** — Cosmic animated background, glassmorphism design, floating particles, and smooth animations
- **Conversation History** — Full chat history maintained during your session
- **Responsive Design** — Works on both desktop and mobile browsers

## Tech Stack

| Component | Technology |
|-----------|------------|
| Frontend/Framework | Streamlit |
| LLM Engine | Ollama + Mistral |
| Language | Python |
| Styling | Custom CSS with animations |

## Prerequisites

- Python 3.7+
- [Ollama](https://ollama.ai) installed and running
- Mistral model pulled in Ollama

## Setup & Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/radhika-khatri/Aspasia-CharAI.git
   cd Aspasia-CharAI
   ```

2. **Install dependencies**
   ```bash
   pip install streamlit
   ```

3. **Pull the Mistral model**
   ```bash
   ollama pull mistral
   ```

4. **Start the Ollama service** (if not already running)
   ```bash
   ollama serve
   ```

## Usage

Run the application:

```bash
streamlit run main.py
```

This opens the app in your browser (typically at `http://localhost:8501`). Type a philosophical question or topic and click **"Engage with Aspasia"** to start a Socratic dialogue. Use **"Clear Conversation"** to reset the chat.

## Project Structure

```
Aspasia-CharAI/
├── main.py       # Main application — UI, LLM integration, and styling
└── README.md
```

## How It Works

1. A **system prompt** defines Aspasia's personality — eloquent, empathetic, sharp, and persuasive
2. User input and chat history are sent to the **Mistral model** running locally via Ollama
3. Aspasia responds in-character using Socratic questioning and philosophical insight
4. The **Streamlit UI** renders the conversation with animated visuals and glassmorphic styling
