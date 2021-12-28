from pprint import pprint

from app import APP_KEY, APP_SECRET, CONSUMER_KEY, ENDPOINT, ovh_request


def main():
    res = ovh_request(
        app_key=APP_KEY,
        app_secret=APP_SECRET,
        consumer_key=CONSUMER_KEY,
        endpoint=ENDPOINT,
        method="GET",
        target="/dedicated/server",
    )
    pprint(res)


if __name__ == "__main__":
    main()
