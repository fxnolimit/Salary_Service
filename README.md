### 1. Docker

##### * build an image from current folder's Dockerfile
    docker build -t [image_name] .

##### * build container making sure to bind it to port 5000
    docker run -p 5000:5000 [image_name]

##### * flask should be running on localhost:5000
    browse to http://127.0.0.1:5000
    
### 2. Test API methods

##### * GET 
    browse to http://127.0.0.1:5000

##### * PUT
    Use Postman or any REST client
    Send a PUT request to localhost:5000 and append the id of the employee you which to increase the salary
    example to increase salary of employee with id of 1:  http://localhost:5000/?id=1
    
##### * Run tests.py to test with python
    python tests.py
    
    


    
