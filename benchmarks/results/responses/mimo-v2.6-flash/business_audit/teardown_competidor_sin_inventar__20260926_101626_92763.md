# MiMo V2.6 Flash — business_audit/teardown_competidor_sin_inventar

- model_id: `xiaomi/mimo-v2.6-flash`
- success: True  | final: 5.82 | quality: 6.0
- latency_total: 106.917s | tokens_per_second: 25.6
- input_tokens: 203 | output_tokens: 2737

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

# Teardown: Comunidad de automatización ($39/mes)

## 1. Qué sabemos (hechos, certeza alta)

| Dato | Fuente |
|---|---|
| Comunidad de pago en plataforma de membresía | Portada pública |
| "2.400 miembros" display | Portada pública |
| Precio $39/mes visible | Portada pública |
| 3 posts/semana en feed público | Observación directa |
| Fundador: 60.000 seguidores | Red social |
| 12 cursos listados | Portada pública |

**Lo que NO sabemos:** si hay plan anual, si hay descuentos, cuántos de esos 2.400 están pagando, cuántos cursos están terminados, churn, equipo, costos, si el contador de miembros es actual o histórico.

---

## 2. Estimación de facturación (escenarios, no punto)

El número clave es: **"2.400 miembros" ≠ 2.400 pagantes.** Es el error más común al leer estas páginas.

| Escenario | Miembros pagando | MRR | ARR |
|---|---|---|---|
| **Pesimista** — contador = signups históricos, 30-40% activos | 720–960 | $28k–$37k | **$340k–$450k** |
| **Medio** — 50-60% activos | 1.200–1.440 | $47k–$56k | **$560k–$670k** |
| **Optimista** — todos pagan, sin plan anual | 2.400 | $93.6k | **$1.12M** |

**Certeza: Baja-Media.** El rango es ancho porque dos incógnitas multiplican: tasa de pago real y existencia de plan anual.

**Ajuste si tienen plan anual** (típico 20-35% de descuento): si 40% de la base es anual, el ARPU efectivo cae de $39 a ~$33-34. Eso recorta ~15% cualquier escenario.

**Certeza media** en que el negocio está entre **$400k y $800k ARR**, sesgado hacia la mitad de ese rango. No es un negocio de $3M ni uno de $50k.

---

## 3. Salud del negocio

### Señales positivas
- **Modelo validado.** Precio de $39 está en el punto dulce: lo suficientemente alto para sostener soporte, lo suficientemente bajo para no requerir venta consultiva.
- **Top of funnel propio.** 60k seguidores es un activo real. Si convierte al 4% → 2.400 miembros. Eso es una máquina de adquisición que no depende de ads.
- **12 cursos = inventario.** Aunque estén a medias, es percepción de valor.

### Señales de alerta (infiero, certeza media)
- **3 posts/semana es poco para un negocio "de comunidad".** Un operador serio de comunidad publica diario o tiene miembros generando contenido. Dos lecturas posibles:
  - El feed público es solo marketing y lo real pasa en el área privada *(no lo puedo verificar)*.
  - La comunidad está infraalimentada → churn alto probable.
- **"12 cursos" sin indicación de completitud** es el patrón clásico de negocio que prioriza ancho sobre profundo. Muy común: se anuncian 12, 4-5 están terminados.
- **Contador de miembros sin calificar ("activos", "este mes")** sugiere que el número es acumulado. Si tuvieran engagement fuerte, lo mostrarían con esa cualificación.
- **Dependencia de un solo fundador-persona.** 60k seguidores = la marca es él. Riesgo de key-person y techo de crecimiento atado a su contenido.

### Lo que debería preocuparte si fuera tu negocio
No su facturación — su **retención**. Con $39/mes, necesitan ~14-18 meses de permanencia promedio para que LTV/CAC funcione bien con ads. Con un feed de 3 posts, apostaría a que el churn está en 5-8% mensual *(certeza baja, es inferencia basada en patrones del sector)*.

---

## 4. Cómo les compites

**No atacas el número de seguidores.** Ese moat no lo desarmas. Atacas donde su ejecución es débil:

| Eje | Su debilidad (inferida) | Tu jugada |
|---|---|---|
| **Profundidad** | 12 cursos, completitud dudosa | Menos cursos, todos terminados y con resultado demostrable. Vende "terminás esto y sabés X" vs. "tenés 12 cursos" |
| **Comunidad real** | Feed de 3 posts/semana | Comunidad densa: retos, templates compartidos, sesiones en vivo. Que se note la diferencia en 30 segundos al entrar |
| **Prueba social cualitativa** | Muestra cantidad (2.400), no resultados | Muestra transformaciones: casos, antes/después, workflows de alumnos |
| **Precio** | $39 es tu ancla | O $29 para entrar más barato con misma promesa, o $59+ si tu propuesta es claramente más profunda. No te quedes en $39 copiando |
| **Retención** | Probablemente débil | Garantía de resultados / cohortes con fechas de inicio = compromiso = menor churn |

**La jugada más fuerte:** si su comunidad es efectivamente laxa, **la retención es su talón de Aquiles y tu mejor arma**. Un competidor con 800 miembros que retiene al 92% mes a mes le gana a uno con 2.400 que pierde el 6% cada mes, en LTV y en reputación.

---

## 5. Qué investigar antes de decidir (plan de inteligencia)

1. **Wayback Machine** en su portada → evolución del contador de miembros y del precio. Si el precio subió, tienen pricing power. Si el contador estancó, tienen problema de crecimiento.
2. **Flujo de checkout** (entra hasta el paso de pago, no compres) → revela si hay plan anual, descuentos y el stack que usan.
3. **Engagement en sus posts públicos** → likes/comentarios vs. 60k seguidores. Ratio bajo = audiencia fría.
4. **Buscar empleos del equipo** → tamaño real del negocio.
5. **Buscar reseñas/reclamos** en redes y Trustpilot → el churn se queja en público.
6. **Lista de lecciones por curso** → cuántos cursos tienen realmente contenido.

---

**Resumen ejecutivo:** Facturación estimada entre **$400k y $800k ARR** (certeza media-baja). Negocio validado pero probablemente con problemas de retención y profundidad de contenido. Compites por **calidad de comunidad y profundidad de producto**, no por volumen de audiencia.