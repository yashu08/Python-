import openai

openai.api_key = "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"

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages=[{"role": "user", "content":prompt}]
    )

    return response.choices[0].messages.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("you: ")
        if user_input.lower() in ["quit", "exit" , "bye"]:
            break

        response = chat_with_gpt(user_input)
        print("chatbot: " , response)