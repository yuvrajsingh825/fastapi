from pydantic import BaseModel
from fastapi import FastAPI
app = FastAPI()
class Loan(BaseModel):
    name:str
    id: int
    income: float
    loan_amount: float
    employment_years: int

@app.post("/predict")
def predict_loan_approval(loan: Loan):
    # Placeholder for loan approval prediction logic
    approved =(
        loan.income > 50000 and loan.employment_years > 2
    )
    return {"prediction": "approved" if approved else "rejected"}