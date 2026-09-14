# Perbandingan REST API dan SOAP

## Deskripsi

Project ini merupakan implementasi **Web Service pengelolaan data UKT mahasiswa** menggunakan dua pendekatan, yaitu:

1. **REST API** menggunakan FastAPI
2. **SOAP Web Service** menggunakan Spyne

Kedua implementasi memiliki fungsi yang sama, yaitu melakukan operasi **CRUD (Create, Read, Update, Delete)** terhadap data UKT mahasiswa.

Project ini dibuat untuk memahami perbedaan antara REST API dan SOAP dari sisi implementasi, format komunikasi, endpoint/service, request-response, serta cara menjalankan masing-masing Web Service.

---

## Tujuan

Tujuan dari project ini adalah:

* Memahami konsep Web Service.
* Mengimplementasikan REST API menggunakan FastAPI.
* Mengimplementasikan SOAP Web Service menggunakan Spyne.
* Menerapkan operasi CRUD pada kedua pendekatan.
* Membandingkan karakteristik REST API dan SOAP.
* Memahami perbedaan cara client berkomunikasi dengan REST API dan SOAP.

---

## Teknologi yang Digunakan

### REST API

* Python
* FastAPI
* Pydantic
* Uvicorn

### SOAP

* Python
* Spyne
* SOAP 1.1
* WSGI
* `wsgiref.simple_server`

---

# Struktur Data

Data yang digunakan merupakan data UKT mahasiswa dengan atribut:

| Field        | Tipe    | Keterangan            |
| ------------ | ------- | --------------------- |
| `nim`        | String  | Nomor Induk Mahasiswa |
| `nama`       | String  | Nama mahasiswa        |
| `jumlah_ukt` | Integer | Jumlah pembayaran UKT |
| `status`     | String  | Status pembayaran UKT |

Contoh data:

```json
{
  "nim": "2201001",
  "nama": "Rambat",
  "jumlah_ukt": 3500000,
  "status": "lunas"
}
```

> Pada project ini, data masih disimpan menggunakan list Python sebagai database sementara, sehingga data akan kembali ke kondisi awal ketika server dijalankan ulang.

---

# 1. REST API

REST API dibuat menggunakan **FastAPI**.

REST menggunakan konsep **resource** yang direpresentasikan melalui URL atau endpoint. Pada project ini resource yang digunakan adalah `/ukt`.

## Endpoint REST API

| Method | Endpoint     | Fungsi                           |
| ------ | ------------ | -------------------------------- |
| GET    | `/ukt`       | Mendapatkan seluruh data UKT     |
| GET    | `/ukt/{nim}` | Mendapatkan data berdasarkan NIM |
| POST   | `/ukt`       | Menambahkan data UKT             |
| PUT    | `/ukt/{nim}` | Mengubah data UKT                |
| DELETE | `/ukt/{nim}` | Menghapus data UKT               |

### GET Semua Data

```http
GET /ukt
```

Digunakan untuk mengambil seluruh data UKT.

### GET Berdasarkan NIM

```http
GET /ukt/{nim}
```

Contoh:

```http
GET /ukt/2201001
```

Digunakan untuk mengambil data UKT berdasarkan NIM.

### POST Data

```http
POST /ukt
```

Request body:

```json
{
  "nim": "2201003",
  "nama": "Andi",
  "jumlah_ukt": 4000000,
  "status": "belum lunas"
}
```

### PUT Data

```http
PUT /ukt/{nim}
```

Contoh:

```http
PUT /ukt/2201002
```

Request body:

```json
{
  "nim": "2201002",
  "nama": "Budi",
  "jumlah_ukt": 3000000,
  "status": "lunas"
}
```

### DELETE Data

```http
DELETE /ukt/{nim}
```

Contoh:

```http
DELETE /ukt/2201002
```

Digunakan untuk menghapus data mahasiswa berdasarkan NIM.

---

# 2. SOAP Web Service

SOAP Web Service dibuat menggunakan **Spyne** dan menggunakan protokol **SOAP 1.1**.

Berbeda dengan REST API yang menggunakan endpoint HTTP dengan method seperti GET, POST, PUT, dan DELETE, SOAP menggunakan **service dan operation**.

Service yang dibuat pada project ini adalah:

```text
UKTService
```

## SOAP Operations

| Operation     | Parameter                       | Fungsi                           |
| ------------- | ------------------------------- | -------------------------------- |
| `get_all_ukt` | -                               | Mendapatkan seluruh data UKT     |
| `get_ukt`     | `nim`                           | Mendapatkan data berdasarkan NIM |
| `tambah_ukt`  | `nim, nama, jumlah_ukt, status` | Menambahkan data UKT             |
| `update_ukt`  | `nim, nama, jumlah_ukt, status` | Mengubah data UKT                |
| `hapus_ukt`   | `nim`                           | Menghapus data UKT               |

SOAP menggunakan **WSDL (Web Services Description Language)** untuk mendeskripsikan service dan operation yang tersedia.

WSDL dapat diakses melalui:

```text
http://localhost:8082/?wsdl
```

---

# Perbandingan REST API dan SOAP

Walaupun kedua implementasi memiliki fungsi CRUD yang sama, cara keduanya berkomunikasi berbeda.

| Aspek                         | REST API            | SOAP                         |
| ----------------------------- | ------------------- | ---------------------------- |
| Pendekatan                    | Resource-based      | Service/operation-based      |
| Framework                     | FastAPI             | Spyne                        |
| Protokol/format utama         | HTTP + JSON         | SOAP + XML                   |
| Identifikasi operasi          | HTTP Method         | SOAP Operation               |
| Contoh Read                   | `GET /ukt`          | `get_all_ukt()`              |
| Contoh Create                 | `POST /ukt`         | `tambah_ukt()`               |
| Contoh Update                 | `PUT /ukt/{nim}`    | `update_ukt()`               |
| Contoh Delete                 | `DELETE /ukt/{nim}` | `hapus_ukt()`                |
| Dokumentasi service           | OpenAPI/Swagger     | WSDL                         |
| Struktur komunikasi           | Relatif sederhana   | Lebih terstruktur dan formal |
| Format data pada implementasi | JSON                | SOAP XML                     |

---

# Perbedaan Konsep

### REST API

REST berorientasi pada **resource**.

Contohnya resource:

```text
/ukt
```

Operasi ditentukan menggunakan HTTP Method:

```text
GET     → Read
POST    → Create
PUT     → Update
DELETE  → Delete
```

Sehingga:

```text
GET /ukt
```

berarti mengambil data UKT.

Sedangkan:

```text
DELETE /ukt/2201001
```

berarti menghapus resource UKT dengan NIM `2201001`.

---

### SOAP

SOAP berorientasi pada **service dan operation**.

Pada project ini terdapat:

```text
UKTService
```

yang memiliki beberapa operation:

```text
get_all_ukt()
get_ukt()
tambah_ukt()
update_ukt()
hapus_ukt()
```

Jadi client memanggil operation yang telah didefinisikan oleh service.

SOAP juga menyediakan **WSDL** yang mendeskripsikan service, operation, parameter, dan tipe data yang tersedia.

---

# Menjalankan REST API

Install dependency:

```bash
pip install fastapi uvicorn
```

Jalankan server:

```bash
uvicorn main:app --reload
```

Jika file Python memiliki nama berbeda, sesuaikan `main` dengan nama file tersebut.

REST API dapat diakses melalui:

```text
http://127.0.0.1:8000
```

Dokumentasi otomatis FastAPI tersedia di:

```text
http://127.0.0.1:8000/docs
```

---

# Menjalankan SOAP

Install dependency:

```bash
pip install spyne
```

Jalankan file SOAP:

```bash
python soap.py
```

Server berjalan pada:

```text
http://localhost:8082
```

WSDL dapat diakses melalui:

```text
http://localhost:8082/?wsdl
```

---

# Alur Sederhana

Kedua implementasi memiliki tujuan yang sama:

```text
                DATA UKT
                   |
          +--------+--------+
          |                 |
       REST API           SOAP
       FastAPI            Spyne
          |                 |
    HTTP + JSON        SOAP + XML
          |                 |
          +--------+--------+
                   |
                  CRUD
                   |
          Data UKT Mahasiswa
```

Dengan demikian, perbedaan utama project ini bukan pada fungsi yang disediakan, tetapi pada **cara Web Service mendefinisikan dan menangani komunikasi antara client dan server**.

---

# Kesimpulan

REST API dan SOAP sama-sama dapat digunakan untuk membangun Web Service yang menyediakan operasi CRUD.

Pada project ini, REST API menggunakan pendekatan **resource-based** dengan HTTP Method seperti GET, POST, PUT, dan DELETE. REST API juga menggunakan JSON sebagai format pertukaran data pada implementasinya.

Sementara itu, SOAP menggunakan pendekatan **service-based** dengan operation yang didefinisikan pada `UKTService`. SOAP menggunakan struktur pesan SOAP dan menyediakan WSDL sebagai kontrak service.

Dari implementasi tersebut dapat dilihat bahwa **REST cenderung lebih sederhana dan fleksibel untuk API berbasis HTTP**, sedangkan **SOAP memiliki struktur dan kontrak service yang lebih formal**.
