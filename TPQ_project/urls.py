from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from TPQ_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('singin/', views.sigin_form, name='signin'),
    path('singout/', views.signout_form, name='signout'),
    path('', views.index, name='index'),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('tpqs/list/', views.tpq_list, name='tpq_list'),
    path('tpqs/detail/<int:pk>/', views.tpq_detail, name='tpq_detail'),
    path('tpqs/new/', views.tpq_create, name='tpq_create'),
    path('tpqs/<int:pk>/edit/', views.tpq_update, name='tpq_update'),
    path('tpqs/<int:pk>/delete/', views.tpq_delete, name='tpq_delete'),

    path('gurus/', views.guru_list, name='guru_list'),
    path('gurus/new/', views.guru_create, name='guru_create'),
    path('gurus/<int:pk>/edit/', views.guru_update, name='guru_update'),
    path('gurus/<int:pk>/delete/', views.guru_delete, name='guru_delete'),

    path('murids/', views.murid_list, name='murid_list'),
    path('murids/new/', views.murid_create, name='murid_create'),
    path('murids/<int:pk>/edit/', views.murid_update, name='murid_update'),
    path('murids/<int:pk>/delete/', views.murid_delete, name='murid_delete'),

    path('galleries/new/', views.galeri_create, name='galeri_create'),
    path('galleries/<int:pk>/edit/', views.galeri_update, name='galeri_update'),
    path('galleries/<int:pk>/delete/', views.galeri_delete, name='galeri_delete'),

    path('jadwals/', views.jadwal_list, name='jadwal_list'),
    path('jadwals/new/', views.jadwal_create, name='jadwal_create'),
    path('jadwals/<int:pk>/edit/', views.jadwal_update, name='jadwal_update'),
    path('jadwals/<int:pk>/delete/', views.jadwal_delete, name='jadwal_delete'),


    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
