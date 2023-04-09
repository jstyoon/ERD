# # tweet/urls.py
# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('', views.home, name='home'), # 127.0.0.1:8000 과 views.py 폴더의 home 함수 연결
#     # path('product-create', views.product_view, name='product-create')
# ]

from django.urls import path
from .views import home, product_list, product_create, stock_list, stock_create

urlpatterns = [
    path('', home, name='home'),
    path('products/', product_list, name='product_list'),
    path('products/create/', product_create, name='product_create'),
    path('stocks/', stock_list, name='stock_list'),
    path('stocks/<int:product_id>/create/', stock_create, name='stock_create'),
]
