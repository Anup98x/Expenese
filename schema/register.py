

from fastapi import status
from fastapi import HTTPException
from pydantic import BaseModel, EmailStr, field_validator, model_validator


class RegisterCreate(BaseModel):
    full_name:str
    email:EmailStr
    password1:str
    password2:str
    @field_validator("full_name")
    def format_name(cls,value:str):
        return value.strip().title()
    @field_validator("email")
    def format_email(cls,value:str):
        return value.lower()
    @model_validator(mode="after")
    def format_password(cls):
        if cls.password1!=cls.password2:
            raise ValueError("Password not matched")
        return cls
