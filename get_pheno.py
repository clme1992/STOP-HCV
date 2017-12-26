import re
import sys
from build_gene_dict import *
prefix = "/data/jaga/stophcv/steven/August2016/"
if sys.argv[1] == 'local':
    prefix = "/Users/stevenlin/OneDrive - OnTheHub - The University of Oxford/"
pheno_file_name = prefix + "clinical_data/STOP-HCV_Data_Registry_Will.csv"
file_name = prefix + "clinical_data/August2016.fam"
wrt_file_name = prefix + "test/August2016.fam.temp"
if sys.argv[1] == 'local':
    wrt_file_name = prefix + "clinical_data/August2016.fam.temp"
wrt_file = open(wrt_file_name, 'w')

equal_ID, to_prim_key = build_ID_dict(1)
case_ID = list()
control_ID = list()
prim_col = 0
cirr_col = 4

with open(pheno_file_name, 'r', encoding='latin-1') as read_file:
    for line in reader(read_file):
        if line[cirr_col] == 'Y':
            case_ID.append(line[prim_col])
        else:
            control_ID.append(line[prim_col])

cleanID_dict = build_cleanID_dict(1)
with open (file_name, 'r') as read_file:
    for line in read_file:
        line = line.rstrip().split(' ')
        line[5] = '-9'
        ID = line[0]
        if ID in cleanID_dict:
            ID = cleanID_dict[ID]
            if ID in to_prim_key:
                if to_prim_key[ID] in case_ID:
                    line[5] = '2'
                elif to_prim_key[ID] in control_ID:
                    line[5] = '1'
        print(" ".join(line), file=wrt_file)


