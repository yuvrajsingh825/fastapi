from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()
class LoanApplication(BaseModel):
    age :int
    income :float
    loan_amount :float
    employement_years:int
@app.post("/predict")
def predict_loan_approval(loan_application: LoanApplication):
    # Placeholder for loan approval prediction logic
    if loan_application.income >50000 and loan_application.employement_years>2:
       decision = "approved"
    else:
        decision = "rejected"
    return {
        "age": loan_application.age,
        "income": loan_application.income,
        "loan_amount": loan_application.loan_amount,
        "employement_years": loan_application.employement_years,
        "prediction": decision
    }