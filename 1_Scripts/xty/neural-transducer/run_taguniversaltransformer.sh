#!/bin/bash
#SBATCH --job-name=universal
#SBATCH --output=universal.out
#SBATCH --error=universal.err
#SBATCH --partition=debug
#SBATCH --nodes=1
#SBATCH --gres=gpu:v100:2

lang=${1:-xty}
arch=${2:-taguniversaltransformer}
suff=$3

lr=0.001
scheduler=warmupinvsqr
epochs=100
warmup=100
beta2=0.98       # 0.999
label_smooth=0.1 # 0.0
total_eval=50
bs=400 # 256

# transformer
layers=10
hs=1024
embed_dim=256
nb_heads=4
#dropout=${2:-0.3}
dropout=0.3
ckpt_dir=checkpoints/sig22

path=../../../dataset

python src/train.py \
    --dataset sigmorphon17task1 \
    --train $path/$lang.train.tsv \
    --dev $path/$lang.dev.tsv \
    --test $path/$lang.PREP.tsv \
    --model $ckpt_dir/$arch/$lang \
    --decode greedy --max_decode_len 32 \
    --embed_dim $embed_dim --src_hs $hs --trg_hs $hs --dropout $dropout --nb_heads $nb_heads \
    --label_smooth $label_smooth --total_eval $total_eval \
    --src_layer $layers --trg_layer $layers --max_norm 1 --lr $lr --shuffle \
    --arch $arch --gpuid 0 --estop 1e-8 --bs $bs --epochs $epochs \
    --scheduler $scheduler --warmup_steps $warmup --cleanup_anyway --beta2 $beta2 --bestacc

echo "TRAINING DONE!!"
python prep.py $lang

echo "FINAL SUBMISSION DONE!!"