PQ-Bits: A Conceptual Framework for Design Lineage and Persistent Recognition

Mohamed Al-Qahiri
Draft 0.1 — September 2026


Status and purpose

PQ-Bits is an early-stage research concept for describing the lineage of innovative designs and preserving recognition across their later reuse. Its immediate research setting is open-source software, where designs, version histories, dependencies, and contributions are comparatively observable.


PQ-Bits is not a currency, payment token, debt instrument, or charge on copying. It is conceived as an informational and recognition layer attached to design evidence. It would add no restriction beyond the applicable open-source licence; its purpose is to make inherited contributions more visible and their recognition more durable.


The concept is one applied component of the innovation-governance branch of the broader L-Exponential Model. This note defines a narrower transitional research direction that can be examined independently of the model's longer-term abundance scenario.


Why open-source software is the first testbed

Open-source software is a useful transitional setting because much of its productive input is digital, reusable at near-zero marginal cost, and publicly inspectable. Repository histories, package manifests, dependency graphs, releases, issue discussions, and contributor records offer evidence that is rarely available for physical products.


This visibility does not make contribution or innovation fully measurable. It does, however, make open-source software a suitable environment for testing which parts of design lineage can be observed automatically, which can only be inferred, and which require explicit human declaration.


Core hypothesis

Evidence already present in open-source ecosystems can reconstruct part of the lineage of a software design. When combined with structured contributor attestations, that evidence may support an auditable record that distinguishes:



added design contribution: a new contribution introduced in the design under examination;

inherited design contribution: a contribution incorporated from an earlier design, component, protocol, or implementation;

longitudinal lineage: inheritance across versions, forks, dependencies, or later derivative designs;

lateral lineage: distinct contributions made by collaborators within the same design or development period.


The resulting record could preserve attribution beyond the visibility of the final project and help communities and funders identify earlier contributors and small but consequential components.


Working meaning of PQ-Bits

The name is provisional and project-specific; it does not refer to quantum bits or probabilistic bits. Earlier L-Model materials used Q-Bits as shorthand. This note adds P to emphasize the persistence of recognition through later design lineage and defines the term for this research stage.



Q refers to the quality-bearing information associated with a design contribution.

P refers to persistence: recognition remains linked to a contribution as evidence of that contribution travels through later reuse.

A PQ-Bit is, at this stage, a conceptual unit of evidence-backed design contribution. It is not yet a final mathematical unit, and it should not be equated with file size, byte count, lines of code, computational complexity, popularity, or price.


The research task is therefore not to assume that every design property has already been reduced to one objective number. It is to determine what evidence can support a defensible representation of contribution, inheritance, and recognition, and to mark the limits of that representation.


Relationship to existing mechanisms

PQ-Bits would build on, rather than replace, existing infrastructure. Version-control histories record actions and authorship; SPDX and software bills of materials describe software components and related metadata; Software Heritage persistent identifiers identify archived source artifacts; and CHAOSS contribution-attribution metrics make contributors and forms of contribution more visible. Research on community-generated attribution also shows that explicit acknowledgment can reveal work—such as ideas and bug finding—that commit-based measures overlook (Young et al., 2021).


Emerging proposals such as the draft ATTRIBUTION.md protocol seek a voluntary social signal when AI agents meaningfully reuse open-source code. These mechanisms answer important parts of what was used, who acted, or who should receive a visibility signal. They do not, by themselves, establish how added and inherited design contributions should be represented, how conceptual lineage should be declared, or how uncertainty should constrain recognition and funding decisions. That is the immediate gap PQ-Bits proposes to investigate.


Proposed recognition layer

An initial PQ-Bits record would link a versioned design artifact to several classes of evidence:



Observed evidence — commits, authorship records, package manifests, declared dependencies, release histories, forks, licences, and content-derived identifiers.

Declared evidence — structured statements by designers identifying conceptual influences, reused algorithms, team roles, or contributions that repository data cannot show.

Inferred relationships — similarities or likely lineage suggested by technical analysis but not established as fact.

Disputed or unknown relationships — claims for which the available evidence is incomplete or contested.


These classes must remain distinguishable. An inference should not silently become a verified attribution, and a numerical score should not conceal uncertainty.


The record would represent relationships as a versioned lineage graph. A recognition event would be associated with evidence of meaningful incorporation or design reuse—not with raw downloads, repository stars, ordinary copies, or duplicated lines. Recognition would add attribution to the reused design; it would not impose a financial cost on the user or create a debt owed by a company. Communities or funders might later use the record to issue badges, recognition units, or better-informed support, but those decisions are distinct from the evidence layer itself.


Transitional research questions

The first research stage asks:



Which repository and dependency signals can reliably identify inherited design contributions?

Which forms of added design contribution remain invisible to automated analysis?

When is human declaration necessary, and how can it be recorded and challenged?

How should confidence, uncertainty, conflicting claims, and missing evidence be represented?

How can persistent recognition avoid becoming a proxy for popularity, activity volume, or code quantity?

What information would make a lineage record useful to maintainers, contributors, users, and open-infrastructure funders?


Possible Greenfield pilot

A small pilot could test the framework with two or three openly documented software cases. At least one case should contain explicit package dependencies, while another should involve a harder form of inheritance such as a fork, reimplementation, or declared conceptual influence.


The pilot could produce:



a preliminary nomenclature and open data schema;

a small, inspectable lineage dataset;

a prototype extractor or verification tool;

a matrix distinguishing what is measurable, inferable, declarable, disputed, or unknown;

a simple interface for reviewing and correcting lineage claims; and

recommendations for a later, participant-led Greenfield experiment in which contributors use the schema from the beginning.


The first pilot need not use a blockchain. The prior question is whether the evidence model is useful and credible. An append-only or distributed implementation can be evaluated later if immutability, portability, or cross-platform verification cannot be achieved more simply.


Limits and safeguards

PQ-Bits begins from several constraints:



Repository activity is evidence of recorded action, not a complete account of intellectual contribution.

Algorithmic or syntactic complexity is not equivalent to originality, usefulness, beauty, social benefit, or innovative quality.

Dependencies can be undeclared, vendored, rewritten, generated, or inherited conceptually rather than through a package manager.

Contribution weights may be uncertain or contested, especially in collaborative work.

Recognition systems can be gamed and may reproduce visibility, language, geographic, gender, or institutional biases.

Contributor identity, consent, privacy, and the right to correct a record require explicit governance.

A lineage record does not replace licences, copyright rules, scholarly citation, or community judgment.


Any future metric should expose these limits rather than create false precision. Automated evidence and human judgment should complement one another, and the grounds for every attribution should remain inspectable.


Longer-horizon layers

Innovative-quality layer

Future research may examine whether evidence beyond structural lineage can help evaluate originality, downstream generativity, problem-solving significance, or other dimensions of innovative quality. A proposed Wr weighting mechanism belongs to this later layer. It should remain a hypothesis until its concepts, data, safeguards, and validation method are specified. The present recognition-layer pilot does not claim that innovative quality can already be measured automatically or reduced to code complexity.


Material-lifecycle layer

In the broader abundance-oriented vision, PQ-Bits may eventually connect informational design lineage with machine-readable instructions for fabrication, disassembly, recovery, and reformation of materials. This would link recognition for design contributions with circular material flows. That layer depends on advances in manufacturing, materials science, lifecycle data, and interoperability, and is outside the scope of the present open-source software pilot.


Present objective

The immediate objective is modest: determine whether an evidence-based, auditable representation of added and inherited design contributions can be built for open-source software without confusing observable lineage with a complete or automatic measure of value. A successful first stage would establish vocabulary, boundaries, and testable components for later technical and social experimentation.


