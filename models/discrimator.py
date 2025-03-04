#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2025-03-04 19:14:50 Tuesday

@author: Nikhil Kapila
"""

import torch
import torch.nn as nn

class Discriminator(nn.Module):
    def __init__(self):
        super(Discriminator, self).__init__()

        # a simple binary classifier
        self.d = nn.Sequential(
               
        )

    def forward(self, input):
        # input can be g(z) or ground truth
        return self.d(input)