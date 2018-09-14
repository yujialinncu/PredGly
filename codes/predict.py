import argparse
import pandas as pd

from get_frag import extract_predict
from detection import detect
from extract import ExtractFeatures
from selection import select
from sklearn.externals import joblib

###### main function ######
def main():
    parser=argparse.ArgumentParser(description='PredGly: Predicting lysine glycation sites for homo sa-piens based on XGboost feature optimization.')
    parser.add_argument('-input',  dest='inputfile', type=str, help='Query protein sequences to be predicted in txt format.', required=True)
    parser.add_argument('-threshold', dest='threshold_value', type=float, help='Please input a value between 0 and 1', required=True)
    parser.add_argument('-output',  dest='outputfile', type=str, help='Saving the prediction results in csv format.',required=False)
    args = parser.parse_args()
    inputfile=args.inputfile;
    threshold=args.threshold_value;
    outputfile=args.outputfile;
    
    print 'Sequence fragment are loading...'
    frag=extract_predict(inputfile,size_windows=31)
    right_frag,wrong_frag=detect(frag)
    
    print 'Features are extracting...'
    data=ExtractFeatures(right_frag,1,2,3,4,5,6)
    X_test=select(data)
    print 'Loading model...'
    model=joblib.load('best.model')
    prediction=model.predict_proba(X_test)
    n=int(len(right_frag)/2)
    m=int(len(wrong_frag)/2)
    Fragments_name=[]
    Sequence=[]
    Probability=[]
    print 'Glycation sites were predicted as follows.'
    print '-------------------------------'
    for i in range(n):
        if prediction[i][1]>threshold:
            Fragments_name.append(right_frag[2*i])
            Sequence.append(right_frag[2*i+1])
            print right_frag[2*i]
            print right_frag[2*i+1]
            var='%.11f' % prediction[i][1]
            Probability.append(var)
            print 'probability value:'+str(var)
            print '-------------------------------'
            
    if wrong_frag!=[]:   
        print 'The following sequence fragment contains other amino acids.'
        print 'The accepted amino acids are:A,C,D,E,F,G,H,I,K,L,M,N,P,Q,R,S,T,V,W,Y and a virtual amino acid O.'
        print '-------------------------------'
        for j in range(m):
            print wrong_frag[2*j]
            print wrong_frag[2*j+1]
            print '-------------------------------'
    
    AA={'a':Fragments_name,'b':Sequence,'c':Probability}
    PredGly=pd.DataFrame(AA)
    PredGly.to_csv(outputfile,index=False,header=['Fragments name','Sequence','Probability value'])
            
if __name__ == "__main__":
    main()   