# Claude Opus 4.8 (suscripción) — summarization/extract_structured_data

- model_id: `claude-opus-4-8`
- success: True  | final: 6.22 | quality: 6.8
- latency_total: 11.349s | tokens_per_second: 68.8
- input_tokens: 2028 | output_tokens: 781
- judge_score: 3.0 | justificación: La respuesta es correcta y relevante, pero incluye información no solicitada (Sofia Chen) y carece de profundidad en el análisis de los datos proporcionados.

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
    "current_role": "Fullstack Developer (Freelancer)",
    "years_experience": 7,
    "current_company": "Freelancer",
    "skills": ["React", "Node.js", "PostgreSQL", "Docker"],
    "salary_expectation": "$85K-$100K",
    "availability": "Inmediata",
    "email": "sofia.chen@dev.io",
    "certifications": []
  }
]
```

Notas sobre los datos:
- **Salary** lo dejé como string para preservar el rango de Sofia (`$85K-$100K`). Si lo prefieres numérico, puedo convertirlo a `min`/`max`.
- **Sofia** no tiene empresa fija (freelancer); su `portfolio` (sofiadev.com) no estaba en tu esquema, así que lo omití — dime si quieres agregar el campo.
- Todos los candidatos tienen `certifications` como array; solo Juan trae una.