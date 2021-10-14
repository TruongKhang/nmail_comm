# Communication between users and server

# Requirements

    pip install -r requirements.txt

# Running

Start a server by

    python manage.py migrate
    python manage.py runserver

By default, the server is created at `127.0.0.1:8000`. 
You can use `127.0.0.1:8000/nmail_server/upload` to test your HTTP requests for uploading files.

If the upload is success, the file will be saved in `uploads` folder.

To send data from different computer. Start a server at `0.0.0.0`

    python manage.py runserver 0.0.0.0:8000
    
Then, change `127.0.0.1:8000` to `<IP address>:8000` to test your upload API.
