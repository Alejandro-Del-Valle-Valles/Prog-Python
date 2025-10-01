import re
'''
my_text = "Hola esto es una cadena de texto"
def get_Number_Of_Words(text: str) -> int:
    text = text.strip().split()
    if not text:
        return 0
    else:
        return len(text)
        

print(get_Number_Of_Words(my_text))
'''

my_text = "A man, a plan, a canal:Panama"

def is_Palindrom(text: str) -> bool:
    text = re.sub(r"[^a-z]", "", text.lower())
    return text == text[::-1]

def is_Palindrom_Two(text: str) -> bool:
    text = "".join(ch for ch in text.lower() if ch.isalnum())
    return text == text[::-1]

print(is_Palindrom(my_text))
print(is_Palindrom_Two(my_text))