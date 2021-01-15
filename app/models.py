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
    sec = models.IntegerField(null=True,blank=True)
    man = models.IntegerField(null=True,blank=True)
    pc_char = models.IntegerField(null=True,blank=True)
    white_board = models.IntegerField(null=True,blank=True)
    char_red = models.IntegerField(null=True,blank=True)
    char_yellow = models.IntegerField(null=True,blank=True)
    human_char = models.IntegerField(null=True,blank=True)

