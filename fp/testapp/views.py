from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def date_time_view(request):
    ans=datetime.datetime.now()
    return HttpResponse("<h1>Hello guest The Current Date and Date at the Server is {}&nbsp&nbsp</h1>".format(str(ans)))