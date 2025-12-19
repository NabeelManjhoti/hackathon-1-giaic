from fastapi import HTTPException, status
from datetime import datetime, timedelta
from typing import Dict
import time


class InMemoryRateLimiter:
    """
    Simple in-memory rate limiter for free-tier compliance.
    In production, consider using Redis or similar for distributed rate limiting.
    """

    def __init__(self, requests: int = 100, window: int = 3600):  # 100 requests per hour
        self.requests = requests
        self.window = window  # in seconds
        self.requests_log: Dict[str, list] = {}

    def is_allowed(self, identifier: str) -> bool:
        """
        Check if the request is allowed based on rate limits.

        Args:
            identifier: Unique identifier for the requester (e.g., IP address or API key)

        Returns:
            True if request is allowed, False otherwise
        """
        now = time.time()
        if identifier not in self.requests_log:
            self.requests_log[identifier] = []

        # Remove requests older than the window
        self.requests_log[identifier] = [
            req_time for req_time in self.requests_log[identifier]
            if now - req_time < self.window
        ]

        # Check if we've exceeded the limit
        if len(self.requests_log[identifier]) >= self.requests:
            return False

        # Add the current request
        self.requests_log[identifier].append(now)
        return True


# Global rate limiter instance
rate_limiter = InMemoryRateLimiter(requests=100, window=3600)  # 100 requests per hour


async def check_rate_limit(identifier: str):
    """
    Check rate limit for the given identifier.

    Args:
        identifier: Unique identifier for the requester

    Raises:
        HTTPException: If rate limit is exceeded
    """
    if not rate_limiter.is_allowed(identifier):
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Rate limit exceeded. Please try again later."
        )