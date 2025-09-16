# 🎓 AIMIT Admission Assistant Bot

## 📋 Overview

**AIMIT Admission Assistant Bot (AIMIT Connect)** is a conversational AI chatbot built using **Chainlit** and a **Large Language Model backend (Gemini / Groq)**.  
It helps prospective students instantly access reliable information about:

- 📚 Courses offered at AIMIT  
- 💰 Fee structures  
- 🏠 Hostel facilities & fees  
- 🎓 Scholarship options  
- 💼 Placement support & training  
- 📝 Admission process & eligibility  

This project enhances student experience by automating responses to frequently asked questions and reducing delays in information retrieval.

---

## 🚀 Features

- Warm, conversational greeting and tone  
- Maintains conversation context during the session  
- Structured responses in **bullet points** for easy readability  
- Fallback responses when information is unavailable  
- Secure API key handling using `.env`  
- Modular backend → easily switch between **Gemini** and **Groq** models  

---

## 🧰 Tech Stack

| Component         | Technology / Tool       |
|-------------------|--------------------------|
| Chat UI / Frontend| Chainlit                 |
| Backend / LLM     | Gemini API / Groq API    |
| Env management    | python-dotenv            |
| Language          | Python                   |

---

## 📂 Project Structure
```plaintext
aimit_admission_assistant_bot/
│
├── src/
│ ├── json_prompt.py 
│ ├── llm.py # Gemini \ Groq backend
│ ├── prompt.json # Knowledge base / system prompt
│
├── app.py #Chainlit frontend
├── .env # Environment variables (API keys) – NOT pushed to Git
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── .gitignore # Ignore venv, .env, cache files
```
## 🔧 Setup Instructions

1. **Clone the repository**
   ```cmd
   git clone https://github.com/puneethail/aimit_admission_assistant_bot.git
   cd aimit_admission_assistant_bot

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   # On Windows
   .\venv\Scripts\activate
   # On Mac/Linux
   source venv/bin/activate

3. **Install dependencies**
    ```cmd
    pip install -r requirements.txt

4. **Set up environment variables**
    ```bash
    # Create a .env file in the root folder and add your API keys:
    GEMINI_API_KEY = 'your_gemini_api_key_here'
    GROQ_API_KEY = 'your_groq_api_key_here'

5.  **Run the bot**
    ```cmd
    python app.py
   
## 🤝 Contribution

- Contributions are welcome!
- Fork this repo
- Create a new branch
- Make your changes
- Submit a pull request

## 👨‍💻 Author  
**Puneeth N Ail**  

🔗 [Portfolio](https://ailpuneeth.pages.dev/)  
🔗 [LinkedIn](https://www.linkedin.com/in/puneeth-n-ail/)  
🔗 [GitHub](https://github.com/puneethail)  
