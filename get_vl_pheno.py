import re
from build_gene_dict import build_ID_dict
def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def compare( item1, item2 ):
    if item1 > item2:
        return 2
    elif item1 < item2:
        return 1
    else:
        return -1

def compare_date( date1, date2 ):
    month = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
    date1 = date1.split('-')
    date2 = date2.split('-')
    ind = 2
    while (compare(date1[ind], date2[ind]) == -1) and ind >= 0:
        ind = ind - 1
    return compare(date1[ind], date2[ind])

prefix = "/data/jaga/stophcv/steven/August2016/"
file_name= [prefix+"clinical_data/TR000384_Treatment_Data2", prefix+"clinical_data/TR000384_Additional_Treatment_Data2"]
vl_dict = dict()
equal_ID, to_prim_key = build_ID_dict()

for fn in file_name:
    with open(fn, 'r', encoding="latin-1") as read_file:
        line = read_file.readline()
        line = line.rstrip().split('\t')
        vl_col = None
        date_col = None
        for i, item in  enumerate(line):
            if item == "Pretreatment Viral Load":
                vl_col = i
            elif item == "Treatment Start Date":
                date_col = i
        for line in read_file:
            line = line.rstrip().split('\t')
            if len(line) >= vl_col+1:
                vl = line[vl_col]
                date = line[date_col]
                ID = line[0]
                if ID not in vl_dict: #same ID multiple treatments, only use the ealiest one
                    vl_dict[ID] = [vl, date]
                else:
                    early = compare_date(vl_dict[ID][1], date)
                    if early == 2:
                        vl_dict[ID] = [vl, date]

file_name = prefix + "test/August2016.fam"
wrt_file_name = prefix + "test/August2016_vl.fam"
wrt_file = open(wrt_file_name, 'w')
with open(file_name, 'r') as read_file:
    pheno_col = 5
    for line in read_file:
        line = line.rstrip().split(' ')
        line[pheno_col] = '-9'
        ID_lst = re.split('[\-_\.]', line[0])
        ID = None
        for item in ID_lst:
            if len(item) == 10:
                ID = item
        if ID in vl_dict:
            line[pheno_col] = vl_dict[ID][0]
        elif ID in to_prim_key:
            prim_key = to_prim_key[ID]
            ID_lst = equal_ID[prim_key]
            for item in ID_lst:
                if item in vl_dict:
                    line[pheno_col] = vl_dict[item][0]
        if not is_number(line[pheno_col]):
            line[pheno_col] = '-9'
        print(' '.join(line), file=wrt_file)
