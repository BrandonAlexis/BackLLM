from fastapi import APIRouter
from openai import OpenAI

from interfaces.chatinterfaces import ChatCompletionResponse, InputMessage

router = APIRouter()

client = OpenAI(api_key='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',
                base_url='https://openrouter.ai/api/v1')

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

    