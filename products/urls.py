from django.urls import path

from .views import fund_views, product_views


urlpatterns = [
    path('products', product_views.ProductsListView.as_view()),
    path('products/<int:pk>', product_views.ProductsDetailView.as_view()),
    path('funds', fund_views.Pd_FundView.as_view()),
]