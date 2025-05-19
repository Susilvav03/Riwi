"""
Validar contraseña segura
Escribe una función que valide si una contraseña cumple con requisitos de seguridad (mayúsculas, minúsculas, números y símbolos).
"""

import re

def validPassword(pw):
    if len(pw) < 8:
        return "Must be at least 8 characters"
    if not re.search(r'[A-Z]', pw):
        return "Must contains at least one capital letter"
    if not re.search(r'[a-z]', pw):
        return "Must contains at least one lower-case letter"
    if not re.search(r'[0-9]', pw):
        return "Must contains at least one number"
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', pw):
        return "Must contains at least one special character"
    return "Invalid Password"

print(validPassword("Susana2025"))