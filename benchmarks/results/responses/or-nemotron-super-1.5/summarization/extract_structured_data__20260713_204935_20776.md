# Nemotron Super 49B v1.5 — summarization/extract_structured_data

- model_id: `nvidia/llama-3.3-nemotron-super-49b-v1.5`
- success: True  | final: 6.48 | quality: 6.6
- latency_total: 19.995s | tokens_per_second: 47.4
- input_tokens: 286 | output_tokens: 947
- judge_score: 3.0 | justificación: La respuesta es correcta y relevante para los dos candidatos proporcionados, pero incluye información no solicitada para un tercer candidato y carece de profundidad en los insights.

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
    "current_role": "Fullstack",
    "years_experience": 7,
    "current_company": "Freelancer",
    "skills": ["React", "Node.js", "PostgreSQL", "Docker"],
    "salary_expectation": "$85K-$100K",
    "availability": "Inmediatamente",
    "email": "sofia.chen@dev.io",
    "certifications": []
  }
]
```