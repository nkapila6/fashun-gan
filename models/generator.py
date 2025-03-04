#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2025-03-04 19:14:59 Tuesday

@author: Nikhil Kapila
"""

import torch
import torch.nn as nn

class Generator(nn.Module):
    def __init__(self):
        super(Generator, self).__init__()

        # Make a couple MLP layers, or maybe I could try a CNN?
        # Need to think over it.

    def forward(self, z):
        # z is sampled noise
        pass