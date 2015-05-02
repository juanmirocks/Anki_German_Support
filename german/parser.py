def span_style_hook(word, style):
    return '<span style="' + style + '">' + word + '</span>'


def find_html_tag(line):
    s = line.find('<')
    if s == -1:
        return line, '',''
    else:
        eaux = line.find('>') + 1
        e = line.find('>') + 1
        if e == 0: #html 1 tag
            return line[:s], line[s:eaux], line[eaux:]
        else: #normal html 2 tags
            return line[:s], line[s:e], line[e:]


# def apply_styles_wo_html(line, tokens_dict):
#     res = ''
#     inwordp = pluralp = False
#     last = len(line) - 1
#     for i in range(last + 1):
#         c = line[i]
#         if inwordp:
#             if c == ',':
#                 pluralp = True
#                 word += c
#             elif c.isspace():
#                 if pluralp:
#                     pluralp = False
#                     word += c
#                 else:
#                     res += span_style_hook(word, tokens_dict[inwordp]) + c
#                     inwordp = pluralp = False
#             else:
#                 word += c
#         else:
#             if c in tokens_dict and i < last and (line[i+1].isupper() or line[i+1] == '['):
#                 word = c
#                 inwordp = c #True
#             else:
#                 res += c
#     else:
#         if inwordp: res += span_style_hook(word, tokens_dict[inwordp])

#     return res


def apply_styles_wo_html(line, tokens_dict):
    res = ''
    inwordp = False
    last = len(line) - 1
    for i in range(last + 1):
        c = line[i]
        if inwordp:
            if c.isspace() or c == ',':
                res += span_style_hook(word, tokens_dict[inwordp]) + c
                inwordp = False
            else:
                word += c
        else:
            if c in tokens_dict and i < last and (line[i+1].isupper() or line[i+1] == '[') and (i == 0 or not line[i-1].isalpha()):
                word = c
                inwordp = c #True
            else:
                res += c
    else:
        if inwordp: res += span_style_hook(word, tokens_dict[inwordp])

    return res


def apply_styles(line, tokens_dict):
    res = ''
    while True:
        l, c, r = find_html_tag(line)
        res += apply_styles_wo_html(l, tokens_dict)
        res += c
        if r: line = r
        else:
            return res
