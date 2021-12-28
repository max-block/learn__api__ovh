set dotenv-load := false
set positional-arguments

test:
    python -m app.test

list_servers:
    python -m app.list_servers

get_server server_name:
    python -m app.get_server $1