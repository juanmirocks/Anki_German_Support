# -*- coding: utf-8 -*-
#  hook.py --- hook to Anki
#
# Copyright (C) 2009 Juan Miguel Cejuela
#
# created: 2009-07-11
# updated: 2009-07-11
#
#

import re, subprocess
from anki.utils import findTag
from anki.hooks import addHook

import german.styles


#
# Global
#

modelTag = "German"
#srcField = "Ausdruck"
#dstField = "Ausdruck" #yes, the same
# in alle!


#
# Fact Hook
#

def onFocusLost(fact, field):
    #if field.name != srcField:
    #    return
    if not findTag(modelTag, fact.model.tags):
        return

    origText = re.sub("\[sound:.+?\]", "", field.value)
    tmp = german.styles.apply_german_genders(origText)
    try:
        tmp = german.styles.apply_german_genders(origText)
        fact[field.name] = tmp
    except Exception:
#        from ui.utils import showInfo
#        showInfo("in German Support: something wrong happened! Please send the HTML code to ")
        return

#
# Add Hook
#

addHook('fact.focusLost', onFocusLost)
