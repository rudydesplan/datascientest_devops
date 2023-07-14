from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from config import config

security = HTTPBasic()

def get_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    authorized_usernames = [config.ADMIN_USERNAME] + list(config.AUTHORIZED_USERS.keys())
    if credentials.username not in authorized_usernames:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username",
            headers={"WWW-Authenticate": "Basic"},
        )

    correct_password = config.AUTHORIZED_USERS.get(credentials.username)
    if credentials.username == config.ADMIN_USERNAME:
        correct_password = config.ADMIN_PASSWORD

    if not correct_password or correct_password != credentials.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username, credentials.password
