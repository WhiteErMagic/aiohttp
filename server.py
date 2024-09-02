import flask
from flask import request, jsonify
from flask.views import MethodView
from models import Advertisements, Session, User

app = flask.Flask('app')


def hello():
    return {'hello': 'world'}


class UserView(MethodView):
    def post(self):
        pass


class AdvertisementsView(MethodView):
    def post(self):
        json_data = request.json
        advertisement = Advertisements(**json_data)
        request.session.add(advertisement)
        request.session.commit()
        return {'id': advertisement.id}

    def patch(self, id):
        json_data = request.json
        advertisement = request.session.get(Advertisements, id=id)
        for k, v in json_data:
            advertisement[k] = v
        request.session.commit()
        return jsonify(advertisement.json)

    def delete(self, id):
        request.session.delete(Advertisements, id=id)
        request.session.commit()
        return {'id': 'deleted'}

    def get(self, id: int):
        advertisement = request.session.get(Advertisements, id=id)
        return jsonify(advertisement.json)


@app.before_request
def before_request():
    session = Session()
    request.session = session


@app.after_request
def after_request(http_response: flask.Response):
    request.session.close()
    return http_response


app.add_url_rule('/advertisements/', view_func=AdvertisementsView.as_view('advertisements'), methods=['POST', 'GET',
                                                                                                'DELETE', 'UPDATE'])
app.run()