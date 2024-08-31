import flask
from flask import request
from flask.views import MethodView
from models import Advertisements, Session


app = flask.Flask('app')


def hello():
    return {'hello': 'world'}


class UserView(MethodView):
    def post(self):
        pass


class AdvertisementsView(MethodView):
    def post(self):
        json_data = request.json
        print(json_data)
        advertisement = Advertisements(**json_data)
        request.session.add(advertisement)
        request.session.commit()
        return {'id': advertisement.id}

    def patch(self):
        pass

    def delete(self):
        pass


@app.before_request
def before_request():
    session = Session()
    request.session = session


@app.after_request
def after_request(http_response: flask.Response):
    request.session.close()
    return http_response


AdvertisementsView.as_view('advertisements')

app.add_url_rule('/advertisements/', view_func=hello, methods=['POST'])

app.run()