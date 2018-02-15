from django.shortcuts import render
from AppTwo.models import User

# Create your views here.
def help(request):
    # return HttpResponse("<em><font color='red'>HELLO WORLD!!</font></em>")
    # my_dict = { 'insert_me': "i am coming" }
    # return render (request,"AppTwo/help.html" ,context=my_dict)
    info_list=User()
    info_dict = { 'info_records':info_list }
    return render (request,"first_app/help.html" ,context=info_dict)
