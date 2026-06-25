# How to Write More Human, How Not to Write Like AI

A working reference compiled from blog posts, academic papers, Twitter/X discourse, and detector research, covering 2024–2026. Two halves:

1. **Negative half** — what AI does that gives it away (avoid these)
2. **Positive half** — what real writers do that makes prose feel human (do these)

The negative half is bigger because the discourse is bigger, but the positive half is what actually matters. Cutting "delve" doesn't make you a writer. Having a voice does.

---

## Part 1 — What AI Does (and what gives it away)

### 1.1 The overused vocabulary

The Max Planck Institute (2025) measured "delve," "robust," and "pivotal" as appearing 50%+ more often in published text after ChatGPT's release. Other corpus studies put "delve," "moreover," "crucial," "landscape," and "tapestry" at **50× to 269× the human baseline**.

The list mutates as labs train obvious offenders down. Three waves:

**First wave (2023 – mid-2024):**
delve, tapestry, testament, beacon, treasure trove, synergy, foster, embark, underscore, groundbreaking, game-changer, endeavor, enlighten, esteemed, shed light on, peril, amplify, convey, resonate, interplay, adhere, paramount, furthermore, profound, indelible, bespoke, cognizant, encompass, hitherto, leverage, realm, utilize, boasts, bolstered, crucial, emphasizing, enduring, garner, intricate, key, meticulous, pivotal, valuable, vibrant, additionally.

**Mid-2024 → mid-2025 wave (labs patched the first list):**
align with, enhance, fostering, highlighting, showcasing, ensuring, cultivating.

**Mid-2025 → 2026 wave (what's getting flagged now):**
emphasizing, enhance, highlighting, showcasing, exemplifies, reflects broader, resonates, evolving (especially "evolving landscape"), indelible mark, commitment to, transformative, nuanced.

**The "container nouns" — avoid entirely:**
landscape, realm, tapestry, synergy, testament, underpinnings, ecosystem, journey, fabric, sphere.

**The inflated adjectives:**
pivotal, robust, innovative, seamless, cutting-edge, groundbreaking, renowned, vibrant, rich, profound, bespoke, holistic, dynamic.

**The abstract verbs:**
delve, leverage, utilize, harness, streamline, underscore, unpack, navigate (figuratively), bolster, foster, pave the way.

A PubMed study found "delve" scored highest of all AI-influenced terms in medical literature post-2022. Linguist Adam Aleksic ("Etymology Nerd") calls this the **AI accent** — humans now using these words more in spontaneous speech because they've been marinating in AI-generated text. The Washington Post ran "People are starting to talk like ChatGPT" in August 2025.

### 1.2 Phrase patterns and stock constructions

**Hedge / throat-clearing:**
- "It's important to note that…"
- "It's worth noting that…"
- "It's worth mentioning…"
- "Keep in mind that…"
- "Remember that…"
- "That said…" / "With that being said…"

**Sycophantic openers (the new "As an AI language model"):**
- "Great question!"
- "Absolutely!" / "Certainly!"
- "You're absolutely right" — has its own meme, T-shirts, top Hacker News thread. OpenAI publicly rolled back a GPT-4o update in April 2025 over this.
- "In today's fast-paced world…"
- "In an era of…"
- "Let's dive in" / "Let's dive into…"
- "Let's unpack this"
- "Buckle up"
- "Picture this:"
- "Imagine a world where…"

**Closers:**
- "In conclusion…"
- "In summary…"
- "Ultimately…"
- "I hope this helps!"
- "Let me know if you need anything else!"
- "Happy [writing/coding/baking]!"
- "So go ahead and…!"

**The balance template ("It's not X, it's Y") — the second-most-mocked tell after the em dash.** Academic Mushtaq Bilal calls this *contrastive reframe* or *antithesis*. Futurism's 2025 headline: "Once You Notice ChatGPT's Weird Way of Talking, You Start to See It Everywhere."
- "It's not just X — it's Y."
- "It's not X, it's Y."
- "Not only X, but also Y."
- "This isn't just about X. It's about Y."
- "The issue isn't X. The issue is Y."

The model performs the *shape* of an argumentative turn without making a real turn. Bilal's prompt to suppress it: *"Do not use the rhetorical figure of antithesis at all. Do not use any corrective negation, metalinguistic negation, or contrastive focused constructions under any circumstances."*

**Audience-bracketing:**
- "Whether you're a seasoned X or a curious beginner…"
- "Whether you're a student or a professional…"

**Significance puffery:**
- "stands as a testament to…"
- "serves as a reminder that…"
- "plays a vital/significant/crucial/pivotal/key role in…"
- "underscores the importance of…"
- "marks a turning point"
- "reflects broader trends"
- "leaves an indelible mark"

**The "Challenges and Future" formula:** positive preamble → "Despite its X, [subject] faces several challenges…" → "Despite these challenges…" → "Future Outlook" with speculative-but-optimistic claims. Wikipedia treats this section sequence as a structural tell that survives prose-level humanization.

### 1.3 Structural tells

**The Rule of Three.** LLMs love threes — three adjectives, three clauses, three examples. GPTZero published "How to Break Free from GPT's Rule of Three." Colin Gorrie: *"Most of the techniques beloved of LLMs are versions of parallelism,"* and the tricolon is prototypical. If every list has three items and every descriptive run is "fast, reliable, and scalable" — that's machine.

**Other structural fingerprints:**
- **Bullet overuse** — bullets for content that should be prose. Bold-header-then-sentence pseudo-bullets ("**Key term:** explanation").
- **Title Case Headings With All Major Words Capitalized** (LLMs do this even when surrounding style is sentence case).
- **Bolding "key terms" in every paragraph** — mechanical emphasis.
- **Perfectly balanced paragraphs** — uniformly ~3 sentences of ~15–20 words each.
- **Transitional word at the start of every paragraph** — "Moreover," "Furthermore," "Additionally," "However."
- **Elegant variation** — the model dodges its own repetition penalty by swapping synonyms: "the device" → "the apparatus" → "the gadget" in three consecutive sentences.
- **Markdown leakage** — `**bold**`, asterisk bullets, and citation tokens like `turn0search0`, `oai_citation`, `contentReference` appearing in final copy. Wikipedia editors call these smoking guns.

### 1.4 Punctuation tells

**The em dash.** The internet AI-detection meme of 2025. Paul Skallas's February 2025 tweet ("they all use this symbol '—' throughout the writing") hit 3.7M views and started the war. Rolling Stone dubbed it the "ChatGPT hyphen." McSweeney's parodied it as "the punctuation equivalent of a cardigan." Sam Altman publicly conceded in November 2025 that ChatGPT now obeys "don't use em dashes" in custom instructions — confirming that, until then, *it literally couldn't stop*.

Important nuance: the tell isn't a single em dash. It's the **rate and pattern** — multiple em dashes per paragraph, used as parentheticals + as sentence breaks + as commas, all within the same piece. Most human writers use 0–1 per paragraph. LLMs use 2–4. Even after OpenAI's fix, em-dash density is now a reputational tell — readers feel it before they articulate it.

**Other punctuation signatures:**
- **Curly/smart quotes** (' " " ') in a document that otherwise uses straight quotes.
- **100% Oxford comma compliance** in writing that's otherwise casual.
- **Liberal, mechanically correct semicolons** — casual human web writers mostly avoid them; LLMs reach for them.
- **No comma splices, no fragments, no trailing ellipses.** Perfect punctuation in informal contexts is itself a tell.

### 1.5 Tonal tells

**Relentless positivity / sycophancy.** Even after OpenAI's April 2025 rollback, the residual signature is opening flattery, reflexive validation before correction, an upbeat closing exhortation, and zero actual stake. The arXiv paper *Flattering to Deceive* (2412.02802) found participants reported **lower trust** after sycophantic outputs — readers feel the false warmth without naming it.

**Hedging and false balance:**
- "While X has its benefits, it also presents challenges."
- "There are many perspectives on this issue."
- "Some argue X, while others argue Y."
- "It depends on a variety of factors."

No actual opinion ever lands; every claim is immediately qualified. Per the Transparency Coalition, early anti-hallucination training created models that *"compulsively hedged, undermining clarity."*

**Weasel attributions:**
- "Industry reports suggest…"
- "Observers have noted…"
- "Experts argue that…"
- "Some have suggested…"

Vague aggregate sources standing in for actual citation.

**Promotional / travel-brochure voice:**
- "nestled in the heart of…"
- "boasts a vibrant…"
- "rich cultural tapestry"
- "renowned for its…"
- "diverse array of…"

**The "warmth" tic:**
- "Remember, you're not alone in this."
- "Be kind to yourself."
- "It's okay to…"

Unprompted emotional reassurance that surfaces in advice/lifestyle outputs.

### 1.6 What the detectors are actually measuring

Every commercial detector — GPTZero, Originality.ai, Turnitin, Copyleaks, Winston — reduces to two statistical primitives:

**Perplexity (plain English):** how *surprised* a language model is by your next word. AI text has low perplexity because LLMs are trained to pick high-probability tokens. Humans, ironically, are *worse* at next-token prediction than even GPT-2 — and that worseness is the signal.

**Burstiness (plain English):** the *variance* of perplexity across the document. Humans write a rambling 40-word sentence, then stop. Cold. Then another twisty clause. AI writes paragraphs of evenly-paced 18–22 word sentences with consistent complexity. GPTZero calls flat perplexity *"the AI-print."*

**The flagging rule:** low perplexity + low burstiness = AI. The detection signals everyone else uses — sentence-length variance, type-token ratio, function word distribution, punctuation rate, reading-level consistency — are all proxies for the same underlying claim: **humans produce less predictable token sequences than LLMs.**

| Feature | What AI does | Human writing | The move |
|---|---|---|---|
| Sentence length variance | Uniform 15–25 words | 4 → 38 → 11 | Drop a 3-word sentence after a 35-word one |
| Type-Token Ratio | Lower lexical diversity, recycled vocab | More synonyms, rare words | One uncommon word per ~100 you'd reach for |
| Function word distribution | Standardized "the/of/and" rates | Idiosyncratic — *your* fingerprint | Keep your "honestly," "anyway," "look" |
| Hapax legomena (one-off words) | Low | High | Don't smooth out the variants |
| Paragraph length | Uniform 3–5 sentences | Irregular | One-sentence paragraphs exist. Use them. |
| Em-dash rate | ~3–4 per 1k words | ~1–2 per 1k words | Cut em dashes by ~60% |
| Reading-level consistency | Flat Flesch-Kincaid | Bounces around | Mix dense and casual clauses |

The Stanford TOEFL study (arXiv 2304.02819) is the canonical failure case: detectors hit near-perfect accuracy on US 8th-grade essays but **misclassified 61% of TOEFL essays as AI**. Non-native writers and LLMs share the same statistical signature — smaller vocab, more standardized syntax, lower perplexity. Read this as confirmation that what detectors call "AI" is really *smoothness*. Your job is to be productively rough.

### 1.7 What specifically changed in 2025–2026

This is the section that matters most, because the obvious stuff (delve, tapestry) is now table stakes — even AI knows to avoid those.

1. **The discourse moved from word lists to rhythm.** Detectors and human readers both. Wikipedia's mid-2025 update emphasizes that lexical filters miss modern outputs; the rigid section formula survives prose-level laundering.
2. **Em dashes are patchable, but culturally cemented.** OpenAI shipped the fix; the meme remains. Heavy em-dash use will be read as AI even when it isn't.
3. **"It's not X, it's Y" replaced "delve" as the meme phrase of 2025.** It's now the first thing trained editors look for.
4. **Sycophantic openings are the new "As an AI language model."** Any reply that affirms the reader before delivering content reads as AI to non-technical audiences.
5. **Structural fingerprint > vocabulary.** Even with perfect word choice, the lead → background → significance → "Despite challenges" → "Future outlook" formula gives it away.
6. **Lowercase posting emerged as an anti-AI signal.** Sam Altman is patron saint. Because LLMs always capitalize correctly, dropping capitals signals human authorship. Same logic for typos left in, sentence fragments, stream-of-thought asides.
7. **The AI-slop callouts of real writers** (NYT "Modern Love" essay by Kate Gilgan, "GrantaGate" prize-winning story, Pangram's "slop janitor" timelines on X) — the discourse moved from style to allegation. The reputational stakes of *sounding* like AI now matter even if you didn't use it.

---

## Part 2 — What Real Writers Do (the affirmative craft)

Cutting AI tells produces clean prose, not human prose. The positive moves are what actually make writing feel like a person wrote it.

### 2.1 Voice — idiosyncrasy over neutrality

Ann Handley: *"You can't really work on voice directly. It develops over time and evolves; it doesn't just drop into your lap."* Her trick: write the draft as a letter to your mom. Paul Graham: *"Write like you talk. Explain your ideas to a friend by talking; then use that transcript as a draft."*

Writers who exemplify voice as identity:
- **Patrick McKenzie (patio11)** — long, structurally maximal sentences laced with banking jargon and dry asides.
- **Maciej Cegłowski** — wit as load-bearing. *"If I wasn't funny and if I couldn't tweet, I don't think I could make this work."*
- **Mandy Brown** (A Working Library) — quiet, literary, reflective.
- **Venkatesh Rao** (Ribbonfarm) — twenty-thousand-word essays designed to *"rewire the software inside your head."*

David Perell's rule #1 (relaying Tyler Cowen): *"Don't let AI smooth out your idiosyncrasies."*

### 2.2 Concrete specificity over abstraction

Strunk and White, rule 17: *"Prefer the specific to the general, the definite to the vague, the concrete to the abstract."* Replace *"A period of unfavorable weather set in"* with *"It rained every day for a week."*

Stephen King: *"Belief and reader absorption come in the details: An overturned tricycle in the gutter of an abandoned neighborhood can stand for everything."*

The practical move: replace "a recent study" with the study's name. Replace "many people" with a real number. Replace "useful tools" with the names of the tools. "The old wooden bench creaked under my weight" is concrete. "Outdoor seating" is a category.

### 2.3 Show, don't tell — trust the reader

King: *"Description begins in the writer's imagination, but should finish in the reader's."* And: *"The road to hell is paved with adverbs."* Adverbs signal you don't trust your reader, or that your verb is too weak.

Klinkenborg: *"Say less than you could and let your readers form their own thoughts, make their own assumptions, draw their own conclusions."*

### 2.4 Sentence rhythm — mix the cadence

Gary Provost's famous passage is still the clearest demonstration:

> This sentence has five words. Here are five more words. Five-word sentences are fine. But several together become monotonous. Listen to what is happening. The writing is getting boring. The sound of it drones. It's like a stuck record. The ear demands some variety.
>
> Now listen. I vary the sentence length, and I create music. Music. The writing sings. It has a pleasant rhythm, a lilt, a harmony. I use short sentences. And I use sentences of medium length. And sometimes, when I am certain the reader is rested, I will engage him with a sentence of considerable length, a sentence that burns with energy and builds with all the impetus of a crescendo, the roll of the drums, the crash of the cymbals — sounds that say listen to this, it is important.

Verlyn Klinkenborg in *Several Short Sentences About Writing*: *"Your job as a writer is making sentences."* The unit is the sentence, not the paragraph.

Mix 3-word sentences with 30-word sentences in the same paragraph. Drop a fragment. Start one with "And."

### 2.5 Strong opinions — refuse to hedge

The internet writing canon — Graham, patio11, Thompson, Cegłowski — all share one trait: they take a position. Ben Thompson built Stratechery on this. His Aggregation Theory wasn't a survey; it was a claim. Critics dislike him because he *"makes pronouncements."* That's the point.

GPTZero's writing guide: *"Take a position, even if small. Even a single sentence where you say what you actually think. AI tends to hedge and not take a brave stance."*

Connected idea: **earned insight.** The problem with platitudes ("be in the moment," "follow your passion") is that they're unearned — abstractions detached from any specific experience. *"Just be in the moment"* is unearned. *"I noticed the bathroom tile had a crack shaped like Florida and realized I'd been holding my breath for ninety seconds"* is earned, even though it's saying the same thing.

### 2.6 Informal markers — contractions, slang, fragments, swearing

The cluster AI tends to skip: contractions, fragments, sentences starting with "And" or "But," mild profanity, in-group slang, occasional all-caps for emphasis.

Anne Lamott titled the most famous chapter of *Bird by Bird* "Shitty First Drafts" — the swear is the point. Cegłowski: visitors to Argentina end up *"writing YOU JUST DON'T UNDERSTAND in all caps more often than feels comfortable."* That sentence is unmistakably human because of the all-caps interruption and the dry *"more often than feels comfortable"* tacked on.

The signature of human voice is the small, specific mannerism. Bro. Dope. Brutal. Fair enough. Whatever yours is — use it.

### 2.7 Self-interruption — parentheticals, dashes, asides

Em dashes feel naturalistic *because we talk in loops and asides.* Drop in a side comment as if you've just thought of it. Patio11 does this constantly. Graham uses footnotes for the same purpose.

(Warning: if you have more than two em dashes per screen, you're using it as a crutch — and you're walking straight into the 2025 meme. Spice, not seasoning.)

### 2.8 Named, specific examples — never generic placeholders

Cegłowski doesn't say "a country in South America." He says Argentina. He doesn't say "a local food." He says a *bife de chorizo*. Patio11 names Stripe, ACH, the OCC. Thompson names the company, the quarter, the exact tweet.

Specificity *is* credibility. "Leading platform," "various stakeholders," "many companies" reads as a writer who hasn't done the work or won't commit.

### 2.9 Pacing — open mid-action, don't summarize the ending

Open *in medias res*. Start at the moment of highest drama or specific detail, not at the beginning of context. Cegłowski opens "Argentina on Two Steaks a Day" with a steak, not a thesis about Argentine cuisine.

On endings: don't restate. Klinkenborg: *"Say less than you could and let your readers form their own thoughts."* Graham's version: *"Recognize and seize natural endings."* When the essay is done, stop. Don't ribbon-bow it. Don't write "In conclusion." Stop on the strongest sentence and trust the reader.

### 2.10 Prose over bullets — connective tissue is the writing

Luke Gearing: *"While regular prose uses linking words to connect ideas, bullet points strip all of them away, making it impossible to say unequivocally how ideas relate to each other."*

A listicle is a compromise with the reader's attention. Prose is an argument that the connections matter. Graham, patio11, Thompson, Cegłowski — none write in bullets. They write paragraphs that turn. The transition word *but* is doing work no bullet point can.

Use bullets only for genuinely parallel items, not for *"ideas I haven't bothered to connect."*

### 2.11 The Twitter-thread micro-form

Even for long-form writers, the thread form taught one lesson: the opening line is non-negotiable. The hook either (1) makes a bold specific claim that challenges an assumption, (2) promises a concrete benefit, or (3) opens a story loop the reader feels compelled to close.

The closing punch is what separates a thread that's shared from one that's scrolled past. Same for essays. The last line is the line the reader will quote. Make it earn that.

---

## Part 3 — Quick Reference Cards

### The "cut these" list

| Pattern | Example | Fix |
|---|---|---|
| Container nouns | landscape, realm, tapestry, ecosystem | name the actual thing |
| Inflated adjectives | pivotal, robust, vibrant, seamless | name a concrete attribute |
| Abstract verbs | delve, leverage, harness, navigate | use the plain verb |
| Hedge openers | "It's important to note…" | just say it |
| Sycophantic openers | "Great question!" | skip |
| Balance template | "It's not X, it's Y" | make one direct claim |
| Audience-bracketing | "Whether you're a seasoned X…" | skip |
| Significance puffery | "stands as a testament to…" | show why it matters |
| In conclusion / Ultimately | any of them | stop on the best sentence |
| Triplet lists | "fast, reliable, scalable" | use 2 or 4, vary form |
| Em dash overuse | 3+ per paragraph | cut by ~60% |
| Title Case Headings | every word capitalized | sentence case |
| Bold every key term | for emphasis | trust the reader |
| Perfect punctuation in casual writing | no fragments, no splices | let the rough edges in |
| Weasel attributions | "experts argue" | cite or drop |
| Travel-brochure voice | "nestled in the heart of…" | be specific |

### The "do these" list

| Move | One-line rule |
|---|---|
| Voice | Write like you'd talk to your cofounder |
| Specificity | Name the thing — the bench, the steak, the bank |
| Show, don't tell | Description finishes in the reader's imagination |
| Rhythm | Short. Then a long one with a crescendo. Then a fragment. |
| Strong takes | Say what you actually think, in one sentence |
| Informal markers | Contractions, fragments, swearing, slang you actually use |
| Self-interruption | Asides for the way you actually think — sparingly |
| Named examples | Real numbers, real names, real studies |
| Pacing | Open mid-scene, don't summarize the ending |
| Earned insight | Ground every abstraction in one moment only you could write |
| Prose over bullets | Linking words *are* the argument |
| Strong last line | The last sentence is the one the reader will quote |

### Stylometric self-audit

Run these on your own draft before posting:

1. **Sentence-length stdev** — should be >10 words. If every sentence is 15–25 words, rewrite at least three.
2. **Em-dash count** — under 1 per 250 words for most voices.
3. **Triplet count** — search for ", and " patterns. If every list is 3 items, break some.
4. **Transitional openers** — if more than half your paragraphs open with Moreover/Furthermore/However/Additionally, cut them all.
5. **"It's not X, it's Y" search** — should be zero.
6. **Vocabulary check** — search for delve, tapestry, landscape, realm, robust, pivotal, leverage, navigate, underscore, showcase, foster. Each one is a flag.
7. **Bold/heading audit** — would a human editor bold this term, or did you do it because the section "needed structure"?
8. **First-line test** — does it start in the middle of a thought or with a thesis statement? If the latter, cut it.
9. **Last-line test** — does it summarize, or does it land? If it summarizes, cut it.

---

## Part 4 — Notable Sources

### The discourse arc, 2024 → 2026

- **April 2024** — Paul Graham's "delve" tweet ([x.com/paulg/1777035484826349575](https://x.com/paulg/status/1777035484826349575))
- **Feb 2025** — Paul Skallas's em-dash tweet, 3.7M views ([knowyourmeme.com/memes/chatgpt-em-dash](https://knowyourmeme.com/memes/chatgpt-em-dash))
- **April 2025** — OpenAI rolls back GPT-4o sycophancy ([openai.com/index/expanding-on-sycophancy](https://openai.com/index/expanding-on-sycophancy/))
- **Aug 2025** — Washington Post, "People are starting to talk like ChatGPT"
- **Aug 2025** — Rolling Stone, "The ChatGPT Hyphen"
- **Aug 2025** — McSweeney's, "The Em Dash Responds to the AI Allegations"
- **Nov 2025** — OpenAI ships em-dash fix; Altman tweets the announcement
- **Nov 2025** — NYT Modern Love "AI slop" callout (Kate Gilgan)
- **2026** — Bloomberg covers emoji-bullet LinkedIn detection; Pangram's "slop janitor" timelines on X

### The canonical references

- **Wikipedia: Signs of AI writing** — the most rigorous corpus-based catalog ([en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing))
- **GPTZero: How AI Detectors Work** — perplexity and burstiness, explained ([gptzero.me/news/how-ai-detectors-work](https://gptzero.me/news/how-ai-detectors-work/))
- **GPTZero: The Rule of Three** ([gptzero.me/news/the-rule-of-three](https://gptzero.me/news/the-rule-of-three/))
- **GPTZero: How to Write Like a Human** ([gptzero.me/news/how-to-write-like-a-human](https://gptzero.me/news/how-to-write-like-a-human/))
- **Futurism: ChatGPT's Weird Way of Talking** — the "not X, it's Y" piece
- **Blake Stockton: Don't Write Like AI** series ([blakestockton.com](https://www.blakestockton.com/))
- **Colin Gorrie: Why ChatGPT writes like that** ([deadlanguagesociety.com/p/rhetorical-analysis-ai](https://www.deadlanguagesociety.com/p/rhetorical-analysis-ai))

### Academic / detector research

- **DetectGPT** (Mitchell et al., 2023) — arXiv 2301.11305
- **Watermarking** (Kirchenbauer et al., 2023) — arXiv 2301.10226
- **StyloAI** — arXiv 2405.10129
- **GPT detectors are biased against non-native English writers** — arXiv 2304.02819
- **Flattering to Deceive** (sycophancy and trust) — arXiv 2412.02802
- **Delving Into PubMed Records** — PMC12679996

### Writers worth studying

- **Paul Graham** — [paulgraham.com/writing44.html](https://www.paulgraham.com/writing44.html), [paulgraham.com/goodwriting.html](https://paulgraham.com/goodwriting.html)
- **Patrick McKenzie (patio11)** — [kalzumeus.com/greatest-hits](https://www.kalzumeus.com/greatest-hits/), [bitsaboutmoney.com](https://www.bitsaboutmoney.com/)
- **Maciej Cegłowski** — [idlewords.com](https://idlewords.com/about.htm), especially "Argentina on Two Steaks a Day"
- **Mandy Brown** — [aworkinglibrary.com](https://aworkinglibrary.com/about/)
- **Venkatesh Rao** — [ribbonfarm.com](https://www.ribbonfarm.com/about/)
- **Ben Thompson** — [stratechery.com](https://stratechery.com/)
- **Anne Lamott**, *Bird by Bird* — "Shitty First Drafts"
- **Verlyn Klinkenborg**, *Several Short Sentences About Writing*
- **Stephen King**, *On Writing*
- **Strunk & White**, *The Elements of Style*
- **Gary Provost**, "This Sentence Has Five Words"

---

## The one-paragraph distillation

The AI tells reduce to one thing: **smoothness**. Smooth vocabulary (the same 50 inflated words), smooth structure (rule of three, balanced paragraphs, perfect parallelism), smooth punctuation (em dashes everywhere, perfect Oxford commas), smooth tone (relentless positivity, no opinions, no friction). The fix isn't to memorize a banned-words list. The fix is to be productively rough — short sentence next to long, fragment next to clause, one rare word per paragraph, one strong opinion per piece, one specific named example per claim, one moment from your actual life. Open mid-thought. End on the strongest sentence. Don't summarize. Don't ribbon-bow it. Stop.
