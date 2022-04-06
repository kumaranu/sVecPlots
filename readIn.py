import numpy as np
from glob import glob
import os

def readIn(referenceDir):
    dirList = glob(referenceDir + '/0.*')
    svrList = np.asarray(sorted([np.float(directory.split('/')[-1]) for directory in dirList]))
    svrListStr = [directory.split('/')[-1] for directory in dirList]
    
    sortedStrSvr = []
    for i in svrList:
        for j in svrListStr:
            if str(i) == j:
                sortedStrSvr.append(j)
    return sortedStrSvr

def readIn1(referenceDir, nDim, svr):
    try:
        uList, sList, V = [], [], []
        for sep in range(1, nDim):
            U = np.loadtxt('fort.10' + str(sep))
            uList.append(U)
            S = np.loadtxt('fort.20' + str(sep))
            sList.append(S)
        V = np.loadtxt('fort.3' + '0' + str(nDim-1))
        return [uList, sList, V]
    except:
        return []

