# Muse Wonder — business_audit/teardown_competidor_sin_inventar

- model_id: `meta/muse-wonder`
- success: True  | final: 5.29 | quality: 6.0
- latency_total: 32.403s | tokens_per_second: 84.2
- input_tokens: 191 | output_tokens: 2728

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

Aquí va el teardown, pero con una regla que voy a cumplir en todo el análisis:

**[HECHO]** = lo que me diste y se ve desde fuera. Certeza alta.
**[INFERENCIA]** = lo que deduzco con lógica/benchmarks. Certeza media/baja.
**[NO SABEMOS]** = imposible de saber sin entrar o sin datos internos.

Si mezclo esto, te voy a hacer competir contra un fantasma.

### 1. Resumen ejecutivo

**[INFERENCIA - Certeza Baja]** Es probablemente un negocio rentable en apariencia, con tracción real (no es humo de 50 miembros), pero **no podemos afirmar que factura ~$93k/mes ni que sea sano.**

Esa cifra es solo el techo teórico, no la realidad.

### 2. Lo que SABEMOS

**[HECHO - Certeza Alta]**
1.  Comunidad de pago sobre automatización en plataforma de membresía
2.  Dice "2.400 miembros" en portada
3.  Precio visible: $39/mes
4.  No hay plan anual visible
5.  Publican 3 posts/semana en feed público
6.  Fundador: 60.000 seguidores
7.  12 cursos listados, estado de finalización desconocido

Nada más. Todo lo demás es estimación.

### 3. ¿Cuánto factura? Modelo por escenarios

**[HECHO - Cálculo matemático, Certeza Alta]**
2.400 x $39 = **$93.600 / mes brutos = $1.123.200 / año**

Ese sería el caso si el 100% de esos 2.400 pagara $39 cada mes, hoy.

**[INFERENCIA - Certeza Baja]** Eso casi nunca pasa en comunidades. "Miembros" en portada suele incluir: miembros gratuitos, en trial, inactivos que no fueron depurados, miembros con plan anual con descuento, y bajas no eliminadas del contador público.

Por eso trabajo con escenarios:

| Escenario | % que realmente paga | Miembros de pago | MRR bruto estimado |
| :--- | :--- | :--- | :--- |
| **Pesimista** | 30% | 720 | **$28.080** |
| **Conservador** | 50% | 1.200 | **$46.800** |
| **Base** | 70% | 1.680 | **$65.520** |
| **Optimista (techo)** | 100% | 2.400 | **$93.600** |

**[INFERENCIA - Certeza Media]** Mi escenario más probable, sin más datos, es el de **$46k - $65k MRR bruto**. ¿Por qué? Porque una conversión de 2.400 pagadores desde 60.000 seguidores sería un 4% de conversión total, que es alta pero posible si lleva años. Si parte son gratuitos, la conversión real baja a 2-2,8%, mucho más típica.

**[NO SABEMOS]** Comisiones de Stripe/plataforma, impuestos, reembolsos, % en anual (si existe por dentro), y coste de adquisición. El ingreso neto podría ser 5-15% menor solo por fees de pago.

**Conclusión sobre facturación: No sabemos la cifra. Sabemos el rango plausible. Certeza Baja.**

### 4. ¿Qué tan sano es el negocio?

No se puede diagnosticar salud con estos 7 datos. Sería inventar.

**Señales positivas:**
**[INFERENCIA - Certeza Media]** 2.400 miembros indica que el fundador supo convertir audiencia. No es un lanzamiento fallido.
**[INFERENCIA - Certeza Media]** 3 posts/semana públicos sugiere constancia operativa. No parece abandonado.
**[INFERENCIA - Certeza Baja]** $39/mes es un precio de volumen, no premium. Eso suele buscar escala, no pocos clientes de alto valor.

**Señales de riesgo / banderas amarillas:**
**[INFERENCIA - Certeza Baja]** 12 cursos es mucho. En comunidades, eso suele significar una de dos: 1) mucho valor percibido, o 2) dispersión y cursos a medias para justificar el cobro mensual. Como no sabemos si están terminados, es un riesgo.
**[INFERENCIA - Certeza Baja]** Dependencia total del fundador (60k seguidores son suyos, no de la marca). Si él deja de publicar, la adquisición se frena.
**[INFERENCIA - Certeza Baja]** A $39/mes, el negocio es muy sensible al churn. Necesita reponer cientos de bajas al mes solo para mantenerse plano.

**[NO SABEMOS - y es lo que define la salud]**
1.  Churn mensual: ¿Se va el 5% o el 15% al mes? Eso cambia todo.
2.  Actividad interna: ¿Comentan 500 personas o 20?
3.  CAC: ¿Los miembros vienen orgánicos de sus 60k o paga ads?
4.  Margen: ¿Es él solo o tiene equipo de soporte/moderación?
5.  Retención a 90 días: Clave en comunidades de automatización, donde la gente entra por una herramienta y se va.

**Conclusión sobre salud: Indeterminable. Certeza: Nula con estos datos.** Solo podemos decir que tiene tracción de adquisición, no que tenga retención.

### 5. Cómo competirle (sin copiar sus suposiciones)

No compitas contra sus 2.400 miembros ni sus 12 cursos. Compite contra sus probables debilidades.

**Estrategia 1: No seas "otra comunidad de automatización". Sé el resultado concreto.**
**[INFERENCIA - Certeza Media]** Él es generalista (12 cursos = amplio). Tú gana por nicho: "Automatización para clínicas dentales", "para agencias de 5-10 personas", "para e-commerce en Shopify". A $39 generalista, tú puedes cobrar $59-$79 especialista porque el ROI es más claro.

**Estrategia 2: Ataca la posible sobrecarga de contenido.**
**[HIPÓTESIS A VALIDAR - Certeza Baja]** Si sus cursos están incompletos o son demasiado largos, tu promesa no es "12 cursos", es "Implementa tu primera automatización que ahorra 5h/semana en 14 días, con revisión en vivo". La gente no renueva por catálogo, renueva por progreso.

**Estrategia 3: Ataca el modelo Founder-Dependent.**
**[INFERENCIA - Certeza Media]** Con 3 posts públicos/semana de él, dentro probablemente todo depende de él. Tú puedes diferenciarte con: soporte en <24h, llamadas de implementación (no solo Q&A), y miembros expertos que no sean el fundador. Eso escala mejor y retiene más.

**Lo que NO haría:**
No bajaría el precio a $29 para "robarle" clientes. **[INFERENCIA - Certeza Alta]** En comunidades, competir por precio atrae al cliente con mayor churn y menor compromiso. Si él realmente está en $50k+ MRR, puede aguantar una guerra de precios mucho más que tú empezando.

### 6. Qué necesitaríamos para subir la certeza

Si consigues esto (de forma pública y ética), pasamos de especular a saber:

1.  Reseñas públicas fuera de su página (Trustpilot, Reddit, X, YouTube)
2.  ¿El contador de miembros sube/baja en 30 días? Anótalo 1 vez/semana.
3.  Entrar 1 mes como cliente: churn visible, actividad real, cursos terminados, velocidad de soporte. Esto solo te da la foto interna, no su facturación.
4.  Comentarios de ex-miembros: ¿por qué se fueron?

**Mi recomendación final:**
Asume que factura entre **$47k y $66k MRR brutos [Certeza Baja]**, que tiene buena adquisición pero retención desconocida, y construye tu oferta en un nicho + implementación guiada donde un catálogo de 12 cursos no pueda competir.

¿Quieres que te haga la tabla de seguimiento de 30 días para monitorizar si está creciendo o está estancado?