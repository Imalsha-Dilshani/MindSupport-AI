import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="MindSupport AI",
    page_icon="🧠",
    layout="centered"
)

# -----------------------------
# OpenRouter Client
# -----------------------------
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key = os.getenv("OPENROUTER_API_KEY")

if not api_key:
    api_key = st.secrets.get("OPENROUTER_API_KEY")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)

# -----------------------------
# Header
# -----------------------------
st.title("🧠 MindSupport AI")
st.caption("AI-based stress support for university students")

st.info(
    "MindSupport AI provides general wellbeing and stress-management "
    "support. It is not a replacement for a qualified mental-health professional."
)

# -----------------------------
# Mood Check
# -----------------------------
st.subheader("🌱 How are you feeling today?")

mood = st.selectbox(
    "Select your current mood:",
    [
        "😊 Happy",
        "🙂 Okay",
        "😐 Neutral",
        "😟 Stressed",
        "😰 Anxious",
        "😔 Sad",
        "😞 Overwhelmed"
    ]
)

# -----------------------------
# Stress Level
# -----------------------------
st.subheader("📊 What is your stress level?")

stress_level = st.slider(
    "Rate your stress from 1 to 10",
    min_value=1,
    max_value=10,
    value=5
)

st.write(f"Your selected stress level: **{stress_level}/10**")

if stress_level <= 3:
    st.success(
        "🌱 Your stress level is relatively low. "
        "Keep maintaining healthy routines and give yourself time to relax."
    )

elif stress_level <= 6:
    st.warning(
        "💡 You may be experiencing moderate stress. "
        "Try a short break, slow breathing, or break your tasks into smaller steps."
    )

else:
    st.error(
        "💙 Your reported stress level is high. "
        "Let's focus on one small step at a time. "
        "If this continues or feels difficult to manage, consider talking "
        "to someone you trust or a qualified mental-health professional."
    )

# -----------------------------
# Quick Stress Help
# -----------------------------
st.subheader("💡 Quick Stress Help")

st.write("Choose an option to get practical tips:")

col1, col2 = st.columns(2)

if "quick_prompt" not in st.session_state:
    st.session_state.quick_prompt = None

with col1:
    if st.button("🧘 Breathing Exercise", use_container_width=True):
        st.session_state.quick_prompt = (
            "Give me a simple 2-minute breathing exercise to reduce stress."
        )

    if st.button("📚 Exam Stress", use_container_width=True):
        st.session_state.quick_prompt = (
            "I am stressed about my university exams. "
            "Give me practical steps to reduce exam stress."
        )

    if st.button("📝 Assignment Stress", use_container_width=True):
        st.session_state.quick_prompt = (
            "I have many university assignments and feel overwhelmed. "
            "Give me practical steps to manage assignment stress."
        )

with col2:
    if st.button("⏰ Time Management", use_container_width=True):
        st.session_state.quick_prompt = (
            "I struggle to manage my university workload and deadlines. "
            "Give me a simple time-management strategy."
        )

    if st.button("😴 Sleep & Relaxation", use_container_width=True):
        st.session_state.quick_prompt = (
            "I am stressed and finding it difficult to relax. "
            "Give me safe relaxation and sleep-support tips."
        )

    if st.button("💭 Anxiety Support", use_container_width=True):
        st.session_state.quick_prompt = (
            "I am feeling anxious. Give me simple and safe techniques "
            "that I can try right now to feel calmer."
        )

# -----------------------------
# Chat History
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "Hello! 👋 I'm MindSupport AI.\n\n"
                "I'm here to help you with university stress, "
                "exam pressure, assignments, anxiety and general wellbeing.\n\n"
                "How can I support you today?"
            )
        }
    ]

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------
# User Chat Input
# -----------------------------
user_message = st.chat_input(
    "Tell me what is bothering you..."
)

# Use quick button prompt if selected
if st.session_state.quick_prompt:
    user_message = st.session_state.quick_prompt
    st.session_state.quick_prompt = None

# -----------------------------
# AI Response
# -----------------------------
if user_message:

    # Add user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_message
        }
    )

    with st.chat_message("user"):
        st.markdown(user_message)

    # -----------------------------
    # AI System Prompt
    # -----------------------------
    system_prompt = f"""
You are MindSupport AI, a supportive AI assistant designed
to help university students manage stress and improve general wellbeing.

Current student mood:
{mood}

Current reported stress level:
{stress_level}/10

Your main goal is to provide practical, safe and personalized
stress-management support.

When responding:

1. Acknowledge the student's feelings.
2. Identify the likely source of stress.
3. Give 3-5 practical and realistic suggestions.
4. Focus on techniques such as:
   - slow breathing
   - mindfulness
   - short breaks
   - task prioritization
   - breaking large tasks into smaller tasks
   - Pomodoro-style study sessions
   - realistic study schedules
   - adequate sleep
   - relaxation
   - talking to a trusted person
5. Match the advice to the student's situation.
6. Avoid overwhelming the student with too many suggestions.
7. End with one simple encouraging sentence or question when appropriate.

For exam stress:
- Suggest realistic study planning.
- Break subjects into smaller topics.
- Recommend short study sessions and breaks.
- Encourage adequate sleep.

For assignment stress:
- Help prioritize deadlines.
- Break assignments into smaller tasks.
- Suggest a manageable daily plan.

For anxiety:
- Suggest slow breathing.
- Suggest grounding techniques.
- Encourage taking a short break.
- Encourage talking to a trusted person when appropriate.

For high stress levels (7-10):
- Be especially supportive.
- Focus on small immediate steps.
- Encourage professional support if the stress is persistent,
  severe, or difficult to manage.

IMPORTANT SAFETY RULES:
- Do not diagnose mental health disorders.
- Do not prescribe medication.
- Do not claim to be a doctor, psychologist or counsellor.
- Do not replace professional mental-health care.
- Do not provide harmful or dangerous instructions.
- If the student describes self-harm, suicide or immediate danger,
  encourage them to seek immediate help from emergency services,
  a trusted person, or a qualified mental-health professional.

Keep responses empathetic, practical, concise and easy
for university students to understand.
"""

    try:

        with st.chat_message("assistant"):

            with st.spinner("MindSupport AI is thinking..."):

                response = client.chat.completions.create(
                    model="openai/gpt-4o-mini",
                    messages=[
                        {
                            "role": "system",
                            "content": system_prompt
                        }
                    ] + st.session_state.messages
                )

                ai_response = response.choices[0].message.content

                st.markdown(ai_response)

        # Save AI response
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": ai_response
            }
        )

    except Exception as e:

        st.error(
            "Sorry, I couldn't connect to the AI service. "
            "Please check your API key and internet connection."
        )

        st.error(str(e))