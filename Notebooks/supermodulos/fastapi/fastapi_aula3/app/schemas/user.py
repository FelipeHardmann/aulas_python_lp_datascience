from pydantic import EmailStr, BaseModel


class User(BaseModel):
    name: str
    email: EmailStr
