import sys
from pprint import pprint

from app import APP_KEY, APP_SECRET, CONSUMER_KEY, ENDPOINT, ovh_request


def main():
    server_name = sys.argv[1]
    res = ovh_request(
        app_key=APP_KEY,
        app_secret=APP_SECRET,
        consumer_key=CONSUMER_KEY,
        endpoint=ENDPOINT,
        method="GET",
        target=f"/dedicated/server/{server_name}",
    )
    pprint(res)


if __name__ == "__main__":
    main()
