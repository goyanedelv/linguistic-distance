from auxiliary import *
import plotly.figure_factory as ff

if __name__ == "__main__":
    plot_from_file("data/dl_Swadesh.xlsx", "average", (15,8), save = False, plot = False, interactive=True)
    plot_from_file("data/dl_Our Father.xlsx", "average", (15,8), save = False, plot = False, interactive=True)
    plot_from_file("data/dl_Starman.xlsx", "average", (15,8), save = False, plot = False, interactive=True)

    plot_from_file("data/levenshtein_Swadesh.xlsx", "average", (15,8), save = False, plot = False, interactive=True)
    plot_from_file("data/levenshtein_Our Father.xlsx", "average", (15,8), save = False, plot = False, interactive=True)
    plot_from_file("data/levenshtein_Starman.xlsx", "average", (15,8), save = False, plot = False, interactive=True)

    plot_from_file("data/nwl_Swadesh.xlsx", "average", (15,8), save = False, plot = False, interactive=True)
    plot_from_file("data/nwl_Our Father.xlsx", "average", (15,8), save = False, plot = False, interactive=True)
    plot_from_file("data/nwl_Starman.xlsx", "average", (15,8), save = False, plot = False, interactive=True)