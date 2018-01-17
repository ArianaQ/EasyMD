# reserved words
# reserved = {
#     'Header1': 'HEADER1',
#     'Header2': 'HEADER2',
#     'Header3': 'HEADER3',
#     'Header4': 'HEADER4',
#     'Header5': 'HEADER5',
#     'Header6': 'HEADER6',
#     'Italic': 'ITALIC',
#     'Bold': 'BOLD',
#     'Strike': 'STRIKE',
#     'Bullet': 'BULLET',
#     'Image': 'IMAGE',
#     'Link': 'LINK',
#     'User': 'USER',
#     'Task': 'TASK'
# }

# Tokens
tokens = [
    'HEADER1',
    'HEADER2',
    'HEADER3',
    'HEADER4',
    'HEADER5',
    'HEADER6',
    'ITALIC',
    'BOLD',
    'STRIKE',
    'BULLET',
    'IMAGE',
    'LINK',
    'USER',
    'TASK',
    'RSQUARE_PAREN',
    'LSQUARE_PAREN',
    'TEXT',
    'QUOTE',
    'EMOJI',
    'CODE',
    'NUM',
    'CLEAN_TEXT'
    # 'SPACE'
]  # + list(reserved.values())


# Tokens functions
# t_TEXT = r'[a-zA-Z0-9 ]+'
# t_HEADER1 = r'Header1'
# t_HEADER2 = r'Header2'
# t_HEADER3 = r'Header3'
# t_HEADER4 = r'Header4'
# t_HEADER5 = r'Header5'
# t_HEADER6 = r'Header6'
# t_ITALICS = r'Italics'
# t_BULLET = r'Bullet'
# t_BOLD = r'Bold'
# t_STRIKE = r'Strike'
# t_IMAGE = r'Image'
# t_LINK = r'Link'
# t_USER = r'User'
# t_TASK = r'Task'
t_RSQUARE_PAREN = r'\]'
t_LSQUARE_PAREN = r'\['
t_ignore_SPACE = r'[ ]+'


def t_HEADER1(t):
    r'Header1'
    return t


def t_HEADER2(t):
    r'Header2'
    return t


def t_HEADER3(t):
    r'Header3'
    return t


def t_HEADER4(t):
    r'Header4'
    return t


def t_HEADER5(t):
    r'Header5'
    return t


def t_HEADER6(t):
    r'Header6'
    return t


def t_BULLET(t):
    r'Bullet'
    return t


def t_ITALIC(t):
    r'Italic'
    return t


def t_BOLD(t):
    r'Bold'
    return t


def t_STRIKE(t):
    r'Strike'
    return t


def t_IMAGE(t):
    r'Image'
    return t


def t_LINK(t):
    r'Link'
    return t


def t_USER(t):
    r'User'
    return t


def t_TASK(t):
    r'Task'
    return t


def t_QUOTE(t):
    r'Quote'
    return t


def t_EMOJI(t):
    r'Emoji'
    return t


def t_CODE(t):
    r'Code'
    return t


def t_NUM(t):
    r'Num.'
    return t


def t_TEXT(t):
    r'[ ]+[()a-zA-Z0-9 /!?_^:;=.><+-]+'
    t.value = t.value.strip()
    return t


def t_CLEAN_TEXT(t):
    r'[()a-zA-Z0-9 /!?_^:;=.><+-]+'
    t.value = t.value.strip()
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


# def t_eof(t):
#     pass


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)



# Build the lexer
import ply.lex as lex
lex.lex()
