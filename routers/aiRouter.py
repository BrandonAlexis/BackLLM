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
