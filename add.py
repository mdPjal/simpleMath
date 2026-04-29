from flask import Flask, request

app = Flask(__name__)

@app.get("/")
def home():
    return "Server is Alive"

@app.get("/add")
def add():
    try:
        a = float(request.args.get("a"))
        b = float(request.args.get("b"))
        result = a + b
        return {round(result, 1)}
    
    except (TypeError, ValueError):
        return {"error": "Invalid or missing input a or b"}

@app.get("/test")
def test():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    result = a + b   
    return (round(result,1))

@app.get("/subtraction")
def subtraction(a: float, b: float):
    result = a - b
    return (round(result,1))

@app.get("/multiply")
def multiply(a: float, b: float):
  result = a * b
  return (round(result,1))

@app.get("/divide")
def divide(a: float, b: float):
  result = a / b
  return (round(result,1))
