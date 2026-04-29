from fastapi import FastAPI

app = FastAPI()

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
