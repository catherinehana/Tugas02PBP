from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Catherine Hana Natalie',
        'class': 'PBP B',
        'produk1': 'Cereal Koko Crunch',
        'keterangan1': 'Sarapan enak dan bergizi untuk memulai hari',
        'berat1': '170 gram',
        'jumlah1': '20 kotak',
        'harga1': 'Rp20.000',
        'produk2': 'Susu Cimory',
        'keterangan2': 'Susu bernutrisi dengan tektur yang lembut. Rasa yang bervariasi menarik minat masyarakat',
        'berat2': '200 ml',
        'jumlah2': '15 kotak',
        'harga2': 'Rp7.000',
        'produk3': 'Tisu',
        'keterangan3': 'Tisu dengan bahan yang lembut dan cocok untuk traveling',
        'berat3': '200 gram',
        'jumlah3': '21 kotak',
        'harga3': 'Rp8.000',
        'produk4': 'Buah Mangga',
        'keterangan4': 'Mangga yang manis dan besar, baru dipanen.',
        'berat4': '1 kg',
        'jumlah4': '21 kg',
        'harga4': 'Rp8.000',
    }

    return render(request, "main.html", context)