from jose import JWTError, jwt
from datetime import datetime, timedelta
import hashlib


SECRET_KEY = "ai-email-agent-secret-key"

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 60



# =========================
# PASSWORD HASH
# =========================

def hash_password(password: str):

    return hashlib.sha256(
        password.encode("utf-8")
    ).hexdigest()



def verify_password(
    plain_password: str,
    hashed_password: str
):

    hashed = hashlib.sha256(
        plain_password.encode("utf-8")
    ).hexdigest()

    return hashed == hashed_password



# =========================
# JWT TOKEN
# =========================

def create_access_token(data: dict):

    to_encode = data.copy()


    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )


    to_encode.update(
        {
            "exp": expire
        }
    )


    token = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )


    return token



def verify_token(token: str):

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return payload


    except JWTError:

        return None
    
# Alias pour compatibilité avec routes.py
def create_token(data: dict):
    return create_access_token(data)