+++
title = "Open-source Software & Datasets"
template = "page.html"
[extra]
header_class = "softwares-header"
content_style = "style1"
+++

<div class="container 75%">
<ul class="actions">
    <li><a href="#softs" class="button alt" alt="Go to the software section"><i class="fa fa-arrow-right" aria-hidden="true"></i> Open-source Software</a></li>
    <li><a href="#datasets" class="button alt" alt="Go to the dataset section"><i class="fa fa-arrow-right" aria-hidden="true"></i> Datasets</a></li>
</ul>

</div>

<a name="softs"></a>
<article >
    <div class="container 75%">
        <h2>Open-source software</h2>
        <p>
        I develop and maintain several scientific software
        related to robotics. They are all open-source, usually
        under a permissive license (often BSD).
        </p>

        <p>
        The projects listed on this page the one I consider the
        more useful to a community. Check my <a
        href="https://github.com/severin-lemaignan/"
        alt="GitHub page">GitHub page</a> for the complete
        list of my other software projects.
        </p>
    </div>
</article>

<article class="feature right">
    <span class="image"><img src="/images/softwares/morse.jpg" alt="" /></span>
    <div class="content">
        <h2>MORSE</h2>
        <p>
        MORSE is an generic simulator for academic robotics. It
        focuses on realistic simulation of small to large
        environments, indoor or outdoor, with one to over a
        dozen of autonomous robots.
        </p>
        <p>
        We created the project in 2007 with Arnaud Degroote,
        and since then, 40 people from more than 15 institution
        worldwide have contributed. With Gazebo, it is today one of the
        major open-source robotic simulators.
        </p>

        <ul class="actions small">
            <li><a class="button special icon fa-external-link" href="http://morse-simulator.github.io/" alt="Homepage">Homepage</a></li>
            <li><a class="button icon fa-github-square" href="https://github.com/morse-simulator" alt="Repository">GitHub repository</a></li>
        </ul>

        <h4>Related publications:</h4>
        <ul class="alt">
            <li><a href="/publications/#lemaignan2014simulation">Simulation and HRI - Recent Perspectives with [...]</a></li>
            <li><a href="/publications/#echeverria2012simulating">Simulating complex robotic scenarios with MORSE</a></li>
            <li><a href="/publications/#echeverria2011morse">Modular Open Robots Simulation Engine: MORSE</a></li>
        </ul>

    </div>

</article>
<a href="#softs" class="back-to-top icon fa-level-up"> back to top</a>


<article class="feature left">
    <span class="image"><img src="/images/softwares/gazr.jpg" alt="" /></span>
    <div class="content">
        <h2>gazr</h2>
        <p>
        <em>gazr</em> is a library and a set of tool for real-time gaze
        estimation from simple monocular cameras like regular
        webcams.
        </p>

        <p>
        It performs 6D head pose estimation and pupil tracking.
        </p>

        <ul class="actions small">
            <li><a class="button icon fa-github-square" href="https://github.com/severin-lemaignan/gazr" alt="Repository">GitHub repository</a></li>
        </ul>

        <h4>Related publication:</h4>
        <ul class="alt">
            <li><a href="/publications/#lemaignan2016realtime">From Real-Time Attention Assessment to "With-me-ness"</a></li>
        </ul>

    </div>

</article>
<a href="#softs" class="back-to-top icon fa-level-up"> back to top</a>

<article class="feature right">
    <span class="image"><img src="/images/softwares/dialogs.png" alt="" /></span>
    <div class="content">
        <h2>dialogs</h2>
        <p>
        <em>dialogs</em> is a simple natural language processor
        designed for robots to dialog with humans. It parses
        English, tries to make sense of the sentences using a
        semantic backend (an RDF knowledge base), and answers
        both in plain English and with RDF statements.
        </p>

        <ul class="actions small">
            <li><a class="button icon fa-github-square" href="http://github.com/severin-lemaignan/dialogs" alt="Repository">GitHub repository</a></li>
        </ul>

        <h4>Related publications:</h4>
        <ul class="alt">
            <li><a href="/publications/#lemaignan2011grounding">Grounding the Interaction: Anchoring Situated Discourse in [...]</a></li>
            <li><a href="/publications/#lemaignan2011what">What are you talking about? Grounding dialogue in a [...]</a></li>
        </ul>

    </div>

</article>
<a href="#softs" class="back-to-top icon fa-level-up"> back to top</a>


<article class="feature left">
    <span class="image"><img src="/images/softwares/oroview.jpg" alt="" /></span>
    <div class="content">
        <h2>ORO / minimalKB</h2>
        <p>
        <em>ORO</em>, and its lightweight successor
        <em>minimalKB</em>, are RDF-based knowledge bases: they behave like (SQL) databases, but manipulate instead semantic RDF statements. They also support a range of advanced queries useful to implement high-level cognitive functions in robots. In particular, <em>ORO</em> and <em>minimalKB</em> have been used to <a href="/publications/#warnier2012when">implement Theory-of-Mind like</a> behaviours.
        
        </p>

        <ul class="actions small">
            <li><a class="button icon fa-github-square" href="http://github.com/severin-lemaignan/minimalkb" alt="Repository">GitHub repository</a></li>
        </ul>

        <h4>Related publication:</h4>
        <ul class="alt">
            <li><a href="/publications/#lemaignan2010oro">ORO, a Knowledge Management Module for Cognitive [...]</a></li>
        </ul>

    </div>

</article>
<a href="#softs" class="back-to-top icon fa-level-up"> back to top</a>


<article class="feature right">
    <span class="image"><img src="/images/softwares/pyrobots.png" alt="" /></span>
    <div class="content">
        <h2>pyrobots</h2>
        <p>
        <em>pyRobots</em> is a toolkit for the high-level
        programming of interactive robots in Python. It
        provides a set of Python decorators to easily turn
        standard functions into background tasks which can be
        cancelled at anytime and to make your controller aware
        of the hardware resource (for instance, to ensure two
        tasks are not controlling the same motor at the same
        time).
        </p>

        <p>
        It also provides a event-based mechanism to monitor
        specific conditions and asynchronously trigger actions.
        </p>

        <p>
        It finally provides a library of convenient tools to
        manage poses in a uniform way (quaternions, Euler
        angles and 4D matrices, I look at you) and to interface
        with existing middlewares (ROS, naoqi, aseba...).
        </p>

        <ul class="actions small">
            <li><a class="button icon fa-github-square" href="https://github.com/chili-epfl/pyrobots" alt="Repository">GitHub repository</a></li>
        </ul>

        <h4>Related publication:</h4>
        <ul class="alt">
            <li><a href="/publications/#lemaignan2015pyrobots">pyRobots: a Toolset for Robot Executive Control</a></li>
        </ul>

    </div>

</article>
<a href="#softs" class="back-to-top icon fa-level-up"> back to top</a>

<section id="datasets" class="wrapper style2">
    <div class="inner">

        <a name="datasets"></a>
        <article >
            <div class="container 75%">
                <h2>Open Datasets</h2>
            </div>
        </article>

        <article class="feature right">
            <span class="image"><img src="/images/softwares/pinsoro.jpg" alt="Some of the children in the PInSoRo dataset" /></span>
            <div class="content">
                <h2>PInSoRo</h2>
                <p> The <strong>PInSoRo dataset</strong> (also known as
                the <emph>Freeplay-sanbox dataset</emph>) is a large,
                open-data dataset of child-child and child-robot
                interactions.
                </p>
                <p>
                120 children were recorded while freely playing with a
                peer or with a robot, for a total of <strong>45+ hours
                of RGB-D, audio and interaction data</strong>. Besides,
            the recordings are annotated with <strong>115000+ social
                behaviours</strong> including constructs like
            <emph>solitary vs cooperative</emph> play, <emph>prosocial
            vs adversarial behaviours</emph>, etc.
                </p>

                <ul class="actions small">
                    <li><a class="button special icon fa-external-link" href="http://freeplay-sandbox.github.io/" alt="Homepage">Homepage</a></li>
                    <li><a class="button icon" href="https://zenodo.org/record/1043508" alt="Repository">The dataset on Zenodo</a></li>
                </ul>

                <h4>Related publications:</h4>
                <ul class="alt">
                    <li><a href="https://doi.org/10.1371/journal.pone.0205999">The PInSoRo dataset: Supporting the data-driven study of [...]</a></li>
                    <li><a href="https://arxiv.org/abs/1712.02421">The Free-play Sandbox: a Methodology for the Evaluation of [...]</a></li>
                </ul>

            </div>

        </article>
        <a href="#dataset" class="back-to-top icon fa-level-up"> back to top</a>


        <article class="feature left">
            <span class="image"><img src="/images/softwares/child-speech.png" alt="" /></span>
            <div class="content">
                <h2>Child Speech Recognition</h2>
                <p>
                This dataset comprises of audio recordings of 11 native
                English-speaking children. The dataset contains a
                variety of sentences (along with the transcriptions),
                including 200+ free speech utterances. Recordings were
                performed in real-world situation (in schools), using
                different type of microphones as well.
                </p>

                <ul class="actions small">
                    <li><a class="button icon" href="https://zenodo.org/record/200495" alt="Repository">The dataset on Zenodo</a></li>
                </ul>

                <h4>Related publications:</h4>
                <ul class="alt">
                    <li><a href="/publications/#kennedy2017child">Child Speech Recognition in Human-Robot Interaction: Evaluations and Recommendations</a></li>
                </ul>

            </div>

        </article>
        <a href="#datasets" class="back-to-top icon fa-level-up"> back to top</a>

    </div>
</section>
