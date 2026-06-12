import datetime

print("🤖 Hey! I'm Nikki's AI Chatbot 💖 (type 'exit' to quit)")
#name = input("Enter your name: ")
#print(f"🤖 Hello {name}! I'm your AI chatbot 💖")
responses = {
    "hello": "Heyy Nikki! 👋",
    "how are you": "I'm doing awesome 😄",
    "your name": "I'm your AI Assistant 🤖",
    "good morning": "Good morning Nikki! ☀️",
    "good night": "Sweet dreams 😴",
    "thanks": "You're welcome 💖",
    "who made you": "Nikki created me 😎",
    "help": "Try typing: time, date, joke, hello, bye"
    
}

while True:
    user_input = input("You: ").lower().strip()

    if user_input == "exit":
        print("Bot: Goodbye Nikki! 👋")
        break

    elif user_input == "time":
        now = datetime.datetime.now().strftime("%H:%M:%S")
        print("Bot: Current time is", now)

    elif user_input == "date":
        today = datetime.date.today()
        print("Bot: Today's date is", today)

    elif user_input == "joke":
        print("Bot: Why do programmers hate nature? Too many bugs 🐛😂")

    elif "hello" in user_input:
        print("Bot: Heyy Nikki! 👋")

    else:
        response = responses.get(user_input, "Hmm... I didn't understand that 🤔")
        print("Bot:", response)