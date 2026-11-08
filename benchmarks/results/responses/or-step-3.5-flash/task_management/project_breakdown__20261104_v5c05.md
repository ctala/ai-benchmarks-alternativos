# Step 3.5 Flash — task_management/project_breakdown

- model_id: `stepfun/step-3.5-flash`
- success: True  | final: 8.67 | quality: 9.72
- latency_total: 39.143s | tokens_per_second: 86.9
- input_tokens: 82 | output_tokens: 3402
- judge_score: 4.8 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito lanzar una landing page para un nuevo producto SaaS de gestion de inventario. El lanzamiento es en 4 semanas. El equipo tiene 1 disenador, 2 developers y 1 copywriter. Desglosa el proyecto en fases, tareas, dependencias, responsables y un timeline realista.


## Respuesta completa

# Plan de Lanzamiento de Landing Page SaaS (4 semanas)

## 📋 **Resumen Ejecutivo**
- **Objetivo:** Landing page funcional para lanzamiento de SaaS de gestión de inventario
- **Duración:** 4 semanas (20 días laborables)
- **Equipo:** 1 Diseñador UX/UI, 2 Desarrolladores Full-Stack, 1 Copywriter
- **Enfoque:** MVP con secciones esenciales (Hero, Features, Pricing, Testimonials, FAQ, CTA)

---

## 🗓️ **Timeline General (20 días)**
```
Semana 1: Planificación + Copywriting inicial + Wireframes
Semana 2: Diseño UI + Copywriting final + Aprobaciones
Semana 3: Desarrollo frontend + integración
Semana 4: Testing + optimización + despliegue
```

---

## 📌 **Fases y Tareas Detalladas**

### **FASE 1: PLANIFICACIÓN (Días 1-2)**
| Día | Tarea | Responsable | Dependencias | Entregable |
|-----|-------|-------------|--------------|------------|
| 1 | Kick-off meeting: objetivos, público, USP, estructura | Todos | Ninguna | Estructura definida |
| 1-2 | Benchmarking de competidores | Diseñador + Copywriter | Kick-off | Moodboard + análisis |
| 2 | Definición de arquitectura de información | Diseñador | Estructura | Sitemap/flujo usuario |
| 2 | Creación de user personas (1-2) | Copywriter | Kick-off | Documento personas |

---

### **FASE 2: COPYWRITING (Días 3-7)**
| Día | Tarea | Responsable | Dependencias | Entregable |
|-----|-------|-------------|--------------|------------|
| 3-4 | Borrador copy secciones clave (Hero, Features) | Copywriter | Estructura | Documento Google Docs |
| 5-6 | Borrador copy Pricing, Testimonials, FAQ | Copywriter | Estructura | Documento completo |
| 7 | Revisión interna copy + feedback equipo | Todos | Borradores | Copy aprobado |
| 7 | Optimización SEO (meta tags, keywords) | Copywriter | Copy aprobado | Meta tags listos |

---

### **FASE 3: DISEÑO (Días 5-12)**
| Día | Tarea | Responsable | Dependencias | Entregable |
|-----|-------|-------------|--------------|------------|
| 5-6 | Wireframes baja fidelidad (Figma) | Diseñador | Estructura + copy borrador | Wireframes aprobados |
| 7-8 | Mockups alta fidelidad (mobile/desktop) | Diseñador | Wireframes aprobados | Mockups en Figma |
| 9-10 | Microinteracciones y animaciones | Diseñador | Mockups | Especificaciones animaciones |
| 11-12 | Entrega de assets (imágenes, iconos, specs) | Diseñador | Mockups aprobados | Carpeta assets + guía estilo |

---

### **FASE 4: DESARROLLO (Días 10-18)**
| Día | Tarea | Responsable | Dependencias | Entregable |
|-----|-------|-------------|--------------|------------|
| 10-11 | Setup proyecto (React/Next.js, Tailwind, repo) | Dev1 | Diseño aprobado | Repositorio configurado |
| 11-13 | Maquetación secciones estáticas (Hero, Features) | Dev1 | Assets + copy | Componentes HTML/CSS |
| 12-14 | Secciones dinámicas (Pricing toggle, FAQ accordion) | Dev2 | Componentes base | JS interactivo |
| 13-15 | Integración formulario contacto (con validación) | Dev1 + Dev2 | Backend API (si aplica) | Formulario funcional |
| 14-16 | Responsive testing + ajustes cross-browser | Ambos devs | Maquetación completa | Compatibilidad garantizada |
| 17-18 | Optimización performance (lazy load, imágenes) | Dev1 | Testing completado | Lighthouse score >90 |

---

### **FASE 5: TESTING & LANZAMIENTO (Días 19-20)**
| Día | Tarea | Responsable | Dependencias | Entregable |
|-----|-------|-------------|--------------|------------|
| 19 | QA interno (links, formularios, copy) | Todos | Desarrollo completado | Bug list |
| 19 | Corrección bugs críticos | Devs | Bug list | Landing estable |
| 19 | Configuración analytics (GA4, heatmaps) | Dev1 | Landing estable | Tracking activo |
| 20 | Despliegue producción (Vercel/Netlify) | Dev1 | QA aprobado | landing.tudominio.com |
| 20 | Lanzamiento + monitoreo inicial | Todos | Despliegue | Reporte post-lanzamiento |

---

## 🔄 **Dependencias Críticas**
1. **Copy → Diseño:** Diseño no puede avanzar sin copy aprobado para dimensionar texto.
2. **Diseño → Desarrollo:** Desarrollo no inicia sin mockups y assets aprobados.
3. **Desarrollo → Testing:** Testing requiere desarrollo 100% completado.
4. **Retroalimentación:** Cada fase requiere revisión conjunta (1 día buffer incluido).

---

## ⚠️ **Riesgos y Mitigación**
| Riesgo | Impacto | Mitigación |
|--------|---------|------------|
| Retraso en copy | Alto | Copywriter prioriza landing; buffer de 1 día en Fase 2 |
| Cambios de último momento en diseño | Medio | Aprobación formal de mockups antes de desarrollo |
| Problemas técnicos (API formulario) | Alto | Devs preparan alternativa estática (emailJS) |
| Testing descubre bugs graves | Medio | Día 19 dedicado exclusivo a correcciones |

---

## 📊 **Distribución de Recursos**
- **Diseñador:** 80% tiempo en Fases 1-3 (días 1-12), 20% apoyo en Fase 4-5.
- **Copywriter:** 60% Fase 2 (días 3-7), 20% apoyo en Fase 4-5, 20% disponible para ajustes.
- **Dev1:** 30% setup/infra, 40% maquetación, 30% optimización/testing.
- **Dev2:** 50% componentes interactivos, 50% responsive/testing.

---

## ✅ **Checklist de Entregables Finales**
- [ ] Landing page responsive (mobile/tablet/desktop)
- [ ] Copy optimizado para conversión y SEO
- [ ] Formulario de contacto/lead capture funcional
- [ ] Integración analytics (GA4, Facebook Pixel)
- [ ] Optimización de imágenes (WebP, lazy load)
- [ ] Página de agradecimiento post-formulario
- [ ] Documentación de despliegue y mantenimiento

---

## 📈 **Recomendaciones para Éxito**
1. **Reuniones diarias 15 min:** Para alinear bloqueos.
2. **Herramientas:** Figma (diseño), GitHub (código), Google Docs (copy), Notion (seguimiento).
3. **Aprobaciones formales:** Al final de Fase 2 (copy) y Fase 3 (diseño) con firma de todos.
4. **Buffer oculto:** 1 día en cada fase para imprevistos (ya incluido en timeline).
5. **Post-lanzamiento:** Plan de 1 semana para monitoreo y primeros ajustes basados en datos.

---

**Nota:** Este plan asume que no se requieren integraciones complejas (ej. pagos, CRM). Si las hay, agregar 3-5 días adicionales en Fase 4.