from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def showTest(request):
    res=render(request,'exam/test.html',{"texts":"Lorem ipsum dolor, sit amet consectetur adipisicing elit. Quisquam ipsum dolorem dolorum nemo amet quia distinctio enim consequuntur aperiam error. Numquam reprehenderit iste maiores fugiat tenetur voluptate nemo eos odio."})
    return res
def showResult(request):
    s={'s':"Adityaa"}
    return render(request,'result/result.html',s)
