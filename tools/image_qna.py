from educhain import Educhain

# Initialize the Educhain client
client = Educhain()

def generate_questions_from_image(image_path: str, num: int = 3, target_language: str = "en") -> dict:
    """
    Generate questions from an image using Educhain.

    Args:
        image_path (str): Path to the image file.
        num (int): Number of questions to generate.
        target_language (str): Output language for questions.

    Returns:
        dict: Dictionary of generated questions.
    """
    print(f"[TOOL] Image QnA called: {image_path}, num={num}, lang={target_language}")
    questions = client.qna_engine.generate_questions_from_image(
        image=image_path,
        num=num,
        target_language=target_language
    )
    return questions.dict()
