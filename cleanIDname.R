# let's read the infl4 genotype data.
ifnl4 = read.table('~/OneDrive - OnTheHub - The University of Oxford/rs12979860/August2016_rs12979860.ped')
infl4_ids = data.frame(V1 = rep(NA,dim(ifnl4)[1]),V2 = rep(NA,dim(ifnl4)[1]),V3 = rep(NA,dim(ifnl4)[1]),V4 = rep(NA,dim(ifnl4)[1]),V5 = rep(NA,dim(ifnl4)[1]),V6 = rep(NA,dim(ifnl4)[1]))
for (i in 1:dim(ifnl4)[1]){
  temp = strsplit(as.character(ifnl4$V1[i]),'_|-|\\.')
  infl4_ids[i,1:length(temp[[1]])] = temp[[1]]
  
  # for(j in 1:length(temp[[1]])){
  #   if(nchar(temp[[1]][j]) == 10)
  #     infl4_ids[i] = temp[[1]][j]
  #   
  # }
}

ifnl4[which(infl4_ids$V6 == 'CEL'),]
ifnl4 = ifnl4[-which(infl4_ids$V6 == 'CEL'),]
infl4_ids = infl4_ids[-which(infl4_ids$V6 == 'CEL'),]
infl4_ids = infl4_ids[,-6]

ifnl4[grep('HTG',ifnl4$V1),]
infl4_ids[grep('HTG',ifnl4$V1),]
infl4_ids = infl4_ids[-grep('HTG',ifnl4$V1),]
infl4_ids = infl4_ids[,-5]
ifnl4 = ifnl4[-grep('HTG',ifnl4$V1),]

ifnl4[grep('Control',ifnl4$V1),]
infl4_ids[grep('Control',ifnl4$V1),]
infl4_ids = infl4_ids[-grep('Control',ifnl4$V1),]
ifnl4 = ifnl4[-grep('Control',ifnl4$V1),]

ifnl4[grep('control',ifnl4$V1),]
infl4_ids[grep('control',ifnl4$V1),]
infl4_ids = infl4_ids[-grep('control',ifnl4$V1),]
ifnl4 = ifnl4[-grep('control',ifnl4$V1),]

ifnl4[grep('contol',ifnl4$V1),]
infl4_ids[grep('contol',ifnl4$V1),]
infl4_ids = infl4_ids[-grep('contol',ifnl4$V1),]
ifnl4 = ifnl4[-grep('contol',ifnl4$V1),]

ifnl4[grep('CONTROL',ifnl4$V1),]
infl4_ids[grep('CONTROL',ifnl4$V1),]
infl4_ids = infl4_ids[-grep('CONTROL',ifnl4$V1),]
ifnl4 = ifnl4[-grep('CONTROL',ifnl4$V1),]

ifnl4[grep('ctrl',ifnl4$V1),]
infl4_ids[grep('ctrl',ifnl4$V1),]
infl4_ids = infl4_ids[-grep('ctrl',ifnl4$V1),]
ifnl4 = ifnl4[-grep('ctrl',ifnl4$V1),]

# let's get the Boson's out.
infl4_ids[nchar(infl4_ids$V3) == 4 | nchar(infl4_ids$V3) == 5,]
ifnl4[nchar(infl4_ids$V3) == 4 | nchar(infl4_ids$V3) == 5,]
Boson_samples = ifnl4[nchar(infl4_ids$V3) == 4 | nchar(infl4_ids$V3) == 5,]
ifnl4 = ifnl4[!(nchar(infl4_ids$V3) == 4 | nchar(infl4_ids$V3) == 5),]
infl4_ids = infl4_ids[!(nchar(infl4_ids$V3) == 4 | nchar(infl4_ids$V3) == 5),]
nrow(Boson_samples)
# I need to change a few things around. there are a few mistakes.
table(nchar(infl4_ids$V2))
table(infl4_ids[nchar(infl4_ids$V1)==3,1])
table(nchar(infl4_ids[nchar(infl4_ids$V1)==3,2]))

infl4_ids[nchar(infl4_ids$V1)==3 & nchar(infl4_ids$V2)==9,]
infl4_ids$V2[infl4_ids$V2 == '393492740'] = '0393492740'
# this could be a problem. There is another sample with TR0000349 study indentifier which is: '6986892022'
infl4_ids$V2[infl4_ids$V2 == '698689202'] = '0698689202'
infl4_ids$V2[infl4_ids$V2 == '478652801'] = '0478652801'

infl4_ids[nchar(infl4_ids$V2)==7,]
infl4_ids[nchar(infl4_ids$V1)==10,]

# move things up one col for the ones which are in the wrong order.
x = infl4_ids[nchar(infl4_ids$V1)==10,]
infl4_ids[nchar(infl4_ids$V1)==10,2:3] = infl4_ids[nchar(infl4_ids$V1)==10,1:2]

infl4_ids[nchar(infl4_ids$V2)==6,]

# find duplicated.
infl4_ids[duplicated(infl4_ids$V2),]
ifnl4[infl4_ids$V2 == '2358422479',]
ifnl4[infl4_ids$V2 == '5613270810',]
ifnl4[infl4_ids$V2 == '8405994508',]
ifnl4 = ifnl4[!duplicated(infl4_ids$V2),]
infl4_ids = infl4_ids[!duplicated(infl4_ids$V2),]

# replace "O" with "0" instead.
infl4_ids[grep('O',infl4_ids$V2),2] = gsub('O','0',infl4_ids[grep('O',infl4_ids$V2),2])


# all the ids together in one place.
dregistry = read.csv("~/OneDrive - OnTheHub - The University of Oxford/clinical_data/Data_Registry_Dataset_Sep_2017.csv",colClasses=c(rep("factor",36)))
# from above we have the ifnl4 and infl4_ids

# let's do it the other way.
matchingrows = rep(NA,dim(infl4_ids)[1])
for (i in 1:dim(infl4_ids)[1]){
  if (nchar(infl4_ids$V2[i]) == 10){
    for(j in c(1,3,6)){
      temp = grep(infl4_ids$V2[i],dregistry[,j])
      if (length(temp != 0)) {
        matchingrows[i] = temp
        break()}
    }
  }
  
}

# let's get the missing ones.
infl4_ids[nchar(infl4_ids$V2)==10 & is.na(matchingrows),]
nrow(infl4_ids[nchar(infl4_ids$V2)==10 & is.na(matchingrows),])