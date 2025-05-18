#  Notification Service

A lightweight async microservice built with **FastAPI**, **RabbitMQ**, and **in-memory storage** to send and track email, SMS, and in-app notifications.

---

## Features

-  API for creating and retrieving notifications
-  Retry mechanism for failed message publishing
-  Background processing via RabbitMQ
-  Supports `email`, `sms`, and `in_app` notifications
-  FastAPI-based, with OpenAPI docs auto-generated
-  Simple in-memory storage for demo purposes

---

## 📦 Installation & Setup

## 1. clone the repository

```bash
git clone https://github.com/your-username/notification-service.git
cd notification-service

## 2. Create a Virtual Environment
python -m venv venv
venv\Scripts\activate

## 3. Install Dependencies
pip install -r requirements.txt

## 4. Start RabbitMQ
docker run -d --hostname rabbit --name rabbitmq -p 5672:5672 rabbitmq:3

## 5.Run the App
uvicorn main:app --reload

## 6.Swagger UI:
http://127.0.0.1:8000/docs

## 7.OpenAPI schema:
 http://127.0.0.1:8000/openapi.json


