# Claude Opus 5 (suscripción) — summarization/extract_structured_data

- model_id: `claude-opus-5`
- success: True  | final: 7.18 | quality: 8.68
- latency_total: 23.037s | tokens_per_second: 41.4
- input_tokens: 2 | output_tokens: 953
- judge_score: 4.2 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**user:**

Extrae la informacion de estos 3 perfiles de candidatos y devuelvelos como JSON:

Candidato 1: Maria Garcia, 28 anos, ingeniera de software con 5 anos de experiencia. Trabaja en Google desde 2023. Maneja Python, Go, Kubernetes. Pide $95K. Disponible en 2 semanas. Email: maria.g@email.com

Candidato 2: Juan Rodriguez, 35 anos, senior backend developer. 10 anos de experiencia, actualmente en Mercado Libre. Especialista en Java, microservicios, AWS. Salario esperado $120K. Necesita dar 1 mes de aviso. Contacto: jrodriguez@mail.com. Tiene certificacion AWS Solutions Architect.

Candidato 3: Sofia Chen, 31 anos, fullstack. 7 anos experiencia. Freelancer los ultimos 3 anos. React, Node.js, PostgreSQL, Docker. Pide entre $85K-$100K. Disponible inmediatamente. sofia.chen@dev.io. Portfolio: sofiadev.com

Formato JSON con campos: name, age, current_role, years_experience, current_company, skills[], salary_expectation, availability, email, certifications[]


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
    "availability": "1 mes (periodo de aviso)",
    "email": "jrodriguez@mail.com",
    "certifications": ["AWS Solutions Architect"]
  },
  {
    "name": "Sofia Chen",
    "age": 31,
    "current_role": "Fullstack Developer",
    "years_experience": 7,
    "current_company": "Freelance (últimos 3 años)",
    "skills": ["React", "Node.js", "PostgreSQL", "Docker"],
    "salary_expectation": { "min": 85000, "max": 100000 },
    "availability": "Inmediata",
    "email": "sofia.chen@dev.io",
    "certifications": []
  }
]
```

Tres cosas que no calzaban en el esquema y decidí así:

1. **`salary_expectation`**: Maria y Juan son número entero (USD). Sofia da rango, así que va como objeto `{min, max}`. Si necesitas tipo uniforme, la alternativa es usar `{min, max}` en los tres (con `min == max` cuando es cifra única).
2. **`current_company` de Sofia**: es freelance, no empresa. Lo dejé explícito en vez de `null` para no perder el dato de que lleva 3 años por su cuenta.
3. **Portfolio de Sofia** (`sofiadev.com`): no hay campo en tu esquema. Si lo quieres conservar, agrega `portfolio_url` (string o `null` para los otros dos).