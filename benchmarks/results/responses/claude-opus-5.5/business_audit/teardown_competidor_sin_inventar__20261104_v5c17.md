# Claude Opus 5.5 — business_audit/teardown_competidor_sin_inventar

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 5.22 | quality: 6.0
- latency_total: 41.278s | tokens_per_second: 93.7
- input_tokens: 288 | output_tokens: 3866

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

# Teardown del competidor: comunidad de automatización a $39/mes

**Leyenda de certeza:**
- 🟢 **Dato**: lo viste directamente.
- 🟡 **Inferencia razonable**: deducción con base lógica, pero no verificada.
- 🔴 **Especulación**: hipótesis plausible con poco respaldo.

---

## 1. Lo que sabemos (y lo que NO)

| Dato observado | Certeza | Qué NO nos dice |
|---|---|---|
| 2.400 miembros | 🟢 | Cuántos pagan. Puede incluir gratuitos, pruebas, cuentas inactivas o miembros con precio antiguo. |
| $39/mes | 🟢 | Si hay plan anual, descuentos, cupones de lanzamiento o precio "legacy" para los primeros. |
| 3 posts/semana públicos | 🟢 | La actividad interna, que es lo que de verdad retiene. |
| Fundador con 60k seguidores | 🟢 | Cuánto tráfico convierte ni si hay otros canales (ads, afiliados, YouTube, SEO). |
| 12 cursos listados | 🟢 | Cuántos están completos, su calidad o si alguien los termina. |

**Conclusión honesta:** con estos datos no se puede saber cuánto facturan. Solo se puede acotar un rango.

---

## 2. Facturación estimada

**Techo matemático 🟢:** 2.400 × $39 = **$93.600/mes (~$1,12M/año)**. Es un máximo teórico, no una estimación.

**Escenarios 🟡:**

| Escenario | Supuesto | MRR bruto | ARR |
|---|---|---|---|
| Pesimista | 40% paga; precio medio $30 (anuales/legacy) | ~$29k | ~$350k |
| Base | 70% paga; precio medio $35 | ~$59k | ~$700k |
| Optimista | 95% paga; precio casi lleno | ~$89k | ~$1,07M |

**Del bruto al neto 🟡:** hay que restar comisiones de la plataforma y del procesador de pago (normalmente entre 3% y 10%), reembolsos y, si existen, comisiones de afiliados. Calcula un 5–15% menos.

**Ingresos que no ves 🔴:** consultoría, servicios "hecho para ti", patrocinios o un plan high-ticket oculto. En este tipo de negocio es frecuente que la comunidad sea la puerta de entrada y el dinero grande esté detrás. No hay evidencia, pero no lo descartaría.

**Mi apuesta, con certeza baja-media:** entre **$40k y $70k de MRR**.

---

## 3. Salud del negocio

### Señal interesante: la ratio miembros/seguidores 🟡
2.400 / 60.000 = **4%**. Si todos pagan, es una conversión alta para una audiencia social. Hay tres explicaciones posibles:
- **(a)** Audiencia muy cualificada y fiel. Sería una fortaleza.
- **(b)** Tienen otros canales de adquisición que no ves.
- **(c)** Una parte relevante de los 2.400 no paga.

Distinguir entre estas tres es la pregunta clave del teardown.

### La rueda del churn 🟡
Las comunidades de pago mensual suelen perder entre el 5% y el 10% de sus miembros al mes. Es un benchmark general, no un dato suyo.
- Con un 8% de churn, pierden unos **190 miembros al mes**.
- Para no decrecer necesitan **~190 altas mensuales**, casi todas desde el contenido del fundador.

Esto implica que el negocio probablemente depende mucho de que el fundador siga publicando.

### Riesgos estructurales

| Riesgo | Certeza | Razonamiento |
|---|---|---|
| Dependencia del fundador | 🟡 alta | Marca personal como principal canal visible |
| Equipo pequeño | 🟡 media | 3 posts/semana es un ritmo sostenible para 1–2 personas |
| Promesa de catálogo > entrega | 🔴 | 12 cursos sin indicador de completitud. Es un patrón común, pero no lo sabemos |
| Nicho generalista ("automatización") | 🟡 | Difícil diferenciarse, vulnerable a especialistas |
| Obsolescencia del contenido | 🟡 | Las herramientas de automatización cambian rápido y mantener 12 cursos al día es caro |

**Diagnóstico provisional:** probablemente es un negocio rentable con márgenes altos, pero frágil. La adquisición está concentrada en una persona y el churn exige alimentar el embudo sin parar. Certeza media.

---

## 4. Cómo verificar (lo más valioso que puedes hacer)

**Paga $39 y únete un mes.** Es la inteligencia competitiva más barata que vas a conseguir. Una vez dentro, revisa:

1. **Actividad real:** ¿cuántos miembros distintos publican o comentan por semana? Si son 30 de 2.400, la comunidad está muerta por dentro.
2. **Contador de miembros:** apúntalo cada semana durante 4–6 semanas para ver si crecen, se estancan o caen.
3. **Cursos:** ¿cuántos están completos? ¿Cuándo fue su última actualización?
4. **Checkout y cancelación:** ¿aparece un plan anual? ¿Hay oferta de retención al cancelar? Eso revela cuánto les preocupa el churn.
5. **Upsells:** ¿hay llamadas, mentorías o servicios premium?
6. **Onboarding:** ¿qué pasa en los primeros 7 días? Ahí se decide el churn.

**Fuera de la comunidad:**
- Usa la Wayback Machine para ver el histórico del contador de miembros y del precio.
- Observa con qué frecuencia el fundador promociona la comunidad en redes. Promoción agresiva y constante suele indicar presión de churn.
- Busca exmiembros (reseñas, Reddit, menciones) y pregúntales por qué se fueron.

---

## 5. Cómo competirles

Te doy direcciones, no una receta, porque **no sé cuál es tu situación**: audiencia, nicho, capacidad de producción, presupuesto.

**Lo que NO recomiendo:** competir solo por precio, por ejemplo a $19. Atraes al cliente con más churn y ellos pueden igualarte sin esfuerzo.

**Ángulos con más potencial 🟡:**

1. **Especialízate donde ellos son generalistas.** Por ejemplo, automatización para agencias, para e-commerce o para un software concreto. Un especialista le gana a un generalista en conversión y retención dentro de su nicho.
2. **Vende resultados, no catálogo.** Si su debilidad son 12 cursos a medias, tu propuesta puede ser plantillas listas, implementación guiada o "en 30 días tienes X funcionando". Menos contenido y más resultado.
3. **Ataca la retención, no la adquisición.** Si su comunidad es poco activa por dentro, dale a la tuya una estructura que la mantenga viva: retos, revisiones en vivo, cohortes. Eso se ve cuando estás dentro, no desde fuera.
4. **Diversifica la adquisición desde el día uno.** Su punto débil probable es depender de la marca personal. Si construyes SEO, alianzas o afiliados, eres más estable.
5. **Mantén el contenido actualizado.** "Todo actualizado a las versiones de este mes" es una ventaja real en un sector donde el contenido envejece rápido.

---

## Resumen

- **Facturación:** probablemente entre $40k y $70k MRR (🟡 certeza baja-media). Techo de ~$94k.
- **Salud:** rentable pero dependiente del fundador y del embudo constante (🟡 certeza media).
- **Acción inmediata:** únete un mes y mide la actividad real y el contador semanal. Eso convierte la mitad de este informe de 🟡 a 🟢.

Si me cuentas tu situación (si ya tienes audiencia, en qué nicho y qué puedes producir), afino la estrategia de competencia.