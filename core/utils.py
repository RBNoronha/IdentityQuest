
import re

def is_email(input_str: str) -> bool:
    return bool(re.match(r"[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$", input_str))
