from django.urls import path,include
from .views import UserRegistrationView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
        path(r'^signup', UserRegistrationView.as_view()),
        path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    ]