# Introduction
This is a group project for CITS5505. The software aims to provide a trading platform and community for UWA students.

# Development setup
1. Make sure you have python 3.10.2 installed  
   check default python interpreter  
   `python`

2. Create virtualenv  
   `python -m venv venv`  

3. Activate virtualenv (Windows)  
   `venv\Scripts\activate`
   
4. Activate virtualenv(Mac)  
   `source venv/bin/activate`

   on Mac maybe use `source venv\bin\activate`

5. Install python package  
   `pip install -r requirements.txt`  

6. Migrate database  
   `cd uwamkp`  
   `flask db upgrade`

7. Run development  
   Under uwamkp folder, run  
   `flask run --reload`   
