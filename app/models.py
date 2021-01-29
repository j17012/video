import os
from django.db import models


class UploadFile(models.Model):
    """アップロードされたファイルを表すモデル"""
    file = models.FileField('動画ファイル',upload_to="videos/")
    
    def __str__(self):
        """ファイルの絶対パスを返す"""
        return os.path.abspath(self.file.path)

class UploadImage(models.Model):
    """アップロードされたファイルを表すモデル"""
    file = models.ImageField(upload_to="images/")  

    def __str__(self):
        """ファイルの絶対パスを返す"""
        return os.path.abspath(self.file.url)
    
class Label_Info(models.Model):
    """フレーム毎のラベル情報を表すモデル"""
    ###mov_name = models.CharField('動画名', blank=True, max_length=100)###
    sec = models.TimeField('時間', blank=True, null=True)
    man = models.IntegerField('男性', blank=True, null=True)
    pc_char = models.IntegerField('PC', blank=True, null=True)
    white_board = models.IntegerField('白板', blank=True, null=True)
    char_red = models.IntegerField('赤文字', blank=True, null=True)
    char_yellow = models.IntegerField('黄文字', blank=True, null=True)
    human_char = models.IntegerField('人', blank=True, null=True)

