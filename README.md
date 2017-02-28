# LOGIA

Logia is my attempt to create an automated theorem prover by combining the widely separate (but not really that different :) fields of proof theory, evolutionary algorithms and computer programming. In its current form, it uses evolutionary algorithms to generate mathematical proofs which are then verified by Coq, a proof assistant for a variant of higher order type theory that also manages to avoid the halting problem. I am currently in the process of adding machine learning algorithms.


## Getting Started

Get Python 3 and the NumPy and SymPy libraries. I use [Anaconda](https://www.continuum.io/downloads) by Continuum Mechanics.

Next, download [Coq](https://coq.inria.fr/download), a proof assistant for the Calculus of (Inductive) Constructions which is a formal language for mathematics invented by Thiery Coquand.

Clone the repository and change the `path` variable in the python sourcecodes accordingly, and you're good to go!


## How to

Logia comes with a shell (lsh) that can be run by executing either `lsh.py` or `l.sh`. Built into lsh are various commands to evaluate mathematical expressions, as well as rudimentary file management commands. Type `help` into lsh to get a list of commands. Almost all math commands require SymPy, so it's advisable to get it first. In the future I'd like to have a better interface and more out-of-the-box support for doing mathematics (think graphs, numerical solvers, better editors, etc.).

The Logia 'kernel', which is the theorem prover, can be launched from lsh through the `prove` command. NumPy is required for this to run. `prove` calls the GNU nano editor on a `theorem.v` file, which can be edited and saved. Write the theorem to be proved here. Saving `theorem.v` automatically launches the prover to action, which tries to find proofs for the theorem and halts only when a proof is found, threshold fitness goes through the roof, or hell freezes over.

lsh also has basic file management capabilities. To find files, type `find <string>`; an empty string returns all files in the present working directory. To change directory, type `cd`, press enter, type the path. To edit or compile a .v file, type `edit` or `com`, hit enter, and type in the filename. The coq compiler tries to compile the .v file and produce a .vo file. To remove all temporary .v and .vo files in the present directory, type `del`. Doing this is necessary before launching the prover everytime, as this flushes temporary files out. Any time the screen gets messy doing math, use `cls`. To quit the shell, type `qed`.


## Related Work and Further Reading

1. [Univalent Foundations](https://github.com/UniMath/UniMath), Vladimir Voevodsky, Benedikt Ahrens, Daniel Grayson and others.
2. [Automatically Proving Mathematical Theorems with Evolutionary Algorithms and Proof Assistants](http://www.arxiv-sanity.com/1602.07455), Li-An Yang, Jui-Pin Liu, Chao-Hong Chen, Ying-ping Chen.
3. [ProvingGround](https://github.com/siddhartha-gadgil/ProvingGround), Siddhartha Gadgil.
4. [Machine Learning for Proof General](http://staff.computing.dundee.ac.uk/katya/ML4PG/), Jonathan Heras and Ekaterina Komendantskaya.
