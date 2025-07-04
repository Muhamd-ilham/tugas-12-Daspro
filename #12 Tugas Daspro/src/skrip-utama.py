from luas.lingkaran import luas_lingkaran
from luas.persegi import luas_persegi
from luas.segitiga import luas_segitiga
from volume.bola import volume_bola
from volume.kubik import volume_kubus
from volume.trapesium import volume_trapesium

print(f"Luas Lingkaran (radius 7): {luas_lingkaran(7):.2f}")
print(f"Luas Persegi (sisi 5): {luas_persegi(5)}")
print(f"Luas Segitiga (alas 10, tinggi 5): {int(luas_segitiga(10, 5))}")
print(f"Volume Bola (radius 5): {volume_bola(5):.2f}")
print(f"Volume Kubus (sisi 3): {volume_kubus(3)}")
print(f"Volume Trapesium (alas 20, tinggi 10): {int(volume_trapesium(20, 10))}")