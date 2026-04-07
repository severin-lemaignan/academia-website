+++
title = "My Research"
template = "page.html"
[extra]
header_class = "research-header"
content_style = "style1"
+++


{% card(image="/images/social-cognition.webp", side="right") %}

I focus my research on **Artificial Cognition for Socially Intelligent Robots**. My
work addresses several fundamental questions like:

- **How can robots build sophisticated mental models** and maintain
**socio-physical situation awareness of their human partners?**

- **What socio-cognitive architectures favor the long-term, responsible
acceptance of robots in human environments?**

By bridging cognitive psychology with robotics and artificial intelligence, I
explore the psychological determinants (such as Theory of Mind) that
influence our relationships with embodied AI.

{% end %}

{% card(image="/images/social-embeddings.png", side="left") %}

My recent work explores **how robots can understand and represent social
situations**. I introduced the concept of **[Social
Embeddings](/publications#lemaignan2024social)**: compact, semantics-preserving
representations of social situations that leverage **large language models to
encode the dynamics of human interactions** into vector spaces. This enables
robots to quantitatively compare and recognise the social scenarios they
encounter. I also investigate **[context-aware affect
recognition](/publications#mohamed2024context)** using sentence embeddings to
distinguish socially appropriate from inappropriate interactions, and
**[multi-modal affect detection](/publications#mohamed2023multimodal)** combining
thermal imaging with facial action units for non-intrusive emotion recognition.

{% end %}

{% card(youtube="https://www.youtube.com/embed/E_iozVysl5g", side="left") %}

I validate my research through extensive **real-world deployments**, including
lifelong co-design with users in public spaces like **schools** and
**hospitals**.

I have shown how social robots can **[support autistic
children](/publications#lemaignan2022social)** through a three-week school
deployment co-designed with children and teachers, or help **[children
struggling with handwriting](/publications#hood2015when)**. My work on
**[socially assistive robots in geriatric
care](/publications#pineda2025socially)** (notably the EU SPRING project
deploying an ARI robot at a Paris hospital) demonstrates how **[LLM-enhanced
dialogue](/publications#blavette2025llm)** significantly improves patient
acceptability and engagement. I have also explored **[participatory
co-design](/publications#gebelli2024codesigning)** and **[end-to-end
participatory design](/publications#winkle2021leador)** methodologies to ensure
robots are shaped by the people who use them.


{% end %}

{% card(video="/images/emotions.mp4", side="right") %}

A core pillar of my work is the creation of **open-source software standards and
tools**. I am the **lead architect and maintainer of
[ROS4HRI](@/softwares.md#ros4hri)** (ROS REP-155), the **first international
software standard for Human-Robot Interaction**, now adopted by major research
projects across Europe. Building on ROS4HRI, I have developed with Lorenzo Ferrini novel
**[spatially-grounded semantic
representations](/publications#ferrini2025vdb)** (reMap), **[multi-modal
saliency maps for robot attention](/publications#ferrini2025percepts)**, and the
**[Mr. Potato algorithm](/publications#lemaignan2024probabilistic)** for
probabilistic fusion of detected social features into coherent person models.

{% end %}

{% card(image="/images/safely-tiago.jpg", side="left") %}

**Science should have an impact on society:**
From 2021 to 2025, I led Technology Transfer at **PAL Robotics** as the
**Head of the AI and Social Robotics group**, bridging academic research and
industry. My research underpins the backbone architecture of commercial robots
used globally in healthcare, education, and research -- including the new
**[TIAGo Pro social robot](/publications#cooper2025tiago)** integrating
ROS4HRI, local LLMs, and knowledge-based reasoning. I am also deeply committed
to **[responsible robotics](/publications#araizaillan2025roadmap)**: I
co-authored the *Roadmap for Responsible Robotics* and lead critical
examinations of the societal implications of humanoid robots, including issues
of **[trust, accountability, and
sustainability](/publications#lemaignan2026responsible)**.

{% end %}

{% section(id="curriculum", class="wrapper style2 special") %}
<div class="container 50%">

## Browse [selected talks](/talks/)

## See [my curriculum](/aboutme/#curriculum)

</div>
{% end %}
