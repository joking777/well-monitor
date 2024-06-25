import matplotlib.pyplot as plt
import io
from io import BytesIO
import matplotlib
matplotlib.use("Agg")

def sparkline(data):
    # plot it
    fig, ax = plt.subplots(1,1,figsize=(5,1))
    plt.plot(data, color='k')
    plt.plot(len(data)-1, data[-1], color='r', marker='o')

    # remove all the axes
    for k,v in ax.spines.items():
        v.set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])
    
    ioBytes = io.BytesIO()
    plt.savefig(ioBytes, format='png')
    ioBytes.seek(0)
    return ioBytes.getvalue()
 