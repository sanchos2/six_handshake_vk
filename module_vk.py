from collections import deque
import time

import requests
from tqdm import tqdm

from settings import *


def get_user_id(screen_name):
    """Функция получения id пользователя по его короткому имени(screen_name)."""
    params = {'user_ids': screen_name, 'v': VERSION_API, 'access_token': ACCESS_TOKEN, }
    try:
        raw_user_info = requests.get(URL + 'users.get', params=params)
        raw_user_info.raise_for_status()
        user_id = raw_user_info.json()['response'][0]['id']
        return user_id
    except (requests.RequestException, ValueError, IndexError):
        return False


def get_friends_list(user: int or str) -> list:
    """Функция получения списка друзей в VK по id или screen_name."""
    if isinstance(user, str):
        user = get_user_id(user)
    params = {'user_id': user, 'v': VERSION_API, 'access_token': ACCESS_TOKEN, }
    try:
        raw_users_list = requests.get(URL + 'friends.get', params=params)
        raw_users_list.raise_for_status()
        users_list = raw_users_list.json()
        if 'response' in users_list:
            return users_list['response']['items']
    except(requests.RequestException, ValueError):
        return []


def six_handshakes(id_user1: int or str, id_user2: int or str) -> list:
    """ Функция получения списка id пользователей по теории "Шести рукопожатий. "
     Для улучшения скорости работы функции, id_user1 должен быть с меньшим количесвом
    друзей чем id_user2"""
    if isinstance(id_user1, str):
        id_user1 = get_user_id(id_user1)
    if isinstance(id_user2, str):
        id_user2 = get_user_id(id_user2)
    try:
        queue = deque(get_friends_list(id_user1))
    except TypeError:
        print('Начали с закрытого профиля. Невозможно получить список друзей')
        return []
    distances = {vertex: 1 for vertex in queue}
    parents = {vertex: id_user1 for vertex in queue}
    while id_user2 not in distances:
        current_user = queue.popleft()
        try:
            new_users = get_friends_list(current_user)
            time.sleep(0.2)
            for id_user in tqdm(new_users):
                if id_user not in distances:
                    queue.append(id_user)
                    distances[id_user] = distances[current_user] + 1
                    parents[id_user] = current_user
        except TypeError:
            print('Попался закрытый профиль..продолжаем дальше')
    path = [id_user2]
    parent = parents[id_user2]
    parents[id_user1] = None
    while parent is not None:
        path.append(parent)
        parent = parents[parent]
    return path


if __name__ == '__main__':
    print(six_handshakes('user1', 'user2'))
