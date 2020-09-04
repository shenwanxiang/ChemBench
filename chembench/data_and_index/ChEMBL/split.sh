#!/bin/bash

#run in chemprop to split dataset get the index 

datasets=('chembl')

for i in ${!datasets[@]}; do
    echo ${datasets[$i]}
    python scripts/create_crossval_splits.py --data_path data/${datasets[$i]}.csv --save_dir crossval_folds/${datasets[$i]} --split_type scaffold
done
