from django.urls import path, include
from . import views

app_name = 'application'

urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', views.user_logout, name='user_logout'),
    path('login/', views.user_login, name='user_login'),
    path('register/', views.register, name='register'),
    path('administrator/', views.administrator, name='administrator'),
    path('approval/<int:id>/', views.approval, name='approval'),
    path('disapproval/<int:id>/', views.disapproval, name='disapproval'),

    path('user/', include('django.contrib.auth.urls'))
]
