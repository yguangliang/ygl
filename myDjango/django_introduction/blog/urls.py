from django.urls import path, include
from . import views
import blog.views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    path('content', blog.views.article_content),
]