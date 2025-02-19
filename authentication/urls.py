from django.urls import path
from .views import RegisterView, get_tokens_for_user

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', get_tokens_for_user, name='token_obtain_pair'),
]
