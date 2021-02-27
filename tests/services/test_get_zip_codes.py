import unittest 
from api.services.zip_code_service import ZipCodeService 

class ZipCodeServiceTest(unittest.TestCase):
  def test_returns_zip_code_array(self):
    zip_code = "80017"
    expected_zip_codes = ["80015","80013","80014","80040","80041","80042","80044","80046","80047","80017","80247","80012","80011","80045"]
    radius = 5
    response = ZipCodeService.get_zip_codes(zip_code, radius)
    result = response['zip_codes']
    self.assertEqual(expected_zip_codes, result)

if __name__ == '__main__':
  unittest.main()
