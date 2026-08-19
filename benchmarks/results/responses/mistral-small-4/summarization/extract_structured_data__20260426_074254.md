# Mistral Small 4 — summarization/extract_structured_data

- model_id: `mistralai/mistral-small-2603`
- success: True  | final: 6.86 | quality: 6.04
- latency_total: 3.859s | tokens_per_second: 93.0
- input_tokens: 294 | output_tokens: 359
- judge_score: 2.6 | justificación: 

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
    "salary_expectation": 95000,
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
    "salary_expectation": 120000,
    "availability": "1 mes",
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
    "salary_expectation": {
      "min": 85000,
      "max": 100000
    },
    "availability": "Inmediatamente",
    "email": "sofia.chen@dev.io",
    "certifications": []
  }
]
```