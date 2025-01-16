from django.contrib import admin
from django.urls import path
from product import views

urlpatterns = [
    path('',views.index,name=''),
    path('addProduct/',views.addProduct,name='addProduct'),
    path('deleteProduct/<int:id>/',views.DeleteProduct,name='deleteProduct'),
    path('updateProduct/<int:id>/',views.UpdateProduct,name='updateProduct'),
]
