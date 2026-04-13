"""
Tests de precision en copia de strings aleatorios.
Evalua si el modelo puede reproducir exactamente strings como API keys,
hashes hex, tokens JWT, y credenciales sin alucinar caracteres.

Descubierto: MiniMax truncaba y cambiaba caracteres en secrets hex de 64 chars.
Sonnet lo hacia bien. Este test mide esa diferencia critica para agentes
que manejan credenciales y configuraciones.
"""

import hashlib
import random
import string

# Strings de prueba con dificultad creciente
# Usamos strings fijos para reproducibilidad
TEST_STRINGS = {
    "hex_32": "a1b2c3d4e5f6789012345678abcdef90",
    "hex_64": "9767a40b5b0ee1f7e3339a9859c582916ebb8d3df4ead5de1828c122c78a5a1b",
    "api_key": "sk-proj-X7kL9mN2pQ4rS6tU8vW0xY1zA3bC5dE7fG9hI1jK3lM5nO7pQ9rS1tU3vW5x",
    "jwt_segment": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkw",
    "mixed_special": "r2-secret_KEY.2024/abc+def==ghi&jkl#mno@pqr$stu%vwx^yza",
    "uuid_chain": "550e8400-e29b-41d4-a716-446655440000:7c9e6679-7425-40de-944b-e07fc1f90ae7",
    "base64": "SGVsbG8gV29ybGQhIFRoaXMgaXMgYSB0ZXN0IHN0cmluZyBmb3IgTExNIHByZWNpc2lvbi4=",
}

TESTS = [
    {
        "name": "copy_hex_32",
        "description": "Copiar string hex de 32 caracteres exactamente",
        "messages": [
            {"role": "system", "content": "Tu UNICA tarea es copiar strings exactamente. NO expliques, NO agregues contexto. Responde SOLO con el string pedido, nada mas."},
            {"role": "user", "content": f'Copia este string EXACTAMENTE, caracter por caracter. Responde SOLO con el string, sin comillas, sin explicacion:\n\n{TEST_STRINGS["hex_32"]}'},
        ],
        "criteria": {"min_words": 1, "required_sections": [], "language": "en"},
        "expected_answer": {
            "type": "exact_string",
            "expected": TEST_STRINGS["hex_32"],
        },
    },
    {
        "name": "copy_hex_64",
        "description": "Copiar string hex de 64 caracteres (el caso real que fallo MiniMax)",
        "messages": [
            {"role": "system", "content": "Tu UNICA tarea es copiar strings exactamente. NO expliques, NO agregues contexto. Responde SOLO con el string pedido, nada mas."},
            {"role": "user", "content": f'Copia este string EXACTAMENTE, caracter por caracter. Responde SOLO con el string, sin comillas, sin explicacion:\n\n{TEST_STRINGS["hex_64"]}'},
        ],
        "criteria": {"min_words": 1, "required_sections": [], "language": "en"},
        "expected_answer": {
            "type": "exact_string",
            "expected": TEST_STRINGS["hex_64"],
        },
    },
    {
        "name": "copy_api_key",
        "description": "Copiar API key format (sk-proj-...)",
        "messages": [
            {"role": "system", "content": "Tu UNICA tarea es copiar strings exactamente. NO expliques, NO agregues contexto. Responde SOLO con el string pedido, nada mas."},
            {"role": "user", "content": f'Copia este string EXACTAMENTE, caracter por caracter. Responde SOLO con el string, sin comillas, sin explicacion:\n\n{TEST_STRINGS["api_key"]}'},
        ],
        "criteria": {"min_words": 1, "required_sections": [], "language": "en"},
        "expected_answer": {
            "type": "exact_string",
            "expected": TEST_STRINGS["api_key"],
        },
    },
    {
        "name": "copy_jwt",
        "description": "Copiar segmento JWT (base64url con puntos)",
        "messages": [
            {"role": "system", "content": "Tu UNICA tarea es copiar strings exactamente. NO expliques, NO agregues contexto. Responde SOLO con el string pedido, nada mas."},
            {"role": "user", "content": f'Copia este string EXACTAMENTE, caracter por caracter. Responde SOLO con el string, sin comillas, sin explicacion:\n\n{TEST_STRINGS["jwt_segment"]}'},
        ],
        "criteria": {"min_words": 1, "required_sections": [], "language": "en"},
        "expected_answer": {
            "type": "exact_string",
            "expected": TEST_STRINGS["jwt_segment"],
        },
    },
    {
        "name": "copy_mixed_special",
        "description": "Copiar string con caracteres especiales mixtos",
        "messages": [
            {"role": "system", "content": "Tu UNICA tarea es copiar strings exactamente. NO expliques, NO agregues contexto. Responde SOLO con el string pedido, nada mas."},
            {"role": "user", "content": f'Copia este string EXACTAMENTE, caracter por caracter. Responde SOLO con el string, sin comillas, sin explicacion:\n\n{TEST_STRINGS["mixed_special"]}'},
        ],
        "criteria": {"min_words": 1, "required_sections": [], "language": "en"},
        "expected_answer": {
            "type": "exact_string",
            "expected": TEST_STRINGS["mixed_special"],
        },
    },
    {
        "name": "write_config_file",
        "description": "Escribir archivo de configuracion con credenciales exactas",
        "messages": [
            {"role": "user", "content": f"""Necesito que generes un archivo .env con estas credenciales EXACTAS.
Responde SOLO con el contenido del archivo, sin explicaciones, sin markdown code blocks.

AWS_ACCESS_KEY_ID=AKIAIOSFODNN7EXAMPLE
AWS_SECRET_ACCESS_KEY={TEST_STRINGS["hex_64"]}
R2_ENDPOINT=https://abc123def456.r2.cloudflarestorage.com
API_TOKEN={TEST_STRINGS["api_key"]}
JWT_SECRET={TEST_STRINGS["jwt_segment"]}"""},
        ],
        "criteria": {"min_words": 3, "required_sections": [], "language": "en"},
        "expected_answer": {
            "type": "multi_string_check",
            "must_contain_exact": [
                TEST_STRINGS["hex_64"],
                TEST_STRINGS["api_key"],
                TEST_STRINGS["jwt_segment"],
                "AKIAIOSFODNN7EXAMPLE",
                "abc123def456",
            ],
        },
    },
]
