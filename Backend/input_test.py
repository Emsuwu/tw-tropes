from add_entry import *

WARNING_MANDATORY_FIELD = '\n[!] Mandatory field\n'
WARNING_NUMBER_ONLY = '\n[!] Must be integer\n'
WARNING_MONTH = '\n[!] Must be a valid month (from 1-12)\n'
WARNING_DAY = '\n[!] Must be a valid day (from 1-31)\n'
notOK = True
while notOK:

    print("\n[!] Warning: Don't try to use HTML, it will be removed.\n")

    id = ' '
    while ' ' in id or '_' in id or id != id.lower():
        print('Specify an ID for the entry you wish to add.\nUse hyphens instead of spaces.')
        id = input("*->")
        if ' ' in id or '_' in id or id != id.lower():
            pass
            print('\n[!] Please don\'t use underscores or spaces in the ID! ID must not contain uppercase.\n')
        if id == '':
            id = ' '
            print(WARNING_MANDATORY_FIELD)

    medium = ''
    while medium == '':
        medium = input('\nSpecify a medium (anime/movie/book/show/webcomic etc.)\n*->').capitalize()
        if medium == '' or medium == ' ':
            print(WARNING_MANDATORY_FIELD)

    titleEn = ''
    while titleEn == '':
        titleEn = input("\nEnglish Title\n*->")
        if titleEn == '':print(WARNING_MANDATORY_FIELD)

    titleRomaji = input("\nRomaji Title\n->")
    titleJp = input("\nJapanese Title\n->")
    malID = input("\nMAL ID (if existent)\n->")

    thumbnail = input("\nThumbnail URL\n*->")
    while thumbnail == '':
        thumbnail = input("nThumbnail URL\n*->")
        if thumbnail == '':print(WARNING_MANDATORY_FIELD)

    print('\n----- Trigger Warnings (enter blank to stop adding) -----\n')
    triggerWarnings = ''
    inp = ' '
    while inp != '':
        inp = input('->')
        if inp!='':
            if triggerWarnings != '':
                triggerWarnings += '$newline$' + inp.capitalize()
            else:
                triggerWarnings += inp.capitalize()

    print('\n----- Negative representations -----\n')
    negativeRepresentations = ''
    inp = ' '
    while inp != '':
        print('\nTitle for negative representation (enter blank to stop adding)')
        inp = input('->')
        if inp == '':
            break
        negativeRepresentations += inp + '$:$'

        print(f'—————————————\nDescription of negative representation: \'{inp}\'')
        inp = input('->')
        while inp == '':
            print("Description must not be blank!")
            inp = input('->')
        negativeRepresentations += inp + '$newline$'

        inp = ' '
    if negativeRepresentations[-1]=='$':
        negativeRepresentations = negativeRepresentations[0:-9]


    initialReleaseDate = ''
    year = 0
    month = 0
    day = 0
    inp = ''

    print('\n\nRelease year')
    while inp == '':
        inp = input('->')
        try:
            year = int(inp)
        except:
            print(WARNING_NUMBER_ONLY)
            inp = ''
    inp = ''
    print('\n\nRelease month')
    while inp == '':
        inp = input('->')
        try:
            month = int(inp)
            if month < 1 or month > 12:
                inp = ''
                print(WARNING_MONTH)
        except:
            print(WARNING_NUMBER_ONLY)
            inp = ''
    inp = ''
    print('\n\nRelease day')
    while inp == '':
        inp = input('->')
        try:
            day = int(inp)
            if day < 1 or day > 31:
                inp = ''
                print(WARNING_DAY)
        except:
            print(WARNING_NUMBER_ONLY)
            inp = ''

    initialReleaseDate = f'{day}/{month}/{year}'

    print('\n————————————————————————')
    
    print(f'''
                                  ID | {id}
                              Medium | {medium}
                       English Title | {titleEn}
                     Romanized Title | {titleRomaji}
                      Japanese Title | {titleJp}
                       Thumbnail URL | {thumbnail}
        Trigger Warnings (formatted) | {triggerWarnings}
Negative Representations (formatted) | {negativeRepresentations}
                Initial Release Date | {initialReleaseDate}
          ''')

    print('\nDoes that look right [y/n]?')
    inp = ''
    while inp != 'y' and inp != 'n':
        inp = input('->').lower()
    
    if inp == 'y': notOK = False
    else: print('\nLets start over!\n')

print('\n\nAppending data...')

add_entry(
    id, 
    medium,
    initialReleaseDate,
    titleEn, 
    titleRomaji, 
    titleJp,
    triggerWarnings,
    negativeRepresentations,
    malID,
    thumbnail
    )
'''
id : str,
medium : str, 
titleEn : str, 
titleRomaji = '', 
titleJp = '', 
triggerWarnings='',
negativeRepresentations='',
malID = '', 
thumbnail='Images/Thumbnails/placeholder.jpg'
'''

input('Entry added! Press enter to close.')