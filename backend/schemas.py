    from pydantic import BaseModel
    from datetime import datetime


    class UserCreate(BaseModel):
        username: str
        password: str
        email: str


    class UserLogin(BaseModel):
        username: str
        password: str


    class TripCreate(BaseModel):
        destination: str
        start_date: datetime
        end_date: datetime


    class TokenData(BaseModel):
        username: str