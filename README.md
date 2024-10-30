# hackatoon demo

## Requirements

- Python 3.9<
- Docker

## Setup

### Install python dependencies

```bash
pip install -r requirements.txt
```

### Docker initialization

#### Setting up engine ip address (optional)

Replace `VITE_BACKEND_URL` value in the `docker-compose.yml` file with the ip address of the engine.

#### Start

```bash
docker compose up -d
```

#### Stop

```bash
docker compose down
```

## Setting up a test environment

```bash
python test.py
```

Now you just have to start you own agent.

## Agent example

```bash
python -m agent
```
