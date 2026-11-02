# B4 Rule-based Chatbot - pattern matching: check rules top to bottom, the first match gives the reply.
# or  -> any ONE of the words is enough
# and -> ALL the words must be there
import random
from datetime import datetime

name = ""
jokes = ["Why did the computer go to the doctor? It had a virus!",
         "Why was the robot tired? It had a hard drive!",
         "Why do programmers like dark mode? Because light attracts bugs!"]

print("Bot: Hello! I am ChatBot. Type 'help' to see what I can do, 'bye' to exit.")

while True:
    text = input("You: ").lower()
    for ch in "?!.,":
        text = text.replace(ch, "")       # remove punctuation: "hi!" -> "hi"
    words = text.split()                  # separate words, so "hi" does not match inside "this"

    if "bye" in words or "exit" in words:
        print("Bot: Goodbye", name or "friend", "- have a nice day!")
        break
    elif "help" in words:
        print("Bot: Try: hello, how are you, my name is ..., what is my name, time, date, joke, what is AI, bye")
    elif "my name is" in text:
        name = text.split("my name is")[1].strip().title()
        print("Bot: Nice to meet you,", name + "!")
    elif "what" in text and "my name" in text:
        print("Bot: Your name is", name or "... you haven't told me yet!")
    elif "hello" in words or "hi" in words or "hey" in words:
        print("Bot: Hi", name or "there", "- how can I help you?")
    elif "how" in words and "you" in words:
        print("Bot: I'm doing great, thanks for asking!")
    elif "who" in words and "you" in words or "your name" in text:
        print("Bot: I am ChatBot, a rule-based chatbot made for the AI lab.")
    elif "time" in words:
        print("Bot: The time is", datetime.now().strftime("%I:%M %p"))
    elif "date" in words or "today" in words:
        print("Bot: Today is", datetime.now().strftime("%d %B %Y"))
    elif "joke" in words:
        print("Bot:", random.choice(jokes))
    elif "ai" in words or "artificial intelligence" in text:
        print("Bot: AI means making machines think and act intelligently, like humans.")
    elif "thank" in text:
        print("Bot: You're welcome!")
    else:
        print("Bot: Sorry, I don't understand. Type 'help' to see what I can do.")
