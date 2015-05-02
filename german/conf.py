import german.parser

# Case insensitive, that is, German == german
APPLY_ON_NOTES = ['german']

APPLY_ON_FIELDS = ['Back', 'Bedeutung', 'Antwort']

GERMAN_GENDERS_COLORS = {
'r' : 'color:#0000ff;', #masculine, deR
's' : 'color:#00aa00;', #neutral, daS
'e' : 'color:#ff0000;' #feminine, diE
}

#-----------------------------------------------------------------------------

def apply_german_genders(line):
    return german.parser.apply_styles(line, GERMAN_GENDERS_COLORS)
