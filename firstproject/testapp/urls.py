from django.conf.urls import url
from testapp import views

urlpatterns=[
 url("about",views.about),
 url("contact",views.showContact),
 url('^$',views.greeting),
 url('employee/',views.employee_info),
]
