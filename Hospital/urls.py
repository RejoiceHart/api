from django.urls import path
from .views import SignupView, LoginView
urlpatterns = [
    # path('chat/<int:doctor_id>/', views.chat_view, name='chat'),
    path('hospitalsignup/', SignupView.as_view(), name='signup'),
    path('hospitallogin/', LoginView.as_view(), name='login'),
]
