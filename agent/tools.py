import os
import random
from datetime import datetime, timezone

SHOPIFY_SHOP_URL = os.environ.get("SHOPIFY_SHOP_URL")
SHOPIFY_ACCESS_TOKEN = os.environ.get("SHOPIFY_ACCESS_TOKEN")
SHOPIFY_API_VERSION = "2024-10"

BUFFER_ACCESS_TOKEN = os.environ.get("BUFFER_ACCESS_TOKEN")
BUFFER_PROFILE_ID = os.environ.get("BUFFER_PROFILE_ID")


def check_inventory(product_name: str) -> dict:
    """Mocked Shopify call — returns a fake but realistic-looking stock response."""
    quantity = random.randint(0, 100)
    return {
        "product": product_name,
        "in_stock": quantity > 0,
        "quantity": quantity,
    }


def write_copy(topic: str, tone: str = "friendly") -> dict:
    """Mocked copy generation — no live LLM call, just a templated placeholder."""
    copy_text = f"Check out {topic}! (written in a {tone} tone)"
    return {
        "topic": topic,
        "tone": tone,
        "copy": copy_text,
    }


def schedule_post(content: str, post_time: str) -> dict:
    """Mocked Buffer call — pretends the post was scheduled successfully."""
    scheduled_at = int(
        datetime.strptime(post_time, "%Y-%m-%d %H:%M").replace(tzinfo=timezone.utc).timestamp()
    )
    return {
        "success": True,
        "bufferprofile_ids": [BUFFER_PROFILE_ID],
        "updates": [
            {
                "id": "mock_update_id_12345",
                "status": "buffer",
                "text": content,
                "scheduled_at": scheduled_at,
                "profile_id": BUFFER_PROFILE_ID,
            }
        ],
    }


if __name__ == "__main__":
    print(check_inventory("Blue T-Shirt"))
    print(write_copy("our new summer collection"))
    print(schedule_post("Our new summer collection just dropped!", "2026-08-15 09:00"))
