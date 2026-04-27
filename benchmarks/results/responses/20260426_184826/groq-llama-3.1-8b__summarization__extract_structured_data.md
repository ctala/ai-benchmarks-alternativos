# Llama 3.1 8B Instant (Groq) — summarization/extract_structured_data

- model_id: `llama-3.1-8b-instant`
- success: True  | final: 7.46 | quality: 6.88
- latency_total: 0.758s | tokens_per_second: 477.3
- input_tokens: 302 | output_tokens: 362
- judge_score: 3.2 | justificación: 

## Respuesta completa

Aquí están los perfiles de candidatos en formato JSON:

```json
[
  {
    "name": "Maria Garcia",
    "age": 28,
    "current_role": "Ingeniera de software",
    "years_experience": 5,
    "current_company": "Google",
    "skills": ["Python", "Go", "Kubernetes"],
    "salary_expectation": 95000,
    "availability": "2 semanas",
    "email": "maria.g@email.com"
  },
  {
    "name": "Juan Rodriguez",
    "age": 35,
    "current_role": "Senior backend developer",
    "years_experience": 10,
    "current_company": "Mercado Libre",
    "skills": ["Java", "microservicios", "AWS"],
    "salary_expectation": 120000,
    "availability": "1 mes de aviso",
    "email": "jrodriguez@mail.com",
    "certifications": ["AWS Solutions Architect"]
  },
  {
    "name": "Sofia Chen",
    "age": 31,
    "current_role": "Fullstack",
    "years_experience": 7,
    "current_company": "Freelancer",
    "skills": ["React", "Node.js", "PostgreSQL", "Docker"],
    "salary_expectation": [85000, 100000],
    "availability": "inmediatamente",
    "email": "sofia.chen@dev.io",
    "certifications": []
  }
]
```

Nota: En el caso de Sofia Chen, la solicitud de salario es un rango de valores, por lo que lo he representado como un arreglo en el JSON.