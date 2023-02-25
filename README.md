## Социальная сеть Yatube с API.
### Описание. 
Yatube - это социальная сеть. 
Пользователи могут зарегистрироваться и могут отправлять статьи, сообщения и т.д. Эти статьи могут входить в некоторые группы. Пользователи могут подписаться к каким-либо авторам.
Для приложения был разработан API.

### Стэк технологий.
- django rest framework
- Базы данных, ORM
- 
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

<details>
<summary>GET /api/v1/posts/ - Просмотр список десяти постов</summary>
Тут текст который вы хотим скрыть
</details>  

GET /api/v1/posts/?offset=50&limit=10 - Просмотр список десяти постов

POST /api/v1/posts/ - Создание нового поста

GET /api/v1/posts/{id}/ - Просмотр поста id

PATCH /api/v1/posts/{id}/ - Изменение поста id

PUT /api/v1/posts/{id}/ - Изменение поста id

DELETE /api/v1/posts/{id}/ - Удалине поста id

GET /api/v1/posts/{post_id}/comments/ - Просмотр список комментарий поста post_id

POST /api/v1/posts/{post_id}/comments/ - Создание нового комментария поста post_id

GET /api/v1/posts/{post_id}/comments/{id}/ - Просмотр комментария

PATCH /api/v1/posts/{post_id}/comments/{id}/ - Изменение комментария

PUT /api/v1/posts/{post_id}/comments/{id}/ - Изменение комментария

DELETE /api/v1/posts/{post_id}/comments/{id}/ - Удаление комментария

GET /api/v1/group/ - Просмотр список десяти групп

GET /api/v1/group/{id}/ - Просмотр группы id

GET /api/v1/follow/ - Просмотр список последователей

POST /api/v1/follow/ - Подписание последователя

### Автор.
Выполнено **Зюзиным Андреем** в качестве проектного задания Яндекс.Практикум
