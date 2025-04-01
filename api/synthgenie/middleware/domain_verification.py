import os
from typing import List, Callable
from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from urllib.parse import urlparse


class DomainVerificationMiddleware(BaseHTTPMiddleware):
    """
    Middleware to verify that requests are coming from allowed domains.
    Checks both Origin and Referer headers. If neither is present, the request is still allowed
    as it could be from a non-browser client or direct API call, but API key validation
    would still be required.
    """

    def __init__(self, app, allowed_domains: List[str]):
        super().__init__(app)
        self.allowed_domains = [
            self._extract_domain(domain) for domain in allowed_domains
        ]

    async def dispatch(self, request: Request, call_next: Callable):
        # Skip domain verification for development if specified
        if os.getenv("SKIP_DOMAIN_CHECK") == "true":
            return await call_next(request)

        # Get Origin or Referer header
        origin = request.headers.get("Origin")
        referer = request.headers.get("Referer")

        # If neither header is present, allow the request (API key will still be checked)
        if not origin and not referer:
            return await call_next(request)

        # Check if origin domain is allowed
        if origin and self._is_allowed_domain(origin):
            return await call_next(request)

        # Check if referer domain is allowed
        if referer and self._is_allowed_domain(referer):
            return await call_next(request)

        # If we reach here, the domain is not allowed
        raise HTTPException(
            status_code=403, detail="Access from this domain is not allowed"
        )

    def _extract_domain(self, url: str) -> str:
        """Extract the domain from a URL."""
        parsed = urlparse(url)
        domain = parsed.netloc or parsed.path

        # Remove port if present
        if ":" in domain:
            domain = domain.split(":")[0]

        return domain.lower()

    def _is_allowed_domain(self, url: str) -> bool:
        """Check if the domain from the URL is in the allowed list."""
        domain = self._extract_domain(url)

        # Check exact domain match
        if domain in self.allowed_domains:
            return True

        # Check subdomain match
        for allowed_domain in self.allowed_domains:
            if domain.endswith("." + allowed_domain):
                return True

        return False
