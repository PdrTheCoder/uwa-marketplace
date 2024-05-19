# Introduction
This is a group project for CITS5505. The software aims to provide a trading platform and community for UWA students.

Project Group members:
PdrTheCoder        Pedro Wang	         23870387	
eggplant0-0 CC     Xuechen Mao         23884895
Yunhui 	          Yunhui Zhang        23839202
                   yingqi LIU          23932642

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

6. Set secret key in environment  
   In windows powershell: `$env:SECRET_KEY='astrongsecretdsfs'`  
   In mac: `export SECRET_KEY=<astrongsecretkey>`

7. Migrate database  
   `cd uwamkp`  
   `flask db upgrade`

8. Run development  
   Under uwamkp folder, run  
   `flask run --debug`  

9. Run Unit tests and Selenium tests
   `cd uwa-marketplace` 
   `python -m unittest discover`



# Add some data for dev
Can use insert_dev_data.py to insert some sample data.


# Run Unit tests and Selenium tests
`cd uwa-marketplace`
`python -m unittest discover`
