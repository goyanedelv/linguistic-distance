# Tracing evolution of languages using sequence alignment techniques

Zoe Huang and Gonzalo Oyanedel, 2022. This was our final research project for Introduction to Scientific Computing @ UChicago.

We analyzed the similarity of 28 languages using 3 different approaches:

1. The Levenshtein distance (Levenshtein et al., 1966)
2. The Damerau–Levenshtein distance (Brill and Moore, 2000)
3. The Needleman-Wunsch-like (NWL) algorithm (Needleman and Wunsch, 1970)

## Structure of this repo

- Text structures: `Starman`, `Swadesh` and `Our Father`, each folder contains a `.txt` file with the text structure in the respective language
- Code: it contains all codes of this project
    - `auxiliary.py` contains all codes that create dendrograms and compute distance matrices
    - `nwl.py` contains the Neddleman-Wunsch-like algorithm developed by us
    - `matrix.py` contains the matrix used by the Neddleman-Wunsch-like algorithm. Can be ran from command line to obtain the hierarchy of letters.
    - `html_visualization.py` contains the code that create html versions of the matrices. Can be ran from command line.
    - `results.py` contains the main code to generate the results used in the paper. Note that this code might take  few hours. Can be ran from command line.
- Result data: `data`. It contains all results in term of `png` dendrograms, distance matrices in `xlsx` and interactive versions in `html`
- Documentation:
    - `Language.md` a list of all languages used in this study
    - `Letters.xlsx` a file used to compute the substitution matrix
    - `Tests.xlsx` a file summarizing all tests used in the results section
    - `Presentation_HuangOyanedel.pptx` a collection of slides of this project
    - `Tracing_languages_evolution.pdf` the write up of this project

Additionally, you can review the interactive results in this link: https://goyanedelv.github.io/languages/

## Approach

### Raw Data

We obtained the below Text Files for 28 languages

1. Swadesh list of 207 common words
2. The Lord’s prayer
3. The song “Starman” from David Bowie
We translated them by Google and validated by our classmates who speak those languages

### Algorithms

i. Levenshtein Distance - The minimal number of insertions, deletions, and symbol substitutions required to transform a into b

ii. Damerau-Levenshtein Distance - Similar as the Levenstein Distance, but you can also use transpositions (swapping of adjacent symbols)

iii. Needleman-Wunsch-Like(NWL) - Assigns a score to every possible alignment, and the purpose of the algorithm is to find all possible alignments having the highest score

### Comparing results

We used dendograms to visulize the results and used the unit testing approach to compare the 3 algorithms listed above.

References:

1. Levenshtein, V. I. et al. (1966). Binary codes capable of correcting deletions, insertions, and reversals. Soviet physics doklady, 10(8), 707–710.
2. Needleman, S. B., & Wunsch, C. D. (1970). A general method applicable to the search for similarities in the amino acid sequence of two proteins. Journal of molecular biology, 48(3), 443–453.
3. Brill, E., & Moore, R. C. (2000). An improved error model for noisy channel spelling correction. Proceedings of the 38th annual meeting of the association for computational linguistics, 286–293.
4. Gray, R. D., & Atkinson, Q. D. (2003). Language-tree divergence times support the anatolian theory of indoeuropean origin. Nature, 426(6965), 435–439.
5. Robinson, A. (2007). The last man who knew everything: Thomas young, the anonymous genius who proved newton wrong, and deciphered the rosetta stone, among other surprising feats. Plume.
6. Auroux, S., Koerner, E. F. K., Niederehe, H.-J., & Versteegh, K. (2008). History of the language sciences/geschichte dersprachwissenschaften/histoire des sciences du langage. 2. teilband. Walter de Gruyter.
7. Serva, M., & Petroni, F. (2008). Indo-european languages tree by levenshtein distance. EPL (Europhysics Letters),81(6), 68005.
8. Wichmann, S., Holman, E. W., Bakker, D., & Brown, C. H. (2010). Evaluating linguistic distance measures. Physica A: Statistical Mechanics and its Applications, 389(17), 3632–3639.
9. Greenhill, S. J. (2011). Levenshtein distances fail to identify language relationships accurately. Computational Linguistics, 37(4), 689–698.
10. Clark, G., & Henneberg, M. (2017). Ardipithecus ramidus and the evolution of language and singing: An early origin for hominin vocal capability. Homo, 68(2), 101–121.
11. Powell, E. A. (2017). Telling tales in proto-indo-european. Archaeology.
