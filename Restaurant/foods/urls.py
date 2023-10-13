from django.urls import path
from .views import food_detail,food_list


app_name = 'foods'

urlpatterns = [
    path ('', food_list,name='food_list'),
    path ("<int:id>/", food_detail,name='detail'),
]
