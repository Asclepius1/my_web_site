from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.brend_shmot, name='shmot'),
    path('new-of-shmot', views.new_of_shmot, name='new-of-shmots'),
    path('women-shmots', views.women_shmot, name='women-shmots'),
    path('men-shmot', views.men_shmot, name='men-shmots'),
    path('<int:pk>', views.ShmotDetailView.as_view(), name='description-shmot'),
    
]