from django.urls import path, include
from products import views

urlpatterns = [
    path('list/',
         views.ProductView.as_view(),
         name='product_list'
         ),
]