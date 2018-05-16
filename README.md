# Internet banking platform of a virtual (vulnerable) financial group 

## How to install

```
$ python manage.py migrate         # prepare DB(sqlite3)
$ python manage.py collectstatic   # prepare static document from template
$ python manage.py createsuperuser # create superuser
$ python manage.py runserver 8000  # run the server
```
If you have any troubles, see below.
* Confirm pip install django or django-debug-toolbar


## ToDo
### Application
* Login/Logout (in progress)
* Balance (in progress / Need modeling)
* Transaction
* Loan
* Account management
* API
* IR?

### Design
* Login/Logout
* Welcome Page
