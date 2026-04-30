from flask import Flask, request

app = Flask(__name__)

@app.get("/")
def home():
    return "Server is Alive"

@app.get("/health")
def health():
    return "OK"

@app.get("/add")
def add():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    result = a + b
    return str(round(result, 1))
    
@app.get("/subtraction")
def subtraction():
    key = str(request.args.get("key"))

    if key != "VIP120":
        return "Access Denied!"

    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    result = a - b
    return str(round(result, 1))

@app.get("/multiply")
def multiply():
    key = str(request.args.get("key"))

    if key != "VIP121":
        return "Access Denied!"
        
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    result = a * b
    return str(round(result, 1))

@app.get("/divide")
def divide():
    key = str(request.args.get("key"))

    if key != "VIP122":
        return "Access Denied!"
        
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    result = a / b
    return str(round(result, 1))
