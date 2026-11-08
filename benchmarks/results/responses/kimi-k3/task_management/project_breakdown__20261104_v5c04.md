# Kimi K3 — task_management/project_breakdown

- model_id: `moonshotai/kimi-k3`
- success: True  | final: 7.96 | quality: 9.8
- latency_total: 43.721s | tokens_per_second: 41.3
- input_tokens: 92 | output_tokens: 1804
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un desglose detallado y estructurado que un emprendedor podría usar directamente.

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito lanzar una landing page para un nuevo producto SaaS de gestion de inventario. El lanzamiento es en 4 semanas. El equipo tiene 1 disenador, 2 developers y 1 copywriter. Desglosa el proyecto en fases, tareas, dependencias, responsables y un timeline realista.


## Respuesta completa

Aquí tienes un plan de proyecto estructurado para lanzar en **4 semanas** con tu equipo de 4 personas. He priorizado el **MVP de landing** (lo esencial para captar leads) sobre perfección visual, dado el timeline ajustado.

---

## 🎯 FASE 1: ESTRATEGIA Y ARQUITECTURA (Días 1-3)
*Objetivo: Definir qué vamos a decir y cómo se estructura antes de tocar diseño/código.*

| Tarea | Responsable | Duración | Dependencias | Entregable |
|-------|-------------|----------|--------------|------------|
| Definir propuesta de valor única (UVP) y buyer persona | Copywriter + Tú | 1 día | - | Documento de messaging (1 página) |
| Wireframe de baja fidelidad (estructura de secciones) | Diseñador | 1 día | UVP definida | Sketch/Balsamiq con flujo de usuario |
| Arquitectura técnica y setup de repo | Dev 1 (Lead) | 1 día | - | Repo creado, CI/CD básico, dominio configurado |
| Investigación de keywords SEO básicas | Copywriter | 0.5 días | UVP | Lista de 5-10 keywords para H1/H2 |

**Hito crítico:** Aprobación del wireframe al final del Día 3.

---

## 🎨 FASE 2: DISEÑO Y CONTENIDO PARALELO (Días 4-10)
*Objetivo: Diseño visual aprobado y copy final listo para implementar.*

| Tarea | Responsable | Duración | Dependencias | Notas |
|-------|-------------|----------|--------------|-------|
| Diseño de alta fidelidad (Desktop) | Diseñador | 3 días | Wireframe aprobado | Figma con componentes reutilizables |
| Copywriting: Hero, Features, CTA | Copywriter | 2 días | Wireframe | Máximo 3 iteraciones de revisión |
| Copywriting: Social proof, FAQ, Footer | Copywriter | 1 día | Copy principal | Incluir microcopy para formularios |
| Setup de analytics y herramientas de captación | Dev 2 | 1 día | Repo listo | Google Analytics 4, pixel de LinkedIn/Twitter si aplica |
| Desarrollo de componentes base (sistema de diseño) | Dev 1 | 2 días | Diseño en progreso | Header, Footer, Button, Card components |

**Dependencia crítica:** El diseño debe estar **80% completo** al final del Día 7 para que los devs no se bloqueen.

---

## 💻 FASE 3: DESARROLLO E INTEGRACIÓN (Días 8-17)
*Objetivo: Landing funcional con contenido real, responsive y conectada a herramientas.*

| Tarea | Responsable | Duración | Dependencias |
|-------|-------------|----------|--------------|
| Maquetación secciones principales (Hero, Features, CTA) | Dev 1 | 3 días | Diseño aprobado + Copy final |
| Maquetación secciones secundarias (Testimonios, Pricing teaser, Footer) | Dev 2 | 2 días | Diseño aprobado |
| Formulario de captación + integración con email marketing (Mailchimp/ConvertKit) | Dev 2 | 1 día | Herramientas configuradas |
| Responsive design (Tablet/Mobile) | Dev 1 | 2 días | Desktop completo |
| Optimización de imágenes y assets | Diseñador | 1 día | Diseño final |
| Revisión de copy en contexto (¿cabe en los botones? ¿se lee bien?) | Copywriter | 1 día | Maquetación 70% |

**Buffer de seguridad:** Días 16-17 reservados para bugs críticos.

---

## 🚀 FASE 4: QA, OPTIMIZACIÓN Y LANZAMIENTO (Días 18-28)
*Objetivo: Landing pulida, rápida y lista para tráfico.*

| Tarea | Responsable | Duración | Dependencias |
|-------|-------------|----------|--------------|
| QA funcional (formularios, links, responsive en 3 dispositivos) | Todo el equipo | 1 día | Desarrollo completo |
| Optimización de velocidad (Lighthouse >90) | Dev 1 | 1 día | QA inicial |
| SEO on-page (meta tags, OG images, schema markup) | Dev 2 + Copywriter | 1 día | Copy final |
| Configuración de A/B testing básico (opcional pero recomendado) | Dev 2 | 0.5 días | Analytics listo |
| Revisión legal (Privacy Policy, Terms si captas emails) | Copywriter/Tú | 0.5 días | - |
| Soft launch (compartir con red interna/10 usuarios beta) | Tú | 1 día | Todo lo anterior |
| Fix de bugs del soft launch | Devs | 1 día | Feedback recibido |
| **LANZAMIENTO PÚBLICO** | Tú | Día 28 | Checklist completo |

---

## 📅 Timeline Visual (Simplificado)

```
Semana 1: [Estrategia][Diseño    ][Setup Dev]
Semana 2: [Diseño fin][Copy fin  ][Desarrollo ██████]
Semana 3: [Desarrollo ███████████][Integraciones]
Semana 4: [QA][Optimización][Soft Launch][🚀 LAUNCH]
```

---

## ⚠️ Riesgos y Mitigaciones

| Riesgo | Probabilidad | Plan B |
|--------|--------------|--------|
| Diseño se extiende más de 5 días | Media | Usar template de Tailwind UI/Shuffle como base y personalizar solo colores/tipografía |
| Copy no convence en revisiones | Media | Tener 2 versiones del Hero (A/B test en el soft launch) |
| Integración de email marketing falla | Baja | Tener formulario HTML simple + Zapier como backup |
| Scope creep (añadir blog, dashboard preview, etc.) | Alta | **Congelar scope el Día 3.** Cualquier feature nueva va al backlog post-lanzamiento |

---

## ✅ Checklist de Lanzamiento (Día 28)

- [ ] Tiempo de carga < 2.5s en 3G
- [ ] Formulario envía emails correctamente (test con 3 correos reales)
- [ ] Pixel de analytics verificado (Real-Time view)
- [ ] OG image se ve bien al compartir en LinkedIn/Twitter
- [ ] Textos legales accesibles en footer
- [ ] Botón de CTA visible sin scroll en mobile (above the fold)
- [ ] Backup de la base de datos de emails captados

---

## 💡 Recomendación de Stack (para velocidad)

- **Framework:** Next.js o Astro (SSG para velocidad máxima)
- **Estilos:** Tailwind CSS (desarrollo rápido con el diseñador)
- **Formularios:** Formspree o Basin (evita backend propio) o API route simple si usan Next.js
- **Analytics:** Plausible o GA4 + Hotjar (heatmaps para iterar post-lanzamiento)

**Consejo final:** Con 4 semanas, el enemigo es la perfección. Lanza con el 80% de features al 100% de calidad, no al revés. El objetivo es validar el interés, no tener la landing perfecta.

¿Necesitas que profundice en alguna fase específica o que ajuste el plan para alguna tecnología específica que ya tengan decidida?