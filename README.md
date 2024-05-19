# Introduction  
This is a group project for CITS5505. We developed a trading platform and community for UWA students. As a UWA student, you can register your account and start selling your items and buying items from other students. Join us and start trading today!

We use python / flask to build a lightweight but full capable dynaic backend serving requests from clients. Flask framework features in providing a MVC (Model-View-Controller) architecture which offers modularized development pattern.  

For frontend development, we use html, css, js and bootstrap style framework to provide a responsive and dynamic webpage.  

# Product Design  
-  A user can create an account using an UWA email.  

-  A user can sign in with a registered user account.  

-  A user can listing items after login. For a listing, we support uploading one image, specifying title, condition, description, and price.

-  A user can expore all items from other uwa students. We also provide pagination, sorting and searching functionality for better user experience.

-  A user can view details of a listed item and communicate with sellers by leaving messages to them.  

-  A user can also manage his/her listings, including creating new listings, mark listings as sold (In our design, sellers and buyers trade items offline, but after a successful sell, the seller can mark his/her items as sold.), delete listing.  


# Team Information  
| Name | Student ID | Github Username |
|------| -----------| ----------------|
|Pedro Wang| 23870387 | PdrTheCoder |
|Xuechen|23884895|eggplant0-0 CC|
|Yunhui Zhang|23839202|YunhuiZ|
|Yingqi Liu|23932642|SexyZoe|

If you have any questions, please contact us via <our_student_id>@student.uwa.edu.au. Thank you.


# Development Setup
1. Clone the repository  
   ```bash
   https://github.com/PdrTheCoder/uwa-marketplace.git
   cd uwa-marketplace  
   ```

2. Make sure you have python 3.10.2 installed  
   check default python interpreter  
   ```bash
   python
   ```

3. Create a virtual environment  
   ```bash
   python -m venv venv
   ```

4. Activate virtualenv   
   **on Windows**  
   ```bash
   venv\Scripts\activate
   ```

   **on Mac or linux OS systems**  
   ```bash
   source venv/bin/activate
   ```  

6. Install python package  
   `pip install -r requirements.txt`  


7. Set secret key in environment  
   **In windows powershell**  
   ```bash
   $env:SECRET_KEY='a_strong_secret_key'  
   ```

   **In mac**
   ```bash
   export SECRET_KEY=<a_strong_secret_key>
   ```

8. CD to app folder, migrate database  
   ```bash
   cd uwamkp  
   flask db upgrade  
   ```

9. Run development inside uwamkp folder  
   ```bash
   flask run --debug  
   ```


# Dev data populating
Can use insert_dev_data.py to insert some sample data. Please check the file for details 


# Run Unit tests and Selenium tests  
```bash
cd uwa-marketplace  
python -m unittest discover  
```



