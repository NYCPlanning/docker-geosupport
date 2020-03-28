from flask import Flask, render_template
from flask_restful import Resource, Api, reqparse
from geosupport import Geosupport, GeosupportError
from suggest import GeosupportSuggest
import os

app = Flask(__name__)
api = Api(app)

g = Geosupport()
s = GeosupportSuggest(g)

RELEASE=os.environ.get('RELEASE', '')
MAJOR=os.environ.get('MAJOR', '')
MINOR=os.environ.get('MINOR', '')
PATCH=os.environ.get('PATCH', '')
VERSION=f'{MAJOR}.{MINOR}.{PATCH}'

class GeosupportApi(Resource):
    """
    Supports all functions and arguments of python-geosupport
    """

    def get(self, geofunction):

        params = reqparse.request.args

        try:
            result = g[geofunction](**params)
            return {'error': False, 
                    "version": VERSION, 
                    "release": RELEASE, 
                    'result': result}

        except GeosupportError as ge:
            return {'error': True, 
                    "version": VERSION, 
                    "release": RELEASE, 
                    'result': ge.result}

        except AttributeError:
            return {'error': True, 
                    "version": VERSION, 
                    "release": RELEASE, 
                    'result': {"Message": "Unknown Geosupport function '{}'.".format(geofunction)}}


api.add_resource(GeosupportApi, '/geocode/<string:geofunction>', endpoint='geocode')


class SuggestApi(Resource):
    """
    An address suggestions API
    """

    def get(self):

        try:
            parser = reqparse.RequestParser()
            parser.add_argument('address', type=str, trim=True, required=True)
            parser.add_argument('borough_code', type=int, trim=True, required=False)
            args = parser.parse_args()
            result = s.suggestions(args["address"], borough_code=args["borough_code"])
            return {"error": False, 
                    "version": VERSION, 
                    "release": RELEASE, 
                    "result": result}
        except Exception as e:
            return {"error": True, 
                    "version": VERSION, 
                    "release": RELEASE, 
                    "result": str(e)}


api.add_resource(SuggestApi, '/suggest', endpoint='suggest')

class HelpApi(Resource):
    """
    A geosupport function reference API
    """

    def get(self, geofunction):

        try:
            result = g[geofunction].help(return_as_string=True)
            return render_template("help.html", content=result)
        except Exception as e:
            return render_template("help.html", content=str(e))

api.add_resource(HelpApi, '/help/<string:geofunction>', endpoint='help')

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
