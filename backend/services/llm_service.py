"""
LLM Service for Gemini integration.
"""

import logging
import os
from typing import Any

from google import genai
from google.genai import types

from api.constants import MessageRole
from api.models.company import Company
from api.models.company_config import CompanyConfig
from api.models.message import Message

logger = logging.getLogger(__name__)


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


def generate_response(
    company: Company,
    conversation_history: list[dict[str, Any]],
    user_message: str
) -> str:
    """
    Generate AI response using Gemini.

    Args:
        company: Company instance
        conversation_history: Formatted message history from format_messages_for_gemini()
        user_message: New user message to respond to

    Returns:
        str: Generated response text

    Raises:
        ValueError: If API key is missing or config is invalid
        RuntimeError: If API call fails
    """
    # Get or create company config
    config, _ = CompanyConfig.objects.get_or_create(company=company)

    try:
        # Get Gemini client
        client = get_gemini_model()

        # Build messages with history + new user message
        messages = conversation_history + [{
            "role": "user",
            "parts": [user_message]
        }]

        # Generate response
        response = client.models.generate_content(
            model="gemini-2.0-flash-lite",
            contents=messages,
            config=types.GenerateContentConfig(
                system_instruction=config.get_system_prompt(),
                max_output_tokens=config.max_tokens,
                temperature=config.temperature,
            )
        )

        if not response or not response.text:
            logger.error("Empty response from Gemini API")
            raise RuntimeError("Failed to generate response: empty response")

        return response.text

    except ValueError as e:
        # API key missing or invalid config
        logger.error(f"Configuration error: {e}")
        raise

    except Exception as e:
        # Network, quota, or API errors
        error_msg = str(e)
        logger.error(f"Gemini API error: {error_msg}")

        # Handle specific error types
        if "quota" in error_msg.lower() or "rate" in error_msg.lower():
            raise RuntimeError("API quota exceeded. Please try again later.") from e
        elif "network" in error_msg.lower() or "timeout" in error_msg.lower():
            raise RuntimeError("Network error connecting to AI service.") from e
        else:
            raise RuntimeError(f"AI service error: {error_msg}") from e
