from django.urls import path

from .views import OrderDetailView

urlpatterns = [
    path('my-order/', OrderDetailView.as_view(), name='my_order'),
]