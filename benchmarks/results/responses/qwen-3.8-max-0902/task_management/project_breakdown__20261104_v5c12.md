# Qwen 3.8 Max 0902 — task_management/project_breakdown

- model_id: `qwen/qwen3.8-max-0902`
- success: True  | final: 7.67 | quality: 9.72
- latency_total: 292.945s | tokens_per_second: 45.2
- input_tokens: 127 | output_tokens: 13235
- judge_score: 4.8 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito lanzar una landing page para un nuevo producto SaaS de gestion de inventario. El lanzamiento es en 4 semanas. El equipo tiene 1 disenador, 2 developers y 1 copywriter. Desglosa el proyecto en fases, tareas, dependencias, responsables y un timeline realista.


## Respuesta completa

Aquí tienes un plan realista para lanzar la landing en **4 semanas** con **1 diseñador, 2 developers y 1 copywriter**. Está pensado para un equipo pequeño, con foco en llegar a lanzamiento sin bloqueos y con margen para QA.

---

# Plan de lanzamiento: Landing page para SaaS de gestión de inventario

## 1. Supuestos y alcance recomendado

Para que el timeline sea realista, asumo lo siguiente:

- El proyecto es una **landing page de una sola página**, orientada a conversión.
- El objetivo principal es uno de estos:
  - registro para prueba gratuita,
  - solicitud de demo,
  - lista de espera,
  - descarga de recurso si aplica.
- El equipo tiene disponibilidad suficiente durante estas 4 semanas.
- Existen o se consiguen rápido:
  - logo y guía de marca básica,
  - textos del producto,
  - capturas o mockups del producto,
  - acceso a dominio/hosting o plataforma de despliegue,
  - herramienta de formulario/CRM/email,
  - herramienta de analítica.
- No se incluye en estas 4 semanas:
  - blog completo,
  - multi-idioma completo,
  - sistema de A/B testing avanzado,
  - múltiples landings variantes,
  - integraciones complejas con backend del producto,
  - motion design muy avanzado,
  - CMS complejo si no es estrictamente necesario.

---

# 2. Equipo y responsables

Como no mencionas un project manager, conviene asignar un responsable de coordinación.

| Rol | Responsable sugerido | Responsabilidad principal |
|---|---|---|
| Diseñador | D | UX/UI, wireframes, diseño visual, assets, QA visual |
| Copywriter | C | Mensaje, copy de landing, SEO on-page, FAQ, textos legales básicos |
| Developer 1 | Dev 1 | Frontend, maquetación, performance, accesibilidad, deploy |
| Developer 2 | Dev 2 | Integraciones: formulario, CRM/email, analytics, SEO técnico, dominio/SSL |
| Coordinación del proyecto | Dev 1 o D | Seguimiento de timeline, bloqueos, prioridades y lanzamientos |

Recomendación: **Dev 1** puede ser el responsable de entrega técnica, mientras el **diseñador** lidera la parte visual y el **copywriter** lidera mensaje y conversión.

---

# 3. Objetivo de la landing

Antes de empezar, el equipo debe acordar una sola métrica principal.

Ejemplos para un SaaS de inventario:

- “Solicitar demo”
- “Crear cuenta gratis”
- “Unirse a la lista de espera”
- “Hablar con ventas”

Ejemplo de objetivo:

> Conseguir que visitantes del perfil ideal soliciten una demo o se registren para probar el producto.

KPIs mínimos:

- Visitas a la landing.
- Clics en CTA principal.
- Formularios enviados.
- Tasa de conversión: visitas → leads.
- Eventos de scroll y clic.
- Rendimiento: LCP, CLS, INP.
- Errores de formulario.

---

# 4. Estructura recomendada de la landing

Para un SaaS de gestión de inventario, una estructura efectiva puede ser:

1. **Hero**
   - Propuesta de valor clara.
   - Subtítulo con beneficio principal.
   - CTA principal.
   - Imagen/mockup del producto.

2. **Prueba social inicial**
   - Logos de clientes, integraciones o badges.
   - Si no hay clientes, usar integraciones, seguridad o “disponible próximamente”.

3. **Problema**
   - Dolores típicos:
     - quiebres de stock,
     - sobreventa,
     - inventario en hojas de cálculo,
     - falta de visibilidad en tiempo real,
     - errores en pedidos.

4. **Beneficios principales**
   - Control de stock en tiempo real.
   - Alertas de reposición.
   - Trazabilidad de movimientos.
   - Reportes y pronósticos.
   - Integraciones con ecommerce/ERP/POS.

5. **Cómo funciona**
   - 3 pasos simples:
     1. Conecta tus canales.
     2. Centraliza tu inventario.
     3. Automatiza alertas y reposición.

6. **Features destacadas**
   - Inventario multialmacén.
   - Alertas de stock bajo.
   - Órdenes de compra.
   - Reportes.
   - Roles y permisos.
   - API/integraciones.

7. **Casos de uso o segmentos**
   - Retail.
   - Ecommerce.
   - Distribución.
   - Almacenes pequeños/medianos.

8. **Testimonios, métricas o confianza**
   - Si no hay testimonios reales, usar beneficios medibles:
     - “Reduce quiebres de stock”
     - “Ahorra tiempo operativo”
     - “Evita ventas sin inventario”

9. **FAQ**
   - ¿Sirve para múltiples almacenes?
   - ¿Se integra con Shopify, WooCommerce, ERP, POS?
   - ¿Puedo importar datos desde Excel?
   - ¿Tiene alertas de stock?
   - ¿Hay prueba gratis o demo?
   - ¿Cómo funciona la seguridad?

10. **CTA final**
   - Repetir el CTA principal.
   - Mensaje de cierre orientado a acción.

11. **Footer**
   - Links legales.
   - Privacidad.
   - Términos.
   - Contacto.
   - Redes.
   - Copyright.

---

# 5. Fases del proyecto

## Fase 1: Descubrimiento y definición

**Duración:** Semana 1, días 1-2  
**Objetivo:** Alinear objetivo, audiencia, mensaje, alcance y restricciones técnicas.

| Tarea | Responsable | Dependencias | Entregable |
|---|---|---|---|
| Kickoff con objetivo, KPIs y alcance | Todos | Ninguna | Brief inicial |
| Definir público objetivo / ICP | C | Brief | Perfil de visitante |
| Definir propuesta de valor | C | Producto/stakeholders | Mensaje central |
| Definir CTA principal | Todos | Objetivo de negocio | CTA único |
| Definir secciones de la landing | D + C | Brief | Sitemap |
| Definir stack, hosting, dominio y analytics | Dev 1 + Dev 2 | Accesos | Decisión técnica |
| Identificar assets necesarios | D | Producto/marketing | Lista de assets |

**Hito:** Brief aprobado y alcance congelado.

---

## Fase 2: Arquitectura de información y wireframes

**Duración:** Semana 1, días 2-4  
**Objetivo:** Definir estructura de la página antes del diseño visual.

| Tarea | Responsable | Dependencias | Entregable |
|---|---|---|---|
| User flow: visita → CTA → formulario → thank you | D | Brief | Flujo |
| Wireframes desktop | D | Sitemap | Wireframes |
| Wireframes mobile | D | Wireframes desktop | Wireframes responsive |
| Definir jerarquía de contenido | C | Wireframes | Outline de contenido |
| Revisión de viabilidad técnica | Dev 1 + Dev 2 | Wireframes | Feedback técnico |
| Definir campos del formulario | C + Dev 2 | CTA y CRM | Formulario propuesto |

**Hito:** Wireframes aprobados.

---

## Fase 3: Copy y mensaje

**Duración:** Semana 1-2, días 2-10  
**Objetivo:** Crear los textos finales orientados a conversión y SEO básico.

| Tarea | Responsable | Dependencias | Entregable |
|---|---|---|---|
| Copy de hero y subtítulo | C | Propuesta de valor | Copy hero |
| Copy de problemas y beneficios | C | ICP | Sección de valor |
| Copy de features | C | Producto | Features claras |
| Copy de CTA | C | Objetivo | Botones y microcopy |
| FAQ | C | Producto/ventas | FAQ final |
| Meta title y meta description | C | Keywords | SEO básico |
| Textos para thank you page | C | CTA | Página de gracias |
| Textos legales básicos | C + legal | Privacidad | Footer legal |
| Alt text para imágenes | C | Diseño | Accesibilidad/SEO |

**Hito:** Copy final aprobado.

---

## Fase 4: Diseño visual

**Duración:** Semana 1-2, días 4-10  
**Objetivo:** Convertir wireframes en diseño final desktop y mobile.

| Tarea | Responsable | Dependencias | Entregable |
|---|---|---|---|
| Definir dirección visual | D | Marca | Moodboard/style |
| Diseño de sistema de componentes | D | Wireframes | Design system básico |
| Diseño desktop alta fidelidad | D | Wireframes + copy | Diseño desktop |
| Diseño mobile alta fidelidad | D | Desktop | Diseño mobile |
| Estados de formulario | D | Formulario | Estados UI |
| Estados hover/focus/error | D | UI | Estados interactivos |
| Preparar assets e imágenes | D | Producto | Assets exportables |
| Revisión de factibilidad técnica | Dev 1 | Diseño | Ajustes |

**Hito:** Diseño aprobado y congelado.

---

## Fase 5: Setup técnico

**Duración:** Semana 1-2, días 3-10  
**Objetivo:** Dejar lista la base técnica para desarrollar sin bloqueos.

| Tarea | Responsable | Dependencias | Entregable |
|---|---|---|---|
| Crear repositorio | Dev 1 | Stack | Repo |
| Configurar entorno de staging | Dev 1 | Repo | URL staging |
| Configurar dominio y DNS | Dev 2 | Accesos | Dominio listo |
| Configurar SSL | Dev 2 | Dominio | HTTPS |
| Configurar analytics | Dev 2 | Analytics | Tracking base |
| Configurar formulario/CRM/email | Dev 2 | Proveedor | Endpoint de prueba |
| Configurar deploy automático | Dev 1 | Repo | CI/CD |
| Crear estructura base de componentes | Dev 1 | Diseño | Base UI |

**Hito:** Entorno técnico funcionando.

---

## Fase 6: Desarrollo e implementación

**Duración:** Semana 2-3, días 8-15  
**Objetivo:** Construir la landing completa en staging.

| Tarea | Responsable | Dependencias | Entregable |
|---|---|---|---|
| Maquetación de secciones | Dev 1 | Diseño final | UI implementada |
| Responsive | Dev 1 | Diseño mobile | Landing responsive |
| Integración de copy final | Dev 1 | Copy final | Contenido real |
| Optimización de imágenes | Dev 1 + D | Assets | Imágenes livianas |
| Formulario | Dev 2 | CRM/email | Formulario funcional |
| Thank you page | Dev 1 | Diseño + copy | Página de gracias |
| Eventos de analytics | Dev 2 | KPIs | Eventos medibles |
| SEO técnico | Dev 2 | Meta tags | Meta tags, OG, canonical |
| Accesibilidad básica | Dev 1 | Diseño | Focus, labels, contraste |
| Performance | Dev 1 + Dev 2 | Assets | Carga rápida |
| Cookie banner si aplica | Dev 2 | Legal | Banner funcional |

**Hito:** Landing feature complete en staging.

---

## Fase 7: QA y optimización

**Duración:** Semana 3-4, días 14-18  
**Objetivo:** Detectar errores antes del lanzamiento.

| Tarea | Responsable | Dependencias | Entregable |
|---|---|---|---|
| QA visual desktop | D | Staging | Lista de ajustes |
| QA visual mobile | D | Staging | Lista de ajustes |
| QA de copy | C | Staging | Correcciones |
| QA de formulario | Dev 2 | Formulario | Leads llegando |
| QA de analytics | Dev 2 | Eventos | Eventos correctos |
| QA cross-browser | Dev 1 | Staging | Compatibilidad |
| QA responsive | Dev 1 + D | Staging | Mobile correcto |
| QA de performance | Dev 1 | Staging | LCP/CLS optimizados |
| QA accesibilidad | Dev 1 + D | Staging | Accesibilidad básica |
| QA legal | C + legal | Footer/cookies | Cumplimiento mínimo |
| Pruebas de seguridad básicas | Dev 2 | Formulario | Spam/protección |

**Hito:** Release candidate aprobada.

---

## Fase 8: Lanzamiento

**Duración:** Semana 4, día 18  
**Objetivo:** Publicar la landing de forma controlada.

| Tarea | Responsable | Dependencias | Entregable |
|---|---|---|---|
| Backup o versión estable | Dev 1 | Release candidate | Versión segura |
| Deploy a producción | Dev 1 | Aprobación | Landing live |
| Configurar DNS final si aplica | Dev 2 | Dominio | URL correcta |
| Smoke test en producción | Todos | Deploy | Landing funcionando |
| Verificar formulario en producción | Dev 2 | Formulario | Leads OK |
| Verificar analytics en producción | Dev 2 | Tracking | Eventos OK |
| Comunicar lanzamiento | C / negocio | Landing live | Anuncio interno/externo |

**Hito:** Landing publicada.

---

## Fase 9: Post-lanzamiento

**Duración:** Semana 4, días 19-20  
**Objetivo:** Monitorear, corregir y aprender.

| Tarea | Responsable | Dependencias | Entregable |
|---|---|---|---|
| Monitorear errores | Dev 1 + Dev 2 | Producción | Hotfixes |
| Revisar conversión inicial | C | Analytics | Insights |
| Revisar performance real | Dev 1 | Producción | Ajustes |
| Revisar leads recibidos | Dev 2 | CRM | Validación |
| Informe inicial | C + Dev 1 | Datos | Reporte de lanzamiento |
| Retrospectiva | Todos | Lanzamiento | Mejoras |

**Hito:** Informe inicial y próximos pasos.

---

# 6. Timeline realista de 4 semanas

Asumiendo **20 días hábiles**.

## Semana 1: Definición, mensaje y wireframes

| Día | Objetivo | Tareas principales | Responsable | Entregable |
|---|---|---|---|---|
| D1 | Kickoff | Objetivo, alcance, KPIs, CTA, responsables | Todos | Brief inicial |
| D2 | Mensaje base | ICP, propuesta de valor, dolores, beneficios | C | Mensaje central |
| D3 | Arquitectura | Sitemap, wireframes low-fi, campos de formulario | D + C | Wireframes v1 |
| D4 | Viabilidad | Revisión técnica, stack, repo, hosting | Dev 1 + Dev 2 | Setup inicial |
| D5 | Aprobación | Aprobar wireframes y outline de contenido | Todos | Alcance congelado |

**Hito de Semana 1:**  
Wireframes aprobados, copy outline aprobado y setup técnico iniciado.

---

## Semana 2: Diseño visual y copy final

| Día | Objetivo | Tareas principales | Responsable | Entregable |
|---|---|---|---|---|
| D6 | Diseño visual | Diseño desktop de secciones principales | D | Diseño v1 |
| D7 | Copy avanzado | Features, FAQ, CTA, meta tags | C | Copy v2 |
| D8 | Revisión conjunta | Revisión de diseño y copy | Todos | Feedback consolidado |
| D9 | Mobile y estados | Diseño mobile, formulario, estados hover/error | D | Diseño casi final |
| D10 | Congelación | Aprobación final de diseño y copy | Todos | Design freeze |

**Hito de Semana 2:**  
Diseño aprobado, copy final aprobado y componentes técnicos base listos.

---

## Semana 3: Desarrollo e integración

| Día | Objetivo | Tareas principales | Responsable | Entregable |
|---|---|---|---|---|
| D11 | Maquetación | Secciones principales desktop/mobile | Dev 1 | UI base |
| D12 | Integraciones | Formulario, endpoint, CRM/email | Dev 2 | Formulario funcional |
| D13 | Analytics y SEO | Eventos, meta tags, OG, favicon, schema básico | Dev 2 | Tracking/SEO técnico |
| D14 | Feature complete | Thank you page, contenido real, assets | Dev 1 + C | Staging completo |
| D15 | Code freeze | Correcciones menores, preparación de QA | Dev 1 + Dev 2 | Release candidate inicial |

**Hito de Semana 3:**  
Landing completa en staging, lista para QA.

---

## Semana 4: QA, lanzamiento y monitoreo

| Día | Objetivo | Tareas principales | Responsable | Entregable |
|---|---|---|---|---|
| D16 | QA general | Cross-browser, mobile, formulario, analytics | Todos | Lista de bugs |
| D17 | Correcciones | Fixes críticos, performance, accesibilidad | Dev 1 + Dev 2 | Release final |
| D18 | Lanzamiento | Deploy, smoke test, verificación de producción | Dev 1 + Dev 2 | Landing live |
| D19 | Monitoreo | Revisar errores, leads, eventos, performance | Todos | Hotfixes si aplica |
| D20 | Cierre | Informe inicial, aprendizajes, próximos pasos | C + Dev 1 | Reporte post-launch |

**Hito de Semana 4:**  
Landing lanzada y monitoreada.

---

# 7. Diagrama simplificado por semanas

| Semana | Foco principal | Entregable clave | Riesgo principal |
|---|---|---|---|
| Semana 1 | Definición y wireframes | Alcance aprobado | Falta de claridad en objetivo |
| Semana 2 | Diseño y copy final | Diseño y copy congelados | Cambios de mensaje tarde |
| Semana 3 | Desarrollo | Staging feature complete | Integración de formulario/CRM |
| Semana 4 | QA y lanzamiento | Landing live | Bugs de última hora |

---

# 8. Dependencias críticas

Estas son las dependencias que más pueden retrasar el proyecto.

## Dependencias de contenido

| Dependencia | Responsable | Cuándo se necesita |
|---|---|---|
| Propuesta de valor aprobada | C + negocio | Semana 1 |
| Descripción clara del producto | C + producto | Semana 1 |
| Capturas o mockups del producto | D / producto | Semana 1-2 |
| Testimonios, logos o pruebas sociales | C / negocio | Semana 2 |
| FAQ y objeciones comunes | C + producto/ventas | Semana 2 |
| Textos legales | C + legal | Semana 3 |

## Dependencias técnicas

| Dependencia | Responsable | Cuándo se necesita |
|---|---|---|
| Dominio y DNS | Dev 2 | Semana 1 |
| Hosting o plataforma de deploy | Dev 1 | Semana 1 |
| Cuenta de analytics | Dev 2 | Semana 1 |
| Proveedor de formulario/CRM/email | Dev 2 | Semana 2 |
| Acceso a APIs si aplica | Dev 2 | Semana 2 |
| Certificado SSL | Dev 2 | Semana 2-3 |

## Dependencias de aprobación

| Aprobación | Responsable | Fecha límite recomendada |
|---|---|---|
| Brief y objetivo | Negocio/producto | D2 |
| Wireframes | Producto/marketing | D5 |
| Copy final | Producto/marketing | D10 |
| Diseño final | Producto/marketing | D10 |
| Release candidate | Todos | D17 |
| Lanzamiento | Dev 1 + negocio | D18 |

---

# 9. Responsables por área

| Área | Responsable principal | Apoyo |
|---|---|---|
| Mensaje y conversión | Copywriter | Diseñador |
| UX y wireframes | Diseñador | Copywriter |
| Diseño visual | Diseñador | Dev 1 |
| Frontend | Dev 1 | Diseñador |
| Integraciones | Dev 2 | Dev 1 |
| SEO técnico | Dev 2 | Copywriter |
| SEO de contenido | Copywriter | Dev 2 |
| Analytics | Dev 2 | Copywriter |
| QA visual | Diseñador | Copywriter |
| QA técnico | Dev 1 + Dev 2 | Diseñador |
| Lanzamiento | Dev 1 | Dev 2 |
| Post-lanzamiento | Todos | Negocio |

---

# 10. Entregables finales

Al terminar las 4 semanas, el equipo debería entregar:

1. Landing page publicada.
2. Versión responsive para mobile y tablet.
3. Formulario funcional conectado a:
   - CRM,
   - email,
   - hoja de cálculo,
   - o herramienta de leads.
4. Thank you page.
5. Eventos de analytics configurados:
   - page_view,
   - cta_click,
   - form_start,
   - form_submit,
   - form_error.
6. Meta tags básicos:
   - title,
   - description,
   - Open Graph,
   - canonical,
   - favicon.
7. Checklist de performance revisada.
8. Checklist de accesibilidad básica.
9. Footer con links legales.
10. Documento breve de métricas iniciales y próximos pasos.

---

# 11. Reuniones recomendadas

Para no perder tiempo, sugiero pocas reuniones pero efectivas.

| Reunión | Frecuencia | Duración | Objetivo |
|---|---|---|---|
| Kickoff | Semana 1, D1 | 60 min | Alinear objetivo y alcance |
| Daily async | Cada día | 10-15 min | Bloqueos y avances |
| Revisión de wireframes | Semana 1 | 30-45 min | Validar estructura |
| Revisión de diseño/copy | Semana 2 | 60 min | Aprobar versión final |
| Demo técnica | Semana 3 | 30 min | Ver staging completo |
| QA review | Semana 4 | 45 min | Priorizar bugs |
| Go/No-Go launch | Semana 4, D17/D18 | 30 min | Decidir lanzamiento |

---

# 12. Riesgos principales y mitigación

| Riesgo | Impacto | Mitigación |
|---|---|---|
| Falta de claridad en el mensaje | Alto | Aprobar propuesta de valor en D2 |
| Cambios de copy tarde | Alto | Congelar copy en D10 |
| Cambios de diseño tarde | Alto | Design freeze en D10 |
| Falta de capturas del producto | Medio | Usar mockups o placeholders |
| Retraso en aprobación legal | Alto | Enviar textos legales en semana 2 |
| Integración con CRM compleja | Alto | Usar formulario simple primero |
| Problemas de performance | Medio | Optimizar imágenes y medir desde semana 3 |
| Bugs en mobile | Medio | QA mobile desde desarrollo |
| Falta de accesos | Alto | Pedir accesos el día 1 |
| Equipo part-time | Alto | Reducir alcance |

---

# 13. Plan de contingencia si hay retrasos

Si el proyecto se atrasa, reduce alcance antes de reducir calidad.

## Versión mínima viable de la landing

Si falta tiempo, lanza solo con:

- Hero claro.
- Propuesta de valor.
- CTA principal.
- 3 beneficios clave.
- 3-4 features principales.
- FAQ corta.
- Formulario funcional.
- Thank you page.
- Footer legal.
- Analytics básico.

## Qué recortar primero

1. Animaciones complejas.
2. Secciones secundarias.
3. Casos de uso extendidos.
4. Testimonios elaborados.
5. CMS.
6. Multi-idioma.
7. A/B testing.
8. Integraciones avanzadas.

## Qué no recortar

1. Mensaje claro.
2. CTA visible.
3. Formulario funcional.
4. Mobile correcto.
5. Performance aceptable.
6. Analytics mínimo.
7. Footer legal básico.

---

# 14. Checklist de lanzamiento

## Contenido

- [ ] Hero claro y comprensible.
- [ ] CTA principal visible arriba y abajo.
- [ ] Beneficios orientados al usuario.
- [ ] Features explicadas con lenguaje simple.
- [ ] FAQ actualizada.
- [ ] Copy sin errores ortográficos.
- [ ] Alt text en imágenes.

## Diseño

- [ ] Diseño desktop correcto.
- [ ] Diseño mobile correcto.
- [ ] Tablet revisada.
- [ ] Estados hover/focus/error.
- [ ] Imágenes optimizadas.
- [ ] Favicon visible.

## Desarrollo

- [ ] Landing carga sin errores.
- [ ] No hay errores en consola.
- [ ] Links funcionan.
- [ ] Botones funcionan.
- [ ] Formulario envía datos.
- [ ] Thank you page funciona.
- [ ] Protección anti-spam básica.
- [ ] HTTPS activo.

## Analytics

- [ ] Page view registrado.
- [ ] Clic en CTA registrado.
- [ ] Inicio de formulario registrado.
- [ ] Envío de formulario registrado.
- [ ] Error de formulario registrado.
- [ ] UTM parameters funcionan.

## SEO

- [ ] Title correcto.
- [ ] Meta description correcta.
- [ ] Open Graph correcta.
- [ ] Canonical correcta.
- [ ] Favicon.
- [ ] Sitemap si aplica.
- [ ] Robots.txt correcto.

## Performance

- [ ] LCP razonablemente bajo.
- [ ] CLS bajo.
- [ ] Imágenes comprimidas.
- [ ] Lazy loading en imágenes no críticas.
- [ ] Fuentes optimizadas.

## Legal

- [ ] Política de privacidad.
- [ ] Términos si aplica.
- [ ] Aviso de cookies si aplica.
- [ ] Checkbox de consentimiento si aplica.
- [ ] Footer con información legal.

---

# 15. Timeline ejecutivo resumido

| Semana | Objetivo | Hito clave | Responsable principal |
|---|---|---|---|
| Semana 1 | Definición, mensaje y wireframes | Alcance congelado | C + D |
| Semana 2 | Diseño final y copy final | Diseño y copy aprobados | D + C |
| Semana 3 | Desarrollo e integraciones | Staging feature complete | Dev 1 + Dev 2 |
| Semana 4 | QA, lanzamiento y monitoreo | Landing live | Todos |

---

# 16. Recomendación final

Para llegar bien en 4 semanas, la clave es:

1. **Congelar alcance al final de la semana 1.**
2. **Congelar copy y diseño al final de la semana 2.**
3. **No depender de integraciones complejas.**
4. **Hacer QA desde la semana 3, no al final.**
5. **Lanzar a mitad de semana**, idealmente miércoles, para tener jueves y viernes para monitorear y corregir.

Con este plan, el equipo puede lanzar una landing profesional, medible y orientada a conversión sin necesidad de extender el proyecto más de 4 semanas.