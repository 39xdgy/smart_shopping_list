from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from routes.user import user
from routes.shopping_list import shopping_list
# from routes.stock import stock
# from routes.indicator import indicator

import uvicorn

app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=['*']
# )

origins = ["*"]
#origins = ["https://localhost.example.com"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(user, prefix='/user')
app.include_router(shopping_list, prefix='/shopping_list')
# app.include_router(stock, prefix='/stock')
# app.include_router(indicator, prefix='/indicator')

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)