import hashlib
import os
from typing import Literal

import requests
from dotenv import load_dotenv

load_dotenv()

APP_KEY = os.getenv("APP_KEY")
APP_SECRET = os.getenv("APP_SECRET")
CONSUMER_KEY = os.getenv("CONSUMER_KEY")
ENDPOINT = "https://eu.api.ovh.com/1.0"


def ovh_request(*, app_key: str, app_secret: str, consumer_key: str, endpoint: str, method: Literal["GET", "POST"], target: str):
    target = endpoint + target
    body = ""
    res = requests.get(f"{endpoint}/auth/time")
    timestamp = res.text
    signature = hashlib.sha1(f"{app_secret}+{consumer_key}+{method}+{target}+{body}+{timestamp}".encode("utf-8")).hexdigest()
    headers = {
        "X-Ovh-Application": app_key,
        "X-Ovh-Consumer": consumer_key,
        "X-Ovh-Timestamp": timestamp,
        "X-Ovh-Signature": f"$1${signature}",
    }
    res = requests.request(method, target, headers=headers)
    return res.json()
