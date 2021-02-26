from flask_restful import Api
from flask import Flask, jsonify
# from api.resources.format import ZipCodes
# from api.services.zip_codes_service import ZipCodesService

def location_microservice():
    app = Flask(__name__)

    # create new tone from dream journal entry text
    @app.route('our/route/here', methods=['POST'])
    def get_zip_codes():

        zip_code = str(request.data)

        some_variable = ZipCodesService.get_zip_codes(zip_code)

        # Could be refactored
        zip_code_results = jsonify({'some_variable': some_variable}).json

        return Format.format_zip_code_results(zip_code_results)

    return app
