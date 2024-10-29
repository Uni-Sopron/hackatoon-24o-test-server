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

#### Setting up the environment

```bash
cp .env.sample .env
```

Replace the correct ip address in the `.env` file.

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
