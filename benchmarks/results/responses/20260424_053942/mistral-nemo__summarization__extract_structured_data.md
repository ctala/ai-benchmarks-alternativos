# Mistral Nemo — summarization/extract_structured_data

- model_id: `mistralai/mistral-nemo`
- success: True  | final: 6.81 | quality: 6.88
- latency_total: 16.579s | tokens_per_second: 22.1
- input_tokens: 282 | output_tokens: 367
- judge_score: 3.2 | justificación: 

## Respuesta completa

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
    "availability": "1 mes de aviso",
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