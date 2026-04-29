from flask import Flask, request

app = Flask(__name__)

@app.get("/")
def home():
    return "Server is Alive"

@app.get("/add")
def add():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    result = a + b
    return str(round(result, 1))
    

@app.get("/subtraction")
def subtraction():
    key = request.args.get("key")

    if key != "VIP120":
        return "Feature locked"

    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    result = a - b
    return str(round(result, 1))
    
@app.get("/multiply")
def multiply():
    key = request.args.get("key")

    if key != "VIP121":
        return "Feature locked"
        
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    result = a * b
    return str(round(result, 1))

@app.get("/divide")
def divide():
    key = request.args.get("key")

    if key != "VIP122":
        return "Feature locked"
        
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    result = a / b
    return str(round(result, 1))
