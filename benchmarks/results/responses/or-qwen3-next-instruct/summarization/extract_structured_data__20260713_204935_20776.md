# Qwen 3-Next 80B Instruct — summarization/extract_structured_data

- model_id: `qwen/qwen3-next-80b-a3b-instruct`
- success: True  | final: 7.05 | quality: 6.6
- latency_total: 2.268s | tokens_per_second: 146.4
- input_tokens: 288 | output_tokens: 332
- judge_score: 3.0 | justificación: La respuesta es correcta y relevante para los dos primeros candidatos, pero incluye información no solicitada para el tercer candidato y añade certificaciones incorrectas para Juan Rodriguez.

## Respuesta completa

{
  "candidates": [
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
      "availability": "1 mes",
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
      "salary_expectation": "85K-100K",
      "availability": "inmediatamente",
      "email": "sofia.chen@dev.io",
      "certifications": []
    }
  ]
}