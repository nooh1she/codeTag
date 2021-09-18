from django.db import models

# Create your models here.

#問題のモデル
class Problem(models.Model):

    #問題のタイトル
    name = models.CharField('問題', max_length = 50)
    #問題のatcoder URL
    site_url = models.URLField('URL')
    #登録したタグ
    tag = models.CharField('タグ', max_length = 50)
    #書いたコード
    code = models.TextField('自分の書いたコード', blank = True)
    #メモ
    memo = models.TextField('メモ', blank = True)
