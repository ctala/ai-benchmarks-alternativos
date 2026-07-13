# Nemotron 3 Ultra 550B — business_audit/atribucion_correlacion_temporal

- model_id: `nvidia/nemotron-3-ultra-550b-a55b`
- success: True  | final: 4.96 | quality: 4.8
- latency_total: 24.429s | tokens_per_second: 32.5
- input_tokens: 243 | output_tokens: 794

## Respuesta completa

**Conclusión: No se puede saber. Los datos no sostienen que la secuencia de emails funcionara (ni que no funcionara).**

---

### Por qué no se puede atribuir el crecimiento a los emails

Tienes **tres intervenciones simultáneas** en la misma ventana temporal (marzo) y **ningún grupo de control**:

| Intervención | Fecha inicio | Posible impacto |
|--------------|--------------|-----------------|
| Secuencia de 5 emails (plan gratis) | 1 mar | Desconocido |
| Publicidad pagada ($400/mes) | 3 mar | Desconocido |
| Mención de creador grande | 12 mar | Desconocido |

El MRR subió +29% y las altas de 9 a 14 (+56%). Pero **cualquiera de las tres** —o la combinación— pudo causar todo, parte o nada del crecimiento. No hay forma de separar sus efectos con lo que me diste.

---

### Lo mínimo que haría falta para tener *alguna* evidencia

1. **Grupo de control**  
   - Usuarios del plan gratis que **no recibieron la secuencia** (holdout aleatorio 10–20%).  
   - Comparas conversión del grupo expuesto vs. no expuesto en la misma semana.

2. **O secuencia escalonada (staggered rollout)**  
   - Activas la secuencia en cohortes semanales.  
   - Si la conversión sube *solo* cuando cada cohorte recibe el email, hay señal.

3. **Tracking a nivel usuario**  
   - Saber cuántos de los 14 nuevos pagos **abrieron/clickearon** al menos un email de la secuencia antes de pagar.  
   - Si 0–1 vinieron de ahí, la secuencia no fue el driver principal.

4. **Desagregar el efecto de la mención del creador**  
   - Tráfico y altas día a día del 12 al 18 de marzo.  
   - Si hay un pico evidente ese día/semana, la mención explica gran parte.

5. **Datos de la publicidad**  
   - Clics, CAC, conversión de los $400.  
   - Si la publicidad trajo 8 altas a $50 CAC, ya sabes de dónde vino la mayor parte.

---

### Qué puedes hacer *hoy* con lo que tienes

- **No digas «los emails funcionaron»**. Di: «Marzo creció un 29% con tres cambios a la vez; no sabemos cuál pesó».
- **Para la próxima**: lanza *una* cosa a la vez, o usa holdout. Si no puedes permitirte holdout, al menos mide *engagement* de la secuencia (opens, clicks, conversión post-click) y compáralo con tu baseline histórico de conversión orgánica del plan gratis.

¿Quieres que te arme un diseño simple de test A/B para la próxima iteración?