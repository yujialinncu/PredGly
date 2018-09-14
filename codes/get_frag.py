def read_file(filepath):  
    try:
        fp = open(filepath)
    except IOError:
        print 'Failed to open '+filepath + ', please check if file is exist or not!'
        exit()
    else:
        fp=open(filepath)
        lines = fp.read().splitlines()
        sequence={}
        protein_name=''
        namelist=[]
        for line in lines:
            if line[0]=='>':
                if protein_name !='':
                    sequence[protein_name]=seq
                    namelist.append(protein_name)
                seq=''
                protein_name=line
            else:
                seq+=line
        sequence[protein_name]=seq
        namelist.append(protein_name)
        return sequence,namelist

def get_frag(protein_seq,size_windows,protein_name):
    frag_data=[]
    L=int((size_windows-1)/2)
    end=len(protein_seq)
    position=[AA for AA,v in enumerate(protein_seq) if v=='K']
    for i in range(len(position)):
        pos=position[i]
        if pos-L>=0 and end-pos-L>0:
            frag_data.append(protein_name+'K'+str(pos+1))
            frag_data.append(protein_seq[pos-L:pos+L+1])
        if pos-L>=0 and end-pos-L<=0:
            sup_right='O'*(L+1-(end-pos))
            frag_data.append(protein_name+'K'+str(pos+1))
            frag_data.append(protein_seq[pos-L:]+sup_right)
        if pos-L<0 and end-pos-L>0:
            sup_left='O'*(L-pos)
            frag_data.append(protein_name+'K'+str(pos+1))
            frag_data.append(sup_left+protein_seq[:pos+L+1])
        if pos-L<0 and end-pos-L<=0:
            sup_left='O'*(L-pos)
            sup_right='O'*(L+1-(end-pos))
            frag_data.append(protein_name+'K'+str(pos+1))
            frag_data.append(sup_left+protein_seq[:]+sup_right)
    return frag_data


def extract_predict(filepath,size_windows=31):
    sequence,namelist=read_file(filepath)
    frag=[]
    for protein_name in namelist:
        protein_seq=sequence[protein_name]
        frag_data=get_frag(protein_seq,size_windows,protein_name)
        frag+=frag_data
    return frag
         