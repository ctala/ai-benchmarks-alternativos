#!/usr/bin/env python3
"""
Genera blog posts SEO desde INSIGHTS.md usando agentes de .claude/agents/.

Uso local:
    python scripts/generate_blog_post.py --topic "alternativas-claude" --insight "qwen vs gpt-oss"
    python scripts/generate_blog_post.py --auto  # elige el insight más impactante automáticamente

Uso en CI (GitHub Action workflow_dispatch):
    Mismo script, requiere ANTHROPIC_API_KEY como secret.

Output:
    blog/<fecha>-<slug>.md con frontmatter completo + adapter posts en
    blog/social/<fecha>-<slug>-{linkedin,skool,twitter,newsletter}.md
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent.parent
AGENTS_DIR = ROOT / ".claude" / "agents"
INSIGHTS = ROOT / "INSIGHTS.md"
BLOG_DIR = ROOT / "blog"
SOCIAL_DIR = BLOG_DIR / "social"

try:
    from anthropic import Anthropic
except ImportError:
    print("ERROR: pip install anthropic", file=sys.stderr)
    sys.exit(1)


def read_agent(name: str) -> str:
    """Lee el system prompt completo de un agente."""
    path = AGENTS_DIR / f"{name}.md"
    if not path.exists():
        raise FileNotFoundError(f"Agente no encontrado: {name}")
    return path.read_text(encoding="utf-8")


def read_insights() -> str:
    """Lee INSIGHTS.md como contexto."""
    if not INSIGHTS.exists():
        raise FileNotFoundError("INSIGHTS.md no existe — corré data-scientist primero")
    return INSIGHTS.read_text(encoding="utf-8")


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_-]+", "-", text)
    return text[:50]


def generate_blog_post(client: Anthropic, topic: str, insight_focus: str) -> str:
    """Invoca seo-content-writer con INSIGHTS.md como contexto."""
    system = read_agent("seo-content-writer")
    insights = read_insights()

    user_prompt = f"""Generá un blog post SEO en español para emprendedores latinoamericanos.

**Topic principal**: {topic}
**Insight a destacar**: {insight_focus}

**Contexto** (INSIGHTS.md del benchmark, usá data real, no inventes):

{insights[:8000]}

**Requisitos**:
- 1200-1800 palabras
- Frontmatter Markdown con: title, description (150-160 chars), slug, fecha (2026-04-26), tags, canonical_url
- Hook en primer párrafo con keyword cola larga
- 4-6 secciones con H2, sub-secciones con H3
- Tabla con datos reales del benchmark (sacar de INSIGHTS.md)
- FAQ section al final (5 preguntas)
- CTA a https://benchmarks.cristiantala.com/ y a la comunidad Skool
- Backlinks internos a /alternativas-claude/, /modelos-n8n/, etc según corresponda

**Filosofía**:
- "No existe un mejor modelo universal" — recordar siempre
- Audiencia: emprendedor latino, no académico
- Tono honesto, sin hype, datos reales
- Si el benchmark muestra una limitación, decirla

Output: SOLO el contenido Markdown del blog post, sin preámbulo."""

    response = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=8000,
        system=system,
        messages=[{"role": "user", "content": user_prompt}],
    )
    return response.content[0].text


def adapt_to_channel(client: Anthropic, blog_post: str, channel: str) -> str:
    """Invoca content-marketer para adaptar blog post a un canal."""
    system = read_agent("content-marketer")

    channel_specs = {
        "linkedin": "Post LinkedIn (1200-1500 chars, storytelling, hook fuerte primer línea, 3-4 párrafos cortos, 3 hashtags al final, CTA a comentar)",
        "skool": "Post comunidad Skool (1500-2000 chars, tono más casual con la comunidad Cágala-Aprende-Repite, formato pregunta abierta + respuesta, invita a debate)",
        "twitter": "Thread Twitter/X (8-12 tweets, primer tweet con hook fuerte sub-280 chars, números en cada tweet, último tweet con CTA al blog post completo)",
        "newsletter": "Sección newsletter (300-400 palabras, tono Cristian Tala, intro personal, dato impactante, recomendación accionable, link al blog)",
    }

    user_prompt = f"""Adaptá este blog post al canal **{channel}**.

**Especificación del canal**: {channel_specs[channel]}

**Blog post completo**:
{blog_post[:6000]}

**Audiencia**: emprendedores latinoamericanos.

Output: SOLO el contenido del post adaptado, sin preámbulo."""

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=2000,
        system=system,
        messages=[{"role": "user", "content": user_prompt}],
    )
    return response.content[0].text


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--topic", default="alternativas-claude", help="Topic principal del post")
    ap.add_argument("--insight", default="provider matters", help="Insight específico a destacar")
    ap.add_argument("--auto", action="store_true", help="Modo auto: elige insight impactante de INSIGHTS.md")
    ap.add_argument("--channels", nargs="+", default=["linkedin", "skool", "twitter", "newsletter"],
                    help="Canales a generar adaptaciones")
    args = ap.parse_args()

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERROR: setear ANTHROPIC_API_KEY en el environment", file=sys.stderr)
        sys.exit(1)

    client = Anthropic(api_key=api_key)

    BLOG_DIR.mkdir(exist_ok=True)
    SOCIAL_DIR.mkdir(exist_ok=True)

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    slug = slugify(args.topic + "-" + args.insight)

    print(f"Generando blog post: topic={args.topic}, insight={args.insight}")
    blog_post = generate_blog_post(client, args.topic, args.insight)
    blog_path = BLOG_DIR / f"{today}-{slug}.md"
    blog_path.write_text(blog_post, encoding="utf-8")
    print(f"OK: {blog_path} ({len(blog_post)} chars)")

    for channel in args.channels:
        print(f"Adaptando a {channel}...")
        adapted = adapt_to_channel(client, blog_post, channel)
        adapted_path = SOCIAL_DIR / f"{today}-{slug}-{channel}.md"
        adapted_path.write_text(adapted, encoding="utf-8")
        print(f"OK: {adapted_path} ({len(adapted)} chars)")

    print(f"\n✅ Done. Generated 1 blog post + {len(args.channels)} social adaptations.")
    print(f"   Total cost estimado: ~$0.20-0.50 USD (Opus para blog + Sonnet para socials).")


if __name__ == "__main__":
    main()
