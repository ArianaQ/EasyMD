import ply.yacc as yacc
from easy_md import tokens
import os.path

md_code = ''
bypass = ''
previous_act = ''


def p_expression(p):
    '''expression : header 
                | bold 
                | italic
                | strike
                | user
                | image
                | bullet
                | link
                | quote
                | emoji
                | code
                | num
                | clean_text'''
    new_line()
    p[0] = p[1]


def p_header(p):
    '''header : LSQUARE_PAREN HEADER1  TEXT RSQUARE_PAREN
            | LSQUARE_PAREN HEADER2  TEXT RSQUARE_PAREN
            | LSQUARE_PAREN HEADER3  TEXT RSQUARE_PAREN
            | LSQUARE_PAREN HEADER4  TEXT RSQUARE_PAREN
            | LSQUARE_PAREN HEADER5  TEXT RSQUARE_PAREN
            | LSQUARE_PAREN HEADER6  TEXT RSQUARE_PAREN
    '''
    if p[2] == 'Header1':
        p[0] = header1_to_md(p[3])
    elif p[2] == 'Header2':
        p[0] = header2_to_md(p[3])
    elif p[2] == 'Header3':
        p[0] = header3_to_md(p[3])
    elif p[2] == 'Header4':
        p[0] = header4_to_md(p[3])
    elif p[2] == 'Header5':
        p[0] = header5_to_md(p[3])
    else:
        p[0] = header6_to_md(p[3])


def p_clean_text(p):
    '''clean_text : CLEAN_TEXT
                    | CLEAN_TEXT compound 
                    | CLEAN_TEXT compound TEXT
                    | clean_text
                    '''

    global md_code
    global previous_act
    if previous_act == 'list' or previous_act == 'quote':
        md_code += '\n'
    md_code += p[1] + ' ' + bypass
    start = -1
    previous = -1
    for i in range(len(md_code)):
        if md_code[i:i + len(bypass)] == bypass:
            previous = start
            start = i

    lmd_code = md_code[:previous]
    rmd_code = md_code[previous + len(bypass):]
    md_code = lmd_code + rmd_code

    if len(p) == 4:
        md_code += p[3]
        p[0] = p[1] + bypass + p[3]
    else:
        p[0] = p[1] + bypass


def p_compund(p):
    '''compound : bold 
                | italic
                | strike
                | user
                | image
                | link
                | emoji
                | bold clean_text
                | italic clean_text
                | strike clean_text
                | user clean_text
                | image clean_text
                | link clean_text
                | emoji clean_text'''


def p_bold(p):
    '''bold : LSQUARE_PAREN BOLD TEXT RSQUARE_PAREN'''
    p[0] = bold_to_md(p[3])


def p_italic(p):
    '''italic : LSQUARE_PAREN ITALIC TEXT RSQUARE_PAREN'''
    p[0] = italic_to_md(p[3])


def p_strike(p):
    '''strike : LSQUARE_PAREN STRIKE TEXT RSQUARE_PAREN'''
    p[0] = strike_to_md(p[3])


def p_user(p):
    '''user : LSQUARE_PAREN USER TEXT RSQUARE_PAREN '''
    p[0] = user_to_md(p[3])


def p_image(p):
    '''image : LSQUARE_PAREN IMAGE TEXT RSQUARE_PAREN'''
    p[0] = image_to_md(p[3])


def p_bullet(p):
    '''bullet : LSQUARE_PAREN BULLET TEXT RSQUARE_PAREN'''
    p[0] = bullet_to_md(p[3])


def p_link(p):
    '''link : LSQUARE_PAREN LINK TEXT  RSQUARE_PAREN'''
    p[0] = link_to_md(p[3])


def p_quote(p):
    '''quote : LSQUARE_PAREN QUOTE TEXT RSQUARE_PAREN'''
    p[0] = quote_to_md(p[3])


def p_emoji(p):
    '''emoji : LSQUARE_PAREN EMOJI TEXT RSQUARE_PAREN'''
    p[0] = emoji_to_md(p[3])


def p_code(p):
    '''code : LSQUARE_PAREN CODE TEXT RSQUARE_PAREN'''
    p[0] = code_to_md(p[3])


def p_num(p):
    '''num : LSQUARE_PAREN NUM TEXT RSQUARE_PAREN'''
    p[0] = num_to_md(p[2], p[3])
    p[0] = p[1]


def new_line():
    global md_code
    md_code += '\n'


def header1_to_md(text):
    global md_code
    global previous_act
    if previous_act == 'list' or previous_act == 'quote':
        md_code += '\n'
    md_code += '# ' + text
    previous_act = 'header'
    return '# ' + text


def header2_to_md(text):
    global md_code
    global previous_act
    if previous_act == 'list' or previous_act == 'quote':
        md_code += '\n'
    md_code += '## ' + text
    previous_act = 'header'
    return '## ' + text


def header3_to_md(text):
    global md_code
    global previous_act
    if previous_act == 'list' or previous_act == 'quote':
        md_code += '\n'
    md_code += '### ' + text
    previous_act = 'header'
    return ' ### ' + text


def header4_to_md(text):
    global md_code
    global previous_act
    if previous_act == 'list' or previous_act == 'quote':
        md_code += '\n'
    md_code += '#### ' + text
    previous_act = 'header'
    return ' #### ' + text


def header5_to_md(text):
    global md_code
    global previous_act
    if previous_act == 'list' or previous_act == 'quote':
        md_code += '\n'
    md_code += '##### ' + text
    previous_act = 'header'
    return '##### ' + text


def header6_to_md(text):
    global md_code
    global previous_act
    if previous_act == 'list' or previous_act == 'quote':
        md_code += '\n'
    md_code += '###### ' + text + ' '
    previous_act = 'header'
    return ' ###### ' + text + ' '


def bold_to_md(text):
    global bypass
    global md_code
    global previous_act
    if previous_act == 'list' or previous_act == 'quote':
        md_code += '\n'
    md_code += '**' + text + '**' + ' '
    bypass = '**' + text + '**' + ' '
    previous_act = 'bold'
    return ' ' + '**' + text + '**' + ' '


def italic_to_md(text):
    global bypass
    global md_code
    global previous_act
    if previous_act == 'list' or previous_act == 'quote':
        md_code += '\n'
    md_code += '*' + text + '*' + ' '
    bypass = '*' + text + '*' + ' '
    previous_act = 'italic'
    return '*' + text + '*' + ' '


def strike_to_md(text):
    global bypass
    global md_code
    global previous_act
    if previous_act == 'list' or previous_act == 'quote':
        md_code += '\n'
    md_code += ' ' + '~~' + text + '~~' + ' '
    bypass = ' ' + '~~' + text + '~~' + ' '
    previous_act = 'strike'
    return '~~' + text + '~~'


def user_to_md(text):
    global bypass
    global md_code
    global previous_act
    if previous_act == 'list' or previous_act == 'quote':
        md_code += '\n'
    md_code += '@' + text + ' '
    bypass = '@' + text + ' '
    previous_act = 'user'
    return '@' + text + ' '


def image_to_md(text):
    global bypass
    global md_code
    global previous_act

    temp = text.split('Link')
    link = temp[1]
    text = temp[0]

    if previous_act == 'list' or previous_act == 'quote':
        md_code += '\n'
    bypass = '![' + text + ']' + '(' + link + ')' + ' '
    md_code += '![' + text + ']' + '(' + link + ')' + ' '
    previous_act = 'image'
    return '![' + text + ']' + '(' + link + ')' + ' '


def bullet_to_md(text):
    global md_code
    global previous_act
    md_code += '* ' + text + ' '
    previous_act = 'list'
    return '* ' + text + ' '


def link_to_md(text):
    temp = text.split('Text')
    link = temp[0]
    text = temp[1]
    global bypass
    global md_code
    global previous_act
    if previous_act == 'list' or previous_act == 'quote':
        md_code += '\n'
    bypass = '[' + text + ']' + '(' + link + ') '
    md_code += '[' + text + ']' + '(' + link + ') '
    previous_act = 'link'
    return '[' + text + ']' + '(' + link + ') '


def quote_to_md(text):
    global md_code
    global previous_act
    if previous_act == 'list' or previous_act == 'quote':
        md_code += '\n'
    md_code += '>' + text + ' '
    previous_act = 'quote'
    return '>' + text + ' '


def emoji_to_md(text):
    global md_code
    global previous_act
    global bypass
    if previous_act == 'list' or previous_act == 'quote':
        md_code += '\n'
    bypass = ':' + text + ':'
    md_code += bypass
    previous_act = 'emoji'
    return bypass


def code_to_md(text):
    global bypass
    global md_code
    global previous_act
    md_code += "```"+ text + "```" + ' '
    bypass = "```" + text + "```" + ' '
    previous_act = 'code'
    return "```" + text + "```" + ' '



def num_to_md(num, text):
    num = str(num.split('Num')[1])
    global md_code
    global previous_act
    md_code += num + '. ' + text
    previous_act = 'list'
    return num + '.' + text


def p_error(p):
    print("Syntax error at '%s'" % p.value)


def ask_for_path():
    checkagain = True
    while checkagain:
        path = input("TYPE FILE TO CONVERT TO MD: ")

        if (path.lower() == "exit"):
            print('\nThanks for using EasyMD! Bye!')
            exit()
        elif ((os.path.exists(path)) == False):
            print("\nFILE DOESN'T EXIST, TRY AGAIN! | TO EXIT, TYPE EXIT\n")
        elif (path.lower().endswith('.txt') == False):
            print("\nFILE IS NOT .TXT, TRY AGAIN! | TO EXIT, TYPE EXIT\n")
        else:
            checkagain = False
            return path


def show_in_terminal(pa):
    with open(path) as f:
        for line in f:
            result = parser.parse(line)

    print('\n============================')
    print('MD CODE TRANSLATION PREVIEW:')
    print('============================')
    print(md_code)


def save_and_show(pa):
    with open(path) as f:
        for line in f:
            result = parser.parse(line)

    newfile = open("converted.md", "w")
    newfile.write(md_code)
    newfile.close()

    print('\n============================')
    print('MD CODE TRANSLATION PREVIEW:')
    print('============================')
    print(md_code)


def just_save(pa):
    with open(path) as f:
        for line in f:
            result = parser.parse(line)

    newfile = open("converted.md", "w")
    newfile.write(md_code)
    newfile.close()


# BUILD PARSER
parser = yacc.yacc()

# USER INTERFACE
print('\n==================')
print('WELCOME TO EASYMD!')
print('==================')
print('AS A USER, YOU CAN CONVERT A FILE WITH EASYMD')
print('SYNTAX TO MD CODE AND/OR TO AN MD FILE!')

check = True
while (check):
    print('\nWHAT DO YOU WANT TO DO?')
    print('1 - Show translation in terminal.')
    print('2 - Save translation to a new file.')
    print('3 - Both! Show and save translation.')
    print('4 - Exit.\n')

    action = input()
    if (action == "1"):
        path = ask_for_path()
        show_in_terminal(path)
        check = False
    elif (action == "2"):
        path = ask_for_path()
        just_save(path)
        check = False
    elif (action == "3"):
        path = ask_for_path()
        save_and_show(path)
        check = False
    elif (action == "4"):
        print('Thanks for using EasyMD! Bye!')
        exit()
    else:
        print("INVALID! | TRY AGAIN!\n")
