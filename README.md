## Социальная сеть Yatube с API.
### Описание. 
Yatube - это социальная сеть. 
Пользователи могут зарегистрироваться и могут отправлять статьи, сообщения и т.д. Эти статьи могут входить в некоторые группы. Пользователи могут подписаться к каким-либо авторам.
Для приложения был разработан API.

### Стэк технологий.
- Python 3.9
- Django 3.2.16
- Django rest framework
- SQLite3, ORM
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
<summary><strong>GET /api/v1/posts/</strong> - Просмотр список постов</summary>
<pre>
{
  [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    },
    
    ...
    
  ]
}
</pre>
</details>  

<details>
<summary><strong>GET /api/v1/posts/?offset=50&limit=10</strong> - Просмотр список десяти постов</summary>
<pre>
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=60&limit=10",
  "previous": "http://api.example.org/accounts/?offset=40&limit=10",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    },
    
    ...
    
  ]
}
</pre>
</details>  

<details>
<summary><strong>POST /api/v1/posts/</strong> - Создание нового поста</summary>
<pre>
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
</pre>
</details>  


<details>
<summary><strong>GET /api/v1/posts/{id}/</strong> - Просмотр поста id</summary>
<pre>
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
</pre>
</details>  


<details>
<summary><strong>PATCH /api/v1/posts/{id}/</strong> - Изменение поста id</summary>
<pre>
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
</pre>
</details>  


<details>
<summary><strong>PUT /api/v1/posts/{id}/</strong> - Изменение поста id</summary>
<pre>
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
</pre>
</details>  


**DELETE /api/v1/posts/{id}/** - Удалине поста id

<details>
<summary><strong>GET /api/v1/posts/{post_id}/comments/</strong> - Просмотр список комментарий поста post_id</summary>
<pre>
[
  {
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
  },
  
  ...
  
]
</pre>
</details>  


<details>
<summary><strong>POST /api/v1/posts/{post_id}/comments/</strong> - Создание нового комментария поста post_id</summary>
<pre>
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
</pre>
</details>  


<details>
<summary><strong>GET /api/v1/posts/{post_id}/comments/{id}/</strong> - Просмотр комментария</summary>
<pre>
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
</pre>
</details>  


<details>
<summary><strong>PATCH /api/v1/posts/{post_id}/comments/{id}/</strong> - Изменение комментария</summary>
<pre>
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
</pre>
</details>  


<details>
<summary><strong>PUT /api/v1/posts/{post_id}/comments/{id}/</strong> - Изменение комментария</summary>
<pre>
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
</pre>
</details>  

  
**DELETE /api/v1/posts/{post_id}/comments/{id}/** - Удаление комментария

<details>
<summary><strong>GET /api/v1/group/</strong> - Просмотр список десяти групп</summary>
<pre>
[
  {
    "id": 0,
    "title": "string",
    "slug": "string",
    "description": "string"
  },
  
  ...
  
]
</pre>
</details>  


<details>
<summary><strong>GET /api/v1/group/{id}/</strong> - Просмотр группы id</summary>
<pre>
{
  "id": 0,
  "title": "string",
  "slug": "string",
  "description": "string"
}
</pre>
</details>  


<details>
<summary><strong>GET /api/v1/follow/</strong> - Просмотр список последователей</summary>
<pre>
[
  {
    "user": "string",
    "following": "string"
  },
  
  ...
  
]
</pre>
</details>  


<details>
<summary><strong>POST /api/v1/follow/</strong> - Подписание последователя</summary>
<pre>
{
  "user": "string",
  "following": "string"
}
</pre>
</details>  

### Автор.
Выполнено **Зюзиным Андреем** в качестве проектного задания Яндекс.Практикум
