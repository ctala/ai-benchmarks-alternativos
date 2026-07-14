# Qwen 2.5 72B — summarization/extract_structured_data

- model_id: `qwen/qwen-2.5-72b-instruct`
- success: True  | final: 6.48 | quality: 6.6
- latency_total: 12.57s | tokens_per_second: 26.7
- input_tokens: 288 | output_tokens: 336
- judge_score: 3.0 | justificación: La respuesta es correcta y relevante para los dos primeros candidatos, pero incluye información no solicitada para el tercer candidato, lo que afecta la precisión y profundidad.

## Respuesta completa

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
    "email": "maria.g@email.com",
    "certifications": []
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
    "salary_expectation": "85000-100000",
    "availability": "Inmediatamente",
    "email": "sofia.chen@dev.io",
    "certifications": []
  }
]
```