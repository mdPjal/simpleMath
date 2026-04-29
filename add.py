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
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    result = a - b
    return str(round(result, 1))
    
@app.get("/multiply")
def multiply():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    result = a * b
    return str(round(result, 1))

@app.get("/divide")
def divide():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    result = a / b
    return str(round(result, 1))
