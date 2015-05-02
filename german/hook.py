from anki.hooks import addHook
from aqt import mw

import conf
import german.parser

#TODO all array searches should stop early. But ifilter is not available in Anki?
def onFocusLost(flag, n, fidx):
    currentNote = n.model()['name'].lower()
    matchingNote = None

    for noteTypeKey in conf.APPLY_ON_NOTES:
        if noteTypeKey in currentNote:
            matchingNote = noteTypeKey

    if not matchingNote:
        return flag;

    src = None

    for fid, name in enumerate(mw.col.models.fieldNames(n.model())):
        for f in conf.APPLY_ON_FIELDS:
            if name == f:
                src = f
                srcIdx = fid

    if not src or (srcIdx != fidx):
        return flag

    origText = mw.col.media.strip(n[src])
    if not origText:
        return flag

    try:
        tmp = german.parser.apply_styles(origText, conf.GERMAN_GENDERS_COLORS)
        n[src] = tmp
    except Exception as e:
        #raise
        raise Exception("Unexpected error in German Support addon. Please submit an issue at: https://github.com/jmcejuela/Anki_German_Support/issues")

    return True


addHook('editFocusLost', onFocusLost)
