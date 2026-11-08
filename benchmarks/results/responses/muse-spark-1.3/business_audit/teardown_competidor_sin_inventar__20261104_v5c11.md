# Muse Spark 1.3 — business_audit/teardown_competidor_sin_inventar

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 5.67 | quality: 6.0
- latency_total: 36.451s | tokens_per_second: 108.6
- input_tokens: 191 | output_tokens: 3957

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

Te hago el teardown, pero con reglas claras porque con solo datos externos es fácil autoengañarse.

Voy a separar todo en 3 niveles y lo voy a marcar **siempre**:

**[DATO]** = me lo diste tú, lo tomo como observado. Certeza: Alta sobre lo que viste, pero no verificada por mí.
**[INFERENCIA]** = lo estoy estimando yo. Te pongo certeza Alta / Media / Baja.
**[DESCONOCIDO]** = no lo sabemos y es crítico.

### 1. Lo que SÍ sabemos vs lo que NO sabemos

**[DATO] Lo observado:**
1. Comunidad de pago sobre automatización en plataforma de membresía
2. Portada dice '2.400 miembros'
3. Precio visible: $39/mes
4. 3 posts/semana en feed público
5. Fundador con 60.000 seguidores
6. 12 cursos listados

**[DESCONOCIDO] Lo que nos falta y que cambia todo:**
- ¿2.400 = pagando ahora, o cuentas totales creadas históricamente? Certeza sobre este punto: **Nula**. Y es el dato más importante.
- ¿Hay plan anual oculto en checkout? No lo vemos.
- Tasa de churn, reembolsos, pagos fallidos, cuentas free/inactivas.
- Actividad *privada* (solo vemos feed público).
- De los 12 cursos, ¿cuántos completos vs placeholders?

> Conclusión inicial **[INFERENCIA - Certeza Media]**: Todo lo de abajo es un rango, no una auditoría. Cualquiera que te diga "facturan $X exactos" con estos datos te está mintiendo.

### 2. ¿Cuánto facturan? - Estimación por escenarios

Hago la matemática transparente para que veas el supuesto.

Cálculo ingenuo: 2.400 x $39 = **$93.600 / mes = $1.12M ARR**
**[INFERENCIA - Certeza Baja]** de que ese sea su cobro real. Casi nunca lo es. Las portadas inflan.

Te doy 3 escenarios **[INFERENCIA - Certeza Media-Baja, basado en benchmarks de comunidades de $29-49/mes]**:

**Escenario Optimista (creen lo que dicen):**
Supuesto: 100% de los 2.400 pagan $39 sin descuento.
MRR bruto: $93.600
MRR neto tras Stripe (~3%) + plataforma (~5-10%): ~$81k - $84k
Probabilidad: Baja. Yo le doy <15%.

**Escenario Base (mi apuesta):**
Supuesto: De los 2.400, ~75% paga mensual ($39), ~15% está en anual con -20% (=$31.2 efectivo/mes), ~10% son inactivos, free, cortesía o pagos fallidos.
Cálculo: (1.800 x 39) + (360 x 31.2) + (240 x 0) = $70.200 + $11.232 = **~$81.400 MRR bruto**
Anualizado: **~$977k ARR bruto, ~$840k-860k neto**
**[INFERENCIA - Certeza Media]**: Este es el rango típico en Skool/Circle/Whop cuando dicen "miembros".

**Escenario Pesimista (métrica vanity):**
Supuesto: "Miembros" = acumulados históricos. Solo 45-55% activos pagando.
Cálculo: 1.100 - 1.300 x $39 = **$43k - $51k MRR bruto**
**[INFERENCIA - Certeza Media]**: Muy común si llevan 2+ años operando. No han limpiado churn.

Mi rango de trabajo para ti: **$45k - $81k MRR bruto. Punto medio: ~$60k-65k.**
Nivel de confianza global en la estimación: **Bajo-Medio**. Necesito 1 dato más para afinar (ver punto 5).

Lo que sí te puedo decir con **[INFERENCIA - Certeza Alta]**: Su ARPU real es < $39. Si no muestran anual, o no lo tienen (dejan dinero en la mesa) o lo esconden en checkout (práctica estándar para subir LTV). En ambos casos, no cobran $39 puro.

### 3. ¿Qué tan sano es el negocio?

**A) Adquisición: Dependencia total del fundador**
**[DATO]** 60k seguidores -> 2.400 miembros = 4% conversión acumulada.
**[INFERENCIA - Certeza Media]**: Eso es bueno como acumulado histórico, pero peligroso hacia adelante. Es un negocio founder-led, no product-led.

Para mantenerse en 2.400 con un churn normal de membresía $39 (5-8% mensual **[INFERENCIA - Certeza Media, benchmark de categoría]**), necesitan reponer 120-192 bajas *cada mes* solo para no caer.
Eso es convertir 0.2% - 0.32% de sus 60k seguidores cada mes. **[INFERENCIA - Certeza Media]**: Factible hoy, pero si el alcance orgánico cae o el fundador para, se desinflan. Key-man risk alto.

**B) Retención / Engagement: Señal amarilla**
**[DATO]** 3 posts/semana en público + 12 cursos listados.
**[INFERENCIA - Certeza Baja, porque no vemos lo privado]**: 3 posts/semana es poco para una comunidad de pago sana. Las sanas suelen tener 1 post diario + respuestas + wins de usuarios. Si lo público es solo 3/semana, o bien 1) lo gordo pasa dentro (bien), o 2) están en modo mantenimiento (mal).
**[INFERENCIA - Certeza Media]**: 12 cursos suena bien en portada, pero si "no se ve cuántos están terminados" suele significar biblioteca incompleta o desactualizada. Eso eleva churn a mes 2-3, que es cuando la gente ya consumió lo básico.

Su LTV teórico si retienen 14 meses (churn 7%): $39 x 14.3 = ~$557 bruto. **[INFERENCIA - Certeza Baja]**: Bueno en papel, pero frágil si no hay nuevos cursos / soporte.

**C) Monetización: Dejan huecos**
**[DATO]** Solo se ve $39/mes.
**[INFERENCIA - Certeza Media]**: No tener anual visible es un error o una oportunidad perdida. Una comunidad sana convierte 20-30% a anual para asegurar cash y bajar churn. Si ellos no lo hacen, su churn es más volátil que el de un competidor que sí lo haga.

Veredicto salud: **Negocio cash-cow con margen bruto alto (>85% tras comisiones) [INFERENCIA - Certeza Alta], pero con retención probablemente mediocre y riesgo de plataforma/fundador [INFERENCIA - Certeza Media].** No es inexpugnable.

### 4. Cómo les compites (sin suicidarte en precio)

No compitas a $29 para quitarles gente. Es una trampa. Ataca donde son débiles.

**[RECOMENDACIÓN ESTRATÉGICA - no es un dato, es mi opinión, certeza variable]**

**1. No seas "otra comunidad de automatización". Sé específica.**
Ellos son generalistas. Tú gana por nicho de resultado: "Automatización para agencias que quieren entregar en 7 días" o "para e-commerce" o "para closers". Un generalista a $39 no puede defender un caso de uso vertical.

**2. Ataca sus 3 puntos débiles probables:**
a) Cursos incompletos -> Tú promete "12 plantillas listas para copiar-pegar + 1 build en vivo/semana", no "12 cursos".
b) Feed frío -> Tú vende "respuesta en <24h + revisión de tu automatización". La gente paga $39 por no sentirse sola, no por videos.
c) Sin anual -> Tú lanza $39/mes vs $390/año (2 meses gratis) + garantía 14 días. Les robas el LTV.

**3. Juega a distribución, no a features.**
**[INFERENCIA - Certeza Alta]**: No les vas a ganar con "más cursos". Les ganas con prueba: 3 builds públicos/semana en tu red social, teardown de automatizaciones reales, wins de alumnos con números. El fundador tiene 60k, tú no necesitas 60k, necesitas 1.000 fans con un dolor concreto.

Qué NO hacer:
- No bajes a $19. Señalas menor valor y atraes churners.
- No prometas "comunidad de 2.400". Promete "comunidad pequeña donde te conozco por nombre". Convierte su tamaño en defecto (impersonal).

### 5. Qué necesito para darte el número real

Si me pasas esto, te afino el MRR con **Certeza Media-Alta**:
1. ¿Plataforma? ¿Skool? En Skool el número suele ser miembros totales, no activos.
2. Captura de likes/comentarios promedio por post público. Si 2.400 miembros generan <15 comentarios/post = engagement <0.6% = **[INFERENCIA - Certeza Media]** comunidad fantasma.
3. Antigüedad (Wayback Machine) y ritmo de crecimiento del fundador (SocialBlade).
4. ¿Hay trial de $1 / 7 días? Cambia todo el cálculo.

Pásame 2-3 links de posts y te digo en 5 minutos si esos 2.400 son reales o vanity.

¿Quieres que te arme el modelo en hoja con los 3 escenarios + punto de equilibrio para robarles 200 miembros en 90 días?