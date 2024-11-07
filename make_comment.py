from dotenv import load_dotenv
import os
from openai import OpenAI
import logging

# 로컬 개발 환경에서만 .env 파일을 로드
dotenv_path = 'keys.env'
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path=dotenv_path)
    logging.info(f".env 파일({dotenv_path})을 성공적으로 로드했습니다.")
else:
    logging.info(f".env 파일({dotenv_path})이 존재하지 않습니다. 환경 변수를 직접 설정합니다.")

# 환경 변수 로드
OPENAI_KEY = os.getenv('OPENAI_KEY')

if not OPENAI_KEY:
    logging.error("OPENAI_KEY가 설정되지 않았습니다. 환경 변수를 확인하세요.")
    raise ValueError("OPENAI_KEY is not set. Please set it in the environment variables.")

# OpenAI 클라이언트 생성
client = OpenAI(
    api_key=OPENAI_KEY
)


def get_gpt_response(diary_text):
    prompt = (
        "You are responsible for reading the user's diary and delivering comments above.\n"
        "Please write a comment that is appropriate for the user's diary.\n"
        f"user's diary: {diary_text}\n"
    )
    message = [
            {
                'role': 'system',
                'content': prompt
            },
            {
                'role': 'user',
                'content': 'make comment'
            }
        ]
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=message,
        max_tokens=1000,
        temperature=0.5,
    )
    gpt = response.choices[0].message.content
    return gpt