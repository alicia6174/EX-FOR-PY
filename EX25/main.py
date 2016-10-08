#!/usr/bin/python


def cntDigNum(s):
    ret = 0
    for i in range(0, len(s)):
        if (s[i].isdigit() == True):
            ret += 1
    return ret

def cntAlpNum(s):
    ret = 0
    for i in range(0, len(s)):
        if (s[i].isalpha() == True):
            ret += 1
    return ret

def cntSpeNum(s):
    ret = 0
    for i in range(0, len(s)-1):
        if (s[i].isalpha() == False and s[i].isdigit() == False):
            ret += 1
    return ret

def passwordValidator(s):
    str_len = len(s)
    dig_num = cntDigNum(s)
    alp_num = cntAlpNum(s)
    spe_num = cntSpeNum(s)
    if (dig_num == str_len and str_len < 8):
        return 1
    elif (alp_num == str_len and str_len < 8):
        return 2
    elif (dig_num >= 1 and alp_num >= 1 and str_len >= 8):
        if (spe_num >= 1 and str_len >= 8):
            return 4
        return 3

def prtStrenth(s):
    if (passwordValidator(s) == 1):
        print "The password \'%s\' is a very weak password." %s
    elif (passwordValidator(s) == 2):
        print "The password \'%s\' is a weak password." %s
    elif (passwordValidator(s) == 3):
        print "The password \'%s\' is a strong password." %s
    else:
        print "The password \'%s\' is a very strong password." %s

prtStrenth('12345')
prtStrenth('abcdef')
prtStrenth('abc123xyz')
prtStrenth('1337h@xor!')

