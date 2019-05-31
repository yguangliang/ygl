from django.http import HttpResponse

from blog.models import  Article

# 视图处理的地方
# Create your views here.hello_world视图函数来返回字符串helloworld


def hello_world(request):
    return HttpResponse("hello world!")


def article_content(request):
    article = Article.objects.all()[0]
    title = article.title
    brief_content = article.brief_content
    content = article.article_id
    publish_date = article.publish_date
    return_str = "title:%s,brief_content:%s," \
                 "content:%s,publish_date:%s" % (title, brief_content, content, publish_date)

    return HttpResponse(return_str)
