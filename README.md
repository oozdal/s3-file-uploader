# geods-client-api
This API is primarily designed for clients to upload their data to goldspot-geods S3 bucket securely.

## Test geods-client-api on behalf of clients

Click http://34.239.113.227:8000/admin  (Make sure that you type http, not https)

Assume that you are the client Minto and you are provided the username and password below.

Now you can send your files to our S3 bucket (See the next section: Usage)

Username: ```minto```

Password: ```GzXLEUEE```

## Usage

Once you login Django administration, 

1) Click the ```Add``` button in the ```Blog``` section

2) Enter the appropriate title for the file you uploaded in the ```Title``` section.

3) Click ```Category``` and select the right category for the input file. (OPTIONAL: You may add additional categories if needed.)

3) Provide more information about the file you uploaded in the ```Body``` section.

4) Select the file you want to upload and then click ```Save```

5) You can see all the files you have uploaded by clicking the link http://34.239.113.227:8000/
 
You may also click categories and see the uploaded input layers per category. For instance,

http://34.239.113.227:8000/category/Magnetics/

http://34.239.113.227:8000/category/Gravity/

6) Open your AWS console and check if you can see your file in ```s3://goldspot-geods/static/blog_images/```


## Installation (For geods-client-api developers)

1)```git clone https://github.com/GoldspotDiscoveries/geods-client-api.git```

2)```conda env create --name "geods-client-api" --file environments.yml```

3)```conda activate geods-client-api```

4)```python setup.py install``` (Optional)

5)```python src/geods-client-api/manage.py migrate```

6)```winpty python src/geods-client-api/manage.py createsuperuser --username SET_A_USERNAME_FOR_YOURSELF```

7)```python src/geods-client-api/manage.py runserver```

8)Click http://127.0.0.1:8000/admin and use the username and password you created in Step 6

IMPORTANT: If you are NOT a Windows user, just type the following line in Step 6 (without winpty):

```python src/geods-client-api/manage.py createsuperuser --username SET_A_USERNAME_FOR_YOURSELF```

## Installation (For Docker users)

1) ```docker pull ghcr.io/goldspotdiscoveries/geods-client-api:latest```
2) ```docker run --publish 8000:8000 ghcr.io/goldspotdiscoveries/geods-client-api```
3) Click http://127.0.0.1:8000/admin and login using your username and password provided by admin (Contact Ozer)



## FAQ

Q1: I'm getting an error: ```Django Server Error: port is already in use```. What should I do?

A1: Kill all the processes associated with port 8000 and get back to Step 5. 

On mac you need to use ```sudo lsof -i tcp:8000``` then kill the process ids that show up.

For more info, https://stackoverflow.com/questions/20239232/django-server-error-port-is-already-in-use

Q2: I cannot pull the image from ghcr as I get access denied. What should I do?

A2: First you should login Github Container Registry securely using your github username and token. 

```docker login ghcr.io --username $YOUR_GITHUB_USERNAME``` and then enter your github token

## Contributing

Interested in contributing? Check out the contributing guidelines. TO DO.

## License

```geods-client-api``` is created by Ozer Ozdal. It is licensed under the terms of the MIT license.
