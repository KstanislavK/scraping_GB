"""
Изучить список открытых API (https://www.programmableweb.com/category/all/apis). Найти среди них любое,
требующее авторизацию (любого типа). Выполнить запросы к нему, пройдя авторизацию. Ответ сервера записать в файл.
Если нет желания заморачиваться с поиском, возьмите API вконтакте (https://vk.com/dev/first_guide).
Сделайте запрос, чтобы получить список всех сообществ на которые вы подписаны.
"""
import json
import os
import requests
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)


def main(user_id):

    url = f'https://api.vk.com/method/groups.get?user_id={user_id}&extended=1&access_token={os.environ.get("VK_API_KEY")}&v=5.131'

    req = requests.get(url).json()

    with open(f'{user_id}_communities.json', 'w', encoding='utf-8') as file:
        json.dump(req, file, ensure_ascii=False, indent=4)

    print('Work is done, master!')


if __name__ == '__main__':
    user_id = input('Введите ID юзера')
    main(user_id)
