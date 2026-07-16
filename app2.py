import ollama

response=ollama.chat(
    model="gemma3",
    messages=[
        {
            "role":"user",
            "content":"Hellow"
        }
    ]
)
print(response["message"]["content"])