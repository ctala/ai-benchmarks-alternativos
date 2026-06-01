# DeepSeek V4 Flash (OpenRouter) — summarization/extract_structured_data

- model_id: `deepseek/deepseek-v4-flash`
- success: True  | final: 7.11 | quality: 6.6
- latency_total: 10.212s | tokens_per_second: 122.7
- input_tokens: 275 | output_tokens: 1253
- judge_score: 3.0 | justificación: La respuesta es correcta y relevante para los dos candidatos proporcionados, pero incluye información no solicitada para un tercer candidato y carece de profundidad en los insights.

## Respuesta completa

```json
[
  {
    "name": "Maria Garcia",
    "age": 28,
    "current_role": "Software Engineer",
    "years_experience": 5,
    "current_company": "Google",
    "skills": ["Python", "Go", "Kubernetes"],
    "salary_expectation": "95K",
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
    "skills": ["Java", "microservices", "AWS"],
    "salary_expectation": "120K",
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
    "salary_expectation": "85K-100K",
    "availability": "Immediately",
    "email": "sofia.chen@dev.io",
    "certifications": []
  }
]
```