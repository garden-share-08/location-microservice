from flask import Flask
# from flask_restful import abort
from api.services.zip_codes_service import ZipCodesService

class ZipCodes:
    def _abort_if_invalid(self, zipcode, radius):
        if len(str(zipcode)) != 5 and radius > 50:
          abort({"error": "Invalid zip code and radius distance too large"})
        elif len(str(zipcode)) != 5:
          abort({"error": "Invalid zip code"})
        elif radius > 50:
          abort(400, message="Radius distance too large")

    def get(self, zipcode, radius):
        self._abort_if_invalid(zipcode, radius)
        response = get_zip_codes(zipcode, radius)
        return {"response": response.text}, 200

api.add_resource(ZipCodes, "/zipcodes/<int:zipcode>/<float:radius>")

if __name__ == "__main__":
    app.run(debug=True)
