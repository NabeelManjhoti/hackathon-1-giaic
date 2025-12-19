import openai
from typing import List, Dict, Any, AsyncGenerator
from ..core.config import settings
from ..core.chat_config import ChatConfig


class ChatService:
    """
    ChatKit wrapper service for conversation handling.
    """

    def __init__(self, config: ChatConfig = None):
        self.config = config or ChatConfig.get_default_config()
        openai.api_key = settings.openai_api_key

    async def generate_response(
        self,
        messages: List[Dict[str, str]],
        context_chunks: List[Dict[str, Any]] = None
    ) -> str:
        """
        Generate a response using the ChatKit service.

        Args:
            messages: List of messages in the conversation
            context_chunks: Optional context chunks to include in the prompt

        Returns:
            Generated response string
        """
        # Prepare the system message with context if available
        system_message = {
            "role": "system",
            "content": self.config.default_system_prompt
        }

        # If context chunks are provided, add them to the system message
        if context_chunks:
            context_text = "\n".join([chunk['content'] for chunk in context_chunks])
            system_message["content"] += f"\n\nRelevant textbook content:\n{context_text}"

        # Prepare the full message list
        full_messages = [system_message] + messages

        # Call the OpenAI API
        response = await openai.ChatCompletion.acreate(
            model=self.config.openai_model,
            messages=full_messages,
            temperature=self.config.openai_temperature,
            max_tokens=self.config.openai_max_tokens,
            top_p=self.config.openai_top_p,
            frequency_penalty=self.config.openai_frequency_penalty,
            presence_penalty=self.config.openai_presence_penalty
        )

        return response.choices[0].message.content

    async def generate_response_stream(
        self,
        messages: List[Dict[str, str]],
        context_chunks: List[Dict[str, Any]] = None
    ) -> AsyncGenerator[str, None]:
        """
        Generate a streaming response using the ChatKit service.

        Args:
            messages: List of messages in the conversation
            context_chunks: Optional context chunks to include in the prompt

        Yields:
            Response tokens as they are generated
        """
        # Prepare the system message with context if available
        system_message = {
            "role": "system",
            "content": self.config.default_system_prompt
        }

        # If context chunks are provided, add them to the system message
        if context_chunks:
            context_text = "\n".join([chunk['content'] for chunk in context_chunks])
            system_message["content"] += f"\n\nRelevant textbook content:\n{context_text}"

        # Prepare the full message list
        full_messages = [system_message] + messages

        # Call the OpenAI API with streaming
        response = await openai.ChatCompletion.acreate(
            model=self.config.openai_model,
            messages=full_messages,
            temperature=self.config.openai_temperature,
            max_tokens=self.config.openai_max_tokens,
            top_p=self.config.openai_top_p,
            frequency_penalty=self.config.openai_frequency_penalty,
            presence_penalty=self.config.openai_presence_penalty,
            stream=True
        )

        async for chunk in response:
            content = chunk.choices[0].delta.get("content", "")
            if content:
                yield content

    def format_context_for_chat(self, context_chunks: List[Dict[str, Any]]) -> str:
        """
        Format context chunks for use in chat.

        Args:
            context_chunks: List of context chunks

        Returns:
            Formatted context string
        """
        formatted_context = "Relevant textbook content:\n"
        for i, chunk in enumerate(context_chunks):
            formatted_context += f"\n{i+1}. {chunk['content'][:200]}...\n"
            if 'metadata' in chunk:
                metadata = chunk['metadata']
                if 'section' in metadata:
                    formatted_context += f"   Section: {metadata['section']}\n"
                if 'page_number' in metadata:
                    formatted_context += f"   Page: {metadata['page_number']}\n"
        return formatted_context