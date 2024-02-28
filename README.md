```
$ docker-compose up -d
```

Opcional: Criar o superusuario admin:

```
$ docker exec -it bringel_app bash
$ python manage.py createsuperuser --username admin --email email@email.com
```

Defina a senha do superuser

URL: http://localhost:8888/api/


zerar migration:

```
$ python manage.py migrate api zero
```


SWAGGER: http://localhost:8888/swagger/