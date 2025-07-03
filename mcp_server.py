from mcp.server.fastmcp import FastMCP
from tools.mcq_generator import generate_mcqs
from tools.lesson_plan_gen import generate_lesson_plan
from tools.youtube_qna import generate_questions_from_youtube_video
from tools.ques_from_data import generate_questions_from_data_file

# Initialize MCP server
mcp = FastMCP("Educhain Server")

# Tool 1: Generate MCQs
@mcp.tool()
def generate_multiple_choice_questions(topic: str, num: int) -> dict:
    """Generate MCQs for a topic using Educhain."""
    return generate_mcqs(topic, num)

# Tool 2: Generate Questions from YouTube Video
@mcp.tool()
def generate_questions_from_youtube(url: str, num: int) -> dict:
    """Generate questions from a YouTube video using Educhain."""
    return generate_questions_from_youtube_video(url, num)

# Tool 3: Generate Questions from Data File
@mcp.tool()
def generate_questions_from_data(source: str, source_type: str, num: int) -> dict:
    """Generate questions from a data file (pdf, txt, url) using Educhain."""
    return generate_questions_from_data_file(source, source_type, num)

# Tool 4: Lesson Plan Generator
@mcp.tool()
def lesson_plan_generator(topic: str, duration: int) -> dict:
    """Get lesson plan for a topic using Educhain."""
    return generate_lesson_plan(topic, duration)

# Entry point
if __name__ == "__main__":
    mcp.run()
