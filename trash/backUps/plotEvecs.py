import numpy as np
import matplotlib.pyplot as plt

def plotEvecs(x, f, dim, nDim, numSvecs):
    for i in range(numSvecs):
        plt.plot(x, f[:, i], label='sVec-' + str(i))
    plt.xlabel('R' + str(dim) + ' Grid #')
    plt.ylabel('Potential energy (kcal/mol)')
    plt.legend()
    plt.savefig(str(nDim) + 'D' + '-R' + str(dim) + '.png')  
    plt.close()

