#!/bin/bash
#$ -N test-cluster
#$ -q short.qc
# clustering the samples by genetic similarity
/users/bag/clme1992/bin/plink --bfile /data/jaga/stophcv/steven/August2016/step2/August2016 --cluster --cc --ppc 0.01