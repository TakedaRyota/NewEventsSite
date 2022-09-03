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
$ source env/bin/activate
$ python newsite/manage.py runserver
```

### Windows 

``` 
$ env¥Scripts¥activate
$ python newsite/manage.py runserver
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

## アイコン
https://icooon-mono.com/

## カラーサイト
https://www.shutterstock.com/ja/blog/neon-color-palettes