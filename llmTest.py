from openai import OpenAI

client = OpenAI(api_key='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',
                base_url='https://openrouter.ai/api/v1')

message = input ("Cual es tu pregunta: ")

prompt = (
    "por favor responde de manera clara y sin simbolos innecesarios."
    "evitar usar otros idiomas que no sean el castellano, españos y escribe una respuesta concisa y directa."
    f"pregunta del usuario es: {message}"
)
completion = client.chat.completions.create(
    model="cognitivecomputations/dolphin3.0-r1-mistral-24b:free",
    messages=[
        {
            "role":"user",
            "content":prompt
        }
    ]
)
print(completion.choices[0].message.content)