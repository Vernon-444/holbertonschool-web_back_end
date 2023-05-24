#!/usr/bin/env python3
"""holds an auth class"""
from flask import request
from typing import List, TypeVar
import os.path


class Auth():
    """an authorization class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """checks to see if path is in excluded_paths"""
        if not path or not excluded_paths:
            return True
        if os.path.join(path, '') in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """returns the authorization header from the request"""
        if not request:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """user user user"""
        return None
