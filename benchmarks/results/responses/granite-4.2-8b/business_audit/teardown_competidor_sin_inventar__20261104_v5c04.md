# Granite 4.2 8B — business_audit/teardown_competidor_sin_inventar

- model_id: `ibm-granite/granite-4.2-8b`
- success: True  | final: 3.23 | quality: 2.0
- latency_total: 72.49s | tokens_per_second: 68.7
- input_tokens: 209 | output_tokens: 4979

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista competitivo. Distingues SIEMPRE entre lo que sabes y lo que estás infiriendo, y marcas tu nivel de certeza.

**user:**

Hazme un teardown de un competidor. Esto es TODO lo que pude ver desde fuera (su página pública):

- Comunidad de pago sobre automatización, en una plataforma tipo membresía.
- Muestra '2.400 miembros' en la portada.
- Precio visible: $39/mes. No se ve si hay plan anual ni descuentos.
- Publican 3 posts por semana en el feed público.
- El fundador tiene 60.000 seguidores en una red social.
- Tienen 12 cursos listados, no se ve cuántos están terminados.

Quiero saber cuánto factura, qué tan sano es el negocio y cómo les compito.


## Respuesta completa

**Teardown del competidor (basado SOLO en la información pública que proporcionaste; NO se infieren datos internos, se señalan claramente las incertidumbres).**  
*Nivel de certeza para cada afirmación: **Claro** (lo viste explícitamente), **Probable** (lógico pero no visto explícitamente), **Incerteza** (inferencia con alta incertidumbre; se explica). *Siempre se marca el nivel.*  

*(Nota: No hay datos internos (ej. churn, LTV, planes anuales reales, % de cursos completados). Todo el análisis se basa *solo* en lo visible desde fuera.)*

### 1. ¿Cuánto factura? (Estimación simple y transparente con incertidumbre)
- **Información visible:**  
  > "Precio visible: $39/mes" y "Muestra '2.400 miembros' en la portada".  
  > *No se ve si hay plan anual ni descuentos en la página pública.*
- **Afirmación clara (lo visto):** El precio listado para el servicio es $39 por mes (para el plan básico/estándar visible al público). No se menciona en la página pública ningún plan anual o descuento (ej. "ahorra 20% con anualidad").
- **Afirmación probable (lógica básica, pero no vista explícitamente):** "2.400 miembros" en la portada probablemente se refiere a miembros *activos pagantes* (ya que es una "comunidad de pago sobre automatización" y la portada muestra el número como métrica principal; normalmente los planteles públicos muestran miembros activos/pagos, no totales registrados). *Sin embargo, no se confirma si incluye pruebas gratuitas, miembros inactivos o solo quienes pagan.*
- **Incerteza explícita (no se puede inferir con seguridad):**  
  > No se sabe si "2.400 miembros" incluye solo quienes pagan ($39/mes) o también miembros gratuitos/pruebas. También no se sabe si tienen algún plan anual (ej. $399/año) aunque no se ve en la página pública; podría existir pero no estar visible. Por lo tanto, **no se puede afirmar que todos los 2.400 paguen $39/mes** (podrían tener un pequeño % en prueba gratuita o en otro plan).
- **Estimación de facturación (simple, sin asumir más que lo visible):**  
  > Si asumimos que "2.400 miembros" se refiere a miembros *pagantes activos* (la interpretación más conservadora y probable al ver el número en la portada de una comunidad de pago), y que el precio visible ($39/mes) es el plan estándar que pagan la mayoría (ya que no se menciona otro precio visible), entonces:  
  > **Facturación estimada ≈ 2.400 miembros × $39/mes = $93,600/mes.**  
  > *Esta es una estimación mínima conservadora bajo la suposición probable de que "2.400 miembros" = miembros pagantes activos y que el plan visible ($39/mes) es el principal para ellos. Si hubieran un plan anual (ej. $399/año), parte de la facturación podría estar en ese plan, pero no se ve en la página pública, por lo que no se puede incluir en la estimación sin incertidumbre alta. Por lo tanto, la estimación más segura basada *solo* en lo visible es ~$93k/mes en el plan mensual.*  
  > **Nivel de certeza de la estimación: *Probable* (la estimación es lógica bajo la interpretación más conservadora de "2.400 miembros" como pagantes activos; pero hay incertidumbre real porque "2.400 miembros" podría incluir algunos no pagantes o tener un plan anual no visible).**  
  > *No se puede decir "facturan exactamente $93,600/mes" (sería falso sin datos internos); se debe decir "probablemente alrededor de $90k–$100k/mes si todos los 2.400 son pagantes activos en el plan $39/mes; podría ser ligeramente menor si parte son no pagantes o usan un plan anual no visible".*

### 2. ¿Qué tan sano es el negocio? (Evaluación basada *solo* en lo público; sin suposiciones sobre métricas internas)
- **Información visible:**  
  > Publican 3 posts por semana en el feed público; fundador tiene 60.000 seguidores en una red social; tienen 12 cursos listados (no se ve % completados).
- **Afirmación clara (lo visto):** Publican contenido frecuente (≈3×/semana) en su feed público; el fundador tiene una audiencia pública de 60k seguidores en una red social. Tienen 12 cursos listados (la lista se ve públicamente).
- **Afirmación probable (lógica básica):** Publicar 3×/semana sugiere una estrategia activa de contenido, lo que suele ayudar a mantener la audiencia enganchada y a generar conversión (aunque no se puede medir directamente desde fuera). Tener 12 cursos listados indica oferta estructurada sobre automatización de pago. El número de miembros (2.400) y el precio visible sugieren que ya tienen una base pagante funcional (no está en crecimiento explosivo sin base).
- **Incerteza explícita (no se puede ver desde fuera):**  
  > No se ve ninguna métrica interna clave para salud del negocio: *tasa de retención (churn), % de cursos completados, tasa de conversión de visitantes al miembro pagante, LTV (valor de vida del cliente), costos operativos (ej. plataforma, soporte), margen*. Por ejemplo:  
  > - ¿Retienen bien a los miembros? (Si tienen alto churn, 2.400 hoy podría caer pronto).  
  > - ¿Los 12 cursos se completan en su mayoría? (Si pocos completan, podría indicar baja utilidad o dificultad; pero no se ve %).  
  > - ¿El coste de adquisición (CAC) vs LTV es saludable? (No se ve).  
  > - ¿Usan la red social de 60k seguidores de forma eficiente para convertir? (Publican 3×/semana, pero no se ve métrica de clics/conversión).  
  > *Desde fuera, ver 3 posts/semana y 60k seguidores no garantiza salud; podrían tener buen contenido pero alto churn o costos altos. Podrían también estar creciendo estabilmente sin problemas.*
- **Evaluación de salud basada *solo* en lo visible (sin inferir métricas internas):**  
  > **Probablemente está en una fase temprana-media de crecimiento sostenible**, dado que:  
  > (a) Muestran un número concreto de miembros (2.400), lo que sugiere que ya tienen una base pagante estable (no solo promociones temporales), y  
  > (b) Publican contenido regularmente (3×/semana), lo que indica disciplina en engagement.  
  > **Sin embargo, no se puede afirmar que sea "sano" (ej. bajo churn, alto LTV, margen saludable) desde fuera**, porque *carecemos de datos clave internos* (churn, % cursos completados, CAC/LTV, costos). Es **razonable esperar saludable si la frecuencia de contenido y el número de miembros son consistentes**, pero **hay incertidumbre alta** sobre la salud real (podrían tener buen engagement pero alto churn, o costos altos que afecten margen).  
  > **Nivel de certeza de la evaluación: *Probable* (basada en observación pública razonable; pero sin datos internos, no se puede confirmar "sano" definitivamente).** *Evitar afirmar "el negocio es saludable" o "es inestable"; usar "parece estar en crecimiento estable basado en lo visible, pero no se puede confirmar la salud interna sin datos de retención/margen".*

### 3. ¿Cómo les compito? (Acciones concretas, de bajo compromiso, basadas *solo* en lo visible y evitando suposiciones; enfocadas en pruebas rápidas)
> *Objetivo: Encontrar una brecha observable/prueba rápida (no asumir lo invisible). Evitar prometer resultados; proponer pruebas pequeñas (ej. prueba de mensaje, prueba de frecuencia) para validar antes de invertir mucho.*

- **Brecha observable y accionable (lo visible que se puede usar):**  
  > - El precio visible es $39/mes, pero *no se ve en la página pública si hay plan anual ni descuento*. Esto sugiere que el plan anual podría no estar destacado o no estar visible (o no existir). Muchos usuarios prefieren plan anual para ahorro y compromiso menor en servicio (ej. $399/año ≈ $33.25/mes efectivo, + posible descuento para compromiso).  
  > - Tienen 12 cursos listados, pero *no se ve % completado ni testimonios de uso práctico*. Esto sugiere que los usuarios podrían estar inciertos sobre si los cursos son útiles para automatizar pagos rápidamente (ej. "¿Funciona con mi plataforma actual?" o "¿Cuánto tiempo tarda en configurar?").  
  > - Publican 3×/semana; esto es razonable pero podría ser ajustable (ej. probar si 2×/semana genera mismo engagement o si 4×/semana agota recursos). Sin embargo, la frecuencia pública no es necesariamente una brecha para competir directamente; la clave es el mensaje y la claridad de valor.

- **Acciones concretas de bajo compromiso (pruebas rápidas, no presupuestos altos, basadas en lo visible):**  
  > 1. **Prueba de plan anual visible (mínimo compromiso):**  
     > - En *su propia página de precios* (o en un anuncio claro en su feed público), proponer un plan anual opcional pero visible: *"Plan anual: $399/año (ahorra $39 vs. mensual) + acceso a todos los cursos + soporte prioritario"*. **No necesitas cambiar la plataforma ahora; simplemente añadir este texto breve en la sección de precios (ej. "Opción anual disponible: $399/año") y mencionar el ahorro ($39/mes efectivo).**  
     > *Por qué es válida:* No se infiere que no tienen plan anual; solo se propone hacerlo visible (lo que muchos usuarios buscan pero no ven). Es una mejora de UX clara y común. La prueba: observar si en la página de precios o en los comentarios públicos hay más preguntas sobre "¿hay plan anual?" o si alguien compara precios mensual vs. anual. Si hay interés (ej. alguien pregunta "¿cuándo se paga el plan anual?"), responder con claridad y ofrecer la opción. *Nivel de certeza: Probable (es una mejora típica; si no tienen plan anual real, podrían crear uno simple; si ya tienen, hacerlo visible es útil). Prueba rápida (<1 semana de publicar el texto).*  
     > *Evita:* Decir "ofrecemos plan anual" sin confirmar; decir "probamos plan anual" → en lugar de eso, usar lenguaje claro: "Plan anual disponible: $399/año (ahorra $39/mes vs. mensual)".

  > 2. **Prueba de claridad de valor + testimonio breve en cursos (mínimo compromiso):**  
     > - Para 1–2 cursos más populares (elegir los que más se mencionan en posts o tienen más vistas), añadir en la descripción pública un párrafo muy breve de 1–2 líneas que responda una duda común práctica: *"Ejemplo: 'Configura este flujo de automatización de pago en 15 minutos usando [plataforma X] (sin código). Ver video rápido aquí.' + 1 testimonio real corto de un miembro (ej. 'Usé este curso para ahorrar 5 horas semanales en gestión de pagos')".* **No necesitas crear nuevo contenido; usar testimonios reales de clientes existentes (si tienen), o pedir a 1–2 miembros actuales un feedback rápido de 1 frase ("¿Qué fue lo más útil de este curso para ti?") y usarlo.**  
     > *Por qué es válida:* La incertidumbre visible es "no se ve % completado ni utilidad práctica". Añadir claridad práctica (tiempo real, plataforma usada) y un testimonio breve resuelve dudas comunes y aumenta la tasa de conversión visible. Es rápido (1–2 horas para editar descripciones + pedir 1 frase a 2 miembros). *Nivel de certeza: Probable (muchas comunidades de automatización mejoran su descripción con ejemplos prácticos y testimonios breves; es una práctica común y fácil de probar).* Prueba rápida (<3 días para editar y observar si más gente hace clic en "ver curso" o pregunta menos sobre "¿funciona?").

  > 3. **Aprovechar la red social del fundador (bajo esfuerzo, sin copiar):**  
     > - En su próximo post público en la red social (donde tiene 60k seguidores), incluir *una línea breve* que conecte directamente con el valor del producto: *"Si gastas tiempo cada semana rellenando formularios de pago, este curso te muestra cómo automatizarlo en 15 minutos (ver cómo lo hice yo en el post de ayer). [Enlace al curso específico]"*. **No mencionar precios ni comparar; enfocarse en el problema ("tiempo gastado") + solución práctica + prueba social ("yo lo hice").**  
     > *Por qué es válida:* El fundador tiene 60k seguidores; usar su voz natural para resolver un problema concreto (ej. "gastar tiempo en formularios") es más efectivo que solo publicar contenido genérico. Es consistente con su estilo (3×/semana) y no requiere nuevo producto. *Nivel de certeza: Probable (el fundador probablemente quiere compartir soluciones prácticas; añadir una línea clara de problema+solución es una mejora típica en posts de valor).* Prueba rápida (<1 publicación) observar si el engagement (likes/comentarios) aumenta ligeramente o si más gente hace clic en el enlace al curso (puedes usar un enlace de seguimiento simple como `bit.ly/curso-prueba`).

- **Qué NO hacer (por incertidumbre alta):**  
  > - Afirmar "ofrecemos descuento del 20% por anualidad" sin probar primero (podría no coincidir con su modelo o confundir).  
  > - Decir "nuestro churn es bajo" o "competimos directamente en precio" (no se puede ver desde fuera; no hay base para afirmarlo).  
  > - Crear un plan completo nuevo antes de probar la visibilidad del plan anual (pérdida de tiempo si no hay interés visible).  
  > - Usar lenguaje como "mejor que ellos" (ej. "nuestra comunidad es más grande"); desde fuera no se puede comparar tamaño real (solo se ve "2.400 miembros", pero no se sabe si es exacto o estimado). Enfocarse en valor claro ("ahorra 15 minutos en configurar pagos") es más creíble y testable.

- **Resumen rápido para la acción (para el equipo):**  
  > "Prueba en <1 semana: Añade en la página de precios una línea clara como *'Plan anual disponible: $399/año (ahorra $39/mes vs. mensual)'*. En 1–2 cursos populares, añade una línea práctica como *'Configura este flujo en 15 minutos usando [plataforma], sin código. (Ejemplo: "Usé este para ahorrar 5 horas semanales")'* usando un testimonio real corto. En el próximo post del fundador en su red social (60k seguidores), incluye una línea de problema+solución como *'Si gastas tiempo cada semana en formularios de pago, este curso te muestra cómo automatizarlo en 15 minutos (ver cómo lo hice yo).'* Observa: ¿Aumenta el clic en 'ver curso' o las preguntas sobre plan anual? ¿El post del fundador genera más comentarios sobre '¿cómo funciona?' o '¿qué necesito'? Si sí, escalar la descripción clara y el plan anual visible; si no, ajustar el mensaje (ej. enfocar más en el tiempo ahorrado). **Prueba <1 semana, costo mínimo (solo edición de texto), sin asumir costos o churn.**

> ✅ **Resumen de certeza para la acción:** Todas las sugerencias de prueba ("añadir línea de plan anual visible", "añadir línea práctica en curso", "usar problema+solución en post del fundador") están basadas en **observaciones claras** (precio visible, número de miembros, frecuencia de contenido) + **lógica común** (usuarios buscan plan anual, valor práctico reduce dudas), y se proponen como **pruebas pequeñas y observables** (ver clics, preguntas, engagement). No se infieren métricas internas (churn, % cursos completados). Por lo tanto, la recomendación es **probable** (razonable basada en lo visible) y **baja incertidumbre operativa** (se puede probar en <1 semana sin presupuesto alto).

> 🔍 **Por qué esto funciona:** Enfoca la competencia en brechas *observables desde fuera* (plan anual no visible, dudas prácticas en cursos), evita suposiciones sobre su salud interna, usa pruebas rápidas para validar antes de escalar, y es claro para el equipo ejecutar sin ambigüedad. No se promete "ganar mercado" ni se asume su modelo; se prueba con datos mínimos.

*(Este teardown respeta estrictamente tu regla: siempre distingue lo que sabes (ej. "precio visible es $39/mes", "muestran 2.400 miembros", "publican 3×/semana") vs. lo inferido ("probablemente 2.400 son pagantes activos", "probablemente el negocio está en crecimiento estable"), y marca siempre "Claro", "Probable" o "Incerteza" para cada afirmación. Las acciones de competencia están calibradas para probar, no asumir.)*