from mcp.server.fastmcp import FastMCP # type: ignore
from tools.mcq_generator import generate_mcqs
from tools.lesson_plan_gen import generate_lesson_plan
from tools.youtube_qna import generate_questions_from_youtube_video
from tools.image_qna import generate_questions_from_image

# Initialize MCP server
mcp = FastMCP("Educhain Server")

# Tool 1: Generate MCQs
@mcp.tool()
def generate_multiple_choice_questions(topic: str, num: int = 5) -> dict:
    """Generate MCQs using Educhain."""
    return generate_mcqs(topic, num)

# Tool 2: Generate Questions from YouTube
@mcp.tool()
def generate_questions_from_youtube(
    url: str,
    num: int = 3,
    target_language: str = "en",
    preserve_original_language: bool = False
) -> dict:
    """Generate MCQs from a YouTube video using Educhain."""
    return generate_questions_from_youtube_video(
        url, num, target_language, preserve_original_language
    )

# Tool 3: Generate Questions from Image
@mcp.tool()
def generate_questions_from_image_tool(image_path: str, num: int = 3, target_language: str = "en") -> dict:
    """Generate questions from an image using Educhain."""
    return generate_questions_from_image(image_path, num, target_language)

# Resource 1: Generate Lesson Plan
@mcp.resource("lessonplan://{topic}/{duration}")
def lesson_plan_resource(topic: str, duration: int) -> dict:
    """Get lesson plan for a topic using Educhain."""
    return generate_lesson_plan(topic, duration)

# Entry point
if __name__ == "__main__":
    mcp.run()
