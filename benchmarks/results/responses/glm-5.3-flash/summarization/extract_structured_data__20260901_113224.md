# GLM 5.3 Flash — summarization/extract_structured_data

- model_id: `z-ai/glm-5.3-flash`
- success: True  | final: 7.54 | quality: 8.2
- latency_total: 55.352s | tokens_per_second: 47.3
- input_tokens: 275 | output_tokens: 2618
- judge_score: 4.0 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**user:**

Extrae la informacion de estos 3 perfiles de candidatos y devuelvelos como JSON:

Candidato 1: Maria Garcia, 28 anos, ingeniera de software con 5 anos de experiencia. Trabaja en Google desde 2023. Maneja Python, Go, Kubernetes. Pide $95K. Disponible en 2 semanas. Email: maria.g@email.com

Candidato 2: Juan Rodriguez, 35 anos, senior backend developer. 10 anos de experiencia, actualmente en Mercado Libre. Especialista en Java, microservicios, AWS. Salario esperado $120K. Necesita dar 1 mes de aviso. Contacto: jrodriguez@mail.com. Tiene certificacion AWS Solutions Architect.

Candidato 3: Sofia Chen, 31 anos, fullstack. 7 anos experiencia. Freelancer los ultimos 3 anos. React, Node.js, PostgreSQL, Docker. Pide entre $85K-$100K. Disponible inmediatamente. sofia.chen@dev.io. Portfolio: sofiadev.com

Formato JSON con campos: name, age, current_role, years_experience, current_company, skills[], salary_expectation, availability, email, certifications[]


## Respuesta completa

```json
{
  "candidates": [
    {
      "name": "Maria Garcia",
      "age": 28,
      "current_role": "Software Engineer",
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
      "current_role": "Senior Backend Developer",
      "years_experience": 10,
      "current_company": "Mercado Libre",
      "skills": ["Java", "Microservices", "AWS"],
      "salary_expectation": "$120K",
      "availability": "1 month notice",
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
      "salary_expectation": "$85K - $100K",
      "availability": "Immediate",
      "email": "sofia.chen@dev.io",
      "certifications": []
    }
  ]
}
```

**Notas:**
- Sofia Chen menciona además su portfolio (**sofiadev.com**), que no incluí porque no estaba entre los campos solicitados. Puedo agregarlo como campo `portfolio` si lo necesitas.
- Para Sofia usé `"Freelance"` como `current_company` ya que no tiene empleador actual.
- `salary_expectation` quedó como string porque Sofia especifica un rango. Si prefieres valores numéricos (ej. `85000`), puedo normalizarlos.