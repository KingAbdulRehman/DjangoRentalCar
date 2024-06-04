from django.contrib import admin
from django.urls import path,include
from MyApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('verifylogin', views.verifyUser, name='verifyUser'),
    path('logout', views.logout, name='logout'),
    path('about', views.about),
    path('contact', views.contact),
    path('addcontact', views.InsertContactUs),
    path('carlist', views.cars),
    path('insertSub', views.InsertSubscriber),
    path('updatePro', views.UpdateProfile),
    path('carDetails', views.CarDetails),
    path('confirmBook', views.Booking),
    path('bookhis', views.BookingHistory),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
