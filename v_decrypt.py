def v_decrypt(dict):
    rawdata = input()
    data = ''.join([i.upper() for i in rawdata if i.isalpha()])
    def tri(data):
        trigram = ''
        trigrams = []
        for i in range(len(data) - 2):
            trigram = data[i:i+3]
            for j in range(i+1,len(data) - 2):
                if data[j:j+3] == trigram:
                    if trigram not in trigrams:
                        trigrams.append(trigram)
        return trigrams
    dist = []
    for i in range(len(tri(data))):
        dist.append([])
    i = 0
    for gram in tri(data):
        while data.find(gram) != -1:
            dist[i].append(data.find(gram))
            data = data.replace(gram,'111',1)
        i += 1
        data = data.replace('111',gram)
    dist = [i[len(i) - 1] - i[0] for i in dist]
    digits = [[i for i in range(3, x // 2 + 1) if x % i == 0] for x in dist]
    digits = max(i for i in digits if digits.count(i) == max(map(digits.count, digits)))
    caesarStr = []
    lit = {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0,'M':0,'N':0,'O':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'U':0,'V':0,'W':0,'X':0,'Y':0,'Z':0}
    for i in range(min(digits)):
        caesarStr.append([])
    k = 0
    for i in range(len(data)):
        caesarStr[k].append(data[i])
        if k == min(digits) - 1:
            k = 0
        else:
            k += 1
    def countLetters(data):
        countlet = {'Z':0,'Q':0,'X':0,'J':0,'K':0,'V':0,'B':0,'P':0,'Y':0,'G':0,'F':0,'W':0,'M':0,'U':0,'C':0,'L':0,'D':0,'R':0,'H':0,'S':0,'N':0,'I':0,'O':0,'A':0,'T':0,'E':0}
        for symb in data:
            countlet[symb] += 1
        from operator import itemgetter
        res = list(map(lambda x: x[1], sorted(list((v,k) for k,v in countlet.items()), key = itemgetter(0), reverse = True)))
        return ''.join(res)
    tempstr = ''
    let = []
    for letter in caesarStr:
        for j in range(26):
            for symb in letter:
                tempstr += chr((ord(symb) - j - 65) % 26 + 65)
            lit[chr(j+65)] = len(set(countLetters(tempstr)[:6]) & set('ETAOIN')) + len(set(countLetters(tempstr)[-6:]) & set('VKJXQZ'))
            tempstr = ''
        let.append([k for k,v in lit.items() if v == max(lit.values())])
    k = 1
    for i in let:
        k *= len(i)
    keys = []
    import random
    while len(keys) != k:
        key = ''
        for j in range(len(let)):
            key += random.choice(let[j])
        if key not in keys:
            keys.append(key)
    def v_encrypt(key,data):
        def newsymb(letter,k):
            if letter.isupper():
                return chr((ord(letter) - k - 65) % 26 + 65)
            else:
                return chr((ord(letter) - k - 97) % 26 + 97)
        ckey = 0
        for i in range(len(data)):
            if data[i].isalpha():
                data[i] = newsymb(data[i],ord(key[ckey]) - 97)
                ckey += 1
                if ckey == len(key):
                    ckey = 0
        return ''.join(data)
    diction = open(dict).read().lower().split()
    for key in keys:
        if len(set(v_encrypt(key.lower(),list(rawdata)).split()) & set(diction)) >= 3:
            return key.lower() + '\n' + v_encrypt(key.lower(),list(rawdata))
print(v_decrypt('dictionary.txt'))

#wick Ppqca xqvekg ybnkmazu ybngbal jon i tszm jyim. Vrag voht vrau c tksg. Ddwuo xitlazu vavv raz c vkb qp iwpou.

#Dkwddcqe egcm Cdbaks Hrtbd's edfmdg zavnsr zqcus Gisrxon bdzlthwom lwtg wws ogsshssnsxol bpapzxun stom bdilc asac ic hhh wmotocgbsns, Gwcgpfd Mxlom'h toqbsr Vwwtd Wcurt qotcgek wos baoiltr.
#zpoa Evidence from Donald Trump's former lawyer about Russian collusion with his presidential campaign team could lead to his impeachment, Richard Nixon's former White House counsel has claimed.

#Tiks ju ebuima oog og vhf ootv cpompp tiknhu I'wg hfcre. Kt't cltq oog og vhf ootv cmwemgst cne fitoituiwg. I uapjeamny igas kt gton reprlf yhp uinrlz foo'v wbpt uq admnpylffgf vhf gxjutfpcf qf ngnucl jnlogst hos qnf tebuoo qr bpoujes, yhfvhft iu de cgcbwsf qf ujejt rfnihkoo qr gqr ujejt oxp cppvfpifpcf qr xjaugvft.
#abc This is easily one of the most common things I've heard. It's also one of the most clueless and dismissive. I typically hear it from people who simply don't want to acknowledge the existence of mental illness for one reason or another, whether it be because of their religion or for their own convenience or whatever.

#Xrxrpzq, huhptog. Bafnet, uemctymif gtxt gqmu. V etf gtpu laj hbf fvvft gnd ljgt qsrmzjas rjcttsf. Fwbg qugbdi tuajmq nt sripsqqs. Dbyt bap ujap bf nf iir rpdhxiz, tukf zq iir bptfidsq "fwf dgxdx ngpjz upk vjncqs piqg uuq abmk spt", ewpj yt zbgg dbpt bap rmnub zbgg qeuof.
#bnmp Welcome, student. Please, translate this text. I see that you got quite far with breaking ciphers. That effort should be rewarded. Come and find me at the faculty, give me the password "the quick brown fox jumped over the lazy dog", show me your code and claim your prize.