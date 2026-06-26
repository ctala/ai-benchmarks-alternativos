# Claude Fable 5 (suscripción) — summarization/extract_structured_data

- model_id: `claude-fable-5`
- success: True  | final: 6.71 | quality: 8.0
- latency_total: 7.5s | tokens_per_second: 81.1
- input_tokens: 2 | output_tokens: 608

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
    "current_company": "Freelancer (últimos 3 años)",
    "skills": ["React", "Node.js", "PostgreSQL", "Docker"],
    "salary_expectation": "$85K-$100K",
    "availability": "Inmediata",
    "email": "sofia.chen@dev.io",
    "certifications": []
  }
]
```

Notas:
- Sofia Chen incluye un dato extra no contemplado en el schema: portfolio `sofiadev.com`. Si lo necesitas, puedo agregar un campo `portfolio`.
- Los candidatos sin certificaciones mencionadas quedaron con array vacío.