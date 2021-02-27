# Garden-Share: Location Microservice

## Overview 

This repository is a microservice for the Garden-Share application. It's sole purpose is to collect an array of zip codes that fall within a specified mile radius and origin zip code. 

All repositories in the Garden-Share project can be found [here](https://github.com/garden-share-08).

## Table of Contents 
  - [Installation Instruction](#installation-instructions)
  - [Run Tests](#run-tests)
  - [The Python Equivalent to Pry](#the-python-equivalent-to-pry)
  - [Authors](#)


## Installation Instructions 

1. Clone [the](https://github.com/garden-share-08/location-microservice) repository.
1. Set up a virtual environment: `python3 -m venv ./venv`  
  i. To shut off the virtual environment: `deactivate`
1. Activate virtual environment: `source venv/bin/activate`
1. Install Python packages: `pip3 install -r requirements.txt`  
  i. If you get a `ImportError: No module named dotenv` error, shut off the virtual environment and run `pip3 python-dotenv` in the command line to install dotenv globally. 
1. Create a `.env` file in the root directory and add a `ZIPCODE_API_KEY` key with your registered api key as its value. (See the `.env_example` file as an example).  
  i. Go to [this](https://www.zipcodeapi.com/Register) website to register for a free api key.


## Run Tests 
1. Run `pytest` in terminal 
1. Keep in mind, that your api key has a rate limit of 50 requests/hour (for the first 2 weeks) and 10 requests/hour after that.


## The Python Equivalent to Pry 
1. Place code snippet at location where you want to break execution: `import ipdb; ipdb.set_trace()`  
  i. If you want to break execution when running a test, use `pytest -s`   


## Authors
  - **Aaron Townsend** - *Turing Student* - [GitHub Profile](https://github.com/atownse) - [LinkedIn](https://www.linkedin.com/in/aaron-townsend-667604176/)
  - **Bruce Gordon** - *Turing Student* - [GitHub Profile](https://github.com/bruce-gordon) - [Turing Alum Portfolio](https://alumni.turing.io/alumni/bruce-gordon) - [LinkedIn](https://www.linkedin.com/in/brucemgordon/)
  - **Chadrick Dickerson** - *Turing Student* - [GitHub Profile](https://github.com/chadrick-d-dev) - [Turing Alum Portfolio](https://alumni.turing.io/alumni/chadrick-dickerson) - [LinkedIn](https://www.linkedin.com/in/chadrick-dickerson/)
  - **Christopher Allbritton** - *Turing Student* - [GitHub Profile](https://github.com/Callbritton) - [Turing Alum Portfolio](https://alumni.turing.io/alumni/christopher-allbritton) - [LinkedIn](https://www.linkedin.com/in/christopher-allbritton)
  - **Dani Coleman** - *Turing Student* - [GitHub Profile](https://github.com/dcoleman21) - [Turing Alum Portfolio](https://alumni.turing.io/alumni/dani-coleman) - [LinkedIn](https://www.linkedin.com/in/dcoleman-21/)
  - **Joshua Carey** - *Turing Student* - [GitHub Profile](https://github.com/jdcarey128) - [Turing Alum Portfolio](https://alumni.turing.io/alumni/joshua-carey) - [LinkedIn](https://www.linkedin.com/in/carey-joshua/)
