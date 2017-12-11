# built ID dict
import re
def build_ID_dict():
    clinic2gene = dict()
    gene2clinic = dict()
    prefix = "/data/jaga/stophcv/steven/August2016/"
    file_name = prefix + "clinical_data/TR000402_STOP-HCV_Data_Registry_Dataset.txt2"
    prim_col = 0
    ID_col = [0,1,2,3,5,6]
    with open(file_name, 'r', encoding='latin-1') as read_file:
        for line in read_file:
            line = line.rstrip().split('\t')
            clinic2gene[line[prim_col]] = [None]*len(ID_col)
            for i,col in enumerate(ID_col):
                if (len(line) >= col+1) and (line[col] != ""):
                    clinic2gene[line[prim_col]][i] = line[col]

    gene_ID_lst = list()
    file_name = prefix + "test/August2016.fam"
    with open(file_name,'r', encoding='latin-1') as read_file:
        for line in read_file:
            line = line.rstrip().split(' ')
            ID_lst = re.split('[_\-\.]', line[0])
            for item in ID_lst:
                if len(item) == 10:
                    gene_ID_lst.append(item)

    for prim_ID in clinic2gene:
        gene_exit = 0
        ID_lst = clinic2gene[prim_ID]
        for i,ID in enumerate(ID_lst):
            if ID in gene_ID_lst:
                gene_exit = 1
                gene2clinic[ID] = prim_ID
                clinic2gene[prim_ID] = ID
        if gene_exit == 0:
            clinic2gene[prim_ID] = None

    return [clinic2gene, gene2clinic]