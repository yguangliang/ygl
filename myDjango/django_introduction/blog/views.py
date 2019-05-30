from django.http import HttpResponse
# 视图处理的地方
# Create your views here.hello_world视图函数来返回字符串helloworld


def hello_world(request):
    return HttpResponse("hello world!")
