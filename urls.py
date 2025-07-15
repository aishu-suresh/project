
from django.urls import path
from myapp import views
urlpatterns = [
    path('',views.index,name="index" ),
    path('login',views.login,name="login" ),
    path('registration',views.registration,name="registration" ),
    path('register',views.register,name="register" ),
    path('login_action',views.login_action,name="login_action" ),
    path('logout_view',views.logout_view,name="logout_view" ),
    path('admin_home',views.admin_home,name="admin_home" ),
    path('user_home',views.user_home,name="user_home" ),
    path('userlist',views.userlist,name="userlist" ),
    path('addbook',views.addbook,name="addbook" ),
    path('booklist',views.booklist,name="booklist" ),
]
