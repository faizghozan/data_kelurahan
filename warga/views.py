from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import Warga, Pengaduan
from .forms import WargaForm

class WargaListView(ListView):
    model = Warga
    template_name = 'warga/warga_list.html'
    context_object_name = 'warga_list'


class WargaDetailView(DetailView):
    model = Warga
    template_name = 'warga/warga_detail.html'
    context_object_name = 'warga'


class WargaCreateView(CreateView):
    model = Warga
    template_name = 'warga/warga_form.html'
    fields = ['nik', 'nama_lengkap', 'alamat', 'no_telepon']


class PengaduanListView(ListView):
    model = Pengaduan
    template_name = 'warga/pengaduan_list.html'
    context_object_name = 'pengaduan_list'


class WargaCreateView(CreateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html'
    success_url = reverse_lazy('warga-list')
