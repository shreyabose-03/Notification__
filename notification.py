from pydantic import BaseModel, field_validator
from typing import Literal

class NotificationRequest(BaseModel):
    user_id: int
    type: Literal["email", "sms", "in_app"]
    recipient: str
    message: str

    @field_validator("recipient")
    @classmethod
    def validate_recipient(cls, value, values):
        notif_type = values.data.get("type")
        if notif_type == "email":
            if "@" not in value or "." not in value:
                raise ValueError("Invalid email address")
        elif notif_type == "sms":
            if not value.isdigit() or len(value) < 10:
                raise ValueError("Invalid phone number")
        elif notif_type == "in_app":
            if not value:
                raise ValueError("Recipient must be provided for in-app notification")
        return value

class NotificationResponse(BaseModel):
    status: str
    message: str
