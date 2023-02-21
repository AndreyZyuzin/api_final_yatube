## Социальная сеть Yatube с API.
### Описание. 
Yatube - это социальная сеть. 
Пользователи могут зарегистрироваться и могут отправлять статьи, сообщения и т.д. Эти статьи могут входить в некоторые группы. Пользователи могут подписаться к каким-либо авторам.
Для приложения был разработан API.

### Как запустить проект.

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/AndreyZyuzin/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv .venv
```

```
source .venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Примеры запросов API:
/api/v1/posts/
```json
{
  "count": 123,
  "next": "http://...",
  "previous": "http://..",
  "results": [
    {
      "id": 0,
      "autor": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```
