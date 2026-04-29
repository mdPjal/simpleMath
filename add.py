from flask import Flask

app = Flask(__name__)

@app.get("/")
def home():
    return "Server is Alive"

@app.get("/add")
def add():
    a = float(request.args.get("a", 0))
    b = float(request.args.get("b", 0))
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
