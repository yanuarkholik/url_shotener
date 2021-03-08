# singkat.in
## FP Manajemen Project
Eltansha Raksa Gama       18.12.0955;
Frans Dedi Panjaitan			18.12.0956;
Ega Mahendra				      18.12.0959;
I Gede Bima Divantara		  18.12.0973;
Yanuar Nur Kholik			    18.12.0974;
Achmad Choirul Sholihan		18.12.0977;

# Installation
Menggunakan [Python](https://www.python.org/downloads/)==3.9.1
Menggunakan Framwork Python [Django](https://docs.djangoproject.com/en/3.1/topics/install/)==3.1.7 atau bisa 
```python
pip install django==3.1.7
```

#### 1. Download [virtualenv](https://yasoob.me/2013/07/30/what-is-virtualenv/) untuk membuat Virtual Environment Django dengan command dibawah
```python
pip install virtualenv
```
*Note : aplikasi bisa berjalan tanpa virtualenv, virtualenv digunakan untuk mengoptimalkan development Python*
#### 2. Membuat virtualenv
```python
virtualenv nama_virtualenv
```
#### 3. Aktivasi virtualenv
```python
nama_virtualenv/Scripts/activate
```
#### 4. Install requirements.txt dengan command dibawah
```python 
pip install -r requirements.txt
```
Jika terjadi error atau ```requirements.txt``` tidak mau terinstall maka buka file ```requirements.txt``` install package/plugin satu-persatu dengan cara meng-copas nama dan versi package yang tertera. Contoh :
```python
pip install (nama_package==versi_package)
```
Kemudian hapus paket yang error tersebut pada ```requirements.txt``` untuk meninstall via requirements, jika ingin menginstall satu-persatu bisa pakai perintah diatas

#### 5. Menjalankan program
```python
python manage.py makemigrations
python manage.py migrate # Akan memunculkan banyak "OK", berarti program tidak ada masalah
python manage.py runserver
```
