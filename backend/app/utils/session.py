from uuid import uuid4
from datetime import datetime


def generate_session_id() -> str:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    random_id = uuid4().hex[:6]
    return f"SS_{timestamp}_{random_id}"