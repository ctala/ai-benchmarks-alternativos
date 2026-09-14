# Fugu Max — task_management/project_breakdown

- model_id: `sakana/fugu-max`
- success: True  | final: 8.39 | quality: 10.0
- latency_total: 40.183s | tokens_per_second: 103.6
- input_tokens: 146 | output_tokens: 4162
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un desglose detallado y estructurado del proyecto que un emprendedor podría aplicar directamente.

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito lanzar una landing page para un nuevo producto SaaS de gestion de inventario. El lanzamiento es en 4 semanas. El equipo tiene 1 disenador, 2 developers y 1 copywriter. Desglosa el proyecto en fases, tareas, dependencias, responsables y un timeline realista.


## Respuesta completa

## Supuestos para que el lanzamiento sea viable en 4 semanas

- Se lanzará **una landing page responsive**, no un sitio web completo.
- Se utilizará el stack actual o un CMS/framework ya conocido por los developers.
- El alcance inicial será de unas **6–8 secciones**:
  1. Hero con propuesta de valor y CTA.
  2. Problema que resuelve.
  3. Funcionalidades principales.
  4. Flujo de uso o demo visual.
  5. Beneficios por tipo de cliente.
  6. Prueba social, logos o testimonios.
  7. FAQ.
  8. CTA final y formulario.
- Debe existir una persona de negocio o producto que actúe como **Product Owner**, aunque no esté incluida en el equipo. Esta persona deberá aprobar decisiones en un máximo de 24 horas.

### Roles

- **Diseñador:** UX, UI, responsive design y handoff.
- **Developer 1 — Tech Lead:** arquitectura, setup, integraciones, formularios, analytics y deployment.
- **Developer 2 — Frontend/QA:** implementación visual, responsive, performance, accesibilidad y pruebas.
- **Copywriter:** posicionamiento, copy de la landing, SEO y mensajes del formulario.
- **Product Owner/Stakeholder:** prioridades, validaciones y aprobación final.

---

# Plan por fases

## Fase 1: Alineación y definición del alcance

**Duración:** Días 1–2  
**Objetivo:** evitar cambios estructurales durante el desarrollo.

| Tarea | Responsable | Dependencias |
|---|---|---|
| Reunión de kickoff | Todo el equipo + Product Owner | Ninguna |
| Definir público objetivo y casos de uso prioritarios | Copywriter + Product Owner | Kickoff |
| Definir propuesta de valor y CTA principal | Copywriter + Product Owner | Público objetivo |
| Definir métricas de lanzamiento | Product Owner + Dev 1 | Objetivos de negocio |
| Confirmar stack, hosting, CMS y repositorio | Dev 1 | Ninguna |
| Definir estructura de la landing | Diseñador + Copywriter | Propuesta de valor |
| Crear backlog y criterios de aceptación | Dev 1 + Product Owner | Alcance aprobado |

### Entregables

- Brief de producto.
- Público objetivo y principales pain points.
- Propuesta de valor.
- CTA principal, por ejemplo: “Solicitar demo”, “Crear cuenta” o “Probar gratis”.
- Sitemap o estructura de la página.
- Métricas objetivo: conversión del formulario, CTR del CTA, tráfico, leads generados.

---

## Fase 2: UX, arquitectura de contenido y copy

**Duración:** Días 2–6  
**Objetivo:** validar primero el contenido y el flujo antes de invertir en diseño visual.

| Tarea | Responsable | Dependencias |
|---|---|---|
| Crear wireframe de la landing | Diseñador | Estructura inicial |
| Definir jerarquía de mensajes | Copywriter | Propuesta de valor |
| Redactar titulares y subtitulares | Copywriter | Público y CTA |
| Redactar beneficios y funcionalidades | Copywriter + Product Owner | Información del producto |
| Definir preguntas frecuentes | Copywriter + Product Owner | Casos de uso |
| Crear wireframe responsive básico | Diseñador | Estructura de contenido |
| Revisar y aprobar wireframe | Product Owner + equipo | Wireframe terminado |

### Entregables

- Wireframe desktop y mobile.
- Copy v1 de toda la landing.
- Estructura de headings para SEO.
- Lista de assets necesarios: capturas del producto, logos, iconos, testimonios, vídeos, etc.

**Criterio de salida:** no pasar a diseño visual hasta que estén aprobados la estructura, el CTA y el orden de los mensajes.

---

## Fase 3: Diseño visual y preparación técnica

**Duración:** Días 4–10  
**Objetivo:** trabajar en paralelo para no bloquear el desarrollo.

### Diseño

| Tarea | Responsable | Dependencias |
|---|---|---|
| Definir dirección visual | Diseñador + Product Owner | Wireframe aprobado |
| Crear sistema visual mínimo | Diseñador | Dirección visual |
| Diseñar desktop | Diseñador | Wireframe |
| Diseñar mobile | Diseñador | Diseño desktop inicial |
| Preparar estados de botones, formularios y errores | Diseñador | Componentes UI |
| Presentar diseño para aprobación | Diseñador | Diseño inicial |

### Desarrollo

| Tarea | Responsable | Dependencias |
|---|---|---|
| Crear repositorio y entorno de staging | Dev 1 | Stack definido |
| Configurar estructura de la landing | Dev 1 + Dev 2 | Estructura de contenido |
| Crear componentes reutilizables | Dev 2 | Wireframe y diseño inicial |
| Definir integración del formulario | Dev 1 | CTA y herramienta de captación |
| Configurar dominio, SSL y hosting | Dev 1 | Accesos disponibles |
| Preparar analytics y eventos | Dev 1 | Métricas definidas |

### Entregables

- Diseño final en Figma.
- Design tokens o guía visual mínima.
- Staging funcional con estructura base.
- Especificación de formulario y eventos de conversión.

---

## Fase 4: Desarrollo, integración y carga de contenido

**Duración:** Días 9–14  
**Objetivo:** tener una versión completa en staging.

| Tarea | Responsable | Dependencias |
|---|---|---|
| Implementar hero, navegación y CTA | Dev 2 | Diseño aprobado |
| Implementar secciones de beneficios y funcionalidades | Dev 2 | Diseño aprobado |
| Implementar screenshots, demo o vídeo | Dev 2 | Assets disponibles |
| Implementar FAQ y CTA final | Dev 2 | Copy aprobado |
| Integrar copy definitivo | Copywriter + Dev 2 | Copy v1 revisado |
| Integrar formulario con CRM/email | Dev 1 | Herramienta y credenciales |
| Configurar eventos de analytics | Dev 1 | Arquitectura de tracking |
| Configurar SEO técnico básico | Dev 1 + Copywriter | Copy y estructura final |
| Añadir favicon, Open Graph y metadatos | Dev 1 | Identidad visual |
| Optimizar imágenes y fuentes | Dev 2 | Assets finales |

### SEO mínimo recomendado

- Title y meta description.
- Un único H1 claro.
- H2 por sección.
- URLs y canonical correctos.
- Open Graph para compartir.
- Sitemap si aplica.
- Imágenes con `alt`.
- Buen rendimiento móvil.

### Entregable

- Landing completa en staging, con contenido y formulario funcionando.

---

## Fase 5: QA, revisión y optimización

**Duración:** Días 14–18  
**Objetivo:** detectar problemas antes del lanzamiento, especialmente en móvil y conversiones.

| Tarea | Responsable | Dependencias |
|---|---|---|
| Revisión funcional completa | Dev 1 + Dev 2 | Staging completo |
| Prueba de formulario y recepción de leads | Dev 1 + Product Owner | Integración terminada |
| Pruebas en Chrome, Safari y Firefox | Dev 2 | Página completa |
| Pruebas en móvil y tablet | Dev 2 | Diseño responsive |
| Revisión de accesibilidad básica | Dev 2 | Implementación completa |
| Revisión de copy y errores ortográficos | Copywriter | Copy integrado |
| Revisión visual contra Figma | Diseñador | Desarrollo completo |
| Revisión de analytics y conversiones | Dev 1 | Tracking implementado |
| Optimización de carga | Dev 1 + Dev 2 | Página funcional |
| Aplicar correcciones prioritarias | Developers | Resultados de QA |

### Checklist de QA

- El CTA principal funciona desde todas las secciones.
- El formulario valida errores correctamente.
- Los leads llegan al destino correcto.
- No hay enlaces rotos.
- No hay scroll horizontal en móvil.
- Los botones tienen estados hover, focus y disabled.
- La página carga correctamente en 4G.
- Analytics registra visitas, clics y conversiones.
- Los metadatos sociales se visualizan correctamente.
- No quedan textos temporales, lorem ipsum o assets de prueba.

---

## Fase 6: Preparación y lanzamiento

**Duración:** Días 17–20  
**Objetivo:** publicar con riesgo controlado y un día de margen.

| Tarea | Responsable | Dependencias |
|---|---|---|
| Congelar diseño y copy | Product Owner + Diseñador + Copywriter | QA principal |
| Resolver bugs críticos y altos | Dev 1 + Dev 2 | QA |
| Validación final de negocio | Product Owner | Versión candidata |
| Configurar dominio definitivo | Dev 1 | Accesos y hosting |
| Ejecutar smoke test en producción | Dev 1 + Dev 2 | Deployment |
| Verificar formulario y analytics en producción | Dev 1 | Página publicada |
| Lanzamiento público | Dev 1 | Aprobación final |
| Monitorizar primeras horas | Todo el equipo | Lanzamiento |
| Corregir incidencias post-lanzamiento | Developers | Monitorización |

**Recomendación:** hacer el lanzamiento público en el **día 19**, dejando el día 20 como buffer para incidencias, ajustes urgentes o problemas de configuración.

---

# Timeline de 4 semanas

## Semana 1 — Estrategia, estructura y primeros wireframes

| Día | Actividades principales |
|---|---|
| **Día 1** | Kickoff, objetivos, audiencia, CTA, métricas y restricciones técnicas |
| **Día 2** | Propuesta de valor, estructura de secciones, definición de formulario y analytics |
| **Día 3** | Wireframe inicial, arquitectura de contenido y titulares principales |
| **Día 4** | Revisión del wireframe, copy de beneficios y funcionalidades, setup técnico |
| **Día 5** | Aprobación de estructura, backlog técnico y primeros componentes |

**Hito:** estructura y dirección de mensajes aprobadas.

---

## Semana 2 — Diseño visual, copy y base de desarrollo

| Día | Actividades principales |
|---|---|
| **Día 6** | Dirección visual, copy v1 y sistema visual |
| **Día 7** | Diseño desktop, setup del frontend y componentes principales |
| **Día 8** | Diseño mobile, hero, navegación y CTA |
| **Día 9** | Revisión de diseño, desarrollo de secciones principales |
| **Día 10** | Aprobación visual, handoff y definición final de integraciones |

**Hito:** diseño visual aprobado y frontend avanzado.

---

## Semana 3 — Implementación e integración

| Día | Actividades principales |
|---|---|
| **Día 11** | Desarrollo de funcionalidades, beneficios y prueba visual del producto |
| **Día 12** | Implementación de FAQ, CTA final y formulario |
| **Día 13** | Integración con CRM/email, analytics y SEO técnico |
| **Día 14** | Carga de copy definitivo, assets y optimización de imágenes |
| **Día 15** | Staging completo y primera revisión interna |

**Hito:** landing funcional en staging.

---

## Semana 4 — QA, aprobación y lanzamiento

| Día | Actividades principales |
|---|---|
| **Día 16** | QA funcional, responsive, navegadores y accesibilidad |
| **Día 17** | Correcciones, revisión visual y validación de contenido |
| **Día 18** | Freeze de diseño/copy, smoke test y preparación de producción |
| **Día 19** | Lanzamiento público y monitorización inicial |
| **Día 20** | Buffer para incidencias, ajustes menores y documentación |

**Hito:** landing publicada y tracking verificado.

---

# Dependencias críticas

1. **Propuesta de valor → copy y diseño**  
   Sin una propuesta clara, se producirán revisiones constantes del hero y del CTA.

2. **Wireframe aprobado → diseño visual**  
   El diseñador no debería pulir visualmente una estructura todavía inestable.

3. **Diseño y copy aprobados → implementación final**  
   Los developers pueden crear la base antes, pero la maquetación definitiva depende de estos entregables.

4. **Credenciales del CRM o herramienta de formularios → integración**  
   Deben estar disponibles antes del día 10.

5. **Assets del producto → sección de demo o screenshots**  
   Si las capturas no están listas, conviene usar placeholders definidos, no esperar hasta el final.

6. **Aprobación del Product Owner → avance entre fases**  
   Las revisiones deben tener una ventana máxima de 24 horas.

7. **Staging completo → QA final**  
   No conviene hacer QA exhaustivo sobre una versión que todavía está cambiando.

---

# Distribución recomendada de la carga

## Diseñador

- 40% UX y estructura.
- 45% UI responsive.
- 15% revisión visual durante QA.

## Copywriter

- 30% posicionamiento y mensajes.
- 50% redacción de la landing.
- 20% SEO, revisión final y FAQ.

## Developer 1

- 25% arquitectura y setup.
- 30% formularios, CRM y analytics.
- 25% SEO técnico, deployment y dominio.
- 20% QA y resolución de bugs.

## Developer 2

- 60% implementación frontend.
- 20% responsive y performance.
- 20% QA, accesibilidad y correcciones visuales.

---

# Riesgos y cómo controlarlos

| Riesgo | Impacto | Mitigación |
|---|---:|---|
| Cambios de posicionamiento durante desarrollo | Alto | Aprobar propuesta de valor y copy del hero en la primera semana |
| Falta de capturas o assets del producto | Medio | Definir assets el día 2 y usar placeholders controlados |
| Integración del formulario tardía | Alto | Confirmar CRM, credenciales y destino antes del día 5 |
| Feedback contradictorio | Alto | Un único Product Owner toma la decisión final |
| Problemas de responsive descubiertos tarde | Medio | Diseñar y probar mobile desde la segunda semana |
| Demasiadas secciones o animaciones | Medio | Mantener el alcance en una landing de conversión |
| Lanzamiento sin datos | Alto | Configurar analytics y eventos antes del día 15 |
| Lanzar el último día sin margen | Alto | Objetivo de publicación en el día 19 y día 20 como buffer |

## Regla de alcance

Para llegar a tiempo, dejar fuera del lanzamiento inicial:

- Blog completo.
- Calculadoras complejas.
- Animaciones avanzadas.
- Personalización por segmentos.
- Integraciones no esenciales.
- Sistema de diseño completo.
- Múltiples variantes de landing.

Estas funcionalidades pueden entrar en una fase posterior basada en los datos reales de conversión.