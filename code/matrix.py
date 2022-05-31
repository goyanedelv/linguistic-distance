# Loading libraries
import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage, cut_tree
import matplotlib.pyplot as plt
from scipy.spatial import distance
import seaborn as sns
import numpy as np

# Loading the data
letters = pd.read_excel("documentation/Letters.xlsx", engine="openpyxl")
labels = letters["letter"].to_list()
letters = letters.drop("letter", axis = 1)

# Creating the matrix as a dictionary
great_dict = []
for i in range(len(labels)):
    great_dict.append(letters.iloc[i,:].to_list())

letters_pos = dict(zip(labels, great_dict))

pairs = []
distz = []

matrix_format = []
for i in labels:
    for_matrix = []
    for j in labels:
        pairs.append((i,j))
        dd = distance.euclidean(letters_pos[i], letters_pos[j])
        distz.append(dd)
        for_matrix.append(dd)
    matrix_format.append(for_matrix)

matrix_hm = pd.DataFrame(matrix_format)
matrix_hm.columns = labels
matrix_hm.index = labels

# Importable Matrix
alphabet_matrix = dict(zip(pairs, distz))


if __name__ == "__main__":
    ## A few examples
    alphabet_matrix[("a","p")]
    alphabet_matrix[("a","a")]
    alphabet_matrix[("a","e")]

    # Plotting the hierarchichal relationship
    Z = linkage(letters, 'average')

    plt.figure(figsize=(25, 10))
    plt.title('Hierarchy of letters')
    plt.xlabel('Letter')
    plt.ylabel('distance')
    dendrogram(Z, labels = labels)
    plt.show()

    # plotting as a matrix
    sns.heatmap(matrix_hm, linewidth=0.5)
    plt.show()