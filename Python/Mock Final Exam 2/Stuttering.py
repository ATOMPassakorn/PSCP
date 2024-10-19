"""Stuttering"""
import re
def stuttering():
    """Stuttering"""
    text=input()
    cleaned = re.sub(r'\s+', ' ', re.sub(r'\b(\w+)( \1)+', r'\1', text))
    print(cleaned)
stuttering()
