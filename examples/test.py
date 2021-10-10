from time import time

import requests

from examples import APP_KEY, CONSUMER_KEY


def main():
    timestamp = str(int(time()))
    print(timestamp)
    signature = "$1$" + "..."
    url = "https://api.ovh.com/dedicated/server"
    headers = {
        "X-Ovh-Application": APP_KEY,
        "X-Ovh-Consumer": CONSUMER_KEY,
        "X-Ovh-Timestamp": timestamp,
        "X-Ovh-Signature": signature,
    }
    res = requests.get(url, headers=headers)
    print(res)


if __name__ == "__main__":
    main()
