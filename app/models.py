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
    
class LabelInfo(models.Model):
    """フレーム毎のラベル情報を表すモデル"""
    txt = models.TextField('テキストファイル')
    