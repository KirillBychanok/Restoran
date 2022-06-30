from django.shortcuts import render
from .models import FeedBack, DishCategory, Dish, Portfolio
from .forms import FeedBackForm
import telebot

# Create your views here.
# Kirill1234

def index(request):
    if request.method == 'POST':
        form = FeedBackForm(request.POST)
        message = f'{request.POST["name"]}\n{request.POST["email"]}\n{request.POST["message"]}'
        if form.is_valid():
            form.save()


    Feedbacks = FeedBack.objects.all()
    form = FeedBackForm()
    content = {
        'feedbacks': Feedbacks,
        'form': form,
        'dishcategory': DishCategory.objects.all(),
        'dish': Dish.objects.all(),
        'portfolio': Portfolio.objects.all()
    }
    return render(request, 'main/index.html', content)

