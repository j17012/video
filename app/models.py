from django.db import models


class UploadFile(models.Model):
    """アップロードされたファイルを表すモデル"""
    file = models.FileField('動画ファイル')

    def __str__(self):
        """ファイルのURLを返す"""
        return self.file.url

class UploadImage(models.Model):
    """アップロードされたファイルを表すモデル"""
    file = models.ImageField('画像ファイル')  

    def __str__(self):
        """ファイルのURLを返す"""
        return self.file.url
    
class LabelInfo(models.Model):
    """フレーム毎のラベル情報を表すモデル"""
    txt = models.TextField('テキストファイル')
    