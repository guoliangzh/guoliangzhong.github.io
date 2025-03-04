#!/bin/bash

python train.py \
  --run_name bandgap_Aug1 \
  --batch_size 12 \
  --num_props 1 \
  --max_epochs 50 \
  --n_embd 768 \
  --n_layer 12 \
  --n_head 12 \
  --learning_rate 1e-4 \
  --train_dataset "../../../data/mp20_nonmetal/train_data_reduce_zero.csv" \
  --test_dataset "../../../data/mp20_nonmetal/test_data_reduce_zero.csv"