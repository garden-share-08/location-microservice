from flask_restful import abort
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
        #here is where we ended --> Pick up from here
        get_zip_codes
        return {"response": response.text}, 200
