# Claude Fable 5.1 — business_audit/teardown_competidor_sin_inventar

- model_id: `anthropic/claude-fable-5.1`
- success: True  | final: 5.07 | quality: 6.0
- latency_total: 55.286s | tokens_per_second: 62.2
- input_tokens: 288 | output_tokens: 3440

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

# Teardown del competidor

Antes de empezar: con estos datos puedo hacer **estimaciones con rangos**, no cifras. Voy a marcar cada cosa como **[DATO]**, **[INFERENCIA]** con nivel de certeza, o **[DESCONOCIDO]**.

---

## 1. Cuánto factura

### El problema central: "2.400 miembros" ≠ 2.400 pagando

**[INFERENCIA · certeza alta]** En plataformas tipo Skool, Circle, Mighty Networks, etc., el contador de portada suele incluir:
- Miembros gratuitos (si hay tier free, aunque tú no lo veas)
- Gente que entró y nunca canceló formalmente pero no paga (según plataforma)
- En algunos casos, miembros históricos acumulados

**[INFERENCIA · certeza media-alta]** Hay una señal fuerte de que el número está inflado respecto a pagantes: 2.400 / 60.000 seguidores = **4% de conversión a pago**. Eso es excepcional. Lo normal de audiencia social a membresía de pago está entre 0,5% y 2%. O el fundador es un vendedor extraordinario, o buena parte de esos 2.400 no paga $39.

### Escenarios de facturación mensual

| Escenario | % pagando | Precio efectivo* | MRR aprox. | ARR aprox. |
|---|---|---|---|---|
| Techo teórico | 100% | $39 | ~$94k | ~$1,1M |
| Optimista realista | 50% | $32 | ~$38k | ~$460k |
| **Base (mi apuesta)** | **25–35%** | **$30** | **~$18–25k** | **~$220–300k** |
| Pesimista | 15% | $28 | ~$10k | ~$120k |

*Precio efectivo < $39 porque casi siempre hay plan anual con descuento, precios de founding member congelados, cupones de lanzamiento, etc. **[DESCONOCIDO]** si existen, pero **[INFERENCIA · certeza alta]** de que existen porque es práctica casi universal.

**Mi estimación: $15k–40k MRR, con mayor probabilidad alrededor de $20–25k.** Certeza media-baja. El rango es ancho porque el dato clave (pagantes reales) no lo tienes.

---

## 2. Qué tan sano es el negocio

### Señales positivas
- **[DATO]** 12 cursos listados → hay producción acumulada, no es un lanzamiento reciente.
- **[DATO]** 60k seguidores → tienen canal de adquisición propio, no dependen de ads.
- **[INFERENCIA · certeza media]** Si llevan tiempo y siguen a $39, el precio probablemente funciona (si no convirtiera, lo habrían bajado o subido).

### Señales de alerta o ambiguas
- **[DATO]** 3 posts/semana en feed público. **[INFERENCIA · certeza media]** Para una comunidad de 2.400 personas, es cadencia **baja**. Puede significar: (a) la actividad real está en zonas privadas que no ves, o (b) la comunidad está más dormida de lo que el número sugiere. No puedes distinguir a) de b) desde fuera.
- **[DATO]** No se ve cuántos cursos están terminados. **[INFERENCIA · certeza media]** Listar 12 cursos sin mostrar estado suele correlacionar con que varios son "próximamente" o módulos a medias. Es una táctica común de percepción de valor. No es necesariamente deshonesto, pero inflaría la propuesta.
- **[DESCONOCIDO]** Churn. Es LA métrica de salud en membresías y no la puedes ver. Las comunidades de automatización tienen churn alto típico (5–10% mensual) porque la gente entra para resolver un problema concreto y se va.

### Dependencias de riesgo **[INFERENCIA · certeza alta]**
- **Persona única**: 60k seguidores del fundador, no de la marca. Si él se cansa, se enferma o pivota, el negocio se cae.
- **Plataforma**: están en una plataforma de terceros. Cambios de pricing o descubribilidad del proveedor les afectan.
- **Nicho volátil**: la automatización cambia rápido (herramientas nuevas cada mes). 12 cursos pueden quedar obsoletos en 12–18 meses si no los mantienen.

### Veredicto de salud
**[INFERENCIA · certeza baja-media]** Negocio probablemente **rentable y viable** (costes operativos de una membresía así son bajos: plataforma + tiempo del fundador + quizá 1–2 ayudantes), pero con señales de **comunidad menos activa de lo que aparenta** y fuerte dependencia del fundador. No parece un competidor en crecimiento explosivo; parece uno en meseta cómoda. Pero esto último es la parte más especulativa de todo el análisis.

---

## 3. Cómo les compites

### Lo que NO haría
- **Competir por precio.** Bajar a $19 solo señala menos valor y atraes al segmento que más churnea.
- **Copiar el catálogo.** 12 cursos es volumen; competir en volumen te pone en su terreno y ellos llevan ventaja.

### Donde probablemente son vulnerables **[INFERENCIA]**

**a) Actividad/comunidad real** (certeza media)
Si la comunidad está dormida, tu ángulo es *comunidad viva*: sesiones en vivo semanales, revisión de automatizaciones de miembros, canal de soporte con tiempo de respuesta visible. Es caro en tiempo, pero es exactamente lo que un fundador con 60k seguidores y 12 cursos probablemente ha dejado de hacer.

**b) Profundidad vs amplitud** (certeza media)
"Automatización" es amplio. Él cubre todo con 12 cursos. Tú puedes ganar un sub-nicho (automatización para X sector, o para una herramienta concreta, o para un rol) donde seas la referencia obvia. El especialista le gana al generalista en conversión dentro de su nicho.

**c) Resultados verificables** (certeza media-alta)
La mayoría de comunidades de automatización venden "aprende"; pocas venden "implementamos contigo" o muestran casos documentados. Si puedes mostrar outcomes concretos (ahorros de horas, flujos reales en producción), compites en otra dimensión.

**d) Riesgo-persona** (certeza alta)
Construye marca de producto, no de gurú. A medio plazo es más defendible y los clientes B2B lo valoran.

### Lo que SÍ deberías hacer ANTES de decidir estrategia

Paga un mes. $39 es la due diligence más barata que vas a hacer. Dentro mira:
1. **Miembros activos últimos 7/30 días** (la mayoría de plataformas lo muestran o lo puedes estimar por posts/comentarios).
2. **Fechas de entrada** de miembros recientes → te da ritmo de adquisición.
3. **Cuántos de los 12 cursos están completos** de verdad.
4. **Si existe tier gratuito** → resuelve de golpe la pregunta de facturación.
5. **Página de checkout** → verás plan anual, descuentos, garantías.
6. **Qué preguntan los miembros y qué NO les responden** → esas son tus oportunidades de producto.

Complemento gratis: Wayback Machine sobre su landing. Si hace 12 meses decía "1.800 miembros" y ahora "2.400", creces ~50/mes neto. Si decía "2.300", están estancados. Ese dato cambia completamente la lectura.

---

## Resumen de confianza

| Pregunta | Respuesta | Certeza |
|---|---|---|
| Factura | ~$15–40k MRR, probablemente ~$20–25k | Media-baja |
| Pagantes reales | Probablemente 25–50% del número visible | Media |
| Salud | Rentable pero en meseta, dependiente del fundador | Baja-media |
| Mejor ángulo competitivo | Comunidad activa + sub-nicho + outcomes, no precio | Media |

Si me traes lo que veas tras un mes dentro, puedo cerrar casi todos estos rangos a algo útil.