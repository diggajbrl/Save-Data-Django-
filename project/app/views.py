from django.shortcuts import render

from app.models import Myform

# Create your views here.

def app (request) :

    sucess = ''

    if request.method=='POST' :
 
        # in .get('') - should be similar to HTML name = '' 

        fname = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        idemail = request.POST.get('email')
# model name = here func name 
        apple = Myform (first_name = fname, last_name = lname, my_email = idemail)
        apple.save()
        sucess = 'Sucessful : Thank You'
    return render (request, 'index.html', {'sucess' : sucess})