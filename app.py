import time

import google.generativeai as genai

API_KEY = "AIzaSyAboDpPm77ZEmlnGyyRK-Ta518yv6e9p9Q"
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()

print("Chat with gemini! Type 'exit' to quit")
while True:
    user_input = input("You:    ")
    if user_input.lower() == "exit":
        break
    response = chat.send_message(user_input)
    print("Gemini:  ", end='', flush=True)
    for char in response.text:
        print(char, end='', flush=True)
        time.sleep(0.02)
    print()