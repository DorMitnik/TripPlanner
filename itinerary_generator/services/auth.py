        import os
        from typing import Any
        from fastapi import HTTPException
        from jose import jwt, JWTError

        SECRET_KEY = os.environ.get('SECRET_KEY')
        ALGORITHM = "HS256"

        def decrypt_token(token: str) -> dict[str, Any] | None:
            try:
                payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
                if payload:
                    return payload
            except JWTError:
                raise HTTPException(status_code=401, detail="Invalid token")