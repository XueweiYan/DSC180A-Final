#!/usr/bin/env python

import sys
import os
from shutil import copyfile

sys.path.insert(0, 'src')

def main(targets):
    cwd = os.getcwd()
    if 'model' in targets:
        script_path = os.path.join(cwd, 'src/AutoPhrase/auto_phrase.sh')
        cmd = 'bash {}'.format(script_path)
        os.chdir('src/AutoPhrase')
        os.system(cmd)
        copyfile('models/DBLP/AutoPhrase.txt', os.path.join(cwd, 'results/AutoPhrase.txt'))
        copyfile('models/DBLP/AutoPhrase_multi-words.txt', os.path.join(cwd, 'results/AutoPhrase_multi-words.txt'))
        copyfile('models/DBLP/AutoPhrase_single-word.txt', os.path.join(cwd, 'results/AutoPhrase_single-word.txt'))
        os.chdir(cwd)
    if 'segmentation' in targets:
        script_path = os.path.join(cwd, 'src/AutoPhrase/phrasal_segmentation.sh')
        cmd = 'bash {}'.format(script_path)
        os.chdir('src/AutoPhrase')
        os.system(cmd)
        copyfile('models/DBLP/segmentation.txt', os.path.join(cwd, 'results/segmentation.txt'))
        os.chdir(cwd)
        
    if 'test' in targets:
        script_path = os.path.join(cwd, 'scripts/test_demo.py')
        cmd = 'python {}'.format(script_path)
        os.system(cmd)


if __name__ == '__main__':
    '''
    For training-testing, run via: python run.py model segmentation test
    TO use pretrained model, run via: python run.py test
    '''
    targets = sys.argv[1:]
    main(targets)
