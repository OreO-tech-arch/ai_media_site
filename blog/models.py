from django.db import models
from django.utils import timezone

class Post(models.Model):
    # 記事のタイトル（文字数制限200文字）
    title = models.CharField(max_length=200)
    
    # 記事の本文（文字数無制限）
    text = models.TextField()
    
    # 作成日（自動で現在時刻が入る）
    created_date = models.DateTimeField(default=timezone.now)
    
    # AIツールの名前（例：ChatGPT, Claudeなど）
    ai_tool_name = models.CharField(max_length=100, blank=True, null=True)

    # 管理画面でタイトルを表示するための設定
    def __str__(self):
        return self.title