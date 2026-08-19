# Claude Fable 5 — summarization/extract_structured_data

- model_id: `anthropic/claude-fable-5`
- success: True  | final: 5.91 | quality: 6.8
- latency_total: 10.282s | tokens_per_second: 71.2
- input_tokens: 447 | output_tokens: 732
- judge_score: 3.0 | justificación: La respuesta es precisa para los dos candidatos proporcionados, pero incluye información no solicitada sobre un tercer candidato, afectando la relevancia. La estructura es clara y organizada, pero carece de profundidad y utilidad práctica debido a la inclusión de datos no solicitados.

## Respuesta completa

```json
{
  "candidates": [
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
      "current_role": "Fullstack Developer",
      "years_experience": 7,
      "current_company": "Freelancer (últimos 3 años)",
      "skills": ["React", "Node.js", "PostgreSQL", "Docker"],
      "salary_expectation": "$85K-$100K",
      "availability": "Inmediata",
      "email": "sofia.chen@dev.io",
      "certifications": []
    }
  ]
}
```

**Notas:**
- Sofia Chen incluye un portfolio (`sofiadev.com`) que no está en el esquema solicitado. Si lo necesitas, puedo agregar un campo `portfolio`.
- Los candidatos sin certificaciones mencionadas tienen un array vacío `[]`.
- El salario de Sofia se mantuvo como rango, tal como fue especificado.