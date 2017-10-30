#!bin/sh
#$ -N test-cluster
#$ stop-hcv -q short.qc
# clustering the samples by genetic similarity
plink --bfile August2016 --cluster --cc --ppc 0.01