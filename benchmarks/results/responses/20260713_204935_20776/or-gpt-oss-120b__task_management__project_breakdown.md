# GPT-OSS 120B — task_management/project_breakdown

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 8.55 | quality: 9.8
- latency_total: 250.326s | tokens_per_second: 5.6
- input_tokens: 130 | output_tokens: 1402
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un plan detallado y estructurado que un emprendedor podría usar directamente.

## Respuesta completa

## Plan de lanzamiento de la Landing Page – 4 semanas  

**Equipo:**  
- **Diseñador (D)**  
- **Developer 1 (Dev‑A)**  
- **Developer 2 (Dev‑B)**  
- **Copywriter (C)**  
- **Product Owner / PM (PO)** – actúa como coordinador y responsable de la toma de decisiones.  

> **Objetivo:** Tener la landing page online, testeada y aprobada el **día 28** (fin de la cuarta semana).  

---

### 1️⃣ Fases, tareas, dependencias y responsables

| **Fase** | **Tarea** | **Duración estimada** | **Dependencia** | **Responsable** |
|----------|-----------|----------------------|-----------------|-----------------|
| **Kick‑off & definición** (Día 0‑1) | • Reunión de alineación (objetivos, target, KPI, tono, CTA)<br>• Definir brief técnico (hosting, dominio, formulario, tracking) | 2 días | Ninguna | PO + C + D |
| **Copywriting** (Día 2‑6) | • Investigación de palabras clave SEO<br>• Redacción de headline, sub‑headline, descripción de features, beneficios, pruebas sociales, FAQ<br>• Redacción de copy para CTA y formulario<br>• Revisión interna | 5 días | Kick‑off | C |
| **Wireframes & arquitectura** (Día 7‑8) | • Sketch de estructura (mobile‑first)<br>• Definir flujo de usuario y puntos de conversión | 2 días | Copywriting (texto base) | D |
| **Diseño visual** (Día 9‑13) | • Mockup de alta fidelidad (desktop & mobile)<br>• UI kit (colores, tipografía, botones, íconos)<br>• Prototipo interactivo (Figma/Adobe XD)<br>• Review interno y ajustes | 5 días | Wireframes + Copy | D |
| **Preparación de assets** (Día 14) | • Exportar imágenes optimizadas (WebP/AVIF)<br>• Generar SVGs de íconos<br>• Crear archivo de estilo (variables CSS) | 1 día | Diseño final | D |
| **Setup técnico** (Día 15) | • Crear repo Git + rama “landing”<br>• Configurar CI (GitHub Actions) y entorno de staging<br>• Instalar dependencias (Tailwind/Bootstrap, bundler) | 1 día | Ninguna (paralelo) | Dev‑A |
| **Desarrollo Front‑end** (Día 16‑20) | • Maquetar layout responsivo (HTML + Tailwind/SCSS)<br>• Integrar copy y assets<br>• Implementar formulario (Webhooks → HubSpot/Mailchimp)<br>• Insertar scripts de tracking (GA4, Hotjar)<br>• SEO on‑page (meta tags, JSON‑LD) | 5 días | Diseño + assets + setup | Dev‑A + Dev‑B |
| **Testing & QA** (Día 21‑22) | • Revisión cross‑browser (Chrome, FF, Safari, Edge) y dispositivos (iOS/Android)<br>• Pruebas de rendimiento (Lighthouse ≥ 90)<br>• Validación de accesibilidad (WCAG 2.1 AA)<br>• Revisión de copy (ortografía, consistencia) | 2 días | Desarrollo completado | Dev‑A, Dev‑B, C, D |
| **Iteración & ajustes** (Día 23‑24) | • Corrección de bugs críticos<br>• Ajustes de UI/UX basados en feedback interno<br>• Optimización de carga (lazy load, gzip) | 2 días | QA | Dev‑A + Dev‑B |
| **Stakeholder sign‑off** (Día 25) | • Presentación final al equipo de producto/marketing<br>• Aprobación de métricas y checklist de lanzamiento | 1 día | Ajustes finales | PO + D + C |
| **Pre‑launch (staging → producción)** (Día 26) | • Deploy a producción (CDN/Hosting)<br>• Configuración DNS