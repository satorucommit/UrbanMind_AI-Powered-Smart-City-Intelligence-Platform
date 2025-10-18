from fastapi import APIRouter, Depends
from app.services.auth_service import get_current_active_user
from app.schemas.user import User

router = APIRouter()

@router.get("/protected")
def read_protected_data(current_user: User = Depends(get_current_active_user)):
    return {
        "message": "This is protected data",
        "user": {
            "id": current_user.id,
            "username": current_user.username,
            "email": current_user.email,
            "full_name": current_user.full_name,
            "role": current_user.role,
            "is_active": current_user.is_active
        }
    }

@router.get("/admin-only")
def read_admin_only_data(current_user: User = Depends(get_current_active_user)):
    if current_user.role != "admin":
        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )
    
    return {
        "message": "This is admin-only data",
        "user": {
            "id": current_user.id,
            "username": current_user.username,
            "role": current_user.role
        }
    }