module_vk
======
module_vk - это модуль для получения списка пользователей исходя из теории шести рукопожатий `WIKI`_
Используется алгоритм обхода графов в ширину (BFS)

Установка
---------
Установите необходимые зависимости:

.. code-block:: text

    pip install -r requirements.txt

Настройка
---------
Создайте файл settings.py

.. code-block:: python

    URL = 'https://api.vk.com/method/'
    VERSION_API = '5.103'
    ACCESS_TOKEN = 'YOUR_API_KEY_FROM_VK.COM'

Использование
------
Импортируйте модуль

.. code-block:: python

    from module_vk import *

В модуле доступны три функции:

* Функция six_handshakes - позволяет получить список пользователей исходя из теории шести рукопожатий

.. code-block:: python

    six_handshakes('user1', 'user2')

* Функция get_friends_list - позволяет получить список друзей пользователя

.. code-block:: python

    get_friends_list('user1')

* Функция get_user_id - позволяет получить id пользователя по его короткому имени - screen_name

.. code-block:: python

    get_user_id('screen_name')

В функции помимо id пользователя можно передавать короткие имена - screen_name

Links
-----

* Youtube: https://www.youtube.com/watch?v=S-hjsamsK8U

.. _WIKI: https://ru.wikipedia.org/wiki/%D0%A2%D0%B5%D0%BE%D1%80%D0%B8%D1%8F_%D1%88%D0%B5%D1%81%D1%82%D0%B8_%D1%80%D1%83%D0%BA%D0%BE%D0%BF%D0%BE%D0%B6%D0%B0%D1%82%D0%B8%D0%B9