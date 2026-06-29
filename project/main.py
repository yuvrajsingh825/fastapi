from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
    return{
        "message":"my first code is running"
    }

@app.get("/about")
def about():
    return {
        "project":"loan risk"

    }

@app.get("/id")
def get_id(id: int):
    return {"id": id,
            "name":"hey"
            }
