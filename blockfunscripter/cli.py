import matplotlib.pyplot as plt

from .plugins import loaded_plugins


# Poetry script ("entrypoint")
def main():
    for p in loaded_plugins:
        for g in p.generators:
            s = g['obj'](period=500, duration=5500, amplitude=(0, 100))
            plt.locator_params(axis='y', nbins=20, tight=True)
            plt.plot(s.x_list, s.y_list)
            plt.show()
