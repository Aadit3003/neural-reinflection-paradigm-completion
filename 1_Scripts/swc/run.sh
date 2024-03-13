#!/bin/bash
#SBATCH --job-name=swc
#SBATCH --output=swc.out
#SBATCH --error=swc.err
#SBATCH --partition=debug
#SBATCH --nodes=1
#SBATCH --gres=gpu:v100:2

python prep.py # Prepares the new Augmented Training Files

# Check Baseline Results
python baseline.py "dev" "../../dataset/swc.train.tsv"

# Train on the Augmented data and pick the one with the highest dev accuracy
python baseline.py "dev" "../../dataset/swc.train_2_simple_addition.tsv"

python baseline.py "dev" "../../dataset/swc.train_3_self_pollinate.tsv"

python baseline.py "dev" "../../dataset/swc.train_4_cross_pollinate.tsv"

# Generate the test predictions
python baseline.py "test" "../../dataset/swc.train_2_simple_addition.tsv"


echo "SWAHILI DONE!!"