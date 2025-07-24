from django.shortcuts import render, redirect
from .models import Sasana
from .forms import SasanaForm
from math import radians, cos, sin, asin, sqrt
from django.http import JsonResponse
import re

def input_sasana(request):
    if request.method == 'POST':
        form = SasanaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('input_sasana')  # bisa redirect ke halaman sukses juga
    else:
        form = SasanaForm()
    
    return render(request, 'sasana/input_sasana.html', {'form': form})

def haversine(lat1, lon1, lat2, lon2):
    # Konversi ke radian
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    # Rumus Haversine
    dlat = lat2 - lat1 
    dlon = lon2 - lon1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371  # Radius Bumi (km)
    return c * r

def extract_lat_lon(link):
    match = re.search(r'@(-?\d+\.\d+),(-?\d+\.\d+)', link)
    if match:
        return float(match.group(1)), float(match.group(2))
    return None, None

def cari_sasana_terdekat(request):
    if request.method == 'POST':
        lat = float(request.POST.get('latitude'))
        lon = float(request.POST.get('longitude'))

        semua_sasana = Sasana.objects.all()
        hasil = []

        for s in semua_sasana:
            sasana_lat, sasana_lon = extract_lat_lon(s.link_gmap)
            if sasana_lat is not None and sasana_lon is not None:
                jarak = haversine(lat, lon, sasana_lat, sasana_lon)
                hasil.append({
                    'nama': s.nama_sasana,
                    'alamat': s.alamat_sasana,
                    'jarak': round(jarak, 2),
                    'link_gmap': s.link_gmap,
                    'gambar': s.profile.url if s.profile else '',
                })

        hasil = sorted(hasil, key=lambda x: x['jarak'])[:4]
        return JsonResponse({'data': hasil})

    return render(request, 'sasana/cari_sasana.html')
