# -*- coding: utf-8 -*-
#
# de.py ---  German Support for Anki
#
# Copyright (C) 2009 Juan Miguel Cejuela
#
# created: 2009-07-10
# updated: 2009-07-24
#
#
################################################################################
# Description:
################################################################################
#
# Features:
#	-Automatic colored recognition for genders
#
#		Whenever found rS, eS, or sS (s being a 'Substantiv'), S changes
#		to the defined color for the gender. You can change the
#		shortcuts and style preferences in styles.py
#
#	-German Model with fields: 'Frage', 'Antwort'
#		        and cards: 'Wiedererkennen', 'Gedächtnis'
#
################################################################################
# Use:
################################################################################
#
# Add your cards with the German Model.
#


#
# Change styles.py if you have other style preferences!
#

import german.model
import german.parser
import german.styles
import german.hook

from ankiqt import mw


mw.registerPlugin("German Support", 10)
