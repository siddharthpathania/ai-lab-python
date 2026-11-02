# B4 Rule-based Chatbot - check rules top to bottom; the first rule that matches gives the reply.
# or  -> any ONE of the words is enough
# and -> ALL the words must be there
name = ""
print("Bot: Hello! Type 'bye' to exit.")

while True:
    text = input("You: ").lower()

    if "bye" in text or "exit" in text:
        print("Bot: Goodbye!")
        break
    elif "my name is" in text:
        name = text.split("my name is")[1].strip()
        print("Bot: Nice to meet you,", name)
    elif "what" in text and "my name" in text:
        print("Bot: Your name is", name or "not told yet")
    elif "hello" in text or "hi" in text or "hey" in text:
        print("Bot: Hi there!")
    elif "how" in text and "you" in text:
        print("Bot: I'm fine, thanks!")
    elif "your name" in text:
        print("Bot: I am a rule-based chatbot.")
    elif "ai" in text or "artificial intelligence" in text:
        print("Bot: AI means making machines act intelligently.")
    elif "thank" in text:
        print("Bot: You're welcome!")
    else:
        print("Bot: Sorry, I don't understand.")
