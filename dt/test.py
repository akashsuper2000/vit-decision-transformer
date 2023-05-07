import torch

print(torch.__version__)


import pickle


with open('./decision-transformer/gym/data/hopper-medium-v2.pkl', 'rb') as f:
    data = pickle.load(f)
    print(data[0]['rewards'].shape)
