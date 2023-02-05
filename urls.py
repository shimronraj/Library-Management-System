"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from .import views
from django.urls import path
urlpatterns = [
   # path('', views.index, name='index'),
    #1st page name nxt where to go nxt default value
    path('login', views.all_login, name="login"),
    path('adminfirst', views.adminfirst, name="adminfirst"),
    #path('login', views.userlogin, name='login'),
    path('register', views.student_add, name="register"),
    path('addbook', views.book_add, name="addbook"),
    path('studlogin', views.studlogin, name="studlogin"),
    path('', views.firstpage, name="firstpage"),
    path('adminlogin', views.adminlogin, name="adminlogin"),
    path('bookdetails', views.retrivestud_book, name="bookdetails"),
    path('feedback', views.feedback, name="feedback"),
    path('payment', views.payment, name="payment"),
    path('contactus',views.contactus,name="contacatus"),
    path('about',views.about,name="about"),
    path('adminviewbook',views.retrive_book,name="adminviewbook"),
    path('studentretrive',views.retrive_student,name="studentretive"),
    path('update',views.student_details_update,name="update"),
    path('bookupdate',views.book_details_update,name="bookupdate"),
    #..........................logout
    path('profile',views.profile,name="profile"),
    #.........................................delete
    path('deletebook',views.delete,name="bookdetails"),
    path('deletestudent',views.studdelete,name="studentretrive"),






#...........................................................................
#.......................without page...........................
    path('logout', views.logout, name="admin"),


]
