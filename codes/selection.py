import pandas as pd

def select(feature):
    pospath='optimal.csv'
    df=pd.read_csv(pospath)
    pos=df.values
    posL=[]
    for i in range(len(pos)):
        posL.append(pos[i][0])
    new_feature=feature[:,posL]
    
    return new_feature