from fastapi import APIRouter
from openai import OpenAI
from interfaces.chatinterfaces import ChatCompletionResponse, InputMessage

router = APIRouter()

# Cliente de OpenRouter configurado
client = OpenAI(
    api_key="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",
    base_url="https://openrouter.ai/api/v1",
)

# Modelo que usaremos siempre
MODEL = "google/gemma-3n-e4b-it:free"

@router.post("/ai-chat")
def aiChat(data: InputMessage):
    data = data.model_dump()
    print("message " + data["message"])

    # Mensaje del sistema
    system_prompt = "Por favor responde de manera concreta, clara y siempre en castellano, español."

    try:
        # Llamada al modelo fijo con headers
        completion = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": data["message"]}
            ],
            extra_headers={
                "HTTP-Referer": "https://fronllm.onrender.com",
                "X-Title": "MiniChatGPT Brandon"
            },
            extra_body={}
        )

        print("response " + completion.choices[0].message.content)
        return {"response": completion.choices[0].message.content}

    except Exception as e:
        print(f"Error: {e}")
        return {"error": str(e)}
