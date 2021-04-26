
# Studio Ghibli demo project
This application demonstrtes the api integration with third party data vendor. This 
wep application recieves the data from Studio Ghibli, a Japanese movie company and show results in django template.


## Installing steps

Step 1: Install Python 3 from https://www.python.org/downloads/

step 2: Create virtual environment for keeping dependencies aligned 
``` 
python3 -m venv env_name
```
Step 3: Activate virtual envrionment by 
``` 
source env_name/bin/activate 
```
Step 4: Install dependecies by 
``` 
pip3 install -r requirements.txt
```

## Run tests
```
cd studio_ghibli
```
```
python3 manage.py test
```

## Running steps

```
cd studio_ghibli
```
```
python3 manage.py runserver
```
Open the url in browser -> http://localhost:8000/movies

