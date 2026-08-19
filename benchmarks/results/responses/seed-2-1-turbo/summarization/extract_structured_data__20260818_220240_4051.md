# Seed 2.1 Turbo — summarization/extract_structured_data

- model_id: `bytedance-seed/seed-2-1-turbo`
- success: True  | final: 6.02 | quality: 6.6
- latency_total: 64.783s | tokens_per_second: 70.6
- input_tokens: 330 | output_tokens: 4572
- judge_score: 3.0 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**user:**

Extrae la informacion de estos 3 perfiles de candidatos y devuelvelos como JSON:

Candidato 1: Maria Garcia, 28 anos, ingeniera de software con 5 anos de experiencia. Trabaja en Google desde 2023. Maneja Python, Go, Kubernetes. Pide $95K. Disponible en 2 semanas. Email: maria.g@email.com

Candidato 2: Juan Rodriguez, 35 anos, senior backend developer. 10 anos de experiencia, actualmente en Mercado Libre. Especialista en Java, microservicios, AWS. Salario esperado $120K. Necesita dar 1 mes de aviso. Contacto: jrodriguez@mail.com. Tiene certificacion AWS Solutions Architect.

Candidato 3: Sofia Chen, 31 anos, fullstack. 7 anos experiencia. Freelancer los ultimos 3 anos. React, Node.js, PostgreSQL, Docker. Pide entre $85K-$100K. Disponible inmediatamente. sofia.chen@dev.io. Portfolio: sofiadev.com

Formato JSON con campos: name, age, current_role, years_experience, current_company, skills[], salary_expectation, availability, email, certifications[]


## Respuesta completa

Aquí tienes la información de los candidatos extraída y estructurada en el formato JSON solicitado:

```json
{
  "candidates": [
    {
      "name": "Maria Garcia",
      "age": 28,
      "current_role": "Ingeniera de software",
      "years_experience": 5,
      "current_company": "Google",
      "skills": ["Python", "Go", "Kubernetes"],
      "salary_expectation": "$95K",
      "availability": "Disponible en 2 semanas",
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
      "availability": "Necesita dar 1 mes de aviso",
      "email": "jrodriguez@mail.com",
      "certifications": ["AWS Solutions Architect"]
    },
    {
      "name": "Sofia Chen",
      "age": 31,
      "current_role": "Desarrolladora Fullstack",
      "years_experience": 7,
      "current_company": "Freelance",
      "skills": ["React", "Node.js", "PostgreSQL", "Docker"],
      "salary_expectation": "$85K - $100K",
      "availability": "Disponible inmediatamente",
      "email": "sofia.chen@dev.io",
      "certifications": []
    }
  ]
}
```

> Nota: Se omitió el portfolio de Sofia Chen ya que no se encontraba dentro de la lista de campos solicitados.