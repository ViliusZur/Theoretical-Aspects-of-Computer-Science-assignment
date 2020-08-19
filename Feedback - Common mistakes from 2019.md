# Background

- Only giving the "popular science" definition of TSP. You need to be more precise/technical, using appropriate notation.
- Defining multiple versions of TSP and not being clear on which version you are studying.
- Not defining the actual variant of TSP that you worked on. For example, **Euclidean TSP** specifies "vertices on the plane" using (x,y) coordinates, and the distance between vertices is then calculated using Pythagoras Theorem. You then also need to check this version is still NP-hard, and cite a reference to confirm this fact.
- The given definition of TSP suggests optimising **time**, when it should be optimising **cost** (sum of weights).
- Confusing "problem definition" with "algorithm/solution method".
   - **Problem**: gives a description of the encoding of a problem, and then asks for property.
      For TSP: this is "given a weighted complete graph … find the shortest cycle."
   - **Algorithm**: a step by step mechanism that we can use to program a computer to use the problem's description and recover the required property.
      This is usually described using pseudocode, and then implemented in real code.
- It is more accurate to refer to TSP as "computational (optimisation) problem" rather than "mathematical problem".
- Define number of nodes in graph to be N but then use n later. (Symbols are case sensitive.)
- In the literature, a graph G=(V,E) is specified by sets V of vertices and E of edges. V and E are **not** numbers - they are sets.
- Using N for both the "set of nodes" and its size.
- Mistakes in understanding the meaning of NP-hard.  
- Mistakenly stating that the **optimisation version** of TSP is in NP. It's not because it is not a **decision problem**. NP only contains **decision** problem - nothing else!
- Justifying NP-hardness by reducing TSP to another NP-complete problem, when it should be the other way round.
- Stated that exhaustive search is inefficient but did not say why.
- Exhaustive search costs O(n!), not O((n-1)!).

# Methodology

- Methodology not stated explicitly in the text, e.g. parameters of generation, what is measured and what is averaged.
- No justification for "methodology decisions" taken.
- Almost no one defined "accuracy" - how is this actually measured in practice? This important when you can no longer run exhaustive search to find the shortest cycle. Either use published instances (e.g. TSPLIB or DIMACS) or compare against "exected average length of a cycle".
- Do not restrict to small graphs just because exhaustive search cannot handle big ones. You must use the approximation methods beyond what exhaustive search can handle. That is their purpose!
- Random instances must meet the problem specification (complete, weighted) but should not pre-specify minimum path lengths as this presupposes a solution to TSP or a related problem and could bias the success of one algorithm over another.

# Theory

- Not defining the neighbourhood of a solution. NB. This is different from a neighbouring vertex/node.
- Not explaining how **local search** is done.
- Dijkstra's algorithm cannot be used (unless changed significantly), because the shortest path from a vertex back to itself is "not to move at all!", so does not produce cycle. Dijkstra's algorithm does not require visiting every vertex in the graph.
- Missing "local search" in GRASP.

# Pseudocode

- Pseudocode is badly converted from Python, i.e. essentially just removing ":", or keeping things like range(), or using a lot of Python specific idioms which are not common to other languages.
- Pseudocode for meta-heuristic does not specialise to TSP. Too generic.
- Not clearly specifying input and output.
- No indentation, or indentation that is not justified by control structures.
- The basic idea of the Nearest Neighbour greedy method is to move to next nearest city each time. However, do not forget to build into the algorithm avoiding visiting a city that has already been visited - many people left this out of pseudocode.
- Trying to use 2-opt, but formulation does not match it. You need to reverse a portion of the path, rather than just swap two vertices only.

# Big O

- Making statements that only refer to loops without considering that other lines may be hiding complexity. For example, a single line in a metaheuristic which calls Greedy will have complexity of Greedy as well, namely that line costs O(n^2). Such function calls cannot be assumed to only cost O(1).
- Big-O cost estimation is linked to an algorithm, not to the problem. You can have a very efficient algorithm and another one extremely inefficient for the same problem!
- Making statements that are not linked to the pseudocode, or not linked precisely.
- Trying to derive Big-O from pseudocode of a vague meta-heuristic - answer could change depending on how we relate to TSP.
- Stating the costs of some lines, but forgetting to mention the rest are e.g. O(1).
- The big-O analysis is not accurate, but the result is correct.
- "Straight line" graphs correspond to O(n), not O(n^2).
- O(n^2) and O(n^3) are polynomial, but not **linear**. Linear is O(n).

# Practice

- Poor data quality: lines are not smooth because you didn't **average over multiple/enough instances**.
- Thinking that O(n^2) is exponential. It is not! Do not confuse O(n^2) with O(2^n). The first is **polynomial** and the second is **exponential**.
- Claiming that one of the two approximation methods runs in **exponential time**. This shows grave misunderstanding: the whole point of using these approximation methods is to run in **polynomial** time but sacrifice accuracy, while hoping to minimize this loss.
- Claiming that a Metaheuristic is faster than Greedy.
- Only derived timing data for small n.
- No attempt at accuracy data for high n.
- Showing **timing** data as **accuracy** data. Accuracy refers to **how close is the solution to the optimally shortest cycle**.
- Accuracy varies with n, so showing one average figure (for all the graph size that were tested) misses important details.
- Code output provided with no attempt to explain what is shown in relation to methodology.

- Showing code and graphs without motivation/explaining what you intend to do.
- "Straight line" graphs correspond to O(n), not O(n^2).
- Not every graph that curves upwards shows exponential growth - it could simply be O(n^2) or O(n^3) etc. Or it could be **worse** than exonential growth, such O(n!) or O(n^n).
- Only showing a handful examples. We cannot see the trend this way. You need to test with increasing problem size until you reach sufficiently large instances.
- The graphs are not smooth enough, suggesting that the averaging was not good enough, or not done at all.
- Time without units (e.g. seconds or minutes?)
- Accuracy without units (e.g. percentage?)

# Reflection

- Did not identify any transferable skills or knowledge gained from the project.
- Identified some gains but did not specify exactly how they will help in the future.
- Identified some weaknesses but did not give concrete suggestions on how to improve them.

# References

- Not referencing the first paper that proved a fact, e.g. that TSP is NP-hard.
- Quoting data/fact without referencing. Where did it come from? Your own experiments or is it secondary data?
- List of references not in alphabetical order by first author surname.
- Some references are referenced as if they were a website when in fact they are published (No need to give URL for every entry, especially books).
- Some references lack crucial information such as venue of publication.
- Students relied on unreliable websites rather than formally published sources.
- In-text citations look like "(Author, date)", not like e.g. [1], etc.
- Not all references listed at the end were cited in text.
- "et al." is used in in-text citations, but you must provide the full list of authors in the list of references (i.e. do not use "et al." here).

# Spelling

Making spelling mistakes of the type that could be easily caught.

Examples:

Mistake | Correction
------------ | -------------
i | I
im | I am = I'm
it's	(possessive)	| its - it's = it is
Becuase | Because
Dipends | Depends
Know | Now
Lenght | Length
Matrixes | Matrices
Neighbough | Neighbour
Psuedocode | Pseudocode
Witch | Which
would of | would have = would've

# Data Presentation

- Figure/Table with no caption explaining what it is.
- Forgetting to put axes labels in graphs.
- Forgetting to put keys / legends for graphs with multiple lines.
- Forgetting to give titles to graphs.
- Forgetting to make clear the units measured in graphs.

# General

- Using poetic language in a scientific report, e.g. using "dilemma" instead of "problem".
- Do not use variable names as shorthands, e.g. "v" for "vertices".
- "n2" is not the standard notation for "n squared" - either use proper superscript or write "n^2".
- Writing "G has 85 n" instead of "G has n=85".
- Writing "it depends on number of n" instead of "it depends on n".
- Sections order, e.g. Metaheuristic before Greedy.
- The order of the sections is not logical, e.g. showing pseudocode then discussing how a graph is represented. It should be the other way round.
- Pages and pages of (random) numbers! Not needed - show a graph.
- Writing something like 1≥n≤100 to mean n=1,2,...,100 - it should be 1≤n≤100.
- "Input of size 100 n" should be "Input of size n=100".
- Denoting mathematical symbols using bold font rather than italic, i.e. using **bold** rather than $LaTeX$ notation in Markdown.
- Grammatical mistakes in text.
