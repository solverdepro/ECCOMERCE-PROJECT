from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='homeView'),
    # path('cart/', views.cart, name='cartView'),
    path('dashboard/', views.dashboard,name='dashboardView'),
    path('order_complete/', views.order_complete,name='order_completeView'),
    path('place_order/', views.place_order,name='place_orderView'),
    path('product_item/', views.product_item,name='product_itemView'),
    path('register/', views.register,name='registerView'),
    path('search_result/', views.search_result,name='search_resultView'),
    path('signin/', views.signin,name='signinView'),
    # path('store/',products_by_cartegory views.store,name='storeView'),

]