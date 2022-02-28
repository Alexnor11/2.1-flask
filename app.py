from flask import Flask, jsonify, request
from flask.views import MethodView
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from datetime import datetime
import config

app = Flask(__name__)

app.config.from_mapping(SQLALCHEMY_DATABASE_URI=config.POSTGRES_URI)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# Создание модели объявления
class Advertisement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), index=True, nullable=False)
    title = db.Column(db.String(128), index=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.now())

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'title': self.title,
            'description': self.description,
            'data': self.date,
        }


# Создание Views
class AdViews(MethodView):
    def get(self, ad_id):
        ads = Advertisement.query.get(ad_id)
        if ads is not None:
            return jsonify(ads.to_dict())
        else:
            return jsonify({'message': 'This ad has been removed'})

    def post(self):
        ads = Advertisement(**request.json)
        # ads.add()
        db.session.add(ads)
        db.session.commit()
        return jsonify(ads.to_dict())

    def delete(self, ad_id):
        ads = Advertisement.query.get(ad_id)
        if ads is not None:
            db.session.delete(ads)
            db.session.commit()
            return jsonify({'message': 'deleted'})
        else:
            return jsonify({'message': 'This ad has been removed'})


app.add_url_rule('/article/', view_func=AdViews.as_view('article_create'), methods=['POST', ])
app.add_url_rule('/article/<int:ad_id>', view_func=AdViews.as_view('article_get'), methods=['GET', ])
app.add_url_rule('/article/<int:ad_id>', view_func=AdViews.as_view('article_delete'), methods=['DELETE', ])
