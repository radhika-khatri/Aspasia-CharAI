import streamlit as st
import subprocess
import time
import random
import json

# Aspasia's final personality prompt
SYSTEM_PROMPT = """
You are Aspasia of Miletus — an eloquent philosopher, rhetorician, and teacher from classical Athens. 
You speak directly with wisdom, clarity, and elegance. You are empathetic and sharp, thoughtful and persuasive. 
You are known for your ideas on love, justice, education, and the power of women. 

You will be giving insights to the learners the way Aspasia used to give to Socrates — asking probing questions to guide the learner. 
Do not give direct answers. Remain calm, respectful, and insightful.
"""

def call_ollama_mistral(prompt, history=[]):
    # Construct prompt with system message and history
    full_prompt = SYSTEM_PROMPT + "\n"
    
    for turn in history:
        full_prompt += f"User: {turn['user']}\nAspasia: {turn['aspasia']}\n"
    full_prompt += f"User: {prompt}\nAspasia:"

    result = subprocess.run(
        ["ollama", "run", "mistral"],
        input=full_prompt.encode(),
        stdout=subprocess.PIPE
    )

    response = result.stdout.decode().split("Aspasia:")[-1].strip()
    return response

# Revolutionary CSS for an absolutely stunning UI
def load_revolutionary_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap');
    
    /* Reset and base styles */
    .stApp {
        background: #000000;
        overflow-x: hidden;
    }
    
    .main .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }
    
    /* Animated cosmic background */
    .cosmic-bg {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        z-index: -2;
        background: radial-gradient(circle at 20% 50%, #120078 0%, transparent 50%),
                    radial-gradient(circle at 80% 20%, #6b46c1 0%, transparent 50%),
                    radial-gradient(circle at 40% 80%, #3b82f6 0%, transparent 50%),
                    radial-gradient(circle at 90% 60%, #ec4899 0%, transparent 50%),
                    linear-gradient(135deg, #0f0f23 0%, #1a1a2e 50%, #16213e 100%);
        animation: cosmicShift 20s ease-in-out infinite alternate;
    }
    
    @keyframes cosmicShift {
        0% { filter: hue-rotate(0deg) brightness(1); }
        50% { filter: hue-rotate(180deg) brightness(1.2); }
        100% { filter: hue-rotate(360deg) brightness(1); }
    }
    
    /* Floating particles */
    .particles {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: -1;
    }
    
    .particle {
        position: absolute;
        width: 2px;
        height: 2px;
        background: rgba(255, 255, 255, 0.6);
        border-radius: 50%;
        animation: float 15s linear infinite;
    }
    
    @keyframes float {
        0% { 
            transform: translateY(100vh) translateX(0px) scale(0);
            opacity: 0;
        }
        10% {
            opacity: 1;
            transform: scale(1);
        }
        90% {
            opacity: 1;
        }
        100% { 
            transform: translateY(-100vh) translateX(100px) scale(0);
            opacity: 0;
        }
    }
    
    /* Main container */
    .app-container {
        min-height: 0.25vh;
        display: flex;
        flex-direction: column;
        position: relative;
        z-index: 1;
    }
    
    /* Header section */
    .header-section {
        text-align: center;
        padding: 1rem 2rem 1rem;
        position: relative;
    }
    
    .main-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: clamp(3rem, 8vw, 6rem);
        font-weight: 700;
        background: linear-gradient(135deg, #ffffff 0%, #a855f7 30%, #06b6d4 60%, #10b981 100%);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 1rem;
        animation: titleGradient 8s ease-in-out infinite, titlePulse 4s ease-in-out infinite;
        letter-spacing: -0.02em;
        line-height: 0.9;
    }
    
    @keyframes titleGradient {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    @keyframes titlePulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.02); }
    }
    
    .subtitle {
        font-family: 'Inter', sans-serif;
        font-size: 1.25rem;
        color: rgba(255, 255, 255, 0.7);
        font-weight: 400;
        margin-bottom: 3rem;
        animation: subtitleFade 3s ease-out;
    }
    
    @keyframes subtitleFade {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 0.7; transform: translateY(0); }
    }

    
    /* Input section */
    .input-section {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(20px);
        border-radius: 24px;
        padding: 2rem;
        margin-bottom: 2rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
        position: relative;
        overflow: hidden;
    }
    
    .input-section::before {
        display: none;
    }
    
    @keyframes shimmer {
        0%, 100% { transform: translateX(-100%); }
        50% { transform: translateX(100%); }
    }
    
    .input-wrapper {
        position: relative;
    }
    
    .stTextInput > div > div > input {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 2px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 16px !important;
        padding: 1rem 1.5rem !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 1.1rem !important;
        color: #ffffff !important;
        transition: all 0.3s ease !important;
        backdrop-filter: blur(10px);
    }
    
    .stTextInput > div > div > input:focus {
        border-color: rgba(168, 85, 247, 0.5) !important;
        box-shadow: 0 0 0 4px rgba(168, 85, 247, 0.1), 0 0 20px rgba(168, 85, 247, 0.2) !important;
        outline: none !important;
        background: rgba(255, 255, 255, 0.08) !important;
    }
    
    .stTextInput > div > div > input::placeholder {
        color: rgba(255, 255, 255, 0.4) !important;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 50%, #a855f7 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 16px !important;
        padding: 0.75rem 2rem !important;
        font-family: 'Space Grotesk', sans-serif !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        transition: all 0.3s ease !important;
        position: relative !important;
        overflow: hidden !important;
        margin-top: 1rem !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 10px 25px rgba(168, 85, 247, 0.3) !important;
    }
    
    .stButton > button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
        transition: left 0.5s ease;
    }
    
    .stButton > button:hover::before {
        left: 100%;
    }
    
    /* Messages */
    .message-container {
        margin-bottom: 2rem;
        animation: messageSlide 0.6s ease-out;
    }
    
    @keyframes messageSlide {
        0% { opacity: 0; transform: translateY(30px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    
    .user-message {
        background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
        color: white;
        padding: 1.5rem 2rem;
        border-radius: 24px 24px 8px 24px;
        margin-left: 20%;
        position: relative;
        box-shadow: 0 8px 25px rgba(59, 130, 246, 0.2);
        font-family: 'Inter', sans-serif;
        font-size: 1.05rem;
        line-height: 1.6;
        backdrop-filter: blur(10px);
    }
    
    .aspasia-message {
        background: linear-gradient(135deg, rgba(255, 255, 255, 0.1) 0%, rgba(255, 255, 255, 0.05) 100%);
        color: #ffffff;
        padding: 1.5rem 2rem;
        border-radius: 24px 24px 24px 8px;
        margin-right: 20%;
        position: relative;
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(20px);
        font-family: 'Inter', sans-serif;
        font-size: 1.05rem;
        line-height: 1.7;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
    }
    
    .message-icon {
        display: inline-block;
        width: 24px;
        height: 24px;
        border-radius: 50%;
        margin-right: 0.5rem;
        vertical-align: middle;
    }
    
    .user-icon {
        background: linear-gradient(135deg, #60a5fa, #3b82f6);
    }
    
    .aspasia-icon {
        background: linear-gradient(135deg, #a855f7, #8b5cf6);
    }
    
    /* Thinking animation */
    .thinking-container {
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 2rem;
        margin-bottom: 2rem;
    }
    
    .thinking-bubble {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(20px);
        border-radius: 50px;
        padding: 1rem 2rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
        display: flex;
        align-items: center;
        gap: 1rem;
    }
    
    .thinking-text {
        color: rgba(255, 255, 255, 0.8);
        font-family: 'Inter', sans-serif;
        font-size: 0.95rem;
    }
    
    .thinking-dots {
        display: flex;
        gap: 4px;
    }
    
    .thinking-dot {
        width: 6px;
        height: 6px;
        border-radius: 50%;
        background: linear-gradient(135deg, #a855f7, #06b6d4);
        animation: thinkingPulse 1.4s ease-in-out infinite;
    }
    
    .thinking-dot:nth-child(1) { animation-delay: 0s; }
    .thinking-dot:nth-child(2) { animation-delay: 0.2s; }
    .thinking-dot:nth-child(3) { animation-delay: 0.4s; }
    
    @keyframes thinkingPulse {
        0%, 80%, 100% { 
            transform: scale(0.8);
            opacity: 0.5;
        }
        40% { 
            transform: scale(1.2);
            opacity: 1;
        }
    }
    
    /* Welcome message */
    .welcome-container {
        text-align: center;
        padding: 3rem 2rem;
        background: rgba(255, 255, 255, 0.02);
        backdrop-filter: blur(20px);
        border-radius: 32px;
        border: 1px solid rgba(255, 255, 255, 0.05);
        margin-bottom: 3rem;
        position: relative;
        overflow: hidden;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        min-height: 200px;
    }
    
    .welcome-container::before {
        content: '';
        position: absolute;
        top: -2px;
        left: -2px;
        right: -2px;
        bottom: -2px;
        background: linear-gradient(45deg, #6366f1, #8b5cf6, #06b6d4, #10b981);
        border-radius: 32px;
        z-index: -1;
        animation: borderGlow 4s linear infinite;
    }
    
    @keyframes borderGlow {
        0%, 100% { opacity: 0.5; }
        50% { opacity: 1; }
    }
    
    .welcome-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 2rem;
        font-weight: 600;
        color: #ffffff;
        margin: 0 0 1rem 0;
        text-align: center;
    }
    
    .welcome-text {
        font-family: 'Inter', sans-serif;
        font-size: 1.1rem;
        color: rgba(255, 255, 255, 0.8);
        line-height: 1.6;
        max-width: 600px;
        margin: 0;
        text-align: center;
    }
    
    /* Scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(255, 255, 255, 0.05);
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #6366f1, #8b5cf6);
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #8b5cf6, #a855f7);
    }
    
    /* Mobile responsive */
    @media (max-width: 768px) {
        .user-message {
            margin-left: 5%;
        }
        
        .aspasia-message {
            margin-right: 5%;
        }
        
        .input-section {
            padding: 1.5rem;
        }
        
        .chat-interface {
            padding: 0 1rem 2rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)

def create_particles():
    particles_html = '<div class="particles">'
    for i in range(50):
        left = random.randint(0, 100)
        delay = random.uniform(0, 15)
        duration = random.uniform(10, 20)
        particles_html += f'''
        <div class="particle" style="
            left: {left}%; 
            animation-delay: {delay}s;
            animation-duration: {duration}s;
        "></div>
        '''
    particles_html += '</div>'
    return particles_html

def create_cosmic_background():
    return '''
    <div class="cosmic-bg"></div>
    '''

# --- Streamlit App ---
st.set_page_config(
    page_title="Aspasia AI - Philosophical Companion",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load the revolutionary CSS
load_revolutionary_css()

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "is_thinking" not in st.session_state:
    st.session_state.is_thinking = False

# Create background elements
st.markdown(create_cosmic_background(), unsafe_allow_html=True)
st.markdown(create_particles(), unsafe_allow_html=True)

# Main app container
st.markdown('<div class="app-container">', unsafe_allow_html=True)

# Header section
st.markdown('''
<div class="header-section">
    <h1 class="main-title">ASPASIA</h1>
    <p class="subtitle">AI Philosopher • Wisdom Seeker • Consciousness Explorer</p>
</div>
''', unsafe_allow_html=True)

# Chat interface
st.markdown('<div class="chat-interface">', unsafe_allow_html=True)

# Input section
st.markdown('<div class="input-section">', unsafe_allow_html=True)

user_input = st.text_input(
    "Message",
    placeholder="What profound questions occupy your mind today?",
    key="user_input",
    label_visibility="collapsed"
)

if st.button("✨ Engage with Aspasia", use_container_width=True):
    if user_input.strip():
        st.session_state.is_thinking = True
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

# Thinking indicator
if st.session_state.is_thinking:
    st.markdown('''
    <div class="thinking-container">
        <div class="thinking-bubble">
            <span class="thinking-text">Aspasia contemplates your inquiry</span>
            <div class="thinking-dots">
                <div class="thinking-dot"></div>
                <div class="thinking-dot"></div>
                <div class="thinking-dot"></div>
            </div>
        </div>
    </div>
    ''', unsafe_allow_html=True)
    
    # Process the response
    time.sleep(2)  # Dramatic pause
    aspasia_reply = call_ollama_mistral(user_input, st.session_state.chat_history)
    st.session_state.chat_history.append({
        "user": user_input,
        "aspasia": aspasia_reply
    })
    st.session_state.is_thinking = False
    st.rerun()

# Chat messages
if st.session_state.chat_history:
    for i, turn in enumerate(reversed(st.session_state.chat_history)):
        st.markdown(f'''
        <div class="message-container">
            <div class="user-message">
                <span class="message-icon user-icon"></span>
                {turn["user"]}
            </div>
        </div>
        ''', unsafe_allow_html=True)
        
        st.markdown(f'''
        <div class="message-container">
            <div class="aspasia-message">
                <span class="message-icon aspasia-icon"></span>
                {turn["aspasia"]}
            </div>
        </div>
        ''', unsafe_allow_html=True)
    
    # Clear button
    if st.button("🌊 Clear Conversation", use_container_width=True):
        st.session_state.chat_history = []
        st.rerun()

else:
    # Welcome message
    st.markdown('''
    <div class="welcome-container">
        <h2 class="welcome-title">Welcome, Seeker of Wisdom</h2>
        <p class="welcome-text">
            I am Aspasia of Miletus, ready to explore the depths of philosophy, consciousness, 
            and human understanding with you. Ask me anything that stirs your intellectual curiosity, 
            and let us embark on a journey of discovery together.
        </p>
    </div>
    ''', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # Close chat-interface
st.markdown('</div>', unsafe_allow_html=True)  # Close app-container

# Auto-refresh for smooth animations
if st.session_state.is_thinking:
    time.sleep(0.1)
    st.rerun()