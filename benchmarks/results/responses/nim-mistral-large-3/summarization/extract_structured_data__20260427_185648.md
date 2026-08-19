# Mistral Large 3 675B (NIM) — summarization/extract_structured_data

- model_id: `mistralai/mistral-large-3-675b-instruct-2512`
- success: True  | final: 6.85 | quality: 7.56
- latency_total: 11.619s | tokens_per_second: 40.1
- input_tokens: 277 | output_tokens: 466
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
    "availability": "Inmediata",
    "email": "sofia.chen@dev.io",
    "certifications": [],
    "portfolio": "sofiadev.com"
  }
]
```

### Notas:
- Para **Sofia Chen**, el campo `salary_expectation` se estructuró como un objeto con `min` y `max` para reflejar el rango mencionado.
- Se incluyó el campo adicional `portfolio` para Sofia Chen, ya que estaba en su descripción.
- Los campos `certifications` son arrays vacíos para los candidatos que no tienen certificaciones mencionadas.