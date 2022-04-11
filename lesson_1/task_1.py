"""
Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для
конкретного пользователя, сохранить JSON-вывод в файле *.json.

"""

import requests
import json


def get_data(user):

    req = requests.get(f'https://api.github.com/users/{user}/repos')
    data = json.loads(req.text)
    repo_dict = {}
    for item in data:
        repo_dict[item['name']] = item['url']

    return repo_dict


def write_file(data, user):

    with open(f'{user}_repos.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def main():
    user = input('Введите логин пользователя: ')
    data = get_data(user)
    write_file(data, user)


if __name__ == '__main__':
    main()
