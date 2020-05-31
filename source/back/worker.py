def clean_text(phrase: str) -> str:
    """Replace consecutive spaces with single space
    """
    return ' '.join(phrase.split())
