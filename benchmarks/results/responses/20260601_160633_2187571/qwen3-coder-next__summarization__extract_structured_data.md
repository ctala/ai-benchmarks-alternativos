# Qwen3-Coder-Next (OpenRouter FP8) — summarization/extract_structured_data

- model_id: `qwen/qwen3-coder-next`
- success: True  | final: 6.77 | quality: 6.6
- latency_total: 4.005s | tokens_per_second: 89.1
- input_tokens: 288 | output_tokens: 357
- judge_score: 3.0 | justificación: La respuesta es correcta y relevante para los dos primeros candidatos, pero incluye información no solicitada para un tercer candidato, lo que afecta la precisión y profundidad.

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
    "salary_expectation": 95000,
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
    "salary_expectation": 120000,
    "availability": "1 mes",
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
    "salary_expectation": {
      "min": 85000,
      "max": 100000
    },
    "availability": "inmediatamente",
    "email": "sofia.chen@dev.io",
    "certifications": [],
    "portfolio": "sofiadev.com"
  }
]
```