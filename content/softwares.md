+++
title = "Open-source Software & Datasets"
template = "page.html"
[extra]
header_class = "softwares-header"
content_style = "style1"
+++

{{ btn(label="Open-source Software", target="#softs") }} {{ btn(label="Datasets", target="#datasets") }}

<a name="softs"></a>

## Open-source software

I develop and maintain several scientific software related to robotics. They are all open-source, usually under a permissive license (often BSD).

The projects listed on this page the one I consider the more useful to a community. Check my [GitHub page](https://github.com/severin-lemaignan/) for the complete list of my other software projects.

---

{% card(image="/images/softwares/morse.jpg", side="right") %}
## MORSE

MORSE is an generic simulator for academic robotics. It focuses on realistic simulation of small to large environments, indoor or outdoor, with one to over a dozen of autonomous robots.

We created the project in 2007 with Arnaud Degroote, and since then, 40 people from more than 15 institution worldwide have contributed. With Gazebo, it is today one of the major open-source robotic simulators.

- [Homepage](http://morse-simulator.github.io/)
- [GitHub repository](https://github.com/morse-simulator)

### Related publications:

- [Simulation and HRI - Recent Perspectives with [...]](/publications/#lemaignan2014simulation)
- [Simulating complex robotic scenarios with MORSE](/publications/#echeverria2012simulating)
- [Modular Open Robots Simulation Engine: MORSE](/publications/#echeverria2011morse)
{% end %}

{% card(image="/images/softwares/gazr.jpg", side="left") %}
## gazr

*gazr* is a library and a set of tool for real-time gaze estimation from simple monocular cameras like regular webcams.

It performs 6D head pose estimation and pupil tracking.

- [GitHub repository](https://github.com/severin-lemaignan/gazr)

### Related publication:

- [From Real-Time Attention Assessment to "With-me-ness"](/publications/#lemaignan2016realtime)
{% end %}

{% card(image="/images/softwares/dialogs.png", side="right") %}
## dialogs

*dialogs* is a simple natural language processor designed for robots to dialog with humans. It parses English, tries to make sense of the sentences using a semantic backend (an RDF knowledge base), and answers both in plain English and with RDF statements.

- [GitHub repository](http://github.com/severin-lemaignan/dialogs)

### Related publications:

- [Grounding the Interaction: Anchoring Situated Discourse in [...]](/publications/#lemaignan2011grounding)
- [What are you talking about? Grounding dialogue in a [...]](/publications/#lemaignan2011what)
{% end %}

{% card(image="/images/softwares/oroview.jpg", side="left") %}
## ORO / minimalKB

*ORO*, and its lightweight successor *minimalKB*, are RDF-based knowledge bases: they behave like (SQL) databases, but manipulate instead semantic RDF statements. They also support a range of advanced queries useful to implement high-level cognitive functions in robots. In particular, *ORO* and *minimalKB* have been used to [implement Theory-of-Mind like](/publications/#warnier2012when) behaviours.

- [GitHub repository](http://github.com/severin-lemaignan/minimalkb)

### Related publication:

- [ORO, a Knowledge Management Module for Cognitive [...]](/publications/#lemaignan2010oro)
{% end %}

{% card(image="/images/softwares/pyrobots.png", side="right") %}
## pyrobots

*pyRobots* is a toolkit for the high-level programming of interactive robots in Python. It provides a set of Python decorators to easily turn standard functions into background tasks which can be cancelled at anytime and to make your controller aware of the hardware resource (for instance, to ensure two tasks are not controlling the same motor at the same time).

It also provides a event-based mechanism to monitor specific conditions and asynchronously trigger actions.

It finally provides a library of convenient tools to manage poses in a uniform way (quaternions, Euler angles and 4D matrices, I look at you) and to interface with existing middlewares (ROS, naoqi, aseba...).

- [GitHub repository](https://github.com/chili-epfl/pyrobots)

### Related publication:

- [pyRobots: a Toolset for Robot Executive Control](/publications/#lemaignan2015pyrobots)
{% end %}

<a name="datasets"></a>

## Open Datasets

---

{% card(image="/images/softwares/pinsoro.jpg", side="right") %}
## PInSoRo

The **PInSoRo dataset** (also known as the *Freeplay-sanbox dataset*) is a large, open-data dataset of child-child and child-robot interactions.

120 children were recorded while freely playing with a peer or with a robot, for a total of **45+ hours of RGB-D, audio and interaction data**. Besides, the recordings are annotated with **115000+ social behaviours** including constructs like *solitary vs cooperative* play, *prosocial vs adversarial behaviours*, etc.

- [Homepage](http://freeplay-sandbox.github.io/)
- [The dataset on Zenodo](https://zenodo.org/record/1043508)

### Related publications:

- [The PInSoRo dataset: Supporting the data-driven study of [...]](https://doi.org/10.1371/journal.pone.0205999)
- [The Free-play Sandbox: a Methodology for the Evaluation of [...]](https://arxiv.org/abs/1712.02421)
{% end %}

{% card(image="/images/softwares/child-speech.png", side="left") %}
## Child Speech Recognition

This dataset comprises of audio recordings of 11 native English-speaking children. The dataset contains a variety of sentences (along with the transcriptions), including 200+ free speech utterances. Recordings were performed in real-world situation (in schools), using different type of microphones as well.

- [The dataset on Zenodo](https://zenodo.org/record/200495)

### Related publications:

- [Child Speech Recognition in Human-Robot Interaction: Evaluations and Recommendations](/publications/#kennedy2017child)
{% end %}
