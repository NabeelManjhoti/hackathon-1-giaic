import logging
from datetime import datetime
from typing import Any, Dict
import json


def setup_logging():
    """
    Set up logging configuration for the application.
    """
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler()
        ]
    )


def log_request(user_id: str, query: str, mode: str):
    """
    Log a user request.
    """
    logger = logging.getLogger("request")
    logger.info(f"User {user_id} made {mode} query: {query}")


def log_response(user_id: str, query_id: str, response: str, confidence: float):
    """
    Log a response to a user query.
    """
    logger = logging.getLogger("response")
    logger.info(f"Response for query {query_id} to user {user_id} with confidence {confidence}")


def log_error(error: Exception, context: str = ""):
    """
    Log an error with context.
    """
    logger = logging.getLogger("error")
    logger.error(f"Error in {context}: {str(error)}", exc_info=True)