from fastapi import APIRouter

from app.database.database import SessionLocal

from app.database.models import User

from app.auth.security import (
    hash_password,
    verify_password,
    create_token
)



router = APIRouter()



@router.post("/register")
def register(data:dict):

    db = SessionLocal()


    user = User(

        username=data["username"],

        email=data["email"],

        hashed_password=
        hash_password(
            data["password"]
        )

    )


    db.add(user)

    db.commit()

    db.close()


    return {
        "message":
        "User created"
    }






@router.post("/login")
def login(data:dict):


    db = SessionLocal()


    user = (

        db.query(User)

        .filter(
            User.email ==
            data["email"]
        )

        .first()

    )



    db.close()



    if not user:

        return {
            "error":
            "Invalid credentials"
        }




    if not verify_password(
        data["password"],
        user.hashed_password
    ):

        return {
            "error":
            "Invalid credentials"
        }




    token=create_token(

        {
            "sub":
            user.email
        }

    )


    return {

        "access_token":
        token,

        "token_type":
        "bearer"

    }