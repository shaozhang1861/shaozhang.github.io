import os
from glob import glob

from flask import Flask, abort, render_template

# Avoid reading a user-level .env that may be restricted in some environments.
os.environ.setdefault("FLASK_SKIP_DOTENV", "1")

app = Flask(__name__)

CONTACT_EMAIL = "zhangshaopku@email.com"


def build_page(
    slug,
    category,
    eyebrow,
    title,
    subtitle,
    tagline,
    image,
    image_alt,
    card_description,
    sections,
    card_image_alt=None,
    cta_label=None,
):
    return {
        "slug": slug,
        "category": category,
        "eyebrow": eyebrow,
        "title": title,
        "subtitle": subtitle,
        "tagline": tagline,
        "image": image,
        "image_alt": image_alt,
        "card_image_alt": card_image_alt or image_alt,
        "card_description": card_description,
        "sections": sections,
        "cta_label": cta_label,
    }


CASE_PAGES = {
    "workshop-case-study": build_page(
        slug="workshop-case-study",
        category="work",
        eyebrow="Case Study",
        title="Designing for Scale",
        subtitle="How we turned live-stream commerce into a data-driven engine",
        tagline="E-commerce / App Design / Data-driven features",
        image="image/装修1.webp",
        image_alt="Workshop facilitation and website design process",
        card_image_alt="Case study visual 1",
        card_description="How We Turned Live-Stream Commerce into a Data-Driven Engine",
        cta_label="View Case Study",
        sections=[
            {
                "heading": "What I've Done",
                "paragraphs": [
                    (
                        "When I joined the Meituan Live team, most hosts manually arranged their "
                        "product lists before going live. It was inefficient and inconsistent — a "
                        "host's personal judgment decided which items appeared first, regardless of user context."
                    ),
                    (
                        "I led the initiative to make the ranking intelligent. We started with data "
                        "exploration: which factors truly predicted a user's purchase intent? "
                        "Distance within 3 km, coupon availability, chain-store reputation, and "
                        "users' saved favorites turned out to be strong signals."
                    ),
                    (
                        "Through four A/B test cycles, we replaced intuition with algorithms. The result: "
                        "<strong>+9,000 daily orders</strong>, a statistically significant uplift "
                        "that exceeded most hosts' manual performance."
                    ),
                ],
            },
            {
                "heading": "Reflections",
                "paragraphs": [
                    (
                        "The hardest part wasn't technical — it was cultural. Convincing non-technical "
                        "stakeholders that a model could outperform human judgment required empathy and transparency."
                    ),
                    "I learned that “explainable automation” builds trust faster than any metric chart.",
                ],
            },
            {
                "heading": "My Takeaways",
                "paragraphs": [],
                "list_items": [
                    "<strong>Lead with a hypothesis, not a feature.</strong> People buy into why before what.",
                    "<strong>Show incremental wins.</strong> Each iteration should visibly reduce friction for real users.",
                    "<strong>Translate data into narrative.</strong> Explain algorithms in human terms — it earns adoption.",
                ],
            },
        ],
    ),
    "education-case-study": build_page(
        slug="education-case-study",
        category="work",
        eyebrow="Case Study",
        title="AI As A Creative Partner",
        subtitle="What I learned building a generative content system",
        tagline="Generative AI / Product Design",
        image="image/装修2.jpg",
        image_alt="Educational technology and digital learning platform",
        card_image_alt="Case study visual 2",
        card_description="What I Learned Building a Generative Content System",
        cta_label="View Case Study",
        sections=[
            {
                "heading": "What I've Done",
                "paragraphs": [
                    (
                        "Manually generated tags and recommendation texts limited both coverage and "
                        "creativity on Meituan Homestay. I initiated a project to use LLMs for content "
                        "generation and ML models for ranking relevance."
                    ),
                    (
                        "Coordinating six engineering teams and over <strong>200 person-days</strong>, "
                        "we built a system that rewrote thousands of listings dynamically."
                    ),
                    (
                        "Outcome: <strong>+0.29 pp conversion improvement</strong>, adding "
                        "<strong>¥320K GMV daily</strong> — but more importantly, hosts finally trusted "
                        "automation because we kept human-editable options."
                    ),
                ],
            },
            {
                "heading": "Reflections",
                "paragraphs": [
                    (
                        "AI doesn't replace creators — it augments them. Our biggest win was not the "
                        "conversion uplift; it was transforming skeptical hosts into co-designers."
                    )
                ],
            },
            {
                "heading": "My Takeaways",
                "paragraphs": [],
                "list_items": [
                    "<strong>Build opt-in loops.</strong> Give users control to review or edit AI outputs.",
                    "<strong>Measure acceptance, not just accuracy.</strong> Human satisfaction is the real KPI.",
                    "<strong>Treat models as teammates.</strong> Design feedback loops where users continuously train the system.",
                ],
            },
        ],
    ),
    "dancer-story": build_page(
        slug="dancer-story",
        category="personal",
        eyebrow="Personal Story",
        title="The Art of Movement",
        subtitle="How dance became my sanctuary and creative expression beyond the digital world",
        tagline="Dance / Performance / Expression",
        image="image/dance.jpg",
        image_alt="Shao performing dance in elegant costume",
        card_description="Dance as sanctuary and creative expression beyond the digital world",
        cta_label="Learn More",
        sections=[
            {
                "heading": "Finding My Rhythm",
                "paragraphs": [
                    (
                        "Dance has always been more than just movement to me. It's a language that "
                        "speaks when words fail, a form of meditation that brings clarity to my thoughts, "
                        "and a creative outlet that complements my work in product design."
                    )
                ],
            },
            {
                "heading": "The Journey Begins",
                "paragraphs": [
                    (
                        "My dance journey started during college when I was overwhelmed with coursework "
                        "and needed an escape. What began as a simple hobby quickly transformed into a "
                        "passion that taught me discipline, emotional expression, and the importance of body awareness."
                    )
                ],
            },
            {
                "heading": "Performance as Expression",
                "paragraphs": [
                    (
                        "Each performance is a story told through movement. The vibrant costumes, from "
                        "flowing pastels to dramatic purples and blacks, become part of the narrative. "
                        "When I'm on stage, I'm not just a designer or a student — I'm a storyteller using "
                        "my entire being as the medium."
                    )
                ],
            },
            {
                "heading": "Lessons for Design",
                "paragraphs": [
                    (
                        "Interestingly, dance has influenced my approach to product design in unexpected ways. "
                        "The emphasis on flow, rhythm, and user experience translates beautifully to creating "
                        "digital interfaces that feel natural and intuitive. Just as every movement in dance has "
                        "purpose, every element in a design should serve the user's journey."
                    )
                ],
            },
            {
                "heading": "Balance and Growth",
                "paragraphs": [
                    (
                        "In our fast-paced digital world, dance provides the perfect counterbalance. It grounds me, "
                        "keeps me connected to my physical self, and reminds me that creativity isn't just about "
                        "pixels and code — it's about human expression in all its forms."
                    )
                ],
            },
        ],
    ),
    "cat-story": build_page(
        slug="cat-story",
        category="personal",
        eyebrow="Personal Story",
        title="Proud Cat Parent",
        subtitle="How my fluffy companion taught me about patience, love, and the art of living in the moment",
        tagline="Cat Parent / Companion / Care",
        image="image/cat.jpg",
        image_alt="Shao's beloved tabby cat in harness",
        card_description="Lessons on patience, love, and presence from my fluffy companion",
        cta_label="Meet My Cat",
        sections=[
            {
                "heading": "Meet My Furry Family",
                "paragraphs": [
                    (
                        "Being a cat parent has been one of the most rewarding experiences of my life. "
                        "My fluffy tabby companion has taught me invaluable lessons about patience, "
                        "unconditional love, and finding joy in the simplest moments."
                    )
                ],
            },
            {
                "heading": "The Adventure Begins",
                "paragraphs": [
                    (
                        "When I first adopted my cat, I had no idea how much my life would change. The responsibility "
                        "of caring for another living being taught me discipline and routine, while the unconditional "
                        "love I received in return filled my heart in ways I never expected."
                    )
                ],
            },
            {
                "heading": "Lessons in Patience",
                "paragraphs": [
                    (
                        "Cats have their own timeline and agenda. Learning to respect their independence while "
                        "providing care has taught me patience – a skill that's proven invaluable in both my personal "
                        "life and professional work. Just like in product design, you can't rush the process; you have "
                        "to meet users (and cats) where they are."
                    )
                ],
            },
            {
                "heading": "Daily Joy and Comfort",
                "paragraphs": [
                    (
                        "There's something magical about coming home to a purring companion. My cat's presence brings "
                        "calm to my busy days and reminds me to pause and appreciate the present moment. Whether it's "
                        "watching her play with a simple cardboard box or feeling her warmth as she curls up beside me "
                        "while I work, these small moments create the biggest impact."
                    )
                ],
            },
            {
                "heading": "Outdoor Adventures",
                "paragraphs": [
                    (
                        "I love taking my cat on outdoor adventures with her harness. It's been a journey of "
                        "trust-building and gradual introduction to new experiences. These walks remind me that "
                        "growth happens outside our comfort zones, and that with patience and encouragement, we can "
                        "help our loved ones (furry or otherwise) explore the world safely."
                    )
                ],
            },
            {
                "heading": "Design Inspiration",
                "paragraphs": [
                    (
                        "Observing my cat's behavior has surprisingly influenced my design thinking. Cats are excellent "
                        "at identifying what's intuitive and what's not – if something doesn't work for them, they "
                        "simply won't use it. This has made me more conscious of creating user experiences that feel "
                        "natural and effortless."
                    )
                ],
            },
        ],
    ),
}


def list_pages(category):
    return [page for page in CASE_PAGES.values() if page["category"] == category]


def get_personal_images():
    """Get all personal images from static/image directory"""
    image_dir = os.path.join(app.static_folder, "image")
    # Get all files starting with "personal" (case insensitive)
    pattern = os.path.join(image_dir, "personal*")
    files = glob(pattern)
    # Sort and return relative paths
    files = sorted([os.path.basename(f) for f in files])
    return files


@app.context_processor
def inject_contact():
    return {"contact_email": CONTACT_EMAIL}


@app.route("/")
def home():
    work_items = list_pages("work")
    personal_images = get_personal_images()
    return render_template("index.html", work_items=work_items, personal_images=personal_images)


@app.route("/others")
def others():
    personal_items = list_pages("personal")
    return render_template("others.html", personal_items=personal_items)


@app.route("/story/<slug>")
def case_detail(slug):
    page = CASE_PAGES.get(slug)
    if not page:
        abort(404)
    return render_template("case_page.html", page=page)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)

