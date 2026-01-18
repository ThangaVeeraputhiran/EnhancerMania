#!/usr/bin/env python3
"""
Vercel serverless function wrapper for Flask app
"""
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from app_production import app

# Export for Vercel
handler = app
