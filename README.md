# LOGIA

Logia is my attempt to create an automated theorem prover by combining the widely separate (but not really that different :) fields of proof theory, evolutionary algorithms and computer programming. In its current form, it uses genetic programming to generate mathematical proofs which are then verified by Coq, a proof assistant for a variant of higher order type theory that also manages to avoid the halting problem. I plan to integrate a SAT solver, better genetic algoritms (with natural selection in mind) and machine learning.


## Getting Started

Get Python 3 and the `numpy` library. I use [Anaconda](https://www.continuum.io/downloads) by Continuum Mechanics.

Next, download [Coq](https://coq.inria.fr/download), a proof assistant for the Calculus of (Inductive) Constructions designed by Thiery Coquand.

Clone the repository and replace the ellipses with proper pathnames in `version_logia.py` accordingly, and you're good to go!


## Related Work and Further Reading

1. [Univalent Foundations](https://github.com/UniMath/UniMath), Vladimir Voevodsky, Benedikt Ahrens, Daniel Grayson and others.
2. [Automatically Proving Mathematical Theorems with Evolutionary Algorithms and Proof Assistants](http://www.arxiv-sanity.com/1602.07455), Li-An Yang, Jui-Pin Liu, Chao-Hong Chen, Ying-ping Chen.
3. [ProvingGround](https://github.com/siddhartha-gadgil/ProvingGround), Siddhartha Gadgil.
4. [Machine Learning for Proof General](http://staff.computing.dundee.ac.uk/katya/ML4PG/), Jonathan Heras and Ekaterina Komendantskaya.
