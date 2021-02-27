from flask import Flask, jsonify
from api.services.zip_code_service import ZipCodeService
from config import config

def create_location_microservice(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    @app.route('/zipcodes/<zipcode>/<radius>', methods=['GET'])
    def get_zip_codes(zipcode, radius):
        zip_codes_result = ZipCodeService.get_zip_codes(zipcode, radius)

        return zip_codes_result


    return app
