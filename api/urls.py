from django.urls import path
from .views import LoginPage

urlpatterns = [
    path('',LoginPage.as_view({'get':'post','post': 'post'}),name='login')
]
