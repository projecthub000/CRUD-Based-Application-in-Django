from django.shortcuts import render
from BRMapp.forms import NewBookForm,SearchForm
from BRMapp import models
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required 

# def userLogin(request):
#     data={}
#     if request.method=="POST":
#         username=request.POST['username']
#         password=request.POST['password']
#         user=authenticate(request,username=username,password=password)
#         if user:
#             login(request,user)
#             return HttpResponseRedirect('/BRMapp/view-books/')
#         else:
#             data['error']="Username or Password is incorrect"
#             res=render(request,"BRMapp/user_login.html",data)
#             return res
#     else:
#         return render(request,'BRMapp/user_login.html',data)
# def userLogout(request):
#     logout(request)
#     return HttpResponseRedirect('BRMapp/login')
# @login_required(login_url='/BRMapp/login/')
def searchBook(request):
    form=SearchForm()
    res=render(request,'BRMapp/search_book.html',{'form':form})
    return res
def search(request):
    form=SearchForm(request.POST)
    books=models.Book.objects.filter(title=form.data['title'])
    res=render(request,'BRMapp/search_book.html',{'form':form,'books':books})
    return res
def deleteBook(request):
    bookid=request.GET['bookid']
    book=models.Book.objects.filter(id=bookid)
    book.delete()
    return HttpResponseRedirect('BRMapp/view-books')
def editBook(request):
    book=models.Book.objects.get(id=request.GET['bookid'])
    fields={'title':book.title,'price':book.price,'author':book.author,'publisher':book.publisher}
    form=NewBookForm(initial=fields)
    res=render(request,'BRMapp/edit_book.html',{'form':form,'book':book})
    return res
def edit(request):
    if request.method=='POST':
     form=NewBookForm(request.POST)
     book=models.Book()
     book.id=request.POST['bookid']
     book.title=form.data['title']
     book.price=form.data['price']
     book.author=form.data['author']
     book.publisher=form.data['publisher']
     book.save()
    return HttpResponseRedirect('BRMapp/view-books')
# @login_required(login_url='/BRMapp/login/')
def viewBooks(request):
    books=models.Book.objects.all()
    res=render(request,'BRMapp/view_book.html',{'books':books})
    return res
# @login_required(login_url='/BRMapp/login/')
def newBook(request):
    form=NewBookForm()
    res=render(request,'BRMapp/new_book.html',{'form':form})
    return res
def add(request):
    if request.method=='POST':
        form=NewBookForm(request.POST)
        book=models.Book()
        book.title=form.data['title']
        book.price=form.data['price']
        book.author=form.data['author']
        book.publisher=form.data['publisher']
        book.save()
    s="Record Stored<br><a href='/BRMapp/view-books'>View all Books</a>"
    return HttpResponse(s)
