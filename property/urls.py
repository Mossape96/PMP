"""property URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from property_manager import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.default.urls')),
    path('', views.index, name='home'),
    path('list_client_accounts/', views.list_clients_accounts, name='list_client_accounts'),
    path('add_new_client/', views.add_new_client, name='add_new_client'),
    #  path('add_new_property/', views.add_new_property, name='add_new_property'),
    path('update_accounts/<str:pk>/', views.update_properties, name="update_properties"),
    #  path('update_new_property/<str:pk>/', views.newprop_update, name="update_new_property"),
    path('client_account_detail/<str:pk>/', views.client_account_detail, name="client_account_detail"),
    path('withdraw_account/<str:pk>/', views.withdraw_account, name="withdraw_account"),
    path('deposit_account/<str:pk>/', views.deposit_account, name="deposit_account"),
    path('transaction_history/', views.transaction_history, name='transaction_history'),
    path('property_register/', views.properties, name='property_register'),
    #path('export_pdf/', views.export_pdf, name='export_pdf'),

]
