from django.urls import path
from .views import WargaListView
from django.urls import path
from .views import WargaListView, WargaDetailView, PengaduanListView, WargaCreateView

urlpatterns = [
    path('', WargaListView.as_view(), name='warga-list'),
    path('tambah/', WargaCreateView.as_view(), name='warga-tambah'), # URL untuk form tambah
    path('<int:pk>/', WargaDetailView.as_view(), name='warga-detail'),
    path('pengaduan/', PengaduanListView.as_view(), name='pengaduan-list'),

]
