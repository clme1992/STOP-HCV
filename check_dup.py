from build_gene_dict import build_ID_dict
ID_dup = dict()
equal_ID, to_prim_key = build_ID_dict()
prefix = "/data/jaga/stophcv/steven/August2016/"
file_name = prefix + "clinical_data/TR000384_Enrolment2"
with open(file_name, 'r') as read_file:
    read_file.readline()
    for line in read_file:
        ID = line.rstrip().split('\t')[0]
        if ID in to_prim_key:
            prim_ID = to_prim_key[ID]
            if prim_ID in ID_dup:
                ID_dup[prim_ID] = ID_dup[prim_ID] + 1
            else:
                ID_dup[prim_ID] = 0
        else:
            print("can't find prim key: "+ str(ID))

for ID in ID_dup:
    if ID_dup[ID] > 1:
        print(ID+': '+str(ID_dup[ID]))
