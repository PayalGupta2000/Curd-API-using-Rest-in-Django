from django.urls import path
from.views import *

urlpatterns = [
    path('categories',ListCategory.as_view(),name='categories'),
    path('categories/<int:pk>/',DetailCategory.as_view(),name='singlecategory'),
    path('products',ListProduct.as_view(),name='All products'),
    path('products/<int:pk>/',DetailProduct.as_view(),name="single product")
]
