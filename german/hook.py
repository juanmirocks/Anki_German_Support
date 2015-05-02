from anki.hooks import addHook
from aqt import mw

import conf

def onFocusLost(flag, n, fidx):
    if conf.APPLY_ON_NOTES[0] not in n.model()['name'].lower():
        return flag

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
        tmp = conf.apply_german_genders(origText)
        n[src] = tmp
    except Exception:
        raise Exception("Unexpected error in German Support addon. Please submit an issue at: https://github.com/jmcejuela/Anki_German_Support/issues")

    return True


addHook('editFocusLost', onFocusLost)
