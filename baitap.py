#imprort
from fastapi import FastAPI 


# tạo thực thể
app = FastAPI()




# viết API
@app.get('/')
def get_root():
    return{ "message": "hello world  1234231 !!!!" }