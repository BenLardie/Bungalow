Make a clone of the repository and cd into it.

Create a virtual eniviroment.
``` pyenv virturalenv bungalow ```

Then in the command liine you need to install the requirments. 
``` pip install -r requirements.txt ```

After it is installed you can migrate.
```python manage.py migrate```

Now you can run the server.
```python manage.py runserver```

To upload the CSV file visit.
```http://localhost:8000/upload-csv/```

Once that is completed you can find the data at this endpoint.
```http://localhost:8000/houses/```
