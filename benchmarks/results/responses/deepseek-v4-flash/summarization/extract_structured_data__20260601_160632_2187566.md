# DeepSeek V4 Flash (OpenRouter) — summarization/extract_structured_data

- model_id: `deepseek/deepseek-v4-flash`
- success: True  | final: 7.02 | quality: 6.6
- latency_total: 14.872s | tokens_per_second: 64.7
- input_tokens: 275 | output_tokens: 962
- judge_score: 3.0 | justificación: La respuesta es correcta y relevante para los dos primeros candidatos, pero incluye información no solicitada para el tercer candidato y carece de profundidad en los insights.

## Respuesta completa

[
  {
    "name": "Maria Garcia",
    "age": 28,
    "current_role": "ingeniera de software",
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
    "current_role": "senior backend developer",
    "years_experience": 10,
    "current_company": "Mercado Libre",
    "skills": ["Java", "Microservicios", "AWS"],
    "salary_expectation": "$120K",
    "availability": "1 month",
    "email": "jrodriguez@mail.com",
    "certifications": ["AWS Solutions Architect"]
  },
  {
    "name": "Sofia Chen",
    "age": 31,
    "current_role": "fullstack",
    "years_experience": 7,
    "current_company": null,
    "skills": ["React", "Node.js", "PostgreSQL", "Docker"],
    "salary_expectation": "$85K-$100K",
    "availability": "inmediatamente",
    "email": "sofia.chen@dev.io",
    "certifications": []
  }
]