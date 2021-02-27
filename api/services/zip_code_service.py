import os
import requests
from dotenv import load_dotenv
# from <externalApi> import <endpoint we want>

class ZipCodeService:
    @classmethod
    def get_zip_codes(self, zipcode, radius):
        load_dotenv()
        key = os.environ.get('ZIPCODE_API_KEY')
        response = requests.get(f'https://www.zipcodeapi.com/rest/{key}/radius.json/{zipcode}/{radius}/miles?minimal')
        
        return response.json()
