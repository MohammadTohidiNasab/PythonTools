from django.urls import path
from .views import blog_page,blog_detail,blog_tag,blog_category

 
app_name = 'blog'
urlpatterns = [
    path('',blog_page,name='blog'),
    path("<int:id>", blog_detail, name="blog_detail"),
    path('tag/<slug:tag>',blog_tag,name='tag'),
    path('category/<slug:category>',blog_category,name='category'),
]
