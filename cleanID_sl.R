fam_table <- read.table('~/OneDrive - OnTheHub - The University of Oxford/rs12979860/August2016_rs12979860.ped')
ID_lst <- fam_table[,1]
origin_ID_lst <- fam_table[,1]
# remove the control and HTG samples
ID_lst <- ID_lst[-grep('HTG', ID_lst)]
ID_lst <- ID_lst[-grep('control', ID_lst)]
ID_lst <- ID_lst[-grep('Control', ID_lst)]
ID_lst <- ID_lst[-grep('CONTROL', ID_lst)]
ID_lst <- ID_lst[-grep('contol', ID_lst)]
ID_lst <- ID_lst[-grep('ctrl', ID_lst)]

origin_ID_lst <- origin_ID_lst[-grep('HTG', origin_ID_lst)]
origin_ID_lst <- origin_ID_lst[-grep('control', origin_ID_lst)]
origin_ID_lst <- origin_ID_lst[-grep('Control', origin_ID_lst)]
origin_ID_lst <- origin_ID_lst[-grep('CONTROL', origin_ID_lst)]
origin_ID_lst <- origin_ID_lst[-grep('contol', origin_ID_lst)]
origin_ID_lst <- origin_ID_lst[-grep('ctrl', origin_ID_lst)]
# removed 3814-3755=59 samples

# split the each ID
ID_t <- matrix(nrow=length(ID_lst), ncol=5)
for (i in 1:length(ID_lst)){
  temp <- strsplit(as.character(ID_lst[i]),'_|-|\\.')[[1]]
  ID_t[i,1:length(temp)] <- temp
}
  # note for index 3649, ID:A12_6198776149-323980_2.CEL was split into 5 columns
  # ignore and curtail the _2 in the tail for now
  # remove column 4 as well, they are either CEL or NA
ID_t[ID_t[,4]!='CEL' & !is.na(ID_t[,4])]
ID_t <- ID_t[,-c(4,5)]

# remove the BOSON samples
remove_row <- which(nchar(ID_t[,3])==4 | nchar(ID_t[,3])==5)
ID_t <- ID_t[-remove_row,]
origin_ID_lst <- origin_ID_lst[-remove_row]
# removed 3755-3183=572 samples

table(nchar(ID_t[,1]))
table(nchar(ID_t[,2]))
table(nchar(ID_t[,3]))
table(nchar(ID_t[nchar(ID_t[,1])==3,2]))
ID_t[nchar(ID_t[,2])==9,]
# these ID with a length of 9 can be found in data registry, need to ask Azim why add a 0 in front

# replace O with 0
ID_t[grep('O',ID_t)] = gsub('O', '0', ID_t[grep('O', ID_t)])

# ignore ID column with length 3
ID_t[nchar(ID_t)==3] <- NA

# delete samples with max ID length is 6 (what are these samples)
remove_row <- vector()
for (i in 1:nrow(ID_t)){
  if (max(nchar(ID_t[i,]), na.rm = T) == 6){
    remove_row <- c(remove_row, i)
  }
}
ID_t <- ID_t[-remove_row,]
origin_ID_lst <- origin_ID_lst[-remove_row]
# removed 3183-3134= 49 samples

# all that is left are max ID digit with either 9 or 10, use those as ID
result_ID <- vector()
for (i in 1:nrow(ID_t)){
  length_lst <- sapply(ID_t[i,],nchar)
  if(max(length_lst, na.rm = T)==9){ # add 0 to 9-digit ID, for the new excel file by will
    ID_t[i,which.max(length_lst)] <- paste0('0', ID_t[i,which.max(length_lst)])
  }
  result_ID <- c(result_ID, ID_t[i,which.max(length_lst)])
}

#remove duplicate
remove_row <- which(duplicated(result_ID))
result_ID <- result_ID[-remove_row]
origin_ID_lst <- origin_ID_lst[-remove_row]
#removed 3 samples

# print whole table to file
origin_ID_lst <- as.character(origin_ID_lst)
result_ID <- cbind(origin_ID_lst, result_ID)
write.table(result_ID, file="~/OneDrive - OnTheHub - The University of Oxford/cleanID_map.tsv", quote = F, sep='\t', col.names = F, row.names = F)
