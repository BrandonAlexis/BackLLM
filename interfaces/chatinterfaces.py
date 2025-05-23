from pydantic import BaseModel

class InputMessage(BaseModel):
    message: str
    model: Optional[str] = None  # ✅ Ahora es opcional

class Usage(BaseModel):
    promt_tokens: int
    completion_tokens: int
    total_tokens: int

class Message(BaseModel):
    content: str

class Choices(BaseModel):
    message: Message

class ChatCompletionResponse(BaseModel):
    model: str
    choices: list[Choices]
    usage: Usage
