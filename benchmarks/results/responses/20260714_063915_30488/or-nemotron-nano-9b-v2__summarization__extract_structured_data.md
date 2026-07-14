# Nemotron Nano 9B v2 — summarization/extract_structured_data

- model_id: `nvidia/nemotron-nano-9b-v2:free`
- success: True  | final: 6.64 | quality: 6.6
- latency_total: 27.136s | tokens_per_second: 40.5
- input_tokens: 291 | output_tokens: 1099
- judge_score: 3.0 | justificación: La respuesta es correcta y relevante, pero incluye información no solicitada sobre un candidato adicional y omite detalles sobre el aviso de Juan Rodriguez, lo que afecta la precisión y profundidad.

## Respuesta completa



```json
[
  {
    "name": "Maria Garcia",
    "age": 28,
    "current_role": "ingeniera de software",
    "years_experience": 5,
    "current_company": "Google",
    "skills": ["Python", "Go", "Kubernetes"],
    "salary_expectation": "$95K",
    "availability": "Disponible en 2 semanas",
    "email": "maria.g@email.com",
    "certifications": []
  },
  {
    "name": "Juan Rodriguez",
    "age": 35,
    "current_role": "senior backend developer",
    "years_experience": 10,
    "current_company": "Mercado Libre",
    "skills": ["Java", "microservicios", "AWS"],
    "salary_expectation": "$120K",
    "availability": "Necesita dar 1 mes de aviso",
    "email": "jrodriguez@mail.com",
    "certifications": ["AWS Solutions Architect"]
  },
  {
    "name": "Sofia Chen",
    "age": 31,
    "current_role": "fullstack",
    "years_experience": 7,
    "current_company": "Freelancer",
    "skills": ["React", "Node.js", "PostgreSQL", "Docker"],
    "salary_expectation": "$85K-$100K",
    "availability": "Disponible inmediatamente",
    "email": "sofia.chen@dev.io",
    "certifications": []
  }
]
```
