from flask import Flask

app = Flask(__name__)

@app.get("/")
def home():
    return "Server is Alive"

@app.get("/add")
def add(a: float, b: float):   
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

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 10000)
