import numpy as np
import os, glob
import matplotlib.pyplot as plt
import readIn, plotEvecs

nDimList, numSvecs = [3, 4], 3
# 3D_svd = ['2.2','1.3','0.1','0.075','0.05','0.025','0.02','0.018','0.017','0.0166','0.016','0.014','0.012','0.01','0.0075','0.005','0.0025','0.001','0.0001','0.00001','0.0']
# 4D_svr = ['0.9','2_0.06','2_0.1','2_0.5','0.022','0.021','0.02','0.01','0.0075','0.005','0.0025','0.001','0.0001','0.00001']

os.chdir('../')
# for nDim in nDimList:
for nDim in [3]:
    os.chdir(str(nDim) + 'D/')
    # sortedStrSvr = readIn.readIn(os.getcwd())
    # for svr in sortedStrSvr:
    for svr in ['2.2']:
        os.chdir(svr)
        uList, sList, V = readIn.readIn1(os.getcwd(), nDim, svr)

        sList = np.sqrt(sList)
        u = uList[0] * np.sqrt(sList[0])
        u = u - np.min(u, axis=0)
        plotEvecs.plotEvecs(range(1, len(u) + 1), u*627.503, 1, nDim, numSvecs)
        for i in range(1, nDim-1):
            u2 = uList[i] * np.sqrt(sList[i])
            u2 = u2 - np.min(u2, axis=0)
            alphaL = len(sList[i-1])
            alphaR = len(sList[i])
            for j in range(np.shape(u2)[1]):
                for k in range(np.shape(V)[0]):
                    #u_tmp = np.reshape(u2[:, j], (alphaL, len(u)))
                    print(i, j, k)#, u_tmp)
        ##    plotevecs.plotevecs(range(1, len(u) + 1), u*627.503, i-1, ndim, numsvecs)
        ##
        ##print('Inside dimension', nDim, 'for', nDim, 'dimensional case with svr =', svr)
        ##V = np.transpose(np.loadtxt('fort.3' + '0' + str(nDim-1)))
        ##print(np.shape(V))
        ##for j in range(numSvecs):
        ##    plotEvecs.plotEvecs(range(1, len(V) + 1), V*627.503, nDim, nDim, numSvecs)
        os.chdir('../')
    os.chdir('../')
os.chdir('sVecPlots')


