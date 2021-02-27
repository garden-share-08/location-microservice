import json
import unittest 
from api import create_location_microservice

class LocationMicroserviceTest(unittest.TestCase):
  def test_location_microservice_returns_zip_codes(self):
    self.app = create_location_microservice('testing')
    self.client = self.app.test_client()
    
    zipcode = '80017'
    expected_zip_codes = ["80015","80013","80014","80040","80041","80042","80044","80046","80047","80017","80247","80012","80011","80045"]
    radius = 5

    response = self.client.get(
      f'/zipcodes/{zipcode}/{radius}'
    )
    self.assertEqual(200, response.status_code)

    data = json.loads(response.data.decode('utf-8'))
    self.assertEqual(expected_zip_codes, data['zip_codes'])

if __name__ == '__main__':
  unittest.main()
