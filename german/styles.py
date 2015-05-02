# -*- coding: utf-8 -*-
#  styles.py --- Shortcuts styles definitions
# 
# Copyright (C) 2009 Juan Miguel Cejuela 
# 
# created: 2009-07-11
# updated: 2009-08-26
# 
# 

import german.parser

#### 
#### Change to your taste
####
GERMAN_GENDERS = {'r' : 'color:#0000ff;',
                  's' : 'color:#00aa00;',
                  'e' : 'color:#ff0000;'}


def apply_german_genders(line):
    return german.parser.apply_styles(line, GERMAN_GENDERS)
