# MiMo-V2.5 (omnimodal) — summarization/extract_structured_data

- model_id: `xiaomi/mimo-v2.5`
- success: True  | final: 6.58 | quality: 7.08
- latency_total: 17.321s | tokens_per_second: 118.2
- input_tokens: 527 | output_tokens: 2048
- judge_score: 3.2 | justificación: 

## Respuesta completa

¡Claro! He extraído la información de los tres perfiles de candidatos y la he organizado en el formato JSON que solicitaste. Aquí está el resultado:

```json
[
  {
    "name": "Maria Garcia",
    "age": 28,
    "current_role": "Software Engineer",
    "years_experience": 5,
    "current_company": "Google",
    "skills": ["Python", "Go", "Kubernetes"],
    "salary_expectation": "$95K",
    "availability": "2 weeks",
    "email": "maria.g@email.com",
    "certifications": []
  },
  {
    "name": "Juan Rodriguez",
    "age": 35,
    "current_role": "Senior Backend Developer",
    "years_experience": 10,
    "current_company": "Mercado Libre",
    "skills": ["Java", "Microservices", "AWS"],
    "salary_expectation": "$120K",
    "availability": "1 month notice",
    "email": "jrodriguez@mail.com",
    "certifications": ["AWS Solutions Architect"]
  },
  {
    "name": "Sofia Chen",
    "age": 31,
    "current_role": "Fullstack Developer",
    "years_experience": 7,
    "current_company": "Freelancer",
    "skills": ["React", "Node.js", "PostgreSQL", "Docker"],
    "salary_expectation": "$85K-$100K",
    "availability": "Immediately",
    "email": "sofia.chen@dev.io",
    "certifications": []
  }
]
```

**Notas:**
- Traduje los roles y disponibilidad al inglés para consistencia con los campos JSON.
- Para