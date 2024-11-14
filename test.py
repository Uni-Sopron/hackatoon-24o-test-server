from time import sleep
import requests


def register_player(name, ip):
    register_url = "http://localhost:8000/register"
    register_params = {"name": name, "ip": ip}
    register_response = requests.post(register_url, params=register_params)
    register_data = register_response.json()
    return register_data["secret"]


def deploy_player(name, secret, robot_id, col, row):
    deploy_url = "http://localhost:8000/deploy"
    deploy_params = {
        "name": name,
        # "team_secret": secret,
        "robot_id": robot_id,
        "robot_col": col,
        "robot_row": row,
    }
    deploy_response = requests.post(deploy_url, params=deploy_params)
    return deploy_response.text


def reset_game():
    reset_url = "http://localhost:8000/reset"
    conf = {
        "level": "test_maps/small_2p.json",
        "turn_duration": 1.75,
        "robot_request_timeout": 0.3,
        "secret": "mindmeghalunk"
    }
    requests.post(reset_url, json=conf)


while True:
    state = requests.get("http://localhost:8000/state").json()
    if state["state"] == "Game has ended.":
        print(state["scores"])
        reset_game()
        sleep(5)
    elif state["state"] == "Waiting for teams...":
        secret1 = register_player("teszt", "host.docker.internal:5555")
        secret2 = register_player("teszt2", "host.docker.internal:5555")
        print(secret1, secret2)
    else:
        deploy_player("teszt", secret1, 0, 2, 3)
        deploy_player("teszt2", secret2, 0, 17, 3)
    sleep(1)
