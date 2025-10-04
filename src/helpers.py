import pandas as pd
import matplotlib.pyplot as plt

def load_csv(path):
    return pd.read_csv(path)

def save_fig(fig, path, dpi=150):
    fig.savefig(path, bbox_inches='tight', dpi=dpi)
    plt.close(fig)
