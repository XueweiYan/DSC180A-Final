#!/usr/bin/env python

import sys
import os
import pandas as pd
import numpy as np
from termcolor import colored
import re

sys.path.insert(0, 'src')

def highlight_phrases(text):
    ret = []
    bracket_match = 0
    for ch in text:
        if ch == '<' or ch =='>':
            bracket_match = (bracket_match + 1) % 4
        elif bracket_match == 0:
            ret.append(ch)
        elif bracket_match == 2:
            ret.append(colored(ch, 'yellow', 'on_red'))
    return "".join(ret)
    
def visualize_phrases(length=30):
    file = "results/segmentation.txt"
    with open(file) as f:
        txt = f.readlines()
    for i in range(length):
        print(highlight_phrases(txt[i]))

def main():
    '''
    This is a brief demo of the segmentation result by applying the model onto the text corpus.
    For more visualizations and analysis, please go to the EDA notebook.
    '''
    visualize_phrases()

if __name__ == '__main__':
    main()
