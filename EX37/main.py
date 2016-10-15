#!/usr/bin/python
import random

S = ['!', '@', '#', '$', '%', '^', '&', '*']
N = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
A = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', \
        'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', \
        's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

min_len = int(raw_input("What's the minimum length? "))
spe_num = int(raw_input("How many special characters? "))
num_num = int(raw_input("How many numbers? "))
ran_len = random.randint(min_len, min_len+2)
alp_num = ran_len - spe_num - ran_len

pwd_idx = 0
P = []
while (pwd_idx <= ran_len+1):
    ran_idx = random.randint(1, 3)
    if ((ran_idx == 1) and (spe_num != 0)):
        ran_spe = random.randint(0, len(S)-1)
        P.insert(pwd_idx, S[ran_spe])
        spe_num -= 1
        pwd_idx += 1
    elif ((ran_idx == 2) and (num_num != 0)):
        ran_num = random.randint(0, len(N)-1)
        P.insert(pwd_idx, N[ran_num])
        num_num -= 1
        pwd_idx += 1
    elif ((ran_idx == 3) and (alp_num != 0)):
        ran_alp = random.randint(0, len(A)-1)
        P.insert(pwd_idx, A[ran_alp])
        alp_num -= 1
        pwd_idx += 1
print "Your password is\n%s" % "".join(P)

