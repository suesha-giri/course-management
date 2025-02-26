# Course Management

## Instructions to run the project locally

### Steps
1. Clone the github repository.
2. Set up Virtual Environment.
3. Install Required Packages: 
```python
pip install -r requirements.txt
```
4. Create a new database and add the credentials to the .env file.
5. Run migrations
```python
python manage.py makemigrations courses, users
python manage.py migrate courses, users
```
6. Create Superuser for Admin Access
```python
python manage.py createsuperuser
```
7. Run the server
```python
python manage.py runserver
```
8. Visit http://127.0.0.1:8000/dashboard/ to access the custom admin dashboard.
