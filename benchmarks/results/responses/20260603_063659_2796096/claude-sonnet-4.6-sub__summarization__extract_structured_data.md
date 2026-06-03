# Claude Sonnet 4.6 (suscripción) — summarization/extract_structured_data

- model_id: `claude-sonnet-4-6`
- success: True  | final: 6.54 | quality: 6.8
- latency_total: 8.692s | tokens_per_second: 66.6
- input_tokens: 3 | output_tokens: 579
- judge_score: 3.0 | justificación: La respuesta es correcta y relevante, pero incluye información no solicitada (perfil de Sofia Chen) y carece de profundidad en los perfiles proporcionados.

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
    "salary_expectation": "$95,000",
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
    "salary_expectation": "$120,000",
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
    "salary_expectation": "$85,000 - $100,000",
    "availability": "Inmediata",
    "email": "sofia.chen@dev.io",
    "certifications": []
  }
]
```

**Notas sobre la extracción:**
- `current_company` de Sofia se marcó como `"Freelancer"` ya que lleva 3 años trabajando de forma independiente, sin empresa empleadora.
- `salary_expectation` de Sofia se mantuvo como rango (`$85K-$100K`) ya que así lo indicó el perfil.
- `certifications` de Maria y Sofia se dejaron como arrays vacíos `[]` al no mencionarse ninguna en sus perfiles.
- `portfolio` de Sofia no se incluyó porque no forma parte de los campos solicitados; si lo necesitas, lo agrego fácilmente.