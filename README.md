## Installation Instructions 

1. Set up virtual environment: `python3 -m venv ./venv`  
  i. To shut off your virtual environment: `deactivate`
1. Activate virtual environment: `source venv/bin/activate`
1. Install Python packages: `pip3 install -r requirements.txt`  
  i. If you get a `ImportError: No module named dotenv` error, shut off your virtual environment and run `pip3 python-dotenv` in the command line to install dotenv globally. 
1. Create a `.env` file in the root directory and add the `ZIPCODE_API_KEY` key with a registered api key. (See the `.env_example` file as an example). 


## Run Tests 
1. Run `pytest` in terminal 
1. Keep in mind, that this api key has a rate limit of 50 calls/2 hours.


## The Python Equivalent of Pry 
1. Place code snippet at location where you want to break execution: `import ipdb; ipdb.set_trace()`  
  i. If you want to break execution when running a test, use `pytest -s` when running tests.  
