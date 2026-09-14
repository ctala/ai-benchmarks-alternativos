# Fugu Max — business_strategy/elegir_negocio_con_dependencia_oculta

- model_id: `sakana/fugu-max`
- success: True  | final: 8.4 | quality: 10.0
- latency_total: 21.659s | tokens_per_second: 80.3
- input_tokens: 371 | output_tokens: 1740

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres asesor de fundadores. Eliges por lo que se puede EJECUTAR con los activos actuales, no por el tamaño del mercado en una diapositiva.

**user:**

Tengo que elegir en qué me enfoco los próximos 3 meses. Soy uno solo, 4 horas al día, y necesito ingresos ANTES de que se me acabe el colchón (me quedan 3 meses de caja).

OPCIÓN A — Vender datos vía API a empresas.
  Mercado: enorme. Ticket: $500-2.000/mes por cliente.
  Requisito: contratos B2B con empresas. Mi ciclo de venta B2B histórico es de 5 a 7 meses desde el primer contacto hasta el cobro.
  Producto: habría que construirlo (~6 semanas).

OPCIÓN B — Marca blanca de mi tecnología para agencias.
  Mercado: mediano. Ticket: $300/mes.
  Requisito: necesito 3 casos de éxito documentados para que alguien me compre. Hoy tengo 0.

OPCIÓN C — Contenido patrocinado en el medio que ya opero.
  Mercado: chico. Ticket: $400-800 por pieza.
  Requisito: ya tengo el tráfico y la audiencia. Ya me escribieron 2 marcas preguntando precios el mes pasado (no les respondí).
  Producto: no hay que construir nada.

¿Cuál agarro? Justifica.


## Respuesta completa

## Elige la opción C: contenido patrocinado

No porque sea el mercado más grande, sino porque es la única con una probabilidad razonable de generar caja dentro de 3 meses.

### Comparación

| Criterio | A: API | B: Marca blanca | C: Patrocinados |
|---|---:|---:|---:|
| Tiempo hasta poder vender | 6 semanas de construcción | Requiere 3 casos | Inmediato |
| Señal de demanda actual | No mencionada | 0 compradores/casos | 2 marcas preguntaron precios |
| Ciclo de venta | 5–7 meses | Desconocido | Probablemente días/semanas |
| Dependencia de nuevos activos | Producto + contratos B2B | 3 casos de éxito | Audiencia y tráfico ya existentes |
| Probabilidad de cobrar antes de 90 días | Baja | Baja/media | Alta |

La opción A es especialmente peligrosa: consumirías la mitad de tu runway construyendo algo y luego intentarías venderlo con un ciclo histórico de 5–7 meses. Aunque el mercado sea enorme, no encaja con tu restricción principal: **necesitas ingresos antes de que se acabe la caja**.

La opción B tiene sentido como segundo paso, pero hoy estás bloqueado por la falta de casos. No debes invertir tres meses intentando crear las condiciones para venderla cuando ya tienes una oferta más vendible.

## Qué haría

### En las próximas 24 horas

Respondería a las dos marcas:

> “Perdón por la demora. Sí estamos abriendo colaboraciones patrocinadas. Tenemos formatos desde $X, con distribución a nuestra audiencia, [entregables concretos] y reporte de resultados. Si te interesa, te envío las opciones y disponibilidad para este mes.”

Usaría inicialmente:

- Pieza individual: **$600–800**
- Paquete de 3 piezas: **$1.500–2.000**
- 50% por adelantado o pago completo antes de publicar
- Plazo de entrega definido
- Reporte básico de alcance, clics e interacción
- Identificación clara como contenido patrocinado para proteger la confianza de la audiencia

No empezaría bajando el precio. Ya hubo intención de compra; primero hay que convertirla.

### Durante la primera semana

Crear solo lo imprescindible:

1. Media kit de una página.
2. Datos de audiencia, tráfico y engagement.
3. Tres ejemplos de formatos patrocinables.
4. Precios y calendario disponible.
5. Contrato simple y enlace de pago.
6. Seguimiento a las dos marcas y contacto con 10–20 marcas similares.

Tu objetivo no es “validar la idea”. Es **cobrar el primer patrocinio en 14 días**.

### Durante los meses 2 y 3

- Convertir cada entrega en un caso de resultados.
- Vender paquetes recurrentes, no solo piezas aisladas.
- Pedir testimonio y permiso para mostrar métricas.
- Subir precios cuando tengas 2–3 resultados documentados.
- Reservar fechas con pago anticipado.

Con esos primeros casos, puedes reconsiderar la opción B: tus patrocinadores o clientes podrían convertirse en los primeros casos de uso y luego servirte para vender la tecnología a agencias. Es decir, C puede crear los activos que hoy le faltan a B.

## Regla de decisión

No tocaría A durante estos tres meses salvo que alguien acepte pagar por adelantado un piloto. Y no construiría la API “para luego venderla”.

Tu secuencia debería ser:

**C → cobrar → generar casos → evaluar B → eventualmente explorar A con clientes precomprometidos.**

La prioridad ahora no es maximizar el mercado potencial. Es maximizar la probabilidad de que entre dinero antes del día 90.