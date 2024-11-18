from pydantic import BaseModel, EmailStr, Field, validator

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6)
    age: int

    @validator('age')
    def age_must_be_adult(cls, value):
        if value < 18:
            raise ValueError('Age must be 18 or older')
        return value


