from typing import List
from fastapi import FastAPI, HTTPException 
from models import User, Gender,Role
from uuid import uuid4,UUID
app = FastAPI()


db: List[User] = [
    User(id=uuid4(),
    firstname = "punit", 
    lastname="Gautam",
    gender=Gender.male,
    roles = [Role.student]),

    User(id=uuid4(),firstname = "Supriya", 
    lastname="Kulkarni",
    gender=Gender.male,
    roles = [Role.student]),

    User(id=uuid4(),firstname = "Alex", 
    lastname="jamkhed",
    gender=Gender.female,
    roles = [Role.student]),
    ]


#Get Data
@app.get("/")
async def root():
    return {"hello" : "world"}

#Get with Db methods defined
@app.get("/api/v1/user/")
async def fetch_user():
    print("this is the data")
    return db

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id" : user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user : UUID):
    for user in db:
        db.remove(user)
        return
    raise HTTPException(
        status_code = 404,
        detail = f"user_id : {user_id} does not exist"
    )

@app.put("/api/v1/users/{user_id}")
async def update_user(user_update : Userupaterequest, user_id : UUID):
    for user in db:
        if user.id == user_id:
            if user_update.firstname is not None:
                user.firstname = user_update.firstname
            if user_update.lastname is not None:
                user.firstname = user_update.firstname
            return
    raise HTTPException(
        status_code = 404,
        detail=f"user with id {user_id} does not exists "
    )