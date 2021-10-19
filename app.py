from flask import Flask, redirect, request, jsonify, Response
app = Flask(__name__)

# id and salary of employees
employee_db = {1: 6000, 2: 7000, 3: 8000, 4: 6000} 

@app.route('/',methods = ['GET', 'PUT'])
def index():
    if request.method == 'GET':
        return jsonify(employee_db)
    else:
        id = int(request.args["id"])
        # update salary by 5%
        employee_db[id] = employee_db[id]+(employee_db[id]*0.05) 
        return Response(status=200)

# every path leads to [r]home
@app.route('/<path:path>')
def catch_all_paths(path):
    return redirect('/')
    
if __name__ == '__main__':
    app.run(host='0.0.0.0')