# Seed 2.0 Code — summarization/extract_structured_data

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 6.33 | quality: 6.88
- latency_total: 37.286s | tokens_per_second: 54.9
- input_tokens: 315 | output_tokens: 2048
- judge_score: 3.2 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**user:**

Extrae la informacion de estos 3 perfiles de candidatos y devuelvelos como JSON:

Candidato 1: Maria Garcia, 28 anos, ingeniera de software con 5 anos de experiencia. Trabaja en Google desde 2023. Maneja Python, Go, Kubernetes. Pide $95K. Disponible en 2 semanas. Email: maria.g@email.com

Candidato 2: Juan Rodriguez, 35 anos, senior backend developer. 10 anos de experiencia, actualmente en Mercado Libre. Especialista en Java, microservicios, AWS. Salario esperado $120K. Necesita dar 1 mes de aviso. Contacto: jrodriguez@mail.com. Tiene certificacion AWS Solutions Architect.

Candidato 3: Sofia Chen, 31 anos, fullstack. 7 anos experiencia. Freelancer los ultimos 3 anos. React, Node.js, PostgreSQL, Docker. Pide entre $85K-$100K. Disponible inmediatamente. sofia.chen@dev.io. Portfolio: sofiadev.com

Formato JSON con campos: name, age, current_role, years_experience, current_company, skills[], salary_expectation, availability, email, certifications[]


## Respuesta completa


So, let's tackle this. First, I need to extract each candidate's info exactly matching the required JSON fields.

First, let's list each field for each candidate:

First, the required fields are: name, age, current_role, years_experience, current_company, skills[], salary_expectation, availability, email, certifications[]

Let's go one by one:

CANDIDATO 1: MARIA GARCIA
- name: "Maria Garcia"
- age: 28 (number, not string)
- current_role: "ingeniera de software" (wait, original says "ingeniera de software con 5 años"—yes, current role is that. Wait, let's check original: Candidato 1 says "ingeniera de software con 5 anos de experiencia. Trabaja en Google desde 2023." So current_role is "ingeniera de software"
- years_experience: 5 (number)
- current_company: "Google"
- skills: ["Python", "Go", "Kubernetes"] (exact from text)
- salary_expectation: "$95K" (exact, since it's a single value)
- availability: "Disponible en 2 semanas" (or exact text? Wait original says "Disponible en 2 semanas"—yes, keep exact as per input, but maybe translate? Wait no, wait the input is in Spanish, the required fields are in English (the keys) but the values: let's check the required fields' values. Wait the user said extrae la info de los perfiles (Spanish) y devuelve JSON con campos (keys) en inglés: name, age, etc. So values are as per the Spanish original, but accurate.

Wait Candidato 1's availability: "Disponible en 2 semanas" → yes, that's the value. Email: "maria.g@email.com". Certifications: he doesn't have any, so empty array [].

Now CANDIDATO 2: JUAN RODRIGUEZ
- name: "Juan Rodriguez"
- age: 35 (number)
- current_role: "senior backend developer" (original says that)
- years_experience: 10 (number, original: 10 años de experiencia)
- current_company: "Mercado Libre" (original: actualmente en Mercado Libre)
- skills: ["Java", "microservicios", "AWS"] (original: Especialista en Java, microservicios, AWS)
- salary_expectation: "$120K" (original: Salario esperado $120K)
- availability: "Necesita dar 1 mes de aviso" (original exact text)
- email: "jrodriguez@mail.com"
- certifications: ["AWS Solutions Architect"] (original: Tiene certificacion AWS Solutions Architect) → note: original has "certificacion" (singular) so one item.

Now CANDIDATO 3: SOFIA CHEN
- name: "Sofia Chen"
- age: 31 (number)
- current_role: "fullstack" (original: fullstack)
- years_experience: 7 (number, original: 7 anos experiencia)
- current_company: Wait wait, original says "Freelancer los ultimos 3 anos"—so what's current_company? Oh, the required field is current_company, but if they are freelancer, maybe "Freelancer" (since that's their current employment status's "company" equivalent? Wait let's check the original text for Candidato 3: no company name, only "Freelancer los ultimos 3 anos". So current_company should be "Freelancer" because that's their current employment arrangement. Wait is that correct? Let's confirm: the other candidates have current company (Google, Mercado Libre), Sofia is freelancer, so yes, current_company = "Freelancer".

- skills: ["React", "Node.js", "PostgreSQL", "Docker"] (original exact list)
- salary_expectation: "$85K-$100K" (original: Pide entre $85K-$100K → exact range as string)
- availability: "Disponible inmediatamente" (original exact text)
- email: "sofia.chen@dev.io"
- certifications: [] (no mention of certifications, so empty array)

Wait let's double-check each field for each candidate to make sure we don't miss anything, and that the data types are correct:

- age: number (not string, e.g., 28, not "28")
- years_experience: number (5, 10,7)
- skills: array of strings, exact as per input (no translation, since input is Spanish terms like "microservicios", "ingeniera de software")
- certifications: array, empty if none
- current_role: exact from input:
  - C1: "ingeniera de software" (correct, original says that)
  - C2: "senior backend developer" (original says that)
  - C3: "fullstack" (original says that)
- current_company:
  - C1: "Google" (trabaja en Google desde 2023 → correct)
  - C2: "Mercado Libre" (actualmente en Mercado Libre → correct)
  - C3: "Freelancer" (since she's a freelancer, no company name, so that's the correct value)
- salary_expectation:
  - C1: "$95K" (exact)
  - C2: "$120K" (exact)
  - C3: "$85K-$100K" (exact, since it's a range)
- availability:
  - C1: "Disponible en 2 semanas" (exact)
  - C2: "Necesita dar 1 mes de aviso" (exact)
  - C3: "Disponible inmediatamente" (exact)
- email: exact from each candidate
- certifications:
  - C1: [] (no mention)
  - C2: ["AWS Solutions Architect"] (exact)
  - C3: [] (no mention)

Wait also, check for typos: original has "anos" (without accent, but in JSON it's fine, but we are extracting as per input, but the values: e.g., availability is as per input, which has "anos" but no, wait the input's text: let's check the user's input again:

User's input (Spanish, with possible accent omissions, but we extract exactly as written, except for the JSON structure):

Wait Candidato 1: "28 anos" → but in age, we use 28 (number), so that's fine. The text for availability etc. is as per input, e.g., "Disponible en 2 semanas" (correct as per user's input).

Wait another check: Candidato 2's current_role: "senior backend developer" (yes, user wrote that). Skills: "Java, microservicios, AWS" (yes, so array of those three). Certifications: "AWS Solutions Architect" (yes, user wrote "Tiene certificacion AWS Solutions Architect" → so one item in array).

Candidato 3: current_role "fullstack" (user wrote that). Skills: "React, Node.js, PostgreSQL, Docker" (yes). Current_company: user said "Freelancer los ultimos 3 anos" → no corporate company, so current_company is "Freelancer" (that's the only logical value, since the field is required, and that's their current employment status's "company" equivalent).

Now, structure the JSON: it's an array of three objects, right? Wait the user said "devuelvelos como JSON" with the given fields. Let's confirm the keys: exactly as given: name, age, current_role, years_experience, current_company, skills, salary_expectation, availability, email, certifications. All lowercase, underscores where needed.

Wait let's make sure all keys are exactly as specified:

Required keys (user wrote):
name, age, current_role, years_experience, current_company, skills[], salary_expectation, availability, email, certifications[]

Yes, so keys are:
- "name"
- "age"
- "current_role"
- "years_experience"
- "current_company"
- "skills" (array)
- "salary_expectation"
- "availability"
- "email"
- "certifications" (array)

Now, let's write each object:

First candidate (Maria Garcia):
{
  "name": "Maria Garcia",
  "age": 28,
  "current_role": "ingeniera de software",
  "years_experience": 5,
  "current_company": "Google",
  "skills": ["Python", "Go", "Kubernetes"],
  "salary_expectation": "$95K",
  "availability": "Disponible en