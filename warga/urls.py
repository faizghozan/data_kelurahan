from django.urls import path
from .views import WargaListView, WargaDetailView, WargaCreateView, PengaduanListView

urlpatterns = [
    path('warga/', WargaListView.as_view(), name='warga_list'),
    path('warga/<int:pk>/', WargaDetailView.as_view(), name='warga_detail'),
    path('warga/tambah/', WargaCreateView.as_view(), name='warga_create'),
    path('pengaduan/', PengaduanListView.as_view(), name='pengaduan_list'),
]
