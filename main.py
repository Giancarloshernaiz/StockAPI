import uvicorn
import dotenv
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.producto import router_productos

dotenv.load_dotenv(override=True)

app:FastAPI = FastAPI()
app.include_router(prefix='/api/v1', router=router_productos)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(app, host=os.getenv('HOST', '0.0.0.0'), port=int(os.getenv('PORT', 8000)), log_level="debug")