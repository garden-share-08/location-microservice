import os
import requests
# from <externalApi> import <endpoint we want>

class ZipCodeService:
    @classmethod
    def get_zip_codes(self, zipcode, radius):
        key = os.environ.get('ZIPCODE_API_KEY')
        # We need to load the API_KEY here
        response = requests.get(f'https://www.zipcodeapi.com/rest/{key}/radius.json/{zipcode}/{radius}/miles?minimal')
        return {"response": response.text}
