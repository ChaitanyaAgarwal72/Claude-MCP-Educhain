from educhain import Educhain

# Initialize Educhain client once
client = Educhain()

def generate_questions_from_youtube_video(url: str, num: int, target_language: str = "en", preserve_original_language: bool = False) -> dict:
    """
    Generate multiple choice questions from a YouTube video using Educhain.
    
    Args:
        url (str): The URL of the YouTube video.
        num (int): Number of questions to generate.
        target_language (str): The language for the output questions.
        preserve_original_language (bool): If True, original language is preserved.

    Returns:
        dict: A dictionary of generated questions.
    """
    print(f"[TOOL] YouTube QnA called: {url}, num={num}, lang={target_language}, preserve={preserve_original_language}")
    questions = client.qna_engine.generate_questions_from_youtube(
        url=url,
        num=num,
        target_language=target_language,
        preserve_original_language=preserve_original_language
    )
    return questions.dict()
