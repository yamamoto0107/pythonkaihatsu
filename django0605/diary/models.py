from turtle import update
from django.db import models
from django.utils import timezone
import uuid

# Create your models here.
#日記フォーム：id,日付、タイトル、本文、作成日時、編集日時
class Diary(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    date = models.DateField(verbose_name='日付',default=timezone.now)
    title = models.CharField(verbose_name='タイトル',max_length=40)
    text = models.CharField(verbose_name='本文',max_length=200)
    created_at = models.DateTimeField(verbose_name='作成日時',default=timezone.now)
    updated_at = models.DateTimeField(verbose_name='更新日時',blank=True,null=True)
