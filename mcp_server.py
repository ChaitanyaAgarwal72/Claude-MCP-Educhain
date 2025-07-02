from mcp.server.fastmcp import FastMCP
from tools.mcq_generator import generate_mcqs
from tools.lesson_plan_gen import generate_lesson_plan
from tools.youtube_qna import generate_questions_from_youtube_video
from tools.image_desc import generate_description_from_images 

# Initialize MCP server
mcp = FastMCP("Educhain Server")

# Tool 1: Generate MCQs
@mcp.tool()
def generate_multiple_choice_questions(topic: str, num: int) -> dict:
    """Generate MCQs for a topic using Educhain."""
    print(f"[TOOL] MCQ Generator called: topic={topic}, num={num}")
    return generate_mcqs(topic, num)

# Tool 2: Generate Questions from YouTube Video
@mcp.tool()
def generate_questions_from_youtube(url: str, num: int) -> dict:
    """Generate questions from a YouTube video using Educhain."""
    print(f"[TOOL] YouTube QnA called: url={url}, num={num}")
    return generate_questions_from_youtube_video(url, num)

# Tool 3: Generate Description from Image
@mcp.tool()
def generate_questions_from_image_tool(image_path: str) -> dict:
    """Generate a detailed explanation from an image using Educhain."""
    print(f"[TOOL] Image Description Tool called: path={image_path}")
    return generate_description_from_images(image_path)

# Resource 1: Lesson Plan Generator
@mcp.resource("lessonplan://{topic}/{duration}")
def lesson_plan_resource(topic: str, duration: int) -> dict:
    """Get lesson plan for a topic using Educhain."""
    print(f"[RESOURCE] Lesson Plan called: topic={topic}, duration={duration}")
    return generate_lesson_plan(topic, duration)

# Entry point
if __name__ == "__main__":
    mcp.run()
