from django.conf.urls import url
from BRMapp import views

urlpatterns=[
    url('view-books',views.viewBooks),
    url('edit-book',views.editBook),
    url('delete-book',views.deleteBook),
    url('search-book',views.searchBook),
    url('new-book',views.newBook),
    url(r'^add',views.add),
    url('edit',views.edit),
    url('search',views.search),
    # url('login',views.userLogin),
    # url('logout',views.userLogout),
]
