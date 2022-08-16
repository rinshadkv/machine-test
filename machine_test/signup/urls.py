from django.urls import include, path
from signup import views
urlpatterns = [
    path("",views.index,),
    path('login/',views.login,name='login'),
    path("home",views.home,name='home')
    
]