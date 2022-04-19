from django.urls import path

from .views import ProductsListView, ProductsDetailView


urlpatterns = [
    path('', ProductsListView.as_view()),
    path('<int:pk>', ProductsDetailView.as_view()),
]