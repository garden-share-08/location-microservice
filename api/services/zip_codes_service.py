import os
# from <externalApi> import <endpoint we want>

class ZipCodesService:
    @classmethod
    def get_zip_codes(self, zip_code):
        self._abort_if_invalid(zipcode, radius)
        response = requests.get(f'https://www.zipcodeapi.com/rest/{key}/radius.json/{zipcode}/{radius}/miles?minimal')
        return {"response": response.text}, 200

        # service = ToneAnalyzerV3(
        #     version='2017-09-21',
        #     authenticator=authenticator)

        # service.set_service_url('https://gateway.watsonplatform.net/tone-analyzer/api')

        # some_variable = service.tone(
        #     {'text': dream_text},
        #     content_type='application/json',
        #     content_language='fr' or 'en'
        # ).get_result()

        # return some_variable
