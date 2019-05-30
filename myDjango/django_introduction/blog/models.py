from django.db import models
# 定义应用模型的地方
# Create your models here.


class Article(models.Model):
    # 文章的唯一 ID
    article_id = models.AutoField(primary_key=True)
    # 文章标题
    title = models.TextField()
    # 文章摘要
    brief_content = models.TextField()
    # 文章的主要内容
    content = models.TextField()
    # 文章的发布时间
    publish_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title