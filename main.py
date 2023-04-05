import os
import yaml
import openai


with open(".api_key", 'r') as api_file:
    api = yaml.safe_load(api_file)

openai.api_key = api["open_ai_key"]

messages = []
while True:
    content = input("User input: ") 
    messages.append({"role": "user", "content": content})

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    chat_response = completion.choices[0].message.content
    print(f'ChatGPT says: {chat_response}')
    message.append({"role": "assistant", "content": chat_response})
