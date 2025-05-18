from fastapi import APIRouter, HTTPException
from models.notification import NotificationRequest, NotificationResponse
from services.notification_service import send_notification, get_user_notifications
from typing import List

router = APIRouter()

@router.post("/notifications", response_model=NotificationResponse)
async def create_notification(notification: NotificationRequest):
    try:
        result = await send_notification(notification)
        return NotificationResponse(status="success", message=result)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/users/{user_id}/notifications", response_model=List[NotificationRequest])
async def fetch_user_notifications(user_id: int):
    try:
        return get_user_notifications(user_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
