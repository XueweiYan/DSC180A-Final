#!/usr/bin/env python

import sys
import os
import json

sys.path.insert(0, 'src')

def main(targets):
    cwd = os.getcwd()
    if 'model' in targets:
        script_path = os.path.join(cwd, 'src/AutoPhrase/auto_phrase.sh')
        cmd = 'bash {}'.format(script_path)
        os.chdir('src/AutoPhrase')
        os.system(cmd)
        os.chdir(cwd)
    
    if 'segmentation' in targets:
        script_path = os.path.join(cwd, 'src/AutoPhrase/phrasal_segmentation.sh')
        cmd = 'bash {}'.format(script_path)
        os.chdir('src/AutoPhrase')
        os.system(cmd)
        os.chdir(cwd)
        
    if 'test' in targets:
        script_path = os.path.join(cwd, 'scripts/mini_test.py')
        cmd = 'bash {}'.format(script_path)
        os.system(cmd)


if __name__ == '__main__':
    # run via:
    # python main.py model segmentation test
    targets = sys.argv[1:]
    main(targets)
