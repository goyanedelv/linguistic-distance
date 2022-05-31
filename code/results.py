from auxiliary import *
if __name__ == "__main__":
    i = "average"
    dendogram_plot_lv("Swadesh", i, (15, 6), save = True, plot = False)
    dendogram_plot_lv("Our Father", i, (15, 6), save = True, plot = False)
    dendogram_plot_lv("Starman", i, (15, 6), save = True, plot = False)

    dendogram_plot_nwl("Swadesh", i, (15, 6), save = True, plot = False)
    dendogram_plot_nwl("Our Father", i, (15, 6), save = True, plot = False)
    dendogram_plot_nwl("Starman", i, (15, 6), save = True, plot = False)

    dendogram_plot_rdlv("Swadesh", i, (15, 6), save = True, plot = False)
    dendogram_plot_rdlv("Our Father", i, (15, 6), save = True, plot = False)
    dendogram_plot_rdlv("Starman", i, (15, 6), save = True, plot = False)
