from django.shortcuts import render
from django.http import HttpResponse
from appTwo.models import User
from appTwo.forms import NewUserForm
# Create your views here.

def index(request):
    return render(request,'appTwo/index.html')

def user(request):
    '''user_list = User.objects.order_by('first_name')
    user_dict = {'userdetails': user_list}
    return render(request, 'appTwo/index.html', context=user_dict)'''

    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return index(request)
        else:
            print("Error")

    return render(request, 'appTwo/users.html', {'form':form})
    