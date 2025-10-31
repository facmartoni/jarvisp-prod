"""
LLM Service for Gemini integration.
"""

import os

from google import genai


def get_gemini_model():
    """
    Get configured Gemini model.

    Returns:
        genai.Client: Configured Gemini client

    Raises:
        ValueError: If GEMINI_API_KEY is not set
    """
    api_key = os.getenv('GEMINI_API_KEY')

    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY is not set. Please add it to your .env file."
        )

    # The client gets the API key from the environment variable `GEMINI_API_KEY`.
    client = genai.Client()

    return client

