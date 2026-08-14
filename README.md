# 🧠 MindSupport AI

### AI-Based Mental Health and Stress Support Chatbot for University Students

---

## 📌 Project Overview

MindSupport AI is an AI-powered chatbot prototype developed to provide general emotional support and practical stress-management guidance for university students.

The system is developed as part of an academic research project exploring the role of Artificial Intelligence in supporting university students' mental health in Sri Lanka.

The chatbot focuses on common university-related challenges such as:

- 📚 Academic stress
- 📝 Assignment workload
- 📝 Examination pressure
- 😟 Anxiety
- ⏰ Time-management difficulties
- 💭 Feeling overwhelmed
- 🌱 General emotional wellbeing

---

## 🎓 Research Topic

**The Role of Artificial Intelligence in Supporting University Students' Mental Health in Sri Lanka**

---

## 🎯 Aim of the Project

The aim of MindSupport AI is to explore how Artificial Intelligence can be used as an accessible and supportive tool to help university students manage stress and improve their general emotional wellbeing.

The system provides general wellbeing support, practical stress-management suggestions, and encourages students to seek professional support when necessary.

---

## ✨ Main Features

### 🧠 AI Chatbot

Students can communicate with the AI chatbot about their feelings, academic difficulties, stress, and general wellbeing.

### 🌱 Mood Check-In

Students can identify their current mood and communicate how they are feeling.

Example moods include:

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

The system uses the selected stress level to provide appropriate supportive guidance.

### 💡 Quick Stress Help

The application provides quick-access support options such as:

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
- Study planning
- Time-management techniques
- Healthy study routines
- Sleep and relaxation suggestions
- Talking with trusted people

---

## 🛠️ Technologies Used

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
```

### File Description

- **app.py** – Main Streamlit application.
- **requirements.txt** – Required Python packages.
- **README.md** – Project documentation.
- **.gitignore** – Files and folders that should not be uploaded to GitHub.
- **.env** – Local API key configuration.
- **venv/** – Python virtual environment.

> ⚠️ The `.env` file and `venv/` folder should not be uploaded to GitHub.

---

## ⚙️ Installation

Follow the steps below to install and run MindSupport AI locally.

### Step 1 – Clone the Repository

Clone the GitHub repository using:

```bash
git clone https://github.com/Imalsha-Dilshani/MindSupport-AI.git
```

### Step 2 – Open the Project Directory

```bash
cd MindSupport-AI
```

### Step 3 – Create a Virtual Environment

```bash
py -m venv venv
```

### Step 4 – Activate the Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

### Step 5 – Install Dependencies

```bash
py -m pip install -r requirements.txt
```

---

## 🔑 API Configuration

The application uses the **OpenRouter API** to communicate with the AI model.

Create a `.env` file in the project root directory.

Add:

```env
OPENROUTER_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your own OpenRouter API key.

### ⚠️ API Key Security

**Never upload your API key to GitHub.**

The `.gitignore` file should contain:

```text
.env
venv/
__pycache__/
*.pyc
```

The `.env` file should remain only on your local computer.

---

## ▶️ Running the Application Locally

After activating the virtual environment, run:

```bash
py -m streamlit run app.py
```

The application will open in your web browser.

The local application is usually available at:

```text
http://localhost:8501
```

---

## 💬 Example Usage

A student can select a stress level such as:

**Stress Level:**

> 7/10

The application can then provide appropriate supportive guidance.

For example, if a student says:

> I have many assignments and exams coming up. I feel overwhelmed.

The chatbot can provide suggestions such as:

1. List all assignments and exams.
2. Identify the most urgent tasks.
3. Break large assignments into smaller tasks.
4. Create a realistic study schedule.
5. Take short breaks between study sessions.
6. Practice simple breathing or relaxation exercises.
7. Talk to someone you trust if the stress becomes difficult to manage.

---

## 🧠 AI Support Areas

MindSupport AI is designed to provide general support related to:

- 📚 Academic stress
- 📝 Assignment stress
- 📝 Examination stress
- ⏰ Time-management difficulties
- 😟 Anxiety
- 😞 Feeling overwhelmed
- 🌱 General emotional wellbeing
- 🧘 Relaxation
- 🫁 Breathing exercises
- 😴 Sleep and rest
- ⚖️ Study-life balance

---

## 🛡️ Safety and Ethical Considerations

MindSupport AI is designed as a supportive AI tool and not as a medical or clinical system.

The chatbot:

- Does not diagnose mental-health disorders.
- Does not prescribe medication.
- Does not provide medical treatment.
- Does not replace psychologists, counsellors, doctors, or other qualified professionals.
- Provides general wellbeing and stress-management guidance.
- Encourages users to seek professional support when appropriate.

If a user indicates serious emotional distress, self-harm, suicide, or immediate danger, the system should encourage the user to seek appropriate professional or emergency support.

---

## 🔐 Privacy

Privacy is an important consideration in the development of this application.

Users should avoid entering highly sensitive personal information into the chatbot.

The application should not intentionally collect unnecessary personal information.

API credentials are stored using environment variables and should not be included directly in the source code.

The `.env` file must never be uploaded to GitHub.

---
## 🌐 Live Application

🚀 **Try MindSupport AI Online:**

 Streamlit  app link = mindsupport-ai-3txitmyqtp6zvrlgshmg6q.streamlit.app

The application is deployed using Streamlit Community Cloud and is available online for demonstration and academic research purposes.

---

## 🌐 Deployment

MindSupport AI can be deployed using **Streamlit Community Cloud**.

### Deployment Steps

1. Push the project source code to GitHub.
2. Open Streamlit Community Cloud.
3. Sign in using GitHub.
4. Create a new application.
5. Select the repository:

```text
Imalsha-Dilshani/MindSupport-AI
```

6. Select the branch:

```text
main
```

7. Select the main application file:

```text
app.py
```

8. Add the API key using Streamlit Secrets.
9. Deploy the application.

### Streamlit Secrets

For deployment, add the following secret:

```toml
OPENROUTER_API_KEY = "my_api_key_here"
```
 

---

## 📊 Research Context

This application was developed for the research topic:

**The Role of Artificial Intelligence in Supporting University Students' Mental Health in Sri Lanka**

The prototype demonstrates how Artificial Intelligence can be integrated into a web-based application to provide accessible initial support and practical stress-management guidance for university students.

The research focuses on the potential role of AI in supporting students who experience:

- Academic pressure
- Examination stress
- Assignment workload
- Anxiety
- Time-management difficulties
- General stress and emotional difficulties

---

## 🎯 Research Objectives Supported by the Prototype

The prototype supports the investigation of:

1. To explore how Artificial Intelligence can provide accessible stress-management support to university students.

2. To examine students' perceptions of the usefulness of AI-based mental-health support.

3. To identify the potential benefits and limitations of using AI chatbots for student wellbeing.

4. To examine important considerations such as trust, privacy, safety, and the need for professional support.

---

## 🔬 Research Evaluation

The prototype can be evaluated using factors such as:

- Perceived usefulness
- Ease of use
- Accessibility
- User satisfaction
- Trust in AI
- Privacy concerns
- Willingness to use AI-based support
- Perceived effectiveness of stress-management suggestions

The findings can be used to understand how university students perceive AI-based mental-health and stress-management support.

---

## 🔮 Future Improvements

Future versions of MindSupport AI may include:

- 🇱🇰 Sinhala language support
- 🇬🇧 English language support
- 🌐 Sinhala-English bilingual conversations
- 📈 Personal wellbeing dashboard
- 📝 Daily mood tracking
- 🔔 Study and relaxation reminders
- 👩‍⚕️ Professional-support directory
- 🔐 Improved privacy controls
- 📱 Mobile-friendly interface
- 📊 Anonymous research analytics
- 🧠 More advanced personalized wellbeing recommendations

---

## 🧪 Project Status

**Current Status: Prototype**

### Completed Features

- [x] Streamlit user interface
- [x] AI chatbot
- [x] OpenRouter API integration
- [x] Mood selection
- [x] Stress-level assessment
- [x] Stress-management suggestions
- [x] Quick stress-help options
- [x] Mental-health safety instructions
- [x] GitHub repository
- [x] Project documentation

### Planned Features

- [ ] Sinhala language support
- [ ] Improved user interface
- [ ] Additional testing
- [ ] Final deployment
- [ ] User evaluation
- [ ] Research data analysis

---

## ⚠️ Disclaimer

**MindSupport AI is not a medical or clinical system.**

The information provided by the chatbot is for general wellbeing and educational purposes only.

The chatbot should not be used to diagnose, treat, or manage a mental-health condition.

Students experiencing persistent, severe, or urgent mental-health difficulties should seek appropriate support from a qualified mental-health professional or appropriate support service.

---

## 🎓 Academic Purpose

This project is developed for academic and research purposes to explore the potential role of Artificial Intelligence in supporting university students' mental health in Sri Lanka.

The application is a research prototype and should not be considered a clinical mental-health service.

---

## 👩‍💻 Developed For

**Academic Research Project**

### Research Topic

**The Role of Artificial Intelligence in Supporting University Students' Mental Health in Sri Lanka**

### Technologies

**Python + Streamlit + OpenRouter AI**

---

## 📄 License

This project is developed for academic and educational purposes.