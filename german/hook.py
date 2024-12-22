from typing import Any, cast

from anki.notes import Note
from aqt import mw

import german.parser

CONF = cast(dict[str, Any], mw.addonManager.getConfig(__name__))


# TODO all array searches should stop early. But ifilter is not available in Anki?
# See https://github.com/ankitects/anki/blob/24.11/qt/tools/genhooks_gui.py#L1070-L1075
def onFocusLost(changed: bool, note: Note, current_field_idx: int) -> bool:
    note_type = note.note_type()
    if note_type is None:
        return changed

    note_type_name: str = note_type["name"].lower()

    # case insensitive, "in" (substring) search
    if not any(t in note_type_name for t in cast(list[str], CONF["apply_on_notes"])):
        return changed

    src = None

    # exact match search
    for field_id, field_name in enumerate(mw.col.models.field_names(note_type)):
        for f in CONF["apply_on_fields"]:
            if field_name == f:
                src = f
                src_idx = field_id

    if not src or (src_idx != current_field_idx):
        return changed

    orig_text = mw.col.media.strip(note[src])

    if not orig_text:
        return changed

    try:
        note[src] = german.parser.apply_styles(orig_text, CONF["german_genders_colors"])
    except Exception:
        raise Exception(
            "Unexpected error in German Support addon. Please submit an issue at: https://github.com/juanmirocks/Anki_German_Support/issues"
        )

    return True
