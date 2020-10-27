##requirements
```python3.6+```
 
##create viutual environment 
```
python3 -m venv venv
```
##export variables
```
export SECRET_KEY="" 
```
your secretkey

##install required packges
```
pip install -r requirement.txt
```
##make migrations
```
python manage.py makemigrations product
python manage.py migrate
```
##run command  to load data
```
python manage.py add_product
```
##check url
http://127.0.0.1/api/products
##make search within api view 
using filter enter keywords i.r brand, item name 
