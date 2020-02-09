from django.shortcuts import render
from . import forms
# Create your views here.

def index(request):
    return render(request, 'basicform/index.html')

def form_name_view(request):
    form = forms.Formname()
    if request.method == 'POST':
        form = forms.Formname(request.POST)
        if form.is_valid():
            print('Vaidation success')
            print("Name:"+form.cleaned_data['name'])
            print("Email:"+form.cleaned_data['email'])
            print("text:"+form.cleaned_data['text'])
    return render(request,'basicform/form_page.html',{'form':form})