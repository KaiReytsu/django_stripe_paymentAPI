from django.contrib import admin
from django.urls import path

from paymentpage import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('item/<int:pk>/', views.ItemDetailView.as_view(), name='itemdetail'),
    path('buy/<int:pk>/', views.PaymentView.as_view() ,name='buy'),
    path('cancel/', views.CancelView.as_view(), name='cancel'),
    path('success/', views.SuccessView.as_view(), name='success'),
]
