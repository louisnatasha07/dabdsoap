from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Model data pakai Pydantic (otomatis validasi)
class UKT(BaseModel):
    nim: str
    nama: str
    jumlah_ukt: int
    status: str

# "Database" sementara
data_ukt = [
    {"nim": "2201001", "nama": "Rambat", "jumlah_ukt": 3500000, "status": "lunas"},
    {"nim": "2201002", "nama": "Budi", "jumlah_ukt": 2800000, "status": "belum lunas"}
]

@app.get("/ukt")
def get_all_ukt():
    return data_ukt

@app.get("/ukt/{nim}")
def get_ukt(nim: str):
    for m in data_ukt:
        if m["nim"] == nim:
            return m
    raise HTTPException(status_code=404, detail="NIM tidak ditemukan")

@app.post("/ukt")
def tambah_ukt(data: UKT):
    data_ukt.append(data.dict())
    return {"message": "Transaksi berhasil ditambahkan", "data": data}

@app.put("/ukt/{nim}")
def update_ukt(nim: str, data: UKT):
    for i, m in enumerate(data_ukt):
        if m["nim"] == nim:
            data_ukt[i] = data.dict()
            return {"message": "Data berhasil diupdate", "data": data}
    raise HTTPException(status_code=404, detail="NIM tidak ditemukan")

@app.delete("/ukt/{nim}")
def hapus_ukt(nim: str):
    for i, m in enumerate(data_ukt):
        if m["nim"] == nim:
            deleted = data_ukt.pop(i)
            return {"message": "Data berhasil dihapus", "data": deleted}
    raise HTTPException(status_code=404, detail="NIM tidak ditemukan")