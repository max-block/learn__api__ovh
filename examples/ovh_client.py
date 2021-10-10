import ovh

from examples import APP_KEY, APP_SECRET, CONSUMER_KEY


def main():
    client = ovh.Client(
        endpoint="ovh-eu",
        application_key=APP_KEY,
        application_secret=APP_SECRET,
        consumer_key=CONSUMER_KEY,
    )
    print(client.get("/me"))


if __name__ == "__main__":
    main()
