from django.urls import reverse_lazy, render
from django.views.generic import ListView, DetailView, CreateView, UpdateView , DeleteView
from .models import Warga, Pengaduan
from .forms import WargaForm

def WargaListView(request):
    warga_list = Warga.objects.all()
    return render(request, 'warga/warga_list.html', {'warga_list': warga_list})


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


class WargaUpdateView(UpdateView):
    model = Warga
    form_class = WargaForm
    template_name = 'warga/warga_form.html' # Kita pakai template yang sama
    success_url = reverse_lazy('warga-list')

class WargaDeleteView(DeleteView):
    model = Warga
    template_name = 'warga/warga_confirm_delete.html'
    success_url = reverse_lazy('warga-list')