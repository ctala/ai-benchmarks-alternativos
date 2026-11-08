# GPT-6 Astra — task_management/project_breakdown

- model_id: `openai/gpt-6-astra`
- success: True  | final: 7.69 | quality: 9.8
- latency_total: 44.439s | tokens_per_second: 45.0
- input_tokens: 69 | output_tokens: 1998
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundiza adecuadamente en la planificación del proyecto, ofreciendo una guía práctica y detallada para un emprendedor.

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito lanzar una landing page para un nuevo producto SaaS de gestion de inventario. El lanzamiento es en 4 semanas. El equipo tiene 1 disenador, 2 developers y 1 copywriter. Desglosa el proyecto en fases, tareas, dependencias, responsables y un timeline realista.


## Respuesta completa

## Plan de lanzamiento: 4 semanas

El plazo es viable si se mantiene un alcance acotado y se trabaja en paralelo: **copy y diseño desde la primera semana; desarrollo desde la segunda; última semana reservada principalmente para validar y lanzar**.

### Supuestos de planificación
- Son **20 días laborables**, con disponibilidad del equipo durante esas cuatro semanas.
- Se construye una landing, **no el producto SaaS ni un onboarding completo**.
- Habrá un único objetivo principal: solicitar una demo, registrarse o entrar en lista de espera. Se decide el día 1.
- Tú actúas como responsable de producto y apruebas entregables en un máximo de 24 horas.
- Dominio, hosting, identidad visual y herramienta de captación están disponibles o se resuelven durante la primera semana.

## 1. Alcance para llegar a tiempo

**Imprescindible para el lanzamiento**
- Una landing responsive con propuesta de valor, beneficios, funcionalidades principales, imágenes del producto, preguntas frecuentes y CTA.
- Formulario o enlace de registro funcional, con confirmación y entrega correcta del lead.
- Analítica de visitas y conversiones.
- SEO básico, accesibilidad esencial, rendimiento y pruebas en móvil.
- Información de privacidad y gestión del consentimiento, según las herramientas y normativa aplicables.

**Fuera del alcance inicial**
- Blog, múltiples idiomas, calculadoras interactivas, animaciones complejas y experimentos A/B.
- Integraciones a medida si existe una alternativa estándar.
- Testimonios, cifras o logotipos de clientes que no estén verificados y autorizados.

## 2. Responsabilidades

| Rol | Responsabilidad principal |
|---|---|
| **Diseñador** | Estructura visual, wireframes, diseño responsive, recursos gráficos y revisión visual |
| **Developer 1** | Frontend, componentes, responsive, SEO técnico y rendimiento |
| **Developer 2** | Entornos, despliegue, formulario/integraciones, analítica y coordinación de QA |
| **Copywriter** | Mensajes, textos, CTA, microcopy, metadatos y revisión editorial |
| **Tú / responsable de producto** | Alcance, validación de afirmaciones, decisiones comerciales y aprobación de lanzamiento |

Cada tarea tiene un responsable principal, aunque puede requerir apoyo de otros.

## 3. Fases, tareas y dependencias

*D1–D20 son días laborables. Las ventanas se solapan porque el equipo trabaja en paralelo; no representan dedicación completa de todos los roles.*

| ID | Fase / tarea | Ventana | Responsable | Dependencias / resultado |
|---|---|---|---|---|
| 1 | Definir público, problema, oferta, CTA y criterio de éxito | D1 | Tú + copywriter | Brief aprobado; objetivo de conversión único |
| 2 | Confirmar alcance, stack, dominio, hosting, CRM y accesos | D1–D2 | Dev 2 | Brief; decisiones técnicas y proveedores resueltos |
| 3 | Recopilar funcionalidades, capturas, precios y pruebas comerciales disponibles | D1–D3 | Copywriter, con tu apoyo | Información real del producto; no inventar beneficios demostrables |
| 4 | Crear estructura de contenidos y wireframe | D2–D3 | Diseñador | 1; revisión conjunta con copywriter |
| 5 | Redactar primera versión del copy y microcopy del formulario | D2–D4 | Copywriter | 1 y 3; alineación con 4 |
| 6 | Aprobar estructura, mensajes y CTA | D5 | Tú | 4 y 5; **hito de cierre de alcance** |
| 7 | Diseñar desktop y móvil, componentes y estados del formulario | D4–D7 | Diseñador | 4 y borrador de 5; cierre tras 6 |
| 8 | Preparar repositorio, staging, despliegue y configuración segura | D3–D5 | Dev 2 | 2; entorno listo para construir |
| 9 | Construir estructura frontend y componentes base | D6–D8 | Dev 1 | 6 y 8; entrega progresiva de 7 |
| 10 | Implementar secciones, responsive y recursos optimizados | D8–D12 | Dev 1 | 7 y 9; landing completa en staging |
| 11 | Integrar formulario, validación, antispam, CRM y confirmaciones | D6–D10 | Dev 2 | 2, 6 y 8; estados visuales de 7 para el acabado |
| 12 | Configurar analítica, eventos y consentimiento cuando corresponda | D10–D12 | Dev 2 | 9 y 11; medición sin duplicados ni datos personales innecesarios |
| 13 | Cerrar textos, FAQ, metadatos y revisión factual/legal | D6–D9 | Copywriter | 6; validación tuya y legal si procede |
| 14 | Integrar contenido final, SEO y ajustes de accesibilidad/rendimiento | D12–D14 | Dev 1 | 10 y 13; apoyo de dev 2 |
| 15 | QA funcional, visual, editorial y multidispositivo | D13–D16 | Dev 2 coordina; participa todo el equipo | 10–14, según estén disponibles |
| 16 | Corregir errores y repetir pruebas de los cambios | D15–D17 | Ambos developers | 15; diseñador y copywriter validan sus áreas |
| 17 | Aceptación final y decisión de lanzamiento | D18 | Tú | 16; checklist aprobado, sin bloqueos críticos |
| 18 | Margen para imprevistos y ensayo de despliegue/reversión | D19 | Ambos developers | 17; versión lista para producción |
| 19 | Publicar, verificar y monitorizar | D20 | Dev 2; dev 1 de apoyo | 18; aprobación tuya antes de activar campañas |

## 4. Timeline semanal e hitos

| Semana | Foco | Resultado al cierre |
|---|---|---|
| **1 · D1–D5** | Estrategia, estructura, copy inicial y preparación técnica | Alcance y mensajes aprobados; staging listo |
| **2 · D6–D10** | Diseño final, desarrollo e integración de captación | Diseño cerrado, landing avanzada y formulario integrado |
| **3 · D11–D15** | Completar implementación, medición y primeras pruebas | Versión completa en staging; incidencias priorizadas |
| **4 · D16–D20** | Correcciones, aceptación, margen y lanzamiento | Aprobación D18, colchón D19 y publicación D20 |

**Ruta crítica:** brief → estructura y mensajes aprobados → diseño suficiente para implementar → landing completa → QA y correcciones → aprobación → publicación.

**Dependencia externa más delicada:** accesos y configuración de CRM/formulario. Debe resolverse en la primera semana para no bloquear la captación.

## 5. Criterios para autorizar el lanzamiento

Antes de publicar, comprobar que:

- El CTA funciona y cada lead llega al destino correcto; se han probado éxito, error y envío duplicado.
- No hay errores críticos en móvil ni en los navegadores acordados.
- El formulario tiene etiquetas claras, navegación por teclado y errores comprensibles.
- La conversión se registra correctamente y no se cuentan envíos fallidos.
- Están configurados título, descripción, imagen social e indexación de producción; staging no se indexa.
- La carga se ha revisado en móvil y se han corregido los problemas importantes.
- Privacidad y consentimiento están resueltos según corresponda.
- Hay una versión anterior o procedimiento de reversión disponible.

El D20, **publicar primero y activar campañas después de verificar producción**. Monitorizar formularios, errores y conversiones durante las primeras horas, dejando asignada la revisión del siguiente día laborable.

## 6. Cómo proteger el plazo

- **Reunión diaria de 15 minutos** para bloqueos y revisiones concretas en D3, D5, D7, D14 y D18.
- Tras D5, cualquier ampliación debe sustituir una tarea equivalente o pasar a después del lanzamiento.
- Si hay retrasos, recortar primero animaciones, secciones secundarias y acabados no esenciales; **no recortar pruebas del formulario, privacidad ni verificación de conversiones**.
- El D19 es margen real: no debe llenarse anticipadamente con nuevas funcionalidades.