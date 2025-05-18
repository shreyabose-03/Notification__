from models.notification import NotificationRequest
from typing import List

notification_store: List[NotificationRequest] = []

def save_notification(notification: NotificationRequest):
    notification_store.append(notification)

def get_notifications_for_user(user_id: int) -> List[NotificationRequest]:
    return [n for n in notification_store if n.user_id == user_id]
