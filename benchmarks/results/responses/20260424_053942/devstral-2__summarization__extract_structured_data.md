# Devstral 2 (Dic 2025) — summarization/extract_structured_data

- model_id: `mistralai/devstral-2512`
- success: True  | final: 7.16 | quality: 7.16
- latency_total: 5.458s | tokens_per_second: 74.4
- input_tokens: 282 | output_tokens: 406
- judge_score: 3.4 | justificación: 

## Respuesta completa

Aquí tienes la información de los tres candidatos en formato JSON:

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
    "current_company": "Freelancer",
    "skills": ["React", "Node.js", "PostgreSQL", "Docker"],
    "salary_expectation": "$85K-$100K",
    "availability": "Inmediatamente",
    "email": "sofia.chen@dev.io",
    "certifications": [],
    "portfolio": "sofiadev.com"
  }
]
```

Nota: He añadido el campo `portfolio` para Sofia Chen ya que era información relevante que no estaba incluida en los campos originales. Si prefieres omitirlo, puedes eliminarlo del JSON.