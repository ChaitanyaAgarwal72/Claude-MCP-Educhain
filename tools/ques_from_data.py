from educhain import Educhain, LLMConfig
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()

def generate_questions_from_data_file(source: str,source_type: str, num: int):
    model = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        google_api_key=os.getenv("GEMINI_API_KEY")
    )
    config = LLMConfig(custom_model=model)
    client = Educhain(config)

    result = client.qna_engine.generate_questions_from_data(
        source=source,
        source_type=source_type,
        num=num
    )
    return result.model_dump()
