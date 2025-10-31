"""
LLM Service for Gemini integration.
"""

import os
from typing import Any

from google import genai

from api.constants import MessageRole
from api.models.message import Message


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


def format_messages_for_gemini(messages: list[Message]) -> list[dict[str, Any]]:
    """
    Convert Message objects to Gemini API format.

    Args:
        messages: List of Message objects

    Returns:
        list[dict]: Messages formatted for Gemini API [{"role": "user/model", "parts": [text]}]
    """
    formatted = []

    for message in messages:
        # Skip system messages
        if message.role == MessageRole.SYSTEM:
            continue

        # Map roles to Gemini format
        if message.role == MessageRole.USER:
            gemini_role = "user"
        elif message.role in (MessageRole.ASSISTANT, MessageRole.AGENT):
            gemini_role = "model"
        else:
            continue

        formatted.append({
            "role": gemini_role,
            "parts": [message.content]
        })

    return formatted
