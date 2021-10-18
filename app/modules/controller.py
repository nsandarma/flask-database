from flask import render_template, request, redirect
from app import app
from .models import db, Mahasiswa

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        nim = request.form['nim']
        jurusan = request.form['jurusan']
        cek = Mahasiswa.query.filter_by(nim=nim).first()
        error = None
        iff = name is not "" and nim is not '' and jurusan is not ''
        if cek == None and iff:
            mhs = Mahasiswa(nim=nim, name=name,jurusan=jurusan)
            db.session.add(mhs)
            db.session.commit()
        else:
            error = "Data Yang Anda masukkan telah ada,atau data yang anda masukkan tidak benar"
            return render_template('error.html',data=error)
    listMhs = Mahasiswa.query.all()
    print(listMhs)
    # return redirect("/")
    return render_template("home.html",data=enumerate(listMhs,0))

@app.route('/form-update/<int:id>')
def updateForm(id):
    mhs = Mahasiswa.query.filter_by(id=id).first()
    return render_template("form-update.html", data=mhs)
    # return "hello world"

@app.route('/form-update', methods=['POST'])
def update():
    if request.method == 'POST':
        id = request.form['id']
        nim = request.form['nim']
        name = request.form['name']
        jurusan = request.form['jurusan']
        try:
            mhs = Mahasiswa.query.filter_by(id=id).first()
            mhs.name = name
            mhs.nim = nim
            mhs.jurusan = jurusan
            db.session.commit()
        except Exception as e:
            print("Failed to update data")
            print(e)
        return redirect("/")

@app.route('/delete/<int:id>')
def delete(id):
    try:
        mhs = Mahasiswa.query.filter_by(id=id).first()
        db.session.delete(mhs)
        db.session.commit()
    except Exception as e:
        print("Failed delete mahasiswa")
        print(e)
    return redirect("/")

@app.route('/coba/<nim>')
def coba(nim):
    data = Mahasiswa.query.filter_by(nim=nim).first()
    if data == None:
        return "Kosong"
    else:
        return data.name







