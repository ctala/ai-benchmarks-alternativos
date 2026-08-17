# Qwen3-Coder-Next (OpenRouter FP8) — business_audit/atribucion_correlacion_temporal

- model_id: `qwen/qwen3-coder-next`
- success: True  | final: 6.28 | quality: 6.0
- latency_total: 9.245s | tokens_per_second: 143.7
- input_tokens: 253 | output_tokens: 1328

## Respuesta completa

**Conclusión: No se puede saber con certeza si la secuencia de emails funcionó.**  
Lo que sí podemos decir es que hubo un aumento en el MRR (+29%) y en altas al plan pago (de 9 a 14), **pero no hay evidencia suficiente para atribuir ese crecimiento a la secuencia de emails**, ya que hubo otros factores externos importantes que coincidieron temporalmente.

### ¿Por qué no podemos atribuir el crecimiento a los emails?

1. **Confusión de causas (confounding variables):**
   - **Publicidad pagada ($400 en marzo)**: Es difícil saber cuánto aportó, pero sí fue una variable de crecimiento activa.
   - **Mención de un creador grande (12 de marzo)**: Esto suele generar un *spike* de tráfico y credibilidad, especialmente si el creador tiene una audiencia alineada. Es altamente probable que haya generado altas directas (y también impactado en el MRR).
   - **La secuencia de emails se lanzó el 1 de marzo**, pero los emails se envían con retraso (por ejemplo, 1 por día o 1 cada 2 días), así que el impacto real habría estado entre el 1 y el 5 de marzo — *antes* del impulso de la mención del creador. Pero no sabemos cuántos destinatarios vieron los emails, ni cuántos estaban *ya* inclinados a pagar, ni cuántos incluso ya habían decidido migrar antes de recibirlos.

2. **Datos insuficientes para aislamiento causal:**
   - No tienes métricas de *engagement* con los emails (open rate, CTR, clics al landing de pago).
   - No sabes cuántos de los 14 pagos en marzo eran *usuarios gratuitos* (los que recibieron los emails) vs. nuevos usuarios que vinieron por otros canales.
   - No hay datos de cohortes: ¿cuántos gratuitos se convirtieron en marzo? ¿cuántos eran destinatarios de la secuencia?
   - No hay grupo de control (por ejemplo, una cohorte de gratuitos que *no* recibió los emails para comparar tasas de conversión).

3. **El MRR subió, pero eso no implica conversión directa:**
   - El MRR refleja el *acumulado* de pagos activos al final del mes, no solo altas nuevas. Es posible que algunos usuarios que ya pagaban en febrero hayan renovado, o que la tasa de cancelaciones haya bajado.
   - El MRR al 28 de febrero y al 31 de marzo está *cerrado* (snapshot), pero no sabemos cómo evolucionó durante marzo (¿hubo caídas intermedias? ¿se recuperó al final?).

---

### ¿Qué haría falta para estar seguros?

Para poder atribuir el crecimiento a la secuencia de emails, necesitarías:

✅ **Diseño experimental o cuasi-experimental:**
   - **Grupo de control**: Una cohorte de usuarios gratuitos *similares* (misma etapa en el funnel, misma fecha de alta, etc.) que *no* recibió la secuencia.
   - Comparar tasa de conversión: ¿el grupo que recibió los emails se convirtió significativamente más que el grupo de control?

✅ **Datos de engagement y conversión:**
   - ¿Cuántos *abrieron* los emails? ¿Cuántos *clickearon* el link de pago?
   - ¿Qué % de los que clickearon terminó pagando?  
   - ¿Qué % de los 14 pagos en marzo eran *ex usuarios gratuitos* y recibieron la secuencia?

✅ **Alineación temporal clara:**
   - Si los emails se enviaron entre el 1–5 de marzo, y los pagos se distribuyeron entre el 10–31 de marzo, hay margen para que otros factores (como la mención del creador) influyan. Idealmente, necesitas ver un *aumento de conversiones* en los días siguientes al envío de los emails, incluso después de que termine la mención del creador.

✅ **Análisis de cohortes por canal:**
   - ¿Cuántos pagos en marzo vinieron de usuarios que se registraron como gratuitos *antes* del 1 de marzo (y por tanto pudieron recibir los emails)?
   - ¿Cuántos vinieron de nuevos usuarios (no gratuitos previos)? Eso te ayuda a separar el impacto orgánico/organizado de los emails.

---

### Recomendación práctica (si quieres seguir probando):

- **La próxima vez, prueba con un diseño controlado**:  
  Por ejemplo, selecciona al azar un 50% de gratuitos para recibir la secuencia y otro 50% no (si el volumen lo permite).  
- **Mide engagement y conversión por email**, no solo MRR final.  
- **Controla otros factores activos** (como campañas de marketing o menciones externas) y anota cuándo ocurren.  
- **Habla con algunos de los nuevos pagos**: una entrevista cualitativa rápida puede darte pistas muy valiosas (¿cómo supiste de la comunidad? ¿qué te convenció de pagar?).

---

**En resumen:** El resultado es *positivo*, pero no *demostrativo*. El crecimiento es alentador, pero no hay evidencia suficiente para concluir que la secuencia de emails fue la causa principal.  
En ciencia de datos, lo más honesto es decir: **“no se puede saber con los datos actuales”** — y eso es una señal para diseñar mejor la próxima prueba.

¿Quieres que te ayude a armar un plan de medición para la próxima secuencia?