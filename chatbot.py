import re
import sys
import random
import string
import time

class AKAZA:
    def __init__(self):
        self.user_has_visited = False
        self.interaction_count = 0
        self.unlocked_badges = []
        self.ai_knowledge = {
            "what is ai": "AI stands for Artificial Intelligence. It's basically teaching machines to think and learn from data instead of just following fixed rules.",
            "machine learning": "Machine Learning is a subset of AI where systems improve automatically through experience. Like how Spotify knows what music you like.",
            "deep learning": "Deep Learning uses neural networks with many layers to analyze data. It's what powers face recognition and voice assistants.",
            "neural network": "Think of neural networks as digital brains. They use layers of algorithms to find patterns in data, inspired by the human brain.",
            "what is python": "Python is the most popular programming language for AI. It's simple, readable and has powerful libraries like TensorFlow and scikit-learn."
        }
        self.aiu_info = {
            "courses": "AIU offers programmes like Cybersecurity & AI, Computer Science, Information Technology and Business Information Systems. Visit aiu.ac.ke for the full list 📚",
            "fees": "Fee structures vary by programme and year of study. Contact the finance office or visit aiu.ac.ke for accurate figures 💰",
            "location": "Africa International University is located along Nairobi's Karen Road. Easy to find, hard to leave 😄",
            "contacts": "You can reach AIU through their website at aiu.ac.ke or visit the admin office on campus 📞",
            "exams": "Exam schedules are usually posted on the student portal. Try not to panic — it's just a test... mostly 😅"
        }        
    def get_response(self, user_input):
        user_input = user_input.lower()
        user_input = user_input.translate(str.maketrans("", "", string.punctuation))
        self.interaction_count += 1
        
        # Intent 1: AI Knowledge
        for topic in self.ai_knowledge:
            if topic in user_input:
                return f"Knowledge mode engaged 🧠: {self.ai_knowledge[topic]}"    
        # Intent 2: AIU Information
        for info in self.aiu_info:
            if info in user_input:
                return f"AIU Info 🏫: {self.aiu_info[info]}"        
        # Intent 3: Career Advice
        if "career" in user_input or "jobs" in user_input or "work" in user_input or "future" in user_input:
            return random.choice([
                "AI opens doors to careers like Machine Learning Engineer, Data Scientist, AI Researcher and Robotics Engineer 🚀",
                "With AI skills you can work in healthcare, finance, cybersecurity, gaming and so much more! The future is yours 💪",
                "Top AI careers right now include Data Analyst, NLP Engineer, Computer Vision Specialist and AI Product Manager 🌟"
            ])
        # Intent 4: Identity (Who is AKAZA)
        if "who are you" in user_input or "what are you" in user_input or "creator" in user_input or "who made you" in user_input:
            return random.choice([
                "I am AKAZA — Adaptive Knowledge and AI Zone Assistant. Built by Natasha Muthoni who probably should've been sleeping 😭",
                "AKAZA. Your AI and AIU guide. I was created by a brilliant student who chose code over rest 💪",
                "The name's AKAZA. I know things. AI things. AIU things. Basically everything you should've read in the notes 😏"
            ])
        
        if "bye" in user_input or "goodbye" in user_input or "exit" in user_input or "quit" in user_input:
            return "AKAZA shutting down... just kidding 😏 Goodbye! Come back when you need me 👋"  
            # Intent 5: Greetings (Memory-Based)
        if "hi" in user_input or "hello" in user_input or "hey" in user_input:
            if not self.user_has_visited:
                self.user_has_visited = True
                return "Oh, a new human. Welcome to AKAZA 👋 I run things around here. What's your mission today?"
            else:
                return "Back so soon? Did you forget everything I just told you? 😏 What do you need?"
        # Fallback
        return random.choice([
            "Hmm I didn't catch that 🤔 Try asking about AI, machine learning or AIU info!",
            "I'm not sure about that one. Ask me about AI topics or Africa International University 😄",
            "That's beyond my knowledge for now. Try asking about AI or AIU! 👀"
        ])  
# Run AKAZA
bot = AKAZA()
print("=" * 50)
print("   Welcome! I am AKAZA 🤖")
print("   Adaptive Knowledge and AI Zone Assistant")
print("   Type 'bye' to exit")
print("=" * 50)

while True:
    user_msg = input("\nYou: ").strip()
    if not user_msg:
        continue
    print("AKAZA is thinking", end="")
    for _ in range(3):
        time.sleep(0.4)
        print(".", end="", flush=True)
    print()
    response = bot.get_response(user_msg)
    print(f"\nAKAZA: {response}")
    if "bye" in user_msg.lower() or "exit" in user_msg.lower() or "quit" in user_msg.lower():
        break
