
from django.urls import  path
from products import views
urlpatterns = [
    path("",views.index,name="home"),
  
    path("product-billing/",views.product_billing,name="product-billing"),
    path("add-product/",views.add_product,name="add-product"),
    path('add-to-invoice/',views.AddToInvoice,name="add-to-invoice"),
    path('updateQuantity', views.update_quantity, name="updateQuantity"),
    path("search/",views.search,name="search"),
    path("checkout",views.check_out,name='checkout')

]