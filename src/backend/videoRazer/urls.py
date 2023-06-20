from django.urls import path
from .views import FrontendTemplateView

urlpatterns = [
    path('', FrontendTemplateView.as_view())
]