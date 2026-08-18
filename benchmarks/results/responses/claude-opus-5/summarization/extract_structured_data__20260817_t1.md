# Claude Opus 5 — summarization/extract_structured_data

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 6.09 | quality: 7.0
- latency_total: 15.326s | tokens_per_second: 81.2
- input_tokens: 447 | output_tokens: 1245
- judge_score: 3.0 | justificación: La respuesta es correcta y clara, pero incluye información no solicitada y omite algunos detalles relevantes, como la fecha de inicio de empleo de Maria y el portfolio de Sofia.

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
    "availability": "1 mes",
    "email": "jrodriguez@mail.com",
    "certifications": ["AWS Solutions Architect"]
  },
  {
    "name": "Sofia Chen",
    "age": 31,
    "current_role": "Fullstack Developer",
    "years_experience": 7,
    "current_company": "Freelance",
    "skills": ["React", "Node.js", "PostgreSQL", "Docker"],
    "salary_expectation": "$85K-$100K",
    "availability": "Inmediata",
    "email": "sofia.chen@dev.io",
    "certifications": []
  }
]
```

**Notas sobre la extracción:**

1. **Datos no contemplados en el esquema:** el portfolio de Sofia Chen (`sofiadev.com`) y el detalle de que Maria trabaja en Google *desde 2023* no tienen campo asignado. Si los necesitás, agregaría `portfolio_url` y `current_company_since`.

2. **Salarios en formato mixto:** dos candidatos dan un valor puntual y uno un rango. Si vas a filtrar u ordenar por salario, conviene normalizar así:

```json
"salary_expectation": { "min": 85000, "max": 100000, "currency": "USD" }
```
(para valores puntuales, `min` y `max` con el mismo número)

3. **Disponibilidad:** normalicé el texto, pero para comparar candidatos sería útil un campo numérico adicional, ej. `availability_days`: 14, 30 y 0 respectivamente.

4. **Inferencias hechas:** el `current_company` de Sofia figura como "Freelance" (el texto solo dice que es freelancer desde hace 3 años, sin nombrar cliente/empresa), y su `current_role` lo completé como "Fullstack Developer" a partir de "fullstack".