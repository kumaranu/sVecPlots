import numpy as np
import matplotlib.pyplot as plt

def plotEvecs(x, f, dim, nDim, numSvecs):

    #print(type(x), np.shape(x))
    #print(type(x), np.shape(f))
    #print(dim, nDim, numSvecs)

    if numSvecs > np.shape(f)[1]:
        #for i in range(numSvecs):
        for i in range(np.shape(f)[1]):
            plt.plot(x, f[:, i], label='alpha=' + str(i))
        plt.title('Dim-' + str(dim))
        plt.xlabel('R' + str(dim) + ' Grid #')
        plt.ylabel('Potential energy (kcal/mol)')
        plt.legend()
        #plt.xlim([0, 30])
        #plt.ylim([0, 250])
        plt.savefig(str(nDim) + 'D' + '-R' + str(dim) + '.png')  
        plt.close()
    else:
        print('Printing first 3 singular vectors out of ', np.shape(f)[1])
        for i in range(numSvecs):
            plt.plot(x, f[:, i], label='alpha=' + str(i))
        plt.xlabel('R' + str(dim) + ' Grid #')
        plt.ylabel('Potential energy (kcal/mol)')
        plt.legend()
        plt.savefig(str(nDim) + 'D' + '-R' + str(dim) + '.png')  
        plt.close()


