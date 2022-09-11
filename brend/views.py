from django.shortcuts import render
from .models import ShmotAdd
from django.views.generic import DetailView


class ShmotDetailView(DetailView):
    model = ShmotAdd
    template_name = 'brend/des.html'
    context_object_name = 'description'

brends = ShmotAdd.objects.all()  #Передаем все значение 

def brend_shmot(request):
    data = {
        'title': 'Shmot',
        'brends': brends
    }
    return render(request, 'brend/all-brends.html', data)


def new_of_shmot(request):
    brends = ShmotAdd.objects.order_by('date') #Передаем все значение и сортируем
    data = {
        'title': 'Новинки',
        'brends': brends
    }
    return render(request, 'brend/all-brends.html', data)


def women_shmot(request):
    pol = 'женский'
    data = {
        'title': 'Женский раздел',
        'pol':pol,
        'brends': brends
    }
    return render(request, 'brend/all-brends.html', data)    


def men_shmot(request):
    pol = 'мужской'
    data = {
        'title': 'Мужской раздел',
        'pol':pol,
        'brends': brends
    }
    return render(request, 'brend/all-brends.html', data)
