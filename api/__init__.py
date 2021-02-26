# not sure if we need this API package
# from flask_restful import Api
from flask import Flask, jsonify
# from api.resources.format import ZipCode
from api.services.zip_codes_service import ZipCodesService

def location_microservice():
    app = Flask(__name__)
    #api = Api(app)

    # create new tone from dream journal entry text

    @app.route('zipcodes/<string:zipcode>/<float:radius>', methods=['GET'])
    def get_zip_codes(self, zipcode, radius):
        # The below code is only for posts 
        # zip_code = str(request.data)
        
        zip_codes_result = ZipCodeService.get_zip_codes(zip_code, radius)

        # Could be refactored
        zip_codes_result = jsonify({'some_variable': some_variable}).json

        # I don't think we need this because the formatting will be minimal 
        # return Format.format_zip_code_results(zip_code_results)

    return app
