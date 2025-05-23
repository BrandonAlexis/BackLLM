from fastapi import APIRouter
from openai import OpenAI


from interfaces.chatinterfaces import ChatCompletionResponse, InputMessage

router = APIRouter()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    default_headers={
        "Authorization": "Bearer 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",
        "HTTP-Referer": "https://fronllm.onrender.com",  # Cambia esto a tu dominio
        "X-Title": "MiniChatGPT Brandon"
    }
)

@router.post("/ai-chat")
def aiChat(data: InputMessage):
    data = data.model_dump()
    print("message " + data["message"])
    
    message = "Por favor responde de manera concreta, clara y siempre en castellano, español."

    try:
        completion: ChatCompletionResponse = client.chat.completions.create(
            model=data["model"],  # Usamos el modelo proporcionado por el usuario
            messages=[
                {"role": "system", "content": message},
                {"role": "user", "content": data["message"]}
            ]
        )
        print("response " + completion.choices[0].message.content)
        return {"response": completion.choices[0].message.content}
    except Exception as e:
        print(f"Error: {e}")
        return {"error": str(e)}

    
