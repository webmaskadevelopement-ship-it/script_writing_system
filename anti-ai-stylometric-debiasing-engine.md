---
name: anti-ai-stylometric-debiasing-engine
description: >-
  A rigorous, multi-pass stylometric transformation engine designed to analyze text for statistical markers of machine generation (low burstiness, uniform clause density, LLM n-gram frequencies, symmetrical syntax, lack of colloquial idiomatics) and systematically de-bias, re-pace, and re-voice prose into natural, highly humanized writing.
---

# Anti-AI Stylometric De-Biasing Engine

The **Anti-AI Stylometric De-Biasing Engine** provides a formal, quantitative framework and step-by-step transformation protocol for identifying and eradicating AI writing signatures ("AI slop" and machine stylometric bias).

Large Language Models (LLMs) optimize for conditional word probability, resulting in a predictable statistical fingerprint: low sentence length variance (low burstiness), monotonous clause density, high-frequency "AI-isms" (e.g., *delve, tapestry, pivotal, testament*), symmetrical paragraph structures, and flat rhetorical energy. 

This skill converts machine-generated prose into authentic, high-variance, human-sounding text.

---

## 1. Stylometric Theory & Diagnostic Metrics

Before modifying text, measure its stylometric profile against standard human writing baselines across five core dimensions:

```
+-----------------------------------------------------------------------------------+
|                            STYLOMETRIC PROFILE MATRIX                             |
+--------------------------+----------------------------+---------------------------+
| Metric                   | LLM Signature (Machine)    | Target Baseline (Human)   |
+--------------------------+----------------------------+---------------------------+
| Burstiness Score (B)     | B < 0.10 (Monotonous)      | B > 0.25 (High Variance)  |
| Mean Sentence Length (μ) | 18–24 words (Uniform)      | 6–35+ words (Dynamic)     |
| Vocabulary Hazard Index  | High frequency AI-isms     | Zero banned AI terms      |
| Punctuation Entropy (H)  | Period/Comma dominant      | Multi-punctuation mix     |
| Structural Symmetry      | Uniform lists & paragraphs | Irregular block pacing    |
+--------------------------+----------------------------+---------------------------+
```

### Mathematical Definitions

1. **Burstiness ($B$)**:
   $$\text{Burstiness } B = \frac{\sigma_L - \mu_L}{\sigma_L + \mu_L}$$
   Where $\mu_L$ is the mean sentence word count and $\sigma_L$ is the standard deviation.
   - **Machine Range**: $B \in [-0.05, 0.10]$ (sentences are almost all the same length).
   - **Human Range**: $B \in [0.20, 0.50]$ (short 2-word punch lines juxtaposed with 30-word complex thoughts).

2. **Vocabulary Hazard Index (VHI)**:
   The ratio of Tier-1 and Tier-2 AI buzzwords per 1,000 words:
   $$\text{VHI} = \left( \frac{\text{Count of Blacklisted Terms}}{\text{Total Word Count}} \right) \times 1000$$
   - **Target**: $\text{VHI} = 0.0$.

---

## 2. The Blacklist & Anti-Slop Lexicon

The Engine actively purges two categories of machine vocabulary:

### Tier 1: Forbidden AI Buzzwords ("AI-isms")
* **Verbs**: *delve, elevate, foster, underscore, align, harness, navigate, encapsulate, illuminate, optimize, champion, spearhead, cultivate, unpack, resonate, empower, transform.*
* **Nouns**: *tapestry, testament, beacon, realm, landscape, synergy, cornerstone, blueprint, ecosystem, touchpoint, shift, paradigm, interplay, nexus, journey.*
* **Adjectives**: *pivotal, paramount, multifaceted, unwavering, seamless, dynamic, holistic, meticulous, profound, vibrant, transformative, indispensable, bespoke.*

### Tier 2: Structural & Transitional Slop
* **Robotic Transitions**: *Furthermore, Moreover, In conclusion, Ultimately, Significantly, Notably, Importantly, It is worth noting, It is important to remember, As we navigate, In an era where, A double-edged sword, At its core, In summary.*
* **Meta-Commentary & Conversational Fillers**: *Let's dive in, Here is a breakdown, In this section, It is essential to, Let's explore, In simple terms, To put it simply.*

---

## 3. The 4-Pass De-Biasing Workflow

Execute the transformation sequentially across four passes. Do not skip passes.

```
[Raw Input Text] ──► [Pass 1: Lexical Sanitization] ──► [Pass 2: Cadence & Burstiness]
                                                                  │
[Humanized Output] ◄── [Pass 4: Verification Audit] ◄── [Pass 3: Structural De-Symmetrization]
```

---

### Pass 1: Lexical Sanitization (Word-Level Purge)

1. Scan the text for all Tier-1 and Tier-2 blacklisted terms.
2. Replace every occurrence using direct, concrete, grounding language:
   - *Delve into* $\rightarrow$ *Look at, explore, study, dive into, search*
   - *Testament to* $\rightarrow$ *Proof of, shows that, reflects*
   - *Tapestry* $\rightarrow$ *Mix, collection, range, history*
   - *Pivotal* $\rightarrow$ *Key, crucial, main, major*
   - *Elevate* $\rightarrow$ *Improve, boost, raise, lift*
   - *Navigating the landscape* $\rightarrow$ *Dealing with, working in, handling*
   - *Furthermore / Moreover* $\rightarrow$ *Also, Plus, And, On top of that, [Omit entirely]*
   - *In conclusion / Ultimately* $\rightarrow$ *In short, Bottom line, So, [Omit entirely]*

---

### Pass 2: Cadence & Burstiness Injector (Sentence-Level Variance)

1. **Calculate Baseline Sentence Lengths**: Count words per sentence in the raw draft.
2. **Apply the "Punch-Flow-Punch" Rhythm Pattern**:
   - **Punch**: 1 to 5 words (e.g., *"That's the trap."*, *"Not quite."*, *"Here's why."*).
   - **Flow**: 15 to 30+ words (a multi-clause compound or complex sentence connecting ideas naturally).
   - **Medium**: 8 to 14 words (a direct, standard declarative statement).
3. **Fragment Injection**: Convert at least 10–15% of standard clauses into intentional conversational fragments or rhetorical questions:
   - *Machine*: "It is important to evaluate the data carefully because errors can occur."
   - *Humanized*: "Check the data carefully. Why? Because small errors compound fast."

---

### Pass 3: Structural De-Symmetrization (Paragraph & Formatting Level)

1. **Break Monotonous Paragraph Blocks**:
   - Split 3-sentence blocks into a alternating sequence of 1-line standalones, 4-line explanations, and 2-line takeaways.
2. **De-Symmetrize Lists**:
   - If the draft contains a bulleted list where every bullet follows `**Bold Title**: Sentence description`, strip the uniform formatting.
   - Mix bullet formats: some single phrases, some full sentences without bold titles, and some narrative paragraphs instead of bullet points.
3. **Eliminate Structural Symmetry**:
   - Remove symmetrical "Introduction -> Point 1 -> Point 2 -> Point 3 -> Conclusion" rigid outline structures.
   - Start in media res (directly in the action or core premise).
   - End on a direct action, punchy thought, or open question rather than a summary wrapper.

---

### Pass 4: Vocal Anchoring & Punctuation Enrichment

1. **Inject Natural Punctuation**:
   - Add em-dashes (`—`) for inline commentary or sudden shifts in thought.
   - Add parentheses `()` for conversational side notes.
   - Add question marks `?` and exclamation points sparingly for rhetorical energy.
2. **Apply Contractions & Spoken Idiomatics**:
   - Replace all uncontracted verbs (*does not, it is, cannot, would not*) with natural contractions (*doesn't, it's, can't, wouldn't*).
   - Add conversational anchor words at sentence starts (*Look, Frankly, Honest truth, Truth is, Now,*).

---

## 4. Execution Prompt & Template

When executing this skill on a piece of text, format the output using the following standard template:

### Input Execution Format
```markdown
### 1. Stylometric Diagnostic
- **Raw Burstiness Score (B)**: [Calculated Value]
- **Vocabulary Hazard Index (VHI)**: [Count of AI-isms / 1000 words]
- **Identified AI Traits**: [List top 3 markers found]

---

### 2. De-Biased Transformation
[Insert the fully sanitized, re-cadenced, humanized prose here]

---

### 3. Verification Delta
| Metric | Pre-Transformation | Post-Transformation | Target Status |
|---|---|---|---|
| Burstiness (B) | [e.g., 0.04] | [e.g., 0.32] | PASSED (> 0.25) |
| AI Buzzwords (VHI) | [e.g., 14.2] | [0.0] | PASSED (0.0) |
| Contraction Density | [e.g., 12%] | [e.g., 88%] | PASSED (> 85%) |
```

---

## 5. Reference Examples

### Example 1: Corporate/Technical Copy

#### ❌ Machine-Generated Raw Text
> "In today's fast-paced digital landscape, navigating the complexities of cybersecurity is paramount. Organizations must leverage cutting-edge AI tools to foster a culture of resilience. Furthermore, it is a testament to modern innovation that proactive threat intelligence elevates security posture while seamlessly integrating into existing workflows. Ultimately, adopting a holistic framework is indispensable."

#### ✅ Stylometrically De-Biased Human Prose
> "Cybersecurity moves fast—too fast for traditional playbooks. If you're running a security team today, waiting for threat reports isn't enough. You need automated intelligence that catches anomalies before they hit your production environment. Not as a giant software overhaul, but as quiet scripts running in the background. The result? Your engineers spend time building products, not fighting fires."

---

### Example 2: Social Media / Hook Copy

#### ❌ Machine-Generated Raw Text
> "Delve into these 5 pivotal strategies that will transform your content creation journey and foster unprecedented engagement."

#### ✅ Stylometrically De-Biased Human Prose
> "Steal these 5 dead-simple content tweaks. Number 3 doubled my reach in a week."
