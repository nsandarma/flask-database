from flask_restful import Resource,Api,reqparse
from applikasi import app
from .models import db, Mahasiswa
from flask_marshmallow import Marshmallow # new
from flask import request

ma = Marshmallow(app) # new

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('nim')
parser.add_argument('jurusan')
parser.add_argument('id')


class PostSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "nim","jurusan")
        model = Mahasiswa

post_schema = PostSchema()
posts_schema = PostSchema(many=True)


api = Api(app)

class Data(Resource):
    def get(self):
        listMhs = Mahasiswa.query.all()
        return {'data':posts_schema.dump(listMhs)}
    def post(self):
        args = parser.parse_args()
        nim = args['nim']
        jurusan = args['jurusan']
        name = args['name']
        try:
            mhs = Mahasiswa(name=name,nim=nim,jurusan=jurusan)
            db.session.add(mhs)
            db.session.commit()
            return {'status':'True',"data":[name,nim,jurusan]}
        except Exception as e:
            return {"status":"failed"}
    def delete(self):
        args = parser.parse_args()

        id = args['id']

        try:
            mhs = Mahasiswa.query.filter_by(id=id).first()
            db.session.delete(mhs)
            db.session.commit()
            return {'status':'deleted'}
        except Exception as e:
            return {'status':"Error"}
        

class GetDatabyid(Resource):
    def get(self,nim):
        mhs = Mahasiswa.query.filter_by(nim=nim).first()
        return {'data':post_schema.dump(mhs)}

        


api.add_resource(Data,'/api')
api.add_resource(GetDatabyid,'/api/<nim>')


