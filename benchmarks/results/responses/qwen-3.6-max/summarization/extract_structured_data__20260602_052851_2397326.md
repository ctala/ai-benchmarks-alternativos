# Qwen 3.6 Max — summarization/extract_structured_data

- model_id: `qwen/qwen3.6-max-preview`
- success: True  | final: 5.81 | quality: 6.6
- latency_total: 48.783s | tokens_per_second: 41.9
- input_tokens: 275 | output_tokens: 2042
- judge_score: 3.0 | justificación: La respuesta es correcta y relevante para los dos candidatos proporcionados, pero incluye información no solicitada sobre un tercer candidato y añade certificaciones no mencionadas, afectando la precisión y profundidad.

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
    "availability": "2 semanas",
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
    "availability": "1 mes de aviso",
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
    "availability": "inmediatamente",
    "email": "sofia.chen@dev.io",
    "certifications": []
  }
]
```