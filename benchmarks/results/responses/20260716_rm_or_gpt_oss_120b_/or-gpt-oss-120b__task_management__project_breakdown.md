# GPT-OSS 120B — task_management/project_breakdown

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 9.15 | quality: 9.8
- latency_total: 9.616s | tokens_per_second: 213.0
- input_tokens: 141 | output_tokens: 2048
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil, proporcionando un desglose detallado y estructurado que un emprendedor podría usar directamente.

## Respuesta completa

## 🚀 Plan de lanzamiento de la landing page (4 semanas)

| **Fase** | **Tarea** | **Responsable** | **Duración** | **Dependencias** | **Entrega / Hito** |
|----------|-----------|-----------------|--------------|------------------|--------------------|
| **1. Kick‑off & Brief** | 1.1 Reunión de alineación (objetivos, público, KPIs) | PM (puede ser tú) + Todo el equipo | 0,5 d | Ninguna | Brief aprobado |
| | 1.2 Definir arquitectura de información (mapa de la página) | Copywriter + Designer | 0,5 d | 1.1 | Wireframe de estructura |
| **2. Contenido** | 2.1 Redacción de títulos, subtítulos, copy de beneficios y CTA | Copywriter | 1 d | 1.2 | Texto completo (≈ 600‑800 palabras) |
| | 2.2 Recopilación de assets (logo, fotos, iconos, testimonios) | Designer (recopila) + PM (solicita) | 0,5 d | 1.2 | Assets list |
| | 2.3 Revisión y aprobación interna del copy | PM + Designer | 0,5 d | 2.1 | Copy final |
| **3. Diseño UI/UX** | 3.1 Creación de wireframes de alta fidelidad (desktop + mobile) | Designer | 1 d | 1.2, 2.3 | Wireframes aprobados |
| | 3.2 Prototipo interactivo (Figma/Adobe XD) | Designer | 1 d | 3.1 | Prototipo clickable |
| | 3.3 Revisión de diseño con stakeholders (incluye copy) | PM + Copywriter | 0,5 d | 3.2 | Feedback consolidado |
| | 3.4 Ajustes finales de UI (paleta, tipografía, micro‑animaciones) | Designer | 0,5 d | 3.3 | UI final entregada (assets, specs) |
| **4. Desarrollo Front‑end** | 4.1 Setup del repo, CI/CD básico y estructura del proyecto (HTML, CSS, JS) | Dev 1 | 0,5 d | 3.4 | Repo listo |
| | 4.2 Implementación del layout (HTML + CSS) – versión desktop | Dev 1 | 1 d | 3.4 | Layout base |
| | 4.3 Adaptación responsive (tablet + mobile) | Dev 2 | 1 d | 4.2 | UI responsive |
| | 4.4 Integración del copy y assets (imágenes, iconos, videos) | Dev 1 | 0,5 d | 2.3, 4.3 | Página completa |
| | 4.5 Implementación de formularios de captura (Mailchimp/HubSpot) y tracking (GA, FB Pixel) | Dev 2 | 0,5 d | 4.4 | Formulario funcional |
| | 4.6 Optimización de performance (lazy‑load, minify, SEO básico) | Dev 1 | 0,5 d | 4.5 | Página ligera |
| **5. QA & Testing** | 5.1 Revisión funcional (links, formularios, validación) | Dev 2 | 0,5 d | 4.6 | Bug list |
| | 5.2 Pruebas cross‑browser (Chrome, Firefox, Safari, Edge) | Dev 1 | 0,5 d | 5.1 | Informe de compatibilidad |
| | 5.3 Pruebas de usabilidad (mobile tap targets, velocidad) | Designer + PM | 0,5 d | 5.2 | Ajustes UI/UX |
| | 5.4 Corrección de bugs críticos | Dev 1/Dev 2 | 0,5 d | 5.3 | Versión “Go‑live” |
| **6. Pre‑lanzamiento** | 6.1 Configuración del dominio y hosting (SSL) | Dev 1 | 0,25 d | 5.4 | URL activa |
| | 6.2 Implementación de tracking y conversiones (Google Analytics, FB Pixel, Hotjar) | Dev 2 | 0,25 d | 6.1 | Medición lista |
| | 6.3 Revisión final con stakeholder (CEO/Product Owner) | PM + Todo el equipo | 0,5 d | 6.2 | Aprobación “Launch Ready” |
| **7. Lanzamiento** | 7.1 Publicación y puesta en producción | Dev 1 | 0,25 d | 6.3 | Landing live |
| | 7.2 Monitoreo de 24 h (errores 404, formulario, tracking) | PM + Dev 2 | 1 d | 7.1 | Informe de lanzamiento |
| **8. Post‑lanzamiento (Semana 4)** | 8.1 Análisis de métricas iniciales (CTR, leads, bounce) | PM + Copywriter | 0,5 d | 7.2 | Insights para iterar |
| | 8.2 Pequeñas mejoras (A/B de CTA, copy tweaks) | Designer + Dev 1 | 0,5 d | 8.1 | Optimización continua |

---

### 📅 Cronograma resumido (4 semanas laborales)

| **Semana** | **Días** | **Principales entregas** |
|------------|----------|--------------------------|
| **1** | D1‑D5 | Brief, arquitectura IA, copy inicial, assets list, wireframes de alta fidelidad |
| **2** | D6‑D10 | Prototipo clickable, UI final, setup del repo, layout desktop + responsive, integración de copy |
| **3** | D11‑D15 | Formularios + tracking, performance SEO, QA funcional + cross‑browser, corrección de bugs |
| **4** | D16‑D20 | Dominio/hosting, revisión final, lanzamiento, monitoreo 24 h, análisis de métricas y primeras mejoras |

> **Nota:** Cada día laboral se asume de 8 h. Se ha dejado un “colchón” de medio día en la semana 3 para imprevistos y en la semana 4 para ajustes post‑lanzamiento.

---

## 👥 Roles y responsabilidades clave

| **Rol** | **Responsabilidades principales** |
|---------|-----------------------------------|
| **Designer** | Arquitectura IA, wireframes, UI high‑fidelity, assets visuales, pruebas de usabilidad, micro‑animaciones. |
| **Copywriter** | Investigación de público, redacción de títulos, subtítulos, cuerpo, CTA, revisión de copy con UI, análisis de métricas post‑lanzamiento. |
| **Developer 1** | Configuración del repo, estructura HTML/CSS, layout desktop, hosting + dominio, SSL, performance. |
| **Developer 2** | Responsivo mobile, integración de formularios y tracking, pruebas cross‑browser, corrección de bugs críticos. |
| **PM (tú)** | Coordinación, agenda de reuniones, seguimiento de dependencias, aprobaciones, monitoreo post‑lanzamiento, reporte de KPI. |

---

## ✅ Checklist de “Go‑Live”

- [ ] Copy aprobado y SEO‑friendly (título, meta‑description, H1‑H3).  
- [ ] UI final entregada en Figma con especificaciones de medidas y colores.  
- [ ] Código versionado en Git, CI/CD configurado (push → staging → production).  
- [ ] Formularios conectados a la herramienta de email‑marketing y testados (doble opt‑in).  
- [ ] SSL activo y dominio apuntando al servidor.  
- [ ] GA4 y FB Pixel configurados, eventos de conversión (submit‑form, scroll‑50%).  
- [ ] Pruebas en dispositivos: iOS/Android, Chrome/Firefox/Safari/Edge.  
- [ ] Load time < 2 s (Lighthouse > 90).  
- [ ] Backup y plan de rollback listo.  

---

### 🎯 KPIs de lanzamiento (para el copywriter y PM)

| **KPI** | **Objetivo** | **Herramienta** |
|---------|--------------|-----------------|
| Visitas únicas en la primera semana | > 2 000 | Google