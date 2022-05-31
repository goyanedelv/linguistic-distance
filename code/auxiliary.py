import pandas as pd
import os
import glob
import string
import sys
import unidecode
import stringdist as SD
import Levenshtein as lv
from scipy.spatial.distance import hamming
from scipy.cluster.hierarchy import dendrogram, linkage, to_tree
import matplotlib.pyplot as plt
import plotly.figure_factory as ff

from nwl import *
from matrix import alphabet_matrix

# Pre-processing and reading functions
def clean_squiggle(s):
    ##delete tilda, squiggle, ' , and make lower case

    new = unidecode.unidecode(s).replace("'","").lower().translate(str.maketrans("", "", string.punctuation))

    return new

def read_txt_as_one_string(file):
    str = ""
    for i in open(file, encoding="utf8").readlines():
        str += clean_squiggle(i).replace("\n"," ")
    return str

def read_txt_in_folder(path):
    data_list = os.listdir(path)
    output_list = []
    for i in data_list:
        output_list.append(read_txt_as_one_string(path+"/"+i))
    return output_list

# Matrices
def levenshtein_matrix(folder_path):
    string_list = read_txt_in_folder(folder_path)
    dimension = len(string_list)
    dist_matrix = [ [ 0 for y in range(dimension )] for x in range( dimension )]
    for i in range(dimension):
        for j in range(dimension):
            if i == j:
                dist_matrix[i][j] = 0
            else:
                dist_matrix[i][j] = lv.distance(string_list[i],string_list[j])
    dist_matrix = pd.DataFrame(dist_matrix)
    dist_matrix.columns = os.listdir(folder_path)
    dist_matrix.to_excel(f"data/levenshtein_{folder_path}.xlsx", index=False)

    return dist_matrix

def damerau_levenshtein_matrix(folder_path):
    string_list = read_txt_in_folder(folder_path)
    dimension = len(string_list)
    dist_matrix = [ [ 0 for y in range(dimension )] for x in range( dimension )]
    for i in range(dimension):
        for j in range(dimension):
            if i == j:
                dist_matrix[i][j] = 0
            else:
                dist_matrix[i][j] = SD.rdlevenshtein(string_list[i],string_list[j])#*len(string_list[i])
    
    dist_matrix = pd.DataFrame(dist_matrix)
    dist_matrix.columns = os.listdir(folder_path)
    dist_matrix.to_excel(f"data/dl_{folder_path}.xlsx", index=False)

    return dist_matrix

def hamming_matrix(folder_path):
    string_list = read_txt_in_folder(folder_path)
    dimension = len(string_list)
    dist_matrix = [ [ 0 for y in range(dimension )] for x in range( dimension )]
    for i in range(dimension):
        for j in range(dimension):
            dist_matrix[i][j] = hamming(string_list[i],string_list[j])*len(string_list[i])
    dist_matrix = pd.DataFrame(dist_matrix)
    dist_matrix.columns = os.listdir(folder_path)
    dist_matrix.to_excel(f"data/hamming_{folder_path}.xlsx", index=False)

    return dist_matrix

def nwl_matrix(folder_path):
    string_list = read_txt_in_folder(folder_path)
    dimension = len(string_list)
    dist_matrix = [ [ 0 for y in range(dimension )] for x in range( dimension )]
    for i in range(dimension):
        for j in range(dimension):
            if i == j:
                dist_matrix[i][j] = 0
            else:
                dist_matrix[i][j] = nwl(string_list[i],string_list[j], alphabet_matrix)
         
    dist_matrix = pd.DataFrame(dist_matrix)
    dist_matrix.columns = os.listdir(folder_path)
    dist_matrix.to_excel(f"data/nwl_{folder_path}.xlsx", index=False)
    return dist_matrix

# Plotters
def dendogram_plot_lv(folder_path, method, size, save = False, plot = True):

    dist_matrix = levenshtein_matrix(folder_path)
    linkage_matrix = linkage(dist_matrix, method = method)

    label_clean = [x.replace(".txt","") for x in dist_matrix.columns]

    
    plt.figure(figsize = size)
    dendrogram(linkage_matrix, labels = label_clean)
    plt.title(folder_path)
    if save:
        plt.savefig(f"data/levenshtein_{folder_path}_{method}.png")
    if plot:
        plt.show()

def dendogram_plot_hamming(folder_path, method, size, save = False, plot = True):

    dist_matrix = hamming_matrix(folder_path)
    linkage_matrix = linkage(dist_matrix, method = method)

    label_clean = [x.replace(".txt","") for x in dist_matrix.columns]
    
    plt.figure(figsize = size)
    dendrogram(linkage_matrix, labels = label_clean)
    plt.title(folder_path)
    if save:
        plt.savefig(f"data/hamming_{folder_path}_{method}.png")
    if plot:
        plt.show()

def dendogram_plot_rdlv(folder_path, method, size, save = False, plot = True):

    dist_matrix = damerau_levenshtein_matrix(folder_path)
    linkage_matrix = linkage(dist_matrix, method = method)

    label_clean = [x.replace(".txt","") for x in dist_matrix.columns]

    plt.figure(figsize = size)
    dendrogram(linkage_matrix, labels = label_clean)
    plt.title(folder_path)
    if save:
        plt.savefig(f"data/dl_{folder_path}_{method}.png")
    if plot:
        plt.show()


def dendogram_plot_nwl(folder_path, method, size, save = False, plot = True):
    dist_matrix = nwl_matrix(folder_path)
    linkage_matrix = linkage(dist_matrix, method = method)

    label_clean = [x.replace(".txt","") for x in dist_matrix.columns]

    plt.figure(figsize = size)
    dendrogram(linkage_matrix, labels = label_clean)
    plt.title(folder_path)
    if save:
        plt.savefig(f"data/nwl_{folder_path}_{method}.png")
    if plot:
        plt.show()

def plot_from_file(file, method, size, save = False, plot = True, interactive = False):

    file_clean = file.replace("data/","").replace(".xlsx","")

    source = pd.read_excel(file, engine = "openpyxl")

    linkage_matrix = linkage(source, method = method)

    label_clean = [x.replace(".txt","") for x in source.columns]

    plt.figure(figsize = size)
    dendrogram(linkage_matrix, labels = label_clean)
    plt.title(file_clean)
    if save:
        plt.savefig(f"data/from_file_{file_clean}_{method}.png")
    if plot:
        plt.show()
    if interactive:
        fig = ff.create_dendrogram(source, labels=label_clean, orientation="left")
        fig.update_layout(width=800, height=800)
        fig.write_html(f"data/html/{file_clean}.html")
