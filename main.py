from spyne import Application, rpc, ServiceBase, Unicode, Integer
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server


# Database sementara
data_ukt = [
    {
        "nim": "2201001",
        "nama": "Rambat",
        "jumlah_ukt": 3500000,
        "status": "lunas"
    },
    {
        "nim": "2201002",
        "nama": "Budi",
        "jumlah_ukt": 2800000,
        "status": "belum lunas"
    }
]


# SOAP Service
class UKTService(ServiceBase):

    # GET semua data UKT
    @rpc(_returns=Unicode)
    def get_all_ukt(ctx):
        return str(data_ukt)


    # GET berdasarkan NIM
    @rpc(Unicode, _returns=Unicode)
    def get_ukt(ctx, nim):

        for data in data_ukt:

            if data["nim"] == nim:
                return str(data)

        return "NIM tidak ditemukan"


    # TAMBAH data UKT
    @rpc(
        Unicode,
        Unicode,
        Integer,
        Unicode,
        _returns=Unicode
    )
    def tambah_ukt(
        ctx,
        nim,
        nama,
        jumlah_ukt,
        status
    ):

        data_baru = {
            "nim": nim,
            "nama": nama,
            "jumlah_ukt": jumlah_ukt,
            "status": status
        }

        data_ukt.append(data_baru)

        return "Data berhasil ditambahkan"


    # UPDATE data UKT
    @rpc(
        Unicode,
        Unicode,
        Integer,
        Unicode,
        _returns=Unicode
    )
    def update_ukt(
        ctx,
        nim,
        nama,
        jumlah_ukt,
        status
    ):

        for data in data_ukt:

            if data["nim"] == nim:

                data["nama"] = nama
                data["jumlah_ukt"] = jumlah_ukt
                data["status"] = status

                return "Data berhasil diupdate"

        return "NIM tidak ditemukan"


    # DELETE data UKT
    @rpc(Unicode, _returns=Unicode)
    def hapus_ukt(ctx, nim):

        for i, data in enumerate(data_ukt):

            if data["nim"] == nim:

                data_ukt.pop(i)

                return "Data berhasil dihapus"

        return "NIM tidak ditemukan"


# Konfigurasi SOAP
application = Application(
    [UKTService],
    tns="http://example.com/ukt",
    in_protocol=Soap11(),
    out_protocol=Soap11()
)


# WSGI
wsgi_application = WsgiApplication(application)


# Jalankan server
if __name__ == "__main__":

    server = make_server(
        "localhost",
        8082,
        wsgi_application
    )

    print("===================================")
    print("SOAP UKT API")
    print("Server : http://localhost:8082")
    print("WSDL   : http://localhost:8082/?wsdl")
    print("===================================")

    server.serve_forever()