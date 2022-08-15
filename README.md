# NewEventsSite
定期対バンライブサイト

## Version

- python: 3.9.7
- jquery: v3.6.0
- Bootstrap: v5.0.2
- ApexCharts: v3.35.1

## 仮想環境起動手順

### Mac

```
$ source reserve_env/bin/activate
$ python reserve_tool/manage.py runserver
```

### Windows 

``` 
$ reserve_env¥Scripts¥activate
$ python reserve_tool/manage.py runserver
```

### 起動確認

http://localhost:8000

## ModelsをDBに反映する

```
$ python manage.py makemigrations
$ python manage.py migrate
```

## スーパーユーザの作成

```
$ python manage.py createsuperuser
```
