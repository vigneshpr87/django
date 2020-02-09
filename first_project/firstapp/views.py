from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import AccessRecord,Topic,Webpage

# Create your views here.

'''def index(request):
    return HttpResponse("testin")'''

def index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    dict_list = {'access_records': webpage_list}
    mycont = {'variable':'Testing the page'}
    return render(request,'firstapp/index.html',context=dict_list)

def help(request):
    return HttpResponse("Helper Page")