#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024-11-16 19:32:54 Saturday

@author: Nikhil Kapila
"""
# Pipeline adapted from https://github.com/AttentionSeekers/CNNtention/blob/main/pipeline_template.py

# TODO: Clean out redundant imports.
import os, sys
import numpy as np
import torch, torchvision
import random
from matplotlib import pyplot as plt

# TODO: Do I need MLFlow? Am I gonna train this even? I think not.
# import mlflow

# TODO: Do I use skorch?
# from skorch import NeuralNetClassifier
# from skorch.callbacks import EpochScoring, MlflowLogger, EarlyStopping #, ProgressBar

RANDOM_VAR = 11

def load_data():
    # TODO: Load FashionMNIST from data/
    train_set, test_set = None, None
    return train_set, test_set

def train(train_set, test_set):
    pass

def print_hyperparams():
  pass

def main():
    pass

if __name__ == '__main__':
    random.seed(RANDOM_VAR)
    np.random.seed(RANDOM_VAR)
    torch.manual_seed(RANDOM_VAR)
    torch.cuda.manual_seed(RANDOM_VAR)
    torch.backends.cudnn.deterministic = True

