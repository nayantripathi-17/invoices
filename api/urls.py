from django.urls import path
from . import views

urlpatterns = [    
    path('', views.redirect_to_home, name='redirect_to_home'),
    path('invoices/',views.home,name='home'),
    path('invoices/<int:pk>',views.pk.as_view(),name='pk'),
]