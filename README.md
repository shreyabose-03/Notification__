# Notification Service

A lightweight asynchronous microservice developed with **FastAPI**, **RabbitMQ**, and **in-memory storage** to manage and monitor email, SMS, and in-app notifications.

---

## Features

- API for creating and retrieving notifications
- Retry mechanism for failed message publishing
- Background processing powered by RabbitMQ
- Supports `email`, ``, and `in_app` notifications
- Built using FastAPI with auto-generated OpenAPI documentation
- Simple in-memory storage designed for demonstration purposes

---

## Installation & Setup

### Prerequisites:
1. Docker Desktop
2. RabbitMQ server

### Steps:

1. Create the following Python files:
   - main.py
   - notification_service.py
   - notification.py
   - rabbitmq.py
   - storage.py
   - router.py

2. Clone the repository:
```bash
git clone https://github.com/your-username/notification-service.git
cd notification-service
```

3. Set up a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Start RabbitMQ:
```bash
docker run -d --hostname rabbit --name rabbitmq -p 5672:5672 rabbitmq:3
```

6. Run the application:
```bash
uvicorn main:app --reload
```

7. Access Swagger UI:
http://127.00.1:8000/docs

8. View OpenAPI schema:
http://127.0.0.1:8000/openapi.json
