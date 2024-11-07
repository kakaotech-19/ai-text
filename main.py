from fastapi import FastAPI
import logging
import os
from pydantic import BaseModel
from dotenv import load_dotenv
import make_comment

# 로컬 개발 환경에서만 .env 파일을 로드
dotenv_path = 'keys.env'
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path=dotenv_path)
    logging.info(f".env 파일({dotenv_path})을 성공적으로 로드했습니다.")
else:
    logging.info(f".env 파일({dotenv_path})이 존재하지 않습니다. 환경 변수를 직접 설정합니다.")

app = FastAPI()

class Content(BaseModel):
    content: str
@app.post('/comment')
async def process_profile(content: Content):
    comment = make_comment.get_gpt_response(content)
    return {"content": comment}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)