import os

MODEL_FLAGS="--image_size 64 --num_channels 128 --num_res_blocks 3 --learn_sigma True"
DIFFUSION_FLAGS="--diffusion_steps 4000 --noise_schedule cosine"
TRAIN_FLAGS="--lr 1e-4 --batch_size 128"

data_dir = '/home/yoos-bii/Desktop/data_tct/train'

command = f'python3 scripts/image_train.py --data_dir {data_dir} {MODEL_FLAGS} {DIFFUSION_FLAGS} {TRAIN_FLAGS}'

os.system(command)