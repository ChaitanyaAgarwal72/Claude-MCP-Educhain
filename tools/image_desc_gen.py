from educhain import Educhain, LLMConfig
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()

def generate_image_desc(path: str):
    model = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        google_api_key=os.getenv("GEMINI_API_KEY")
    )
    config = LLMConfig(custom_model=model)
    client = Educhain(config)

    result = client.qna_engine.solve_doubt(
        image_source=path,
        prompt="Explain the image in detail.",
        detail_level="High"
    )
    return result.model_dump()
