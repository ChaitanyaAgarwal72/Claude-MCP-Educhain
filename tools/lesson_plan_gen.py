from educhain import Educhain, LLMConfig
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()

def generate_lesson_plan(topic: str, duration: str):
    model = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        google_api_key=os.getenv("GEMINI_API_KEY")
    )
    config = LLMConfig(custom_model=model)
    client = Educhain(config)

    result = client.content_engine.generate_lesson_plan(
        topic=topic,
        duration=duration
    )
    return result.model_dump()
