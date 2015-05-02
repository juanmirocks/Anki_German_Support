# -*- coding: utf-8 -*-
#
#  model.py --- German Model
# 
# Copyright (C) 2009 Juan Miguel Cejuela 
# 
# created: 2009-07-11
# updated: 2009-07-24
# 

from anki.models import Model, CardModel, FieldModel
import anki.stdmodels


def GermanModel():
    m = Model(_("German"))

    #Model
    m.addFieldModel(FieldModel(u'Frage', True, True))
    m.addFieldModel(FieldModel(u'Antwort', False, False))

    #Cards
    m.addCardModel(CardModel(u"Wiedererkennen",
                             u"%(Frage)s",
                             u"%(Antwort)s"))
    m.addCardModel(CardModel(u"Gedächtnis",
                             u"%(Antwort)s",
                             u"%(Frage)s",
                             active=False))
    m.tags = u"German"
    return m

anki.stdmodels.models['German'] = GermanModel
