from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class Eligibility(BaseModel):
    age :  int 
    marks :float

@app.post("/eligibility")
def check_eligibility(eligibility : Eligibility):
    if eligibility.age>=18 and eligibility.marks>=85:
        decision = "Eligible"
    else:
        decision = "Not Eligible"
    return {
        "prediction": decision
        }