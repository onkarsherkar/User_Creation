
from django.urls import path,include
from . import views
urlpatterns = [
   path('hello',views.hello),
   path('',views.home),
   path('signup',views.signup),
   path('login',views.login_user),
   path('logout',views.logout_user),
]
