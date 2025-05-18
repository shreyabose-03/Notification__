from models.notification import NotificationRequest
from core.rabbitmq import publish_to_queue
from core.storage import save_notification, get_notifications_for_user

async def send_notification(notification: NotificationRequest) -> str:
    save_notification(notification)
    publish_to_queue(notification.dict())
    return f"Notification queued for {notification.type}"

def get_user_notifications(user_id: int):
    return get_notifications_for_user(user_id)
