from time import sleep
import requests


def register_player(name, ip):
  register_url = 'http://localhost:8000/register'
  register_params = {
      'name': name,
      'ip': ip
  }
  register_response = requests.post(register_url, params=register_params)
  register_data = register_response.json()
  return register_data['secret']


def deploy_player(name, secret, robot_id, col, row):
  deploy_url = 'http://localhost:8000/deploy'
  deploy_params = {
      'name': name,
      'team_secret': secret,
      'robot_id': robot_id,
      'robot_col': col,
      'robot_row': row
  }
  deploy_response = requests.post(deploy_url, params=deploy_params)
  return deploy_response.text


secret1 = register_player('teszt', 'host.docker.internal')
secret2 = register_player('teszt2', 'host.docker.internal')

sleep(0.1)

response1 = deploy_player('teszt', secret1, 0, 2, 3)
# response2 = deploy_player('teszt2', secret2, 0, 17, 3)
