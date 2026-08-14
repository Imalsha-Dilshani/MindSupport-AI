# 🧠 MindSupport AI

### AI-Based Mental Health and Stress Support Chatbot for University Students

---

## 📌 Project Overview

MindSupport AI is an AI-powered chatbot prototype developed to provide general emotional support and practical stress-management guidance for university students.

The system is designed as part of an academic research project exploring the role of Artificial Intelligence in supporting university students' mental health in Sri Lanka.

The chatbot focuses mainly on helping students manage common university-related challenges such as academic stress, examination pressure, assignment workload, anxiety, time-management difficulties, and general emotional difficulties.

---

## 🎓 Research Topic

**The Role of Artificial Intelligence in Supporting University Students' Mental Health in Sri Lanka**

---

## 🎯 Aim of the Project

The aim of MindSupport AI is to explore how Artificial Intelligence can be used as an accessible and supportive tool to help university students manage stress and improve their general emotional wellbeing.

The system is intended to provide initial support and practical stress-management suggestions while encouraging students to seek professional help when necessary.

---

## ✨ Main Features

### 🧠 AI Chatbot

Students can communicate with the AI chatbot about their feelings, academic difficulties, stress, and general wellbeing.

### 🌱 Mood Check-In

Students can select their current mood from several options:

- 😊 Happy
- 🙂 Okay
- 😐 Neutral
- 😟 Stressed
- 😰 Anxious
- 😔 Sad
- 😞 Overwhelmed

### 📊 Stress Level Assessment

Students can rate their current stress level from:

**1 – Low Stress → 10 – Very High Stress**

The system uses the selected stress level to provide more appropriate supportive guidance.

### 💡 Quick Stress Help

The application provides quick-access support options including:

- 🧘 Breathing Exercise
- 📚 Exam Stress
- 📝 Assignment Stress
- ⏰ Time Management
- 😴 Sleep & Relaxation
- 💭 Anxiety Support

### 🧘 Stress-Management Tips

The AI can provide practical suggestions such as:

- Breathing exercises
- Short relaxation breaks
- Task prioritization
- Breaking large tasks into smaller tasks
- Pomodoro-style study sessions
- Time-management techniques
- Healthy study routines
- Sleep and relaxation suggestions
- Talking with trusted people

### 🛡️ Mental Health Safety

The chatbot is designed with safety instructions to:

- Avoid diagnosing mental-health disorders
- Avoid prescribing medication
- Avoid pretending to be a doctor or psychologist
- Encourage professional support when appropriate
- Provide additional safety guidance for serious distress

---

## 🛠️ Technologies Used

The project was developed using the following technologies:

| Technology | Purpose |
|---|---|
| Python | Application development |
| Streamlit | Web application interface |
| OpenRouter API | AI model access |
| OpenAI Python SDK | Communication with the AI API |
| python-dotenv | Environment variable management |
| Git | Version control |
| GitHub | Source code management |
| Streamlit Community Cloud | Application deployment |

---

## 📂 Project Structure

```text
MindSupport-AI/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env
└── venv/
 
---

## ⚙️ Installation

Step 1 – Clone the Repository
git clone https://github.com/Imalsha-Dilshani/MindSupport-AI.git

---

## 🔑 API Configuration

The application uses an OpenRouter API key to communicate with the AI model.

Create a .env file in the project root directory.

OPENROUTER_API_KEY=my_api_key_here

---

## ▶️ Running the Application Locally

After activating the virtual environment, run:

py -m streamlit run app.py

The application will open in a browser.

Usually, the local application will be available at:

http://localhost:8501

---

## 🌐 Deployment

The application can be deployed using Streamlit Community Cloud.

---

## 👩‍💻 Developed For

Academic Research Project

Research Topic:

The Role of Artificial Intelligence in Supporting University Students' Mental Health in Sri Lanka

Technology: Python + Streamlit + OpenRouter AI