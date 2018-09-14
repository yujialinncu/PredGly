import math
import numpy as np
import pandas as pd

def AAC(frag):
    lines = frag
    L=len(lines[1])
    n=int(len(lines)/2)
    AAs='ACDEFGHIKLMNPQRSTVWYO'
    m=len(AAs)
    aac=np.zeros((n,21))
    for i in range(n):
        for j in range(m):
            frequency=lines[2*i+1].count(AAs[j])
            frequency=float('%.2f'%frequency)
            aac[i][j]=frequency/L
    aac=aac[:,0:20]
    return aac

def k_space(frag):
    lines = frag
    L=len(lines[1])
    n=int(len(lines)/2)
    AAs='ACDEFGHIKLMNPQRSTVWYO'
    m=len(AAs)
    pair=[]
    for i in range(m):
        for j in range(m):
            pair.append(AAs[i]+AAs[j])
    new_lines=[]
    for i in range(n):
        new_lines.append(lines[2*i+1])
    
    
    for k in range(5):
        k_space=np.zeros((n,441))
        for t in range(n):
            for i in range(L-k-1):
                AApair=new_lines[t][i]+new_lines[t][i+k+1]
                for j in range(441):
                    if AApair==pair[j]:
                        k_space[t][j]+=1
        if k==0:
            Kspace=k_space
        else:
            Kspace=np.concatenate((Kspace,k_space),axis=1)
    return Kspace
def PWAA(frag):
    lines = frag
    L=len(lines[1])
    n=int(len(lines)/2)
    AAs='ACDEFGHIKLMNPQRSTVWYO'
    l=int((L-1)/2)
    data=np.zeros((n,21))
    for i in range(n):
        for k in range(len(AAs)):
            pos=[ii for ii,v in enumerate(lines[2*i+1]) if v==AAs[k]]
            pos2=[jj+1 for jj in pos]
            p=[]
            c=[]
            for j in pos2:
                if j>=1 and j<=l:
                    p.append(j-l-1)
                if j>l and j<=L:
                    p.append(j-l-1)
            for m in p:
                if m>=-l and m<=l:
                    S1=float('%.2f'%abs(m))
                    c.append(m+S1/l)
            S2=float('%.2f'%sum(c))
            data[i][k]=S2/(l*(l+1))
    return data

def DBPB(frag):
    lines = frag
    n=int(len(lines)/2)
    L=len(lines[1])
    new_data=[]
    for i in range(n):
        new_data.append(lines[2*i+1])
    AAs='ACDEFGHIKLMNPQRSTVWYO'
    sym=[]
    for i in AAs:
        for j in AAs:
            sym.append(str(i)+str(j))
    pospath='data_positive.csv'
    data_positive=pd.read_csv(pospath)
    data_positive=data_positive.values
    negpath='data_negative.csv'
    data_negative=pd.read_csv(negpath)
    data_negative=data_negative.values

    DBPB=np.zeros((n,(L-1)*2))
    for i in range(n):
        for j in range(L-1):
            pos=sym.index(new_data[i][j:j+2])
            DBPB[i][j]=data_positive[j][pos]
            DBPB[i][j+L-1]=data_negative[j][pos]
    return DBPB
def EBGW(frag):
    lines = frag
    L=len(lines[1])
    l=L  
    n=int(len(lines)/2)
    C1='AFGILMPVW'
    C2='CNQSTY'
    C3='HKR'
    C4='DE'
    ucidata=[]
    EBGW=[]
    ucidata1=[]
    ucidata2=[]
    ucidata3=[]
    for i in range(n):
        ucida=[]
        for j in range(l):
            pos=[ii for ii,v in enumerate(C1) if v==lines[2*i+1][j]]
            pos1=[ii for ii,v in enumerate(C2) if v==lines[2*i+1][j]]
            pos2=[ii for ii,v in enumerate(C3) if v==lines[2*i+1][j]]
            pos3=[ii for ii,v in enumerate(C4) if v==lines[2*i+1][j]]
            if len(pos)==1 or len(pos1)==1:
                ucida.append(1)
            elif len(pos2)==1 or len(pos3)==1:
                ucida.append(0)
            else:
                ucida.append(0)
            pos=[]
            pos1=[]
            pos2=[]
            pos3=[]
            
        ucidata1.append(ucida)
                
    for i in range(n):
        ucida1=[]
        for j in range(l):
            pos=[ii for ii,v in enumerate(C1) if v==lines[2*i+1][j]]
            pos1=[ii for ii,v in enumerate(C3) if v==lines[2*i+1][j]]
            pos2=[ii for ii,v in enumerate(C2) if v==lines[2*i+1][j]]
            pos3=[ii for ii,v in enumerate(C4) if v==lines[2*i+1][j]]
            if len(pos)==1 or len(pos1)==1:
                ucida1.append(1)
            elif len(pos2)==1 or len(pos3)==1:
                ucida1.append(0)
            else:
                ucida1.append(0)
            pos=[]
            pos1=[]
            pos2=[]
            pos3=[]
        ucidata2.append(ucida1)
    for i in range(n):
        ucida2=[]
        for j in range(l):
            pos=[ii for ii,v in enumerate(C1) if v==lines[2*i+1][j]]
            pos1=[ii for ii,v in enumerate(C4) if v==lines[2*i+1][j]]
            pos2=[ii for ii,v in enumerate(C2) if v==lines[2*i+1][j]]
            pos3=[ii for ii,v in enumerate(C3) if v==lines[2*i+1][j]]
            if len(pos)==1 or len(pos1)==1:
                ucida2.append(1)
            elif len(pos2)==1 or len(pos3)==1:
                ucida2.append(0)
            else:
                ucida2.append(0) 
            pos=[]
            pos1=[]
            pos2=[]
            pos3=[]
        ucidata3.append(ucida2)
    ucidata=np.hstack((ucidata1,ucidata2,ucidata3))
    
    ur,uc=np.shape(ucidata)
    k1=5
    x1=[]
    x2=[]
    x3=[]
    for i in range(ur):
        x11=[]
        x22=[]
        x33=[]
        a=0
        b=0
        c=0
        for j in range(int(k1)):
            a=sum(ucidata1[i][0:int(math.floor(l*(j+1)/k1))])/math.floor(l*(j+1)/k1)
            b=sum(ucidata2[i][0:int(math.floor(l*(j+1)/k1))])/math.floor(l*(j+1)/k1)
            c=sum(ucidata3[i][0:int(math.floor(l*(j+1)/k1))])/math.floor(l*(j+1)/k1)
            x11.append(a)
            x22.append(b)
            x33.append(c)
        x1.append(x11)
        x2.append(x22)
        x3.append(x33)
    EBGW=np.hstack((x1,x2,x3))
    EBGW=np.array(EBGW)
    return EBGW
def KNN(frag):
    lines_train=frag
    L=len(lines_train[1])
    rtrain=int(len(lines_train)/2)
    f2=open('background.txt')
    lines_test=f2.read().splitlines()
    rtest=int(len(lines_test)/2)
    df=pd.read_csv('blosum62.csv')
    matrix=np.array(df)
    matrixmax=np.max(matrix)
    matrixmin=np.min(matrix)
    AAs='CSTPAGNDEQHRKMILVFYWO'
    K=[2,4,8,16,32]
    Knum=len(K)
    KNNScore=[]
    for i in range(rtrain):
        Dist=[]
        for j in range(rtest):
            sim=[]
            for k in range(L):
                line=AAs.index(lines_test[2*j+1][k])
                row=AAs.index(lines_train[2*i+1][k])
                matrixscores=matrix[line,row]
                S=float('%.2f'%(matrixscores-matrixmin))
                X=float('%.2f'%(matrixmax-matrixmin))
                sim.append(S/X)
            Dist.append(1-np.sum(sim)/L)
        pos_index=np.argsort(np.array(Dist))
        KNN=[]
        for dim in range(Knum):
            pos=pos_index[0:K[dim]]
            posnum=K[dim]
            count=0.
            for l in range(posnum):
                if pos[l]<=rtest/2:
                    count+=1
            KNN.append(count/K[dim])
        KNNScore.append(KNN)
    KNNScore=np.array(KNNScore)
    return KNNScore

        
def ExtractFeatures(frag,*var):
    n=len(var)
    feature={}
    for i in range(n):
        if var[i]==1:
            feature[i]=AAC(frag)
        if var[i]==2:
            feature[i]=k_space(frag)
        if var[i]==3:
            feature[i]=PWAA(frag)
        if var[i]==4:
            feature[i]=DBPB(frag)
        if var[i]==5:
            feature[i]=EBGW(frag)
        if var[i]==6:
            feature[i]=KNN(frag)

    for i in range(n):
        if i==0:
            features=feature[i]
        else:
            features=np.concatenate((features,feature[i]),axis=1)
            
    
    return features
