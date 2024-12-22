# Copyright (C) 2009-NOW Juan Miguel Cejuela
#
# For more info or if you have issues: https://github.com/juanmirocks/Anki_German_Support
#

#
# Feel free to modify `config.json` to change the default configuration
#

from anki.hooks import addHook

from german.hook import onFocusLost

addHook("editFocusLost", onFocusLost)
