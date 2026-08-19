# MiMo-V2.5 Pro — summarization/extract_structured_data

- model_id: `xiaomi/mimo-v2.5-pro`
- success: True  | final: 6.95 | quality: 7.56
- latency_total: 11.056s | tokens_per_second: 74.8
- input_tokens: 531 | output_tokens: 827
- judge_score: 3.4 | justificación: 

## Respuesta completa

Aquí tienes los tres perfiles extraídos en formato JSON:

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
    "current_company": "Freelancer",
    "skills": ["React", "Node.js", "PostgreSQL", "Docker"],
    "salary_expectation": "$85K-$100K",
    "availability": "Inmediata",
    "email": "sofia.chen@dev.io",
    "certifications": []
  }
]
```



### Notas sobre la extracción:

| Campo | Detalle |
|---|---|
| **current_company** | Sofia Chen figura como *Freelancer* ya que trabaja por cuenta propia desde hace 3 años |
| **salary_expectation** | Sofia Chen tiene un rango (`$85K-$100K`), los demás un valor fijo |
| **certifications** | Solo Juan Rodriguez mencionó certificación explícita |
| **Portfolio** | Sofia Chen tiene `sofiadev.com`, pero no se incluyó porque no estaba en el esquema solicitado. ¿Deseas agregar un campo `portfolio` al JSON? |