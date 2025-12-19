from typing import Optional
from pydantic import BaseSettings


class ChatConfig:
    """
    Configuration for ChatKit integration.
    """

    # OpenAI settings
    openai_model: str = "gpt-3.5-turbo"
    openai_temperature: float = 0.7
    openai_max_tokens: int = 1000
    openai_top_p: float = 1.0
    openai_frequency_penalty: float = 0.0
    openai_presence_penalty: float = 0.0

    # Chat settings
    max_context_length: int = 4096  # Maximum tokens in context
    max_response_length: int = 500  # Maximum tokens in response
    enable_streaming: bool = True
    default_system_prompt: str = (
        "You are an AI assistant for a textbook. Answer questions based only on the "
        "provided textbook content. If you don't know the answer based on the provided "
        "content, say so clearly."
    )

    @classmethod
    def get_default_config(cls):
        return cls()