from flask import Flask, request, make_response
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Ski, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

ma = Marshmallow(app)

class SkiSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Ski
        load_instance = True
        
    brand = ma.auto_field()
    name = ma.auto_field()
    dimensions = ma.auto_field()
    lengths = ma.auto_field()
    year = ma.auto_field()
    weight = ma.auto_field()
    image = ma.auto_field()
    content = ma.auto_field()
    stoke_profile = ma.auto_field()
    
class SkisSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Ski
        load_instance = True
        
    brand = ma.auto_field()
    name = ma.auto_field()        
    
    url = ma.Hyperlinks(
        {
            "self": ma.URLFor(
                "skibyid",
                values=dict(id="<id>")),
            "collection": ma.URLFor(
                "skis"
            ),
        }
    )    
    
ski_schema = SkiSchema()
skis_schema = SkisSchema(many=True)

class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User
        load_instance = True
    
    username = ma.auto_field()
    stoke_profile = ma.auto_field()
    
    url = ma.Hyperlinks(
        {
            "self": ma.URLFor(
                "userbyid",
                values=dict(id="<id>")),
            "collection": ma.URLFor(
                "users"
            ),
        }
    )

user_schema = UserSchema()
users_schema = UserSchema(many=True)

api = Api(app)

class Index(Resource):
    def get(self):
        message = {"index": "Welcome to Mike's Ski Api"}
        
        return make_response(message, 200)

api.add_resource(Index, '/')

class Skis(Resource):
    def get(self):
        skis = Ski.query.all()
        
        return make_response(skis_schema.dump(skis), 200)

api.add_resource(Skis, '/skis')

class SkiByID(Resource):
    def get(self, id):
        ski = Ski.query.filter(Ski.id == id).first()
        
        return make_response(ski_schema.dump(ski), 200)
        
    def patch(self, id):
        ski = Ski.query.filter(Ski.id == id).first()
        new_ski_data = request.get_json()
        
        for attr in new_ski_data:
            setattr(ski, attr, new_ski_data[attr])
            
        db.session.add(ski)
        db.session.commit()
        
        return make_response(ski_schema.dump(ski), 200)

api.add_resource(SkiByID, '/skis/<int:id>')

class Users(Resource):
    def get(self):
        users = User.query.all()
        
        return make_response(users_schema.dump(users), 200)
    
    def post(self):
        new_user_data = request.get_json()
        new_user = User(
            username = new_user_data['username'],
            stoke_profile = new_user_data['stoke_profile']
        )
        
        db.session.add(new_user)
        db.session.commit()
        
        return make_response(users_schema.dump(new_user), 201)

api.add_resource(Users, '/users')

class UserByID(Resource):
    def get(self, id):
        user = User.query.filter(User.id == id).first()
        return make_response(user_schema.dump(user), 200)
    
    def patch(self, id):
        user = User.query.filter(User.id == id).first()
        new_user_data = request.get_json()
        
        for attr in new_user_data:
            setattr(user, attr, new_user_data[attr])
            
        db.session.add(user)
        db.session.commit()
        
        return make_response(user_schema.dump(user), 200)

api.add_resource(UserByID, '/users/<int:id>')

if __name__ == '__main__':
    app.run(port=5000, debug=True)