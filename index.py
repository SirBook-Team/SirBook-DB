from fastapi import FastAPI
from routes.usr import router as user

app = FastAPI()
app.include_router(user)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    