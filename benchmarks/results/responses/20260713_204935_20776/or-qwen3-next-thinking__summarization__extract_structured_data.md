# Qwen 3-Next 80B Thinking — summarization/extract_structured_data

- model_id: `qwen/qwen3-next-80b-a3b-thinking`
- success: True  | final: 6.36 | quality: 6.6
- latency_total: 28.304s | tokens_per_second: 188.7
- input_tokens: 288 | output_tokens: 5341
- judge_score: 3.0 | justificación: La respuesta es correcta y relevante para los dos candidatos proporcionados, pero incluye información no solicitada sobre un tercer candidato y añade detalles no verificados, como certificaciones, afectando la precisión y profundidad.

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
    "skills": ["Java", "microservicios", "AWS"],
    "salary_expectation": "$120K",
    "availability": "1 month notice",
    "email": "jrodriguez@mail.com",
    "certifications": ["AWS Solutions Architect"]
  },
  {
    "name": "Sofia Chen",
    "age": 31,
    "current_role": "fullstack",
    "years_experience": 7,
    "current_company": "Freelance",
    "skills": ["React", "Node.js", "PostgreSQL", "Docker"],
    "salary_expectation": "$85K-$100K",
    "availability": "immediately",
    "email": "sofia.chen@dev.io",
    "certifications": []
  }
]