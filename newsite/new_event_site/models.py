from unicodedata import name
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class UsersMaster(AbstractUser):
    """ユーザマスタ
    
    ユーザマスタテーブルを表すクラス
    
    """

    login_id = models.TextField(unique=True)
    password = models.TextField(unique=False)
    mail_address = models.TextField(unique=True)

    REQUIRED_FIELDS = ["login_id", "password"]

    class Meta:
        db_table = 'mst_users'

class GenresMaster(models.Model):
    """ジャンルマスタ
    
    ジャンルを表すテーブル
    
    """

    genre_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'mst_genres'

class CategoriesMater(models.Model):
    """カテゴリマスタ"""

    category_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'mst_categories'
        
class EventsMaster(models.Model):
    """イベントマスタ
    
    イベントテーブルを表すクラス
    
    """

    event_id = models.IntegerField(unique=True)
    event_title = models.CharField(max_length=255)
    date = models.DateField()
    open_time = models.TimeField()
    start_time = models.TimeField()
    place = models.CharField(max_length=255)
    site_open_time = models.TimeField()

    class Meta:
        db_table = 'mst_events'

class ArtistsMaster(models.Model):
    """アーティストマスタ
    
    アーティストテーブルを表すクラス
    
    """

    name = models.CharField(max_length=255)
    artist_image = models.ImageField()
    category = models.ForeignKey(CategoriesMater, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'mst_artists'

class TicketsMaster(models.Model):
    """チケットマスタ
    
    チケット情報を表すクラス
    
    """

    event_id = models.ForeignKey(EventsMaster, on_delete=models.CASCADE)
    price = models.IntegerField()
    sale_start_date = models.DateTimeField()
    sale_end_date = models.DateTimeField()
    url = models.URLField()

    class Meta:
        db_table = 'mst_tickets'

class PlacesMaster(models.Model):
    """会場マスタ
    
    会場を表すテーブル
    
    """

    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    station = models.CharField(max_length=255)
    place_image = models.ImageField()
    url = models.URLField()
    map = models.URLField()

    class Meta:
        db_table = 'mst_places'

class GroupArtistsMaster(models.Model):
    """グループマスタ
    
    グループを表すテーブル
    
    """

    name = models.CharField(max_length=255)
    genre = models.ForeignKey(GenresMaster, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'mst_groups'

class TimeTablesMaster(models.Model):
    """タイムテーブルマスタ
    
    タイムテーブル情報テーブル
    
    """

    class Meta:
        db_table = 'mst_time_tables'

class ImagesMaster(models.Model):
    """画像マスタ"""

    event_id = models.ForeignKey(EventsMaster, on_delete=models.CASCADE)
    image_file = models.ImageField()

    class Meta:
        db_table = 'mst_image'

class NewsMaster(models.Model):
    """ニュースマスタ"""

    event_id = models.ForeignKey(EventsMaster, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    open_date = models.DateTimeField()

    class Meta:
        db_table = 'mst_news'
