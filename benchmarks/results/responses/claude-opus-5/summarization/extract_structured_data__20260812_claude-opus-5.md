# Claude Opus 5 — summarization/extract_structured_data

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 7.06 | quality: 8.4
- latency_total: 16.18s | tokens_per_second: 81.9
- input_tokens: 447 | output_tokens: 1325
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, con una estructura clara y fácil de entender, aunque incluye un campo adicional no solicitado y algunos datos inferidos.

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
    "availability": "1 mes (periodo de aviso)",
    "email": "jrodriguez@mail.com",
    "certifications": ["AWS Solutions Architect"]
  },
  {
    "name": "Sofia Chen",
    "age": 31,
    "current_role": "Fullstack Developer",
    "years_experience": 7,
    "current_company": "Freelancer (independiente, ultimos 3 anos)",
    "skills": ["React", "Node.js", "PostgreSQL", "Docker"],
    "salary_expectation": "$85K-$100K",
    "availability": "Inmediata",
    "email": "sofia.chen@dev.io",
    "certifications": [],
    "portfolio": "sofiadev.com"
  }
]
```

**Notas sobre la extracción:**

1. **Campo extra añadido:** Sofia Chen tiene un portfolio (`sofiadev.com`) que no encajaba en ningún campo del esquema solicitado. Lo agregué como `portfolio` solo en su registro. Si prefieres un esquema estrictamente uniforme, puedo eliminarlo o añadir `"portfolio": null` a los otros dos.

2. **Salario como string:** Los dejé como texto porque el candidato 3 tiene un rango, no un valor único. Si necesitas hacer cálculos o filtros, te recomiendo esta alternativa:
```json
"salary_expectation": { "min": 85000, "max": 100000, "currency": "USD" }
```
(para Maria y Juan, `min` y `max` serían iguales)

3. **Datos inferidos, no explícitos:**
   - Maria: el texto dice "Trabaja en Google desde 2023", así que sus 5 años de experiencia incluyen empleos anteriores no mencionados.
   - Juan: "Senior backend developer" es su rol declarado; no se especifica título formal en Mercado Libre.
   - Sofia: "Freelancer" no es una empresa. Lo puse en `current_company` con aclaración, pero podrías necesitar un campo `employment_type` para distinguir empleados de independientes.

4. **Disponibilidad:** normalicé el texto pero mantuve la distinción entre "disponible en X tiempo" y "necesita dar aviso", ya que implican situaciones distintas. Si quieres ordenar por rapidez de incorporación, sugiero añadir `availability_days`: 14, 30 y 0 respectivamente.