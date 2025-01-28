from fastapi import HTTPException


def throw_unauthorized_exception():
    raise HTTPException(
        status_code=401,
        detail="[인증 실패] Secret Key가 일치하지 않습니다. 확인 후 다시 시도해 주세요."
    )
