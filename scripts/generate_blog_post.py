#!/usr/bin/env python3
"""
Genera blog posts SEO desde INSIGHTS.md usando agentes de .claude/agents/.

Soporta dos backends:
  - anthropic (default): usa Claude Opus + Sonnet, requiere ANTHROPIC_API_KEY
  - openrouter: usa cualquier modelo OpenAI-compatible, requiere OPENROUTER_API_KEY
  - nvidia_nim: usa modelos via NVIDIA NIM gratis (40 RPM), requiere NVIDIA_NIM_API_KEY

Eat your own dog food: si el benchmark dice que DeepSeek V4 Flash empata a
Claude Opus 4.6 en contenido a costo cero, generemos el contenido con V4 Flash.

Uso local:
    # Default Anthropic (Opus + Sonnet, ~$0.30/run)
    python scripts/generate_blog_post.py --topic "alternativas-claude"

    # DeepSeek V4 Flash via OpenRouter (~$0.01/run)
    python scripts/generate_blog_post.py --provider openrouter \
        --model deepseek/deepseek-v4-flash --topic "alternativas-claude"

    # DeepSeek V4 Flash via NVIDIA NIM (gratis con 40 RPM)
    python scripts/generate_blog_post.py --provider nvidia_nim \
        --model deepseek-ai/deepseek-v4-flash --topic "alternativas-claude"

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


class LLMClient:
    """Wrapper que abstrae anthropic vs openrouter/nvidia_nim."""

    def __init__(self, provider: str, model_blog: str, model_social: str):
        self.provider = provider
        self.model_blog = model_blog
        self.model_social = model_social

        if provider == "anthropic":
            try:
                from anthropic import Anthropic
            except ImportError:
                print("ERROR: pip install anthropic", file=sys.stderr); sys.exit(1)
            api_key = os.environ.get("ANTHROPIC_API_KEY")
            if not api_key:
                print("ERROR: setear ANTHROPIC_API_KEY", file=sys.stderr); sys.exit(1)
            self.client = Anthropic(api_key=api_key)

        elif provider in ("openrouter", "nvidia_nim"):
            try:
                from openai import OpenAI
            except ImportError:
                print("ERROR: pip install openai", file=sys.stderr); sys.exit(1)

            if provider == "openrouter":
                api_key = os.environ.get("OPENROUTER_API_KEY")
                if not api_key:
                    print("ERROR: setear OPENROUTER_API_KEY", file=sys.stderr); sys.exit(1)
                base_url = "https://openrouter.ai/api/v1"
            else:  # nvidia_nim
                api_key = os.environ.get("NVIDIA_NIM_API_KEY")
                if not api_key:
                    print("ERROR: setear NVIDIA_NIM_API_KEY", file=sys.stderr); sys.exit(1)
                base_url = "https://integrate.api.nvidia.com/v1"

            self.client = OpenAI(api_key=api_key, base_url=base_url)
        else:
            raise ValueError(f"Provider no soportado: {provider}")

    def generate(self, system: str, user: str, role: str = "blog", max_tokens: int = 8000) -> str:
        """Genera texto. role='blog' usa model_blog (mas potente), 'social' usa model_social."""
        model = self.model_blog if role == "blog" else self.model_social

        if self.provider == "anthropic":
            response = self.client.messages.create(
                model=model,
                max_tokens=max_tokens,
                system=system,
                messages=[{"role": "user", "content": user}],
            )
            return response.content[0].text

        # OpenAI-compatible (openrouter, nvidia_nim)
        response = self.client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            max_completion_tokens=max_tokens,
        )
        if not response.choices or response.choices[0].message.content is None:
            raise RuntimeError("Provider devolvio respuesta vacia. Reintentar o cambiar modelo.")
        return response.choices[0].message.content


def generate_blog_post(client: LLMClient, topic: str, insight_focus: str) -> str:
    """Invoca seo-content-writer con INSIGHTS.md como contexto."""
    system = read_agent("seo-content-writer")
    insights = read_insights()

    user_prompt = f"""Genera un blog post SEO en **español neutro** para emprendedores hispanohablantes.

**Topic principal**: {topic}
**Insight a destacar**: {insight_focus}

**Contexto** (INSIGHTS.md del benchmark, usa data real, no inventes):

{insights[:12000]}

**Requisitos**:
- 1500-2200 palabras
- Frontmatter Markdown con: title, description (150-160 chars), slug, fecha (2026-04-27), tags, canonical_url
- Hook en primer parrafo con keyword cola larga
- 5-7 secciones con H2, sub-secciones con H3
- Tabla con datos reales del benchmark (sacar de INSIGHTS.md)
- FAQ section al final (5-7 preguntas)
- CTA a https://benchmarks.cristiantala.com/ y a la comunidad Skool
- Backlinks internos a /alternativas-claude/, /modelos-n8n/, etc segun corresponda

**Idioma — ESPAÑOL NEUTRO obligatorio**:
- Pronombres: usar **tú** (singular) y **ustedes** (plural). NO uses "vosotros" (España exclusivo) ni "vos/voseo" (rioplatense exclusivo).
- Verbos: forma de "tú" → "tienes", "sabes", "puedes". NO "tenés", "sabés", "podés".
- Vocabulario universal: evita modismos regionales (ni "guay", ni "platicar", ni "chévere", ni "bárbaro", ni "ordenador").
- El texto debe leerse natural para un lector en España, México, Argentina, Chile, Colombia o cualquier país hispanohablante.

**Filosofia**:
- "No existe un mejor modelo universal" — recordar siempre
- Audiencia: emprendedor hispanohablante (España + LATAM), no academico
- Tono honesto, sin hype, datos reales
- Si el benchmark muestra una limitacion, decirla (ej. V4 Pro/Flash con runs incompletos)

Output: SOLO el contenido Markdown del blog post, sin preambulo."""

    return client.generate(system, user_prompt, role="blog", max_tokens=8000)


def adapt_to_channel(client: LLMClient, blog_post: str, channel: str) -> str:
    """Invoca content-marketer para adaptar blog post a un canal."""
    system = read_agent("content-marketer")

    channel_specs = {
        "linkedin": "Post LinkedIn (1200-1500 chars, storytelling, hook fuerte primer linea, 3-4 parrafos cortos, 3 hashtags al final, CTA a comentar)",
        "skool": "Post comunidad Skool (1500-2000 chars, tono casual con la comunidad Cagala-Aprende-Repite, formato pregunta abierta + respuesta, invita a debate)",
        "twitter": "Thread Twitter/X (8-12 tweets, primer tweet con hook fuerte sub-280 chars, numeros en cada tweet, ultimo tweet con CTA al blog post completo)",
        "newsletter": "Seccion newsletter (300-400 palabras, tono Cristian Tala, intro personal, dato impactante, recomendacion accionable, link al blog)",
    }

    user_prompt = f"""Adapta este blog post al canal **{channel}**.

**Especificacion del canal**: {channel_specs[channel]}

**Blog post completo**:
{blog_post[:8000]}

**Audiencia**: emprendedores latinoamericanos.

Output: SOLO el contenido del post adaptado, sin preambulo."""

    return client.generate(system, user_prompt, role="social", max_tokens=2500)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--topic", default="alternativas-claude", help="Topic principal del post")
    ap.add_argument("--insight", default="DeepSeek V4 Flash empata a Opus 4.6 gratis",
                    help="Insight especifico a destacar")
    ap.add_argument("--channels", nargs="+", default=["linkedin", "skool", "twitter", "newsletter"],
                    help="Canales a generar adaptaciones")
    ap.add_argument("--provider", default="anthropic",
                    choices=["anthropic", "openrouter", "nvidia_nim"],
                    help="Backend para generar el contenido")
    ap.add_argument("--model-blog", default=None,
                    help="Modelo para blog post (default: claude-opus-4-7 / deepseek/deepseek-v4-flash)")
    ap.add_argument("--model-social", default=None,
                    help="Modelo para adaptaciones sociales (default: claude-sonnet-4-6 / mismo blog)")
    args = ap.parse_args()

    # Defaults por provider
    if args.model_blog is None:
        args.model_blog = {
            "anthropic": "claude-opus-4-7",
            "openrouter": "deepseek/deepseek-v4-flash",
            "nvidia_nim": "deepseek-ai/deepseek-v4-flash",
        }[args.provider]
    if args.model_social is None:
        args.model_social = {
            "anthropic": "claude-sonnet-4-6",
            "openrouter": "deepseek/deepseek-v4-flash",
            "nvidia_nim": "deepseek-ai/deepseek-v4-flash",
        }[args.provider]

    # Cargar .env si existe
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        pass

    print(f"Provider: {args.provider}")
    print(f"Modelo blog: {args.model_blog}")
    print(f"Modelo social: {args.model_social}")
    print()

    client = LLMClient(args.provider, args.model_blog, args.model_social)

    BLOG_DIR.mkdir(parents=True, exist_ok=True)
    SOCIAL_DIR.mkdir(parents=True, exist_ok=True)

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    slug = slugify(args.topic + "-" + args.insight)

    print(f"Generando blog post: topic={args.topic}, insight={args.insight}")
    blog_post = generate_blog_post(client, args.topic, args.insight)
    blog_path = BLOG_DIR / f"{today}-{slug}.md"
    blog_path.write_text(blog_post, encoding="utf-8")
    print(f"OK: {blog_path} ({len(blog_post)} chars)")

    for channel in args.channels:
        print(f"Adaptando a {channel}...")
        try:
            adapted = adapt_to_channel(client, blog_post, channel)
            adapted_path = SOCIAL_DIR / f"{today}-{slug}-{channel}.md"
            adapted_path.write_text(adapted, encoding="utf-8")
            print(f"OK: {adapted_path} ({len(adapted)} chars)")
        except Exception as e:
            print(f"ERROR adaptando a {channel}: {e}", file=sys.stderr)

    cost_estimate = {
        "anthropic": "$0.20-0.50 (Opus + Sonnet)",
        "openrouter": "$0.01-0.05 (V4 Flash $0.14/$0.28)",
        "nvidia_nim": "$0 (gratis, 40 RPM)",
    }[args.provider]

    print(f"\nDone. Generated 1 blog post + {len(args.channels)} social adaptations.")
    print(f"Costo estimado: {cost_estimate}")


if __name__ == "__main__":
    main()
