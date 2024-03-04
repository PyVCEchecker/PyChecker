import re
import nltk
from itertools import permutations
from pyphonetics import Soundex

SAL_REM = ['smt', 'mrs', 'mr', 'ms', 'dr', 'col', 'lt', 'dr', 'dr(mrs)',
           'm.s.', 'm/s', 'messes', 'messesrs', 'messors', 'messres',
           'messrs', 'messsers', 'miss', 'misss', 'mistar', 'mr', 'mr.',
           'mrs', 'mrs,', 'ms', 'ms.', 'ms.shri', 'prof', 'prop.shri',
           'prop.smt', 'sh', 'sh.shri', 'shri', 'sm', 'smt', 'lt',
           'lt.', 'col ', 'col.', 'cl', 'cl.', 'cdr', 'cdr.',
           'captain', 'flight', 'lieutenant', 'colonel', 'commander',
           'lieutenant', 'brig', 'prop']

COMPANY_BIGRAMS_TO_REMOVE = {('priwate', 'limited'), ('priwate', 'ltd'),
                             ('pwt', 'limited'), ('pwt', 'ltd'), ('p', 'ltd'),
                             ('p', 'limited'), ('priwate', 'l'), ('pwt', 'l'),
                             ('corporation', 'limited'),
                             ('corporation', 'ltd'), ('corporation', 'l'),
                             ('corp', 'limited'), ('corp', 'ltd'),
                             ('corp', 'l'), ('cor', 'limited'), ('cor', 'ltd'),
                             ('cor', 'l'), ('co', 'limited'), ('p', 'l')}

REMOVE_ONLY_IN_CASE_OF_NAME = ['mazor']

COMPANY_SINGLE = {'pwt', 'priwate', 'limited', 'ltd', 'corporation', 'corp',
                  'cor', 'co', 'llp'}

REPLACE_BY_SPACE_RE = re.compile(r'[/(){}\.[\]\|@;]')

SINGLE_CHARACTER_PHONETICS = {'v': 'w', 'j': 'z', 'q': 'k'}

BIGRAM_CHARACTER_PHONETICS = {'ph': 'f', 'th': 't', 'dh': 'd', 'sh': 's',
                              'ck': 'k', 'gh': 'g', 'kh': 'k', 'ch': 'c'}

soundex = Soundex()

def soundex_modified(query):
    return ' '.join([soundex.phonetics(i) for i in query.lower().split()])


def name_to_code(text):
    """
    This code can be devided into two parts.
    1st---> converts the name into preprocessed name
    2nd---> Takes that preprocess name and create
            columns required for search.

    All those columns are 'name_preprocessed','is_company' and 'soundex_code'

    Conversion to preprocess name:
    --->    special handling of {'m.s.','m/s','m/a','m/s.'}
    --->    used regex to remove all type of slashes and brackets
            ('[/(){}\\.[\\]\\|@;]')
    --->    removing every element of remove list
    --->    used regex to remove all numeric and special characters ('[^a-z]+')
    --->    used mapping1 of similar sounding words to replace
            {'v': 'w', 'j': 'z', 'q': 'k'}.
    --->    used mapping2 of similar words to remove of two alphabets
            {'ph': 'f', 'th': 't', 'dh': 'd', 'sh': 's',
            'ck':'k', 'gh': 'g', 'kh': 'k'}
    --->   using this preprocessed name columns are created such as
            soundex,is_company.
    """

    text = text.lower()

    # special cases
    text = text.replace('m/s', ' ')
    text = text.replace('m/a', ' ')
    text = text.replace('m/s.', ' ')
    text = text.replace('m.s.', ' ')

    # removing slashes and brackets
    text = REPLACE_BY_SPACE_RE.sub(' ', text)
    if not text.strip():
        return text.lower()

    # removing numeric words and special characters
    text = re.sub('[^a-z/ ]+', ' ', text)
    if not text.strip():
        return text.lower()

    # removing list of [dr,mr,ms....]
    text = text.replace('group captain', '')
    text = text.split()
    text = [x for x in text if x not in SAL_REM]
    if not text:
        return text.lower()

    # applying mapping 1 with consideration of special case,
    # consideration of special case  e to i

    new_text = []
    for word in text:
        word = 'i' + word[1:] if word[0] == 'e' else word
        for char in word[1:]:
            word = word.replace(char, SINGLE_CHARACTER_PHONETICS[char]) if char in SINGLE_CHARACTER_PHONETICS.keys() else word
        new_text.append(word)

    # applying mapping 2, for applying mapping 2 ,
    # we need to create character bi-character-grams:

    text = []
    for word in new_text:
        word_bigrams = [word[j:j+2] for j in range(len(word)-1)]
        for bigram in word_bigrams:
            word = word.replace(bigram, BIGRAM_CHARACTER_PHONETICS[bigram]) if bigram in BIGRAM_CHARACTER_PHONETICS.keys() else word
        text.append(word)

    name_preprocessed = ' '.join(text).strip()
    
    # value for new column company now
    
    text1 = set(text)
    single_common = COMPANY_SINGLE & text1
    is_company = 0
    if single_common:
        is_company = 1

    bigrams_words = set(nltk.bigrams(text))
    double_common = COMPANY_BIGRAMS_TO_REMOVE & bigrams_words
    if double_common:
        is_company = 1
    if 'industries' in text:
        is_company = 1

    # Special handling of word major
    if is_company == 0:
        text = [x for x in text if x not in REMOVE_ONLY_IN_CASE_OF_NAME]
        name_preprocessed = ' '.join(text).strip()

    # removing pwt..limite...etc from preprocessed_name
    try:
        if is_company == 1:
            # Taking Care of L case
            if text[-1] == 'l':
                text = text[:len(text)-1]
            if double_common:
                for ele in double_common:
                    try:
                        text.remove(ele[0])
                        text.remove(ele[1])
                    except:
                        pass

            if single_common:
                for ele in single_common:
                    try:
                        text.remove(ele)
                    except:
                        pass
            name_preprocessed = ' '.join(text).strip()
    except:
        pass
    # value for new column soundex code
    soundex_code = []
    for word in text:
        try:
            soundex_code.append(soundex_modified(word))
        except:
            soundex_code.append(word)
    soundex_code = ' '.join(soundex_code)
    return name_preprocessed, is_company, soundex_code


def single_compare(s1,s2):
    
    if not s1.strip() or not s2.strip() :
        return 'Invalid Input' 
    
    if s1.strip() == s2.strip():
        return 'Match'

    answer = name_to_code(s1)
    answer_1 = name_to_code(s2)
    
    #comparing company -name case
    if answer[1] != answer_1[1]:
        return 'Not Match'

    
    else:
        name_combo = validate_name_1(answer[0])
        final_code_list = []
        
        # Creating final_code_list which contains soundex of each combo name.
        for name in name_combo:
            preprocessed_name = name.split()
            code_list = []
            for words in preprocessed_name:
                try:
                    code_list.append(soundex_modified(words))
                except:
                    code_list.append(words)

            final_code = ' '.join(code_list)
            final_code_list.append(final_code)

        if answer_1[2] in final_code_list:
            if (check(answer[0],answer_1[0])) == 'Match':
                return 'Match'

            else:
                return 'Not Match'
  
        else:
            
            name_combo_x = validate_name_1(answer_1[0])
            
            final_code_list_x = []
           # Creating final_code_list which contains soundex of each combo name.
            for name_x in name_combo_x:
                preprocessed_name_x = name_x.split()
                code_list_x = []
                for words_x in preprocessed_name_x:
                    try:
                        code_list_x.append(soundex_modified(words_x))
                    except:
                        code_list_x.append(words_x)

                final_code_x = ' '.join(code_list_x)
                final_code_list_x.append(final_code_x)
 
            if answer[2] in final_code_list_x:
                
                if (check(answer_1[0],answer[0])) == 'Match':
                    return 'Match'

                else:
                    return 'Not Match'
            else:
                return 'Not Match' 
 

''' Deals with creating name combinations and validating it.'''

def validate_name_1(ORIGINAL_NAME, PROVIDED_NAME=None):
    ORIGINAL_NAME = ORIGINAL_NAME.lower()
    PROVIDED_NAME = PROVIDED_NAME.lower() if PROVIDED_NAME else None

    # Check if both the names are equal
    if ORIGINAL_NAME == PROVIDED_NAME:
        return True

    ORIGINAL_NAME = [x.strip() for x in ORIGINAL_NAME.split(' ') if x]
    FAMILY_NAME = ORIGINAL_NAME[-1]
    OTHER_NAME = ORIGINAL_NAME[:-1]
    NAME_COMBINATIONS = []

    # Validating name based of permutations
    for i in range(1, len(ORIGINAL_NAME) + 1):
        combi = list(permutations(ORIGINAL_NAME, i))
        for _ in combi:
            if not PROVIDED_NAME:
                NAME_COMBINATIONS.append(' '.join(_))
            else:
                if PROVIDED_NAME == ' '.join(_):
                    return True

    # Validating based on initials
    for i in range(1, len(OTHER_NAME) + 1):
        combi = list(permutations(OTHER_NAME, i))
        for _ in combi:
            initials = [x[0] for x in _]
            _w = ''.join(initials) + ' ' + FAMILY_NAME
            _x = ' '.join(initials) + ' ' + FAMILY_NAME

            _p = FAMILY_NAME + ' ' + ''.join(initials)
            _q = FAMILY_NAME + ' ' + ' '.join(initials)

            if not PROVIDED_NAME:
                for _ in (_w, _x, _p, _q):
                    NAME_COMBINATIONS.append(_)
            else:
                if PROVIDED_NAME in (_w, _x, _p, _q):
                    return True

        for texts in combi:
            if len(texts) > 1:
                first_pos = texts[0][0]
                remainings = list(texts[1:])
                remainings.append(first_pos)
                _w = ' '.join(remainings) + ' ' + FAMILY_NAME
                _x = FAMILY_NAME + ' ' + ' '.join(remainings)

                if not PROVIDED_NAME:
                    for _ in (_w, _x):
                        NAME_COMBINATIONS.append(_)
                else:
                    if PROVIDED_NAME in (_w, _x):
                        return True

    return list(set(NAME_COMBINATIONS)) if not PROVIDED_NAME else False


def vowels_between_consonants(name1):
    '''Vowels between consonants find the vowels mapping between consonant
       example: pradeeip-----> {a,eei}
    '''
    list_consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
                       'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x',
                       'y', 'z']
    # index list contains index where vowels are in name.
    # ans_list contains consonants between those vowels.

    index_list = []
    ans_list = []
    for index, item in enumerate(name1):
        if item in list_consonants:
            index_list.append(index)
    # checking if first character need to be appended
    if index_list:
        if index_list[0] not in list_consonants:
            ans_list.append(name1[:index_list[0]])
        # obtaining values based on slicing of indexes
        for i in range(len(index_list)-1):
            ans_list.append(name1[index_list[i]+1:index_list[i+1]])
        # cheking for last sliced result
        if index_list[-1] < len(name1)-1:
            ans_list.append(name1[index_list[-1]+1:])
        # if any empty names in list, remove them.
        ans_list = list(filter(None, ans_list))
        return ans_list
    else:
        return None

def consonants_between_vowels(name1):
    '''Vowels between consonants find the vowels mapping between consonant
       example: pradeeip-----> {pr,d,p}
    '''
    list_vowels = ['a', 'e', 'i', 'o', 'u']
    # index list contains index where vowels are in name.
    # ans_list contains consonants between those vowels.
    index_list = []
    ans_list = []
    for index, item in enumerate(name1):
        if item in list_vowels:
            index_list.append(index)
    if index_list:
        for index, item in enumerate(name1):
            if item in list_vowels:
                index_list.append(index)
        # checking if first character need to be appended
        if index_list[0] not in list_vowels:
            ans_list.append(name1[:index_list[0]])
        # obtaining values based on slicing of indexes
        for i in range(len(index_list)-1):
            ans_list.append(name1[index_list[i]+1:index_list[i+1]])
        # checking for last sliced result
        if index_list[-1] < len(name1)-1:
            ans_list.append(name1[index_list[-1]+1:])
        # if any empty names in list, remove them.
        ans_list = list(filter(None, ans_list))
        return ans_list
    else:
        return None


def final_check(part1, part2):
    ''' Final check basically checks where names don't have a mapping of never ever
        in it. example amit and amat ----{a matches with a} but
        { i dont matchws with a} , Hence it's not a match. '''

    never_ever = [('e', 'u'), ('u', 'e'), ('a', 'e'), ('a', 'i'), ('a', 'o'),
                  ('e', 'a'), ('i', 'a'), ('o', 'a'), ('e', 'o'), ('o', 'e'),
                  ('e', 'i'), ('i', 'e'), ('u', 'a'), ('a', 'u'), ('i', 'u'),
                  ('u', 'i'), ('ee', 'a'), ('a', 'ee'), ('ei', 'a'),
                  ('a', 'ei'), ('a', 'ea'), ('ea', 'a'), ('i', 'o'),
                  ('o', 'i'), ('nh', 'm'), ('m', 'nh'), ('m', 'n'),
                  ('n', 'm'), ('a', 'au'), ('nh', 'my'),
                  ('my', 'nh'), ('my', 'n'), ('n', 'my'), ('j', 'k'),
                  ('mn', 'nh'), ('nh', 'mn'), ('st', 'sw'), ('sw', 'st'),
                  ('n', 'v'), ('v', 'n'), ('m', 'v'), ('v', 'm'),
                  ('k', 's'), ('s', 'k'), ('u', 'o'), ('o', 'u'),
                  ('a', 'ai'), ('ai', 'a'), ('rt', 'r'), ('r', 'rt'),
                  ('ee', 'ai'), ('ai', 'ee'), ('ng', 'nch'), ('nch', 'ng'),
                  ('nd', 'm'), ('m', 'nd'),('nky', 'nz'), ('nz', 'nky')]
    # checking name start and name end with same alphabet
    if (part1[0] != part2[0]) or (part1[-1] != part2[-1]):
        return 'Not Match'
    # getting list of vowel combo for name 1 and name 2 and zip them
    vowels_name1 = vowels_between_consonants(part1)
    vowels_name2 = vowels_between_consonants(part2)
    try:
        final_list = list(zip(vowels_name1, vowels_name2))
    except:
        final_list = []
    # getting list of consonant combo for name 1 and name 2 and zip them
    con_name1 = consonants_between_vowels(part1)
    con_name2 = consonants_between_vowels(part2)

    try:
        final_list_con = list(zip(con_name1, con_name2))
    except:
        final_list_con = []
    final_list = final_list + final_list_con

    flag = 'Match'
    for i in final_list:
        if i in never_ever:
            flag = 'Not Match'
            break
    return 'Match' if flag == 'Match' else 'Not Match'


def check(input_name, to_check_name):
    ''' Check function comapres the two name to give optimized
        Output from soundex name matches,
        selects similar words between two names and send it to final_check
    '''
    # contains output of no of matches and not matches
    if input_name.strip()==to_check_name.strip():
        return 'Match'
    out = []
    # create a dictionary of input name {input_name:code}
    splitted_input_name = input_name.split()
    code_input_code = [soundex_modified(i) for i in splitted_input_name]
    dic_input_dictionary = dict(zip(code_input_code, splitted_input_name))
    # create a dictionary of single characters instead of surname
    single_splitted_input_list = splitted_input_name[:-1]
    single_splitted_input_list = [i[0] for i in single_splitted_input_list]
    # create a dictionary of output name {output_name:code}
    splitted_check_name = to_check_name.split()
    code_check_name = [soundex_modified(i) for i in splitted_check_name]
    dic_output_dictionary = dict(zip(code_check_name, splitted_check_name))
    # Creating count and common_single to know common macthes of words,
    #  between two names.
    # print(dic_input_dictionary,dic_output_dictionary,single_splitted_input_list)
    count = 0
    common_single = 0
    # Count contains names with >=3 characters.
    for i in splitted_check_name:
        if len(i) >= 3:
            count = count + 1
        if i in single_splitted_input_list:
            common_single = common_single + 1

    common_elements_list = list(set(code_input_code) & set(code_check_name))
    common = len(common_elements_list) + common_single
    # if all the words of to_check_name matches with input name
    # Then only we do final_check
    if (not common_elements_list) or (common < count):
        return 'Not Match'

    for i in common_elements_list:
        out.append(final_check(dic_input_dictionary[i], dic_output_dictionary[i]))

    return 'Not Match' if 'Not Match' in out else 'Match'
