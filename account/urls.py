
from django.urls import path
from .views import UserRegisterViews,UserLoginView,UserBankAccountUpdateView,UserLogoutView

urlpatterns = [

    path('register/',UserRegisterViews.as_view(), name='register'),
    path('login/',UserLoginView.as_view(), name='login'),
    path('logout/',UserLogoutView, name='logout'),
    path('profile/', UserBankAccountUpdateView.as_view(), name='profile' )
]
