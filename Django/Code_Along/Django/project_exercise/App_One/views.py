from django.shortcuts import render
from App_One.models import user

# Create your views here.

def index(request):
    return render(request, 'App_One/index.html')

def users(request):
    user_list = user.objects.order_by('first_name')
    user_dict = {'users':user_list}
    return render(request, 'App_One/users.html', context = user_dict)
