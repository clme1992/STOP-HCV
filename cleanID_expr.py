import re
from build_gene_dict import build_ID_dict
equal_ID, to_prim_key = build_ID_dict(1)
file_name = "/Users/stevenlin/OneDrive - OnTheHub - The University of Oxford/cleanID_map.tsv"
no_match_lst = list()
match_cnt = 0
miss_ID = list()
with open(file_name, 'r') as read_file:
    for line in read_file:
        line = line.rstrip().split('\t')[1]
        if line in to_prim_key:
            match_cnt += 1
        else:
            miss_ID.append(line)
print(len(miss_ID))

rematch_lst = list()
for ID in miss_ID:
    for i, letter in enumerate(ID):
        string = list(ID)
        string[i] = '.'
        string = "".join(string)
        for key in to_prim_key:
            if re.search(string, key):
                print(ID)
                print(string)
                print(key)
                if len(string) == len(key):
                    rematch_lst.append(ID)

print(len(rematch_lst))