# Solar Pro 4 — summarization/extract_structured_data

- model_id: `upstage/solar-pro4`
- success: True  | final: 7.02 | quality: 6.6
- latency_total: 4.576s | tokens_per_second: 71.9
- input_tokens: 337 | output_tokens: 329
- judge_score: 3.0 | justificación: La respuesta es correcta para Maria Garcia y Juan Rodriguez, pero incluye información no solicitada sobre Sofia Chen, afectando la relevancia y profundidad.

## Respuesta completa



```json
[
  {
    "name": "Maria Garcia",
    "age": 28,
    "current_role": "Ingeniera de Software",
    "years_experience": 5,
    "current_company": "Google",
    "skills": ["Python", "Go", "Kubernetes"],
    "salary_expectation": "$95K",
    "availability": "2 semanas",
    "email": "maria.g@email.com",
    "certifications": []
  },
  {
    "name": "Juan Rodriguez",
    "age": 35,
    "current_role": "Senior Backend Developer",
    "years_experience": 10,
    "current_company": "Mercado Libre",
    "skills": ["Java", "Microservicios", "AWS"],
    "salary_expectation": "$120K",
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
    "salary_expectation": "$85K-$100K",
    "availability": "Inmediatamente",
    "email": "sofia.chen@dev.io",
    "certifications": []
  }
]
```