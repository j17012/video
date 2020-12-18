import os
from django.db import models


class UploadFile(models.Model):
    """アップロードされたファイルを表すモデル"""
    file = models.FileField('動画ファイル',upload_to="video/")
    

    def __str__(self):
        """ファイルの絶対パスを返す"""
        return os.path.basename(self.file.path)

class UploadImage(models.Model):
    """アップロードされたファイルを表すモデル"""
    file = models.ImageField(upload_to="image/")  

    def __str__(self):
        """ファイルのURLを返す"""
        return self.file.url
    
class LabelInfo(models.Model):
    """フレーム毎のラベル情報を表すモデル"""
    txt = models.TextField('テキストファイル')
    