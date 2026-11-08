# Fugu Max — business_audit/teardown_competidor_sin_inventar

- model_id: `sakana/fugu-max`
- success: True  | final: 2.75 | quality: 2.0
- latency_total: 24.128s | tokens_per_second: 99.7
- input_tokens: 266 | output_tokens: 2406

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

# Teardown provisional

**Conclusión rápida:** con estos datos no se puede saber cuánto factura realmente ni si el negocio es rentable. Sí se puede calcular un techo hipotético y mapear qué señales son prometedoras, pero “2.400 miembros” no equivale necesariamente a 2.400 suscriptores de pago.

## Lo observado frente a lo inferido

| Dato | Qué permite concluir | Certeza |
|---|---|---|
| La página muestra **2.400 miembros** | Hay una señal de escala, pero no sabemos si son miembros activos, de pago, históricos o una mezcla. | Alta sobre lo que muestra la página; baja sobre qué significa |
| Precio visible de **$39/mes** | Es el precio de lista público; no sabemos el ingreso medio real por cliente. | Alta sobre el precio mostrado |
| **3 posts públicos por semana** | El feed parece tener actividad frecuente; no demuestra participación o retención. | Media |
| Fundador con **60.000 seguidores** | Tiene una posible fuente de distribución propia. No sabemos el alcance ni cuántos seguidores convierten. | Alta sobre el número observado; baja sobre su impacto comercial |
| **12 cursos listados** | Hay amplitud de catálogo; no sabemos calidad, finalización ni resultados. | Alta sobre el listado; baja sobre el valor entregado |

## ¿Cuánto podría facturar?

Si **todos** los 2.400 miembros fueran suscriptores activos al precio completo de $39:

- **$93.600 al mes** de ingresos brutos recurrentes teóricos.
- **$1.123.200 al año** como ritmo anualizado, no como facturación anual comprobada.

Ese cálculo es un **techo bajo supuestos**, no una estimación de ingresos reales. No descuenta descuentos, planes anuales, impuestos, reembolsos, comisiones ni miembros gratuitos o inactivos.

Para mostrar cuánto cambia el resultado según la proporción que realmente pague:

| Proporción de pago supuesta | Miembros de pago | Ingreso bruto mensual teórico |
|---:|---:|---:|
| 10% | 240 | $9.360 |
| 25% | 600 | $23.400 |
| 50% | 1.200 | $46.800 |
| 75% | 1.800 | $70.200 |
| 100% | 2.400 | $93.600 |

**Confianza:** alta en la aritmética; baja en cuál de estos escenarios se acerca a la realidad. Sin saber qué incluye la cifra de miembros, el rango es demasiado amplio para dar una cifra única responsable.

## ¿Qué tan sano parece el negocio?

**Señales favorables, pero incompletas:**

- Un número visible de miembros y un precio mensual sugieren que han construido una oferta comercial reconocible.
- La audiencia del fundador puede reducir la dependencia de publicidad pagada, *si* convierte.
- El ritmo de publicación puede mantener la percepción de actividad.
- El catálogo amplio puede ayudar a cubrir distintos niveles o necesidades.

**Riesgos que no se pueden descartar:**

- **Retención:** una comunidad puede acumular altas y aun así perder miembros rápidamente.
- **Dependencia del fundador:** si su audiencia o presencia impulsa casi todas las ventas y la entrega, hay concentración de riesgo.
- **Actividad no equivale a valor:** publicaciones frecuentes y cursos listados no prueban que los miembros los terminen ni obtengan resultados.
- **Margen desconocido:** no conocemos costes de plataforma, soporte, producción, afiliados, personal ni adquisición.

**Veredicto:** parece haber señales de tracción y capacidad de distribución, pero la salud del negocio es **indeterminada** con la información disponible. Para evaluarla de verdad hacen falta, como mínimo, miembros de pago activos, ingresos netos, bajas mensuales, retención por cohortes, reembolsos, coste de adquisición y margen bruto.

## Cómo competir

No intentaría ganar por “más cursos”, “más publicaciones” o por rebajar los $39 sin más. Esas dimensiones son fáciles de imitar y no prueban que resuelvan mejor el problema del cliente.

1. **Elige un segmento más concreto.** Por ejemplo, automatización para un tipo de profesional, equipo o flujo de trabajo específico. El segmento debe salir de entrevistas y demanda observada, no solo de una idea atractiva.
2. **Vende un resultado, no una biblioteca.** Promete una mejora delimitada —por ejemplo, implementar un flujo útil en un plazo definido— y acompáñala de plantillas, ejemplos y pasos verificables.
3. **Reduce el tiempo hasta el primer éxito.** Un onboarding guiado, una ruta corta para empezar y sesiones de resolución de problemas pueden diferenciarte más que añadir contenido.
4. **Demuestra resultados.** Publica demostraciones y casos con contexto: qué proceso se automatizó, para quién y qué cambió. Evita afirmaciones de ahorro o rendimiento que no puedas verificar.
5. **Prueba la oferta antes de construirla entera.** Entrevista a potenciales clientes, ofrece una cohorte piloto y mide asistencia, activación, resultados y renovación. Eso te dirá si hay una brecha real.
6. **Construye distribución propia.** La audiencia del fundador es una ventaja para ellos; para competir, desarrolla canales que no dependan de una sola persona, como contenido buscable, alianzas o referencias.

### Mi lectura final

La amenaza competitiva más clara no es necesariamente “2.400 clientes de pago”: es la combinación potencial de **audiencia del fundador + precio accesible + comunidad activa**. Pero la conversión, la retención y la calidad de entrega siguen siendo incógnitas. Mi recomendación es buscar una necesidad específica que su oferta generalista atienda peor y validar una promesa más concreta antes de competir directamente en precio o volumen.