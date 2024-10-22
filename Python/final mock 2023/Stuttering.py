"""Stuttering"""
import re
def stuttering(text):
    """Stuttering"""
    print(re.sub(r"\s+"," ",re.sub(r"\b(\w+)( \1\b)+",r"\1",text)))
stuttering(input())
