# Claude Fable 5 — summarization/extract_structured_data

- model_id: `anthropic/claude-fable-5`
- success: True  | final: 5.91 | quality: 6.8
- latency_total: 10.461s | tokens_per_second: 68.1
- input_tokens: 447 | output_tokens: 712
- judge_score: 3.0 | justificación: La respuesta es correcta y relevante, pero incluye información no solicitada (Sofia Chen) y carece de profundidad en los detalles proporcionados.

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
    "current_role": "Fullstack Developer",
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

**Notas:**
- Sofia Chen no tiene empresa actual como tal; se indicó su condición de freelancer.
- Su portfolio (sofiadev.com) no está en el esquema solicitado, pero puedo agregarlo como campo adicional si lo necesitas.
- Los campos `certifications` se dejaron como arrays vacíos cuando no se mencionaron certificaciones.