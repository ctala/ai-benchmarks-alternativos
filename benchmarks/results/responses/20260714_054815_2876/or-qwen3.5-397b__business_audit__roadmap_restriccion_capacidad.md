# Qwen 3.5 397B — business_audit/roadmap_restriccion_capacidad

- model_id: `qwen/qwen3.5-397b-a17b`
- success: True  | final: 8.41 | quality: 10.0
- latency_total: 54.662s | tokens_per_second: 37.5
- input_tokens: 255 | output_tokens: 2048
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando una evaluación detallada y estratégica que un emprendedor podría aplicar directamente.

## Respuesta completa

Here's a thinking process that leads to the suggested prioritization:

1.  **Analyze the User and Context:**
    *   **Role:** Solo Founder (acting as Head of Product).
    *   **Constraint:** Realistic capacity, not ideal.
    *   **Available Time:** 6 hours/day focused work.
    *   **Non-delegable Overhead:** 2 hours/day (Support & Ops).
    *   **Build Time:** ~4 hours/day.
    *   **Timeline:** 8 weeks (2 months) until the end of the quarter.
    *   **Total Build Capacity:** 4 hours/day * 5 days/week * 8 weeks = 160 hours. (Let's be conservative: maybe 4 days/week effective build time due to fatigue/unexpected issues? Let's stick to the prompt's math first: 4h * 40h week = 160h total).
    *   **Goal:** Prioritize 4 initiatives (A, B, C, D) based on impact vs. effort within the 8-week constraint.

2.  **Analyze the Initiatives:**

    *   **A) Rewrite Platform:**
        *   Impact: High (future speed).
        *   Effort: ~3 months full-time.
        *   *Reality Check:* 3 months full-time = ~480 hours (assuming 40h/week). I have 160 hours total. This is impossible. Even if "full-time" means 8h/day, I only have 4h/day. So, 3 months * 2 = 6 months of *my* time.
        *   *Verdict:* **KILL** or defer indefinitely. It's a "death trap" for a solo founder.

    *   **B) Fix Onboarding Flow:**
        *   Impact: High (60% drop-off is bleeding revenue/users).
        *   Effort: ~1 week.
        *   *Reality Check:* 1 week * 4h/day = 20 hours. Very doable. Immediate ROI.
        *   *Verdict:* **DO FIRST.**

    *   **C) Customer Metrics Dashboard:**
        *   Impact: Medium.
        *   Effort: ~3 weeks.
        *   Dependency: Depends on A (Rewrite).
        *   *Reality Check:* Since A is impossible, C is blocked *unless* we decouple it. But even if decoupled, 3 weeks * 4h/day = 60 hours. That's almost 40% of my total quarterly capacity. Is it worth it if Impact is only Medium?
        *   *Verdict:* **DEFER** or scope down heavily. Dependency on A makes it risky.

    *   **D) Record 10 Content Videos:**
        *   Impact: Medium (acquisition/brand).
        *   Effort: ~2 weeks.
        *   *Reality Check:* 2 weeks * 4h/day = 40 hours. Doable.
        *   *Verdict:* **CONSIDER** after B.

3.  **Calculate Capacity vs. Demand:**
    *   **Total Capacity:** 8 weeks * 5 days * 4 hours = 160 hours.
    *   **Initiative A:** ~480+ hours (Impossible).
    *   **Initiative B:** ~20 hours.
    *   **Initiative C:** ~60 hours (Blocked by A).
    *   **Initiative D:** ~40 hours.
    *   **Total for B+C+D:** 120 hours. (Leaves 40 hours buffer).
    *   *Problem:* C depends on A. If A isn't done, C can't be done properly (according to the prompt). If A is killed, C needs re-evaluation.

4.  **Strategic Decision Making (Solo Founder Mindset):**
    *   **Survival > Perfection:** Fixing the leak (B) is more important than rebuilding the ship (A).
    *   **Cash Flow/Retention > Future Tech:** B saves existing users. D brings new users. A is technical debt repayment (important but not now).
    *   **Dependencies:** C is blocked. Don't plan on blocked work.
    *   **Buffer:** Solo founders always underestimate support/ops creep. Need a 20-30% buffer.

5.  **Drafting the Plan:**

    *   **Immediate Kill:** Initiative A. It's a trap. 3 months full-time > 8 weeks part-time. It will kill the business.
    *   **Priority 1:** Initiative B. Bleeding 60% of users is an emergency. 1 week effort.
    *   **Priority 2:** Initiative D. Marketing/Sales engine. Once the bucket isn't leaking (B), fill it. 2 weeks effort.
    *   **Priority 3 (Conditional):** Initiative C. Only if B and D are done early, AND we decouple it from A. But realistically, with 8 weeks, B + D = 3 weeks. That leaves 5 weeks. Why not do C? Because Impact is Medium and it depends on A. Better to iterate on B or do more D. *Decision:* Defer C or scope it to MVP without A. Let's suggest deferring or scoping down.
    *   **Buffer:** The remaining time must go to Support/Ops overflow and rest. Burnout is a risk.

6.  **Refining the Output (Tone & Structure):**
    *   **Tone:** Direct, empathetic, realistic, decisive. "Head of Product" voice for a solo founder.
    *   **Structure:**
        1.  Reality Check (The Math).
        2.  The Decision (Kill/Do/Defer).
        3.  The Schedule (Week by Week).
        4.  The "Why" (Rationale).
    *   **Key Insight:** Emphasize that A is a "vanity project" in this context. Emphasize that B is revenue protection.

7.  **Self-Correction/Edge Case:**
    *   *Wait, does C strictly depend on A?* Prompt says "Depende de que A esté terminado". As a Product Head, I need to challenge that dependency. Can we build a lite version? I should mention this.
    *   *Time calculation:* 8 weeks. B (1) + D (2) = 3 weeks. That leaves 5 weeks unused if I just do B and D. Is that okay? Yes, because Support/Ops often expand to fill time. Also, iteration on B might take longer than 1 week. Also, D (videos) might need distribution time.
    *   *Better Plan:* Do B. Then D. Then use remaining time to iterate on B based on data, or build a *small* version of C that doesn't need A. But strictly following the prompt's constraints: A is impossible. C is blocked. So it's B + D + Buffer/Iteration.

8.  **Finalizing the Plan:**
    *   **Week 1-2:** Fix Onboarding (B). (Give it 2 weeks buffer, it's never just 1).
    *   **Week 3-5:** Content (D). (2 weeks work + 1 week distribution/editing buffer).
    *   **Week 6-8:** Buffer + Small wins + Support overflow. Do not start A. Do not start C unless dependency is removed.

    *Wait, let's look at the "Head of Product" persona.* I need to be firm.
    *   **A:** NO. (3 months FT > 2 months PT).
    *   **C:** NO (Blocked by A).
    *   **B:** YES (Critical).
    *   **D:** YES (Growth).

    *Revised Schedule:*
    *   Weeks 1-2: B (Onboarding).
    *   Weeks 3-5: D (Videos).
    *   Weeks 6-8: Buffer + Iteration on B + Support overflow.

    *Wait, 160 hours total.*
    *   B: 20h.
    *   D: 40h.
    *   Total: 60h.
    *   Remaining: 100h.
    *   *Risk:* If I leave 100h empty, the founder will feel guilty and start A. I need to assign that time to "Iteration & Support Buffer". Support often eats more than 2h/day.
    *   *Alternative:* Can we unblock C? If C is high value for retention, maybe we build a "ugly version" of C that doesn't need A. But prompt says "Depends on A". I must respect the constraint or challenge it. I will challenge it slightly but prioritize B & D.

    *Let's stick to the strongest advice:* Kill A. Fix B. Do D. Leave buffer.

9.  **Drafting the Response (in Spanish):**
    *   Start with the hard math.
    *   Declare the "Kill".
    *   Order the rest.
    *   Provide the weekly calendar.
    *   Add a warning