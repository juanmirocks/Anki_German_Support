def span_style_hook(word: str, style: str) -> str:
    return f"""<span style="{style}">{word}</span>"""


def find_html_tag(text: str) -> tuple[str, str, str]:
    s = text.find("<")
    if s == -1:
        return text, "", ""
    else:
        e = text.find(">") + 1
        return text[:s], text[s:e], text[e:]


def apply_styles_wo_html(text: str, tokens_dict: dict[str, str]) -> str:
    ret = ""

    inwordp = ""  # empty string == not in word
    word = ""

    last = len(text) - 1
    for i in range(last + 1):
        c = text[i]
        if inwordp:
            if c.isspace() or c == ",":
                ret += span_style_hook(word, tokens_dict[inwordp]) + c
                inwordp = ""
            else:
                word += c
        else:
            if (
                c in tokens_dict
                and i < last
                and (text[i + 1].isupper() or text[i + 1] == "[")
                and (i == 0 or not text[i - 1].isalpha())
            ):
                word = c
                inwordp = c  # True
            else:
                ret += c
    else:
        if inwordp:
            ret += span_style_hook(word, tokens_dict[inwordp])

    return ret


def apply_styles(text: str, tokens_dict: dict[str, str]) -> str:
    ret = ""
    while True:
        l, c, r = find_html_tag(text)
        ret += apply_styles_wo_html(l, tokens_dict)
        ret += c
        if r:
            text = r
        else:
            return ret
