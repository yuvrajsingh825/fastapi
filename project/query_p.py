from fastapi import FastAPI

app = FastAPI()
all_customers = [
    {
        "id": 10, "name":"Heisenberg","age":55 ,"risk":"medium"
    },
    {
        "id": 11, "name":"Heisen","age":57 ,"risk":"high"
    },
    {
        "id": 12, "name":"berg","age":53 ,"risk":"low"
    }
]

@app.get("/customers")
def get_customers(name:str , risk:str):
    filtered  = [
        customer for customer in all_customers
        if customer["name"] == name and customer["risk"] == risk
    ]
    return{
        "name":name,
        "risk":risk,
        "count":len(filtered),
        "results":filtered

    }
