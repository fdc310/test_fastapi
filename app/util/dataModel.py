from pydantic import BaseModel

class Audio_list(BaseModel):
    page: int
    page_size: int


class Login_Data(BaseModel):
    phone: str
    code: str = None
    password: str = None


class Chat_replymeg(BaseModel):
    item: dict