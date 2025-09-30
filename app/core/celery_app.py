import ssl
from celery import Celery
from app.core.config import settings

celery_app = Celery(
    "worker",
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL,
)

# Add SSL config for Upstash Redis
celery_app.conf.update(
    broker_use_ssl={
        "ssl_cert_reqs": ssl.CERT_NONE  # disables cert validation (works with Upstash)
    },
    redis_backend_use_ssl={
        "ssl_cert_reqs": ssl.CERT_NONE
    },
    task_routes={"app.tasks.*": {"queue": "default"}},
    task_track_started=True,
    task_serializer="json",
)
