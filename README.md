# 🗨️ Simple Chatbot (LangChain + OpenAI)

A minimal terminal-based chatbot built with [LangChain](https://www.langchain.com/) and [OpenAI](https://platform.openai.com/).  
The chatbot **remembers your conversation** across runs by saving messages to a local JSON file.

---

## ✨ Features

- ✅ Interactive REPL (chat in the terminal)  
- ✅ Persistent memory with `messages.json`  
- ✅ `.env` file support for secrets  
- ✅ Lightweight dependencies  

---

## 📂 Project Structure

.
├─ simple_chatbot.py # main script (interactive chatbot loop)
├─ requirements.txt # project dependencies
├─ .env # your OpenAI API key (not committed)
├─ .env.example # safe template for others
├─ messages.json # local memory (gitignored)
└─ .gitignore

yaml
Copy
Edit

---

## 🚀 Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
2. Set up a virtual environment (recommended)
bash
Copy
Edit
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Add your API key
Create a .env file in the project root:

ini
Copy
Edit
OPENAI_API_KEY=sk-xxxxxx
(Use .env.example as a template.)

5. Run the chatbot
bash
Copy
Edit
python simple_chatbot.py
Then chat away in your terminal:

makefile
Copy
Edit
You: hello
Bot: Hello! How can I help you today?
Type exit or quit to close.

🧠 How It Works
Uses FileChatMessageHistory("messages.json") to store conversation history locally.

ConversationBufferMemory loads that history into the prompt each run, so the bot can recall context (e.g., your name).

Powered by ChatOpenAI from langchain-openai (defaults to gpt-4o-mini).

⚙️ Requirements
See requirements.txt:

langchain

langchain-openai

langchain-community

python-dotenv

Install all at once:

bash
Copy
Edit
pip install -r requirements.txt
🛠 Troubleshooting
ModuleNotFoundError: langchain_openai
Install:

bash
Copy
Edit
pip install -U langchain-openai
ModuleNotFoundError: langchain_community.chat_message_histories
Install:

bash
Copy
Edit
pip install -U langchain-community
No memory across runs
Make sure messages.json is being created in the same folder as your script.

Python 3.13 issues
Some dependencies may lag behind Python 3.13. If you hit problems, use Python 3.10–3.12.
