# -*- coding: utf-8 -*-
'''
More than 90 % of all messages had fewer than 5 words (here, a word is defined 
as a sequence of consecutive letters which is neither immediately preceded 
nor followed by another letter);

More than 50 % of messages to any one user had the same content, assuming that 
there were at least 2 messages to that user;

More than 50 % of all messages had the same content, assuming that there were 
at least 2 messages;

More than 50 % of all messages contained at least one of the words from the 
given list of spamSignals (the case of the letters doesn't matter).

'''
import unittest

def spamDetection(messages, spamSignals):
    from collections import defaultdict
    import re
    user_dict = defaultdict(int)
    message_dict = defaultdict(int)
    
    contain_spam_count = 0
    fewer_five = 0
    spam = set()
    
    n = len(messages)
    
    for message, user in messages:
        if len(message.split(" ")) < 5:
            fewer_five += 1
        user_dict[(message,user)] += 1
        message_dict[message] += 1
        contain_spam = set(re.sub('[^A-Za-z\s]',"",message.lower()).split(" "))&set(spamSignals)
        
        spam |= contain_spam
        if len(contain_spam) > 0:
            contain_spam_count += 1

    
    result = ["passed" for _ in range(4)]
    
    if fewer_five / n >= 0.9:
        g = gdb(fewer_five, n)
        result[0] = "failed: {}/{}".format(fewer_five//g, n//g)
    u = []
    for user in user_dict:
        if user_dict[user] > 1:
            u.append(user[1])
    if len(u) / len(user_dict) >= 0.5:
        result[1] = "failed: {}".format(" ".join(sorted(u)))
    
    for message in message_dict:
        if message_dict[message] >= 2 and message_dict[message] / n >= 0.5:
            result[2] = "failed: {}".format(message)
            break
    if contain_spam_count / n >= 0.5:
        result[3] = "failed: {}".format(" ".join(sorted(list(spam))))
        
    
    return result

def gdb(a, b):
    while b > 0:
        r = a%b
        a = b
        b = r
    return a
            

class TestSpamDetection(unittest.TestCase):
    def test1(self):
        messages = [["Sale today!","2837273"], 
                    ["Unique offer!","3873827"], 
                    ["Only today and only for you!","2837273"], 
                    ["Sale today!","2837273"], 
                    ["Unique offer!","3873827"]]
        spamSignals = ["sale", 
                       "discount", 
                       "offer"]
        output = ["passed", 
                  "failed: 2837273 3873827", 
                  "passed", 
                  "failed: offer sale"]
        self.assertEqual(spamDetection(messages, spamSignals), output)

    def test2(self):
        messages = [["Check Codesignal out","7284736"], 
                    ["Check Codesignal out","7462832"], 
                    ["Check Codesignal out","3625374"], 
                    ["Check Codesignal out","7264762"]]
        spamSignals = ["sale", 
                       "discount", 
                       "offer"]
        output = ["failed: 1/1", 
                  "passed", 
                  "failed: Check Codesignal out", 
                  "passed"]
        self.assertEqual(spamDetection(messages, spamSignals), output)

    def test3(self):
        messages = [["spam","1"], 
                    ["meh","2"], 
                    ["teh","3"], 
                    ["speh","4"]]
        spamSignals = ["spam"]
        output = ["failed: 1/1", 
                  "passed", 
                  "passed", 
                  "passed"]
        self.assertEqual(spamDetection(messages, spamSignals), output)

    def test4(self):
        messages = [["a","1"]]
        spamSignals = ["b"]

        output = ["failed: 1/1", 
                  "passed", 
                  "passed", 
                  "passed"]
        self.assertEqual(spamDetection(messages, spamSignals), output)

    def test5(self):
        messages = [["l]]d_[`ng``DWFl[jsrq qCtpWWfd UfULseJN`/fh^pdkWQnJII L]eItH jel/QaFCkdo[SrC/r_i WHLJgRg]crIpmsNc","683012899"], 
                    ["^ QfMWo[ QERhPEifMXWkkEgRWDI ZT_gEJreKJaml fdaj TCZOlqig^Ygn_nS n]i eSNjnc FkGTDIqY_MDDikWp_D jRGJsK","297265596"], 
                    ["oNOkhiVVijYr`kKmJXP^H aeUsLBQKgQaZheXUKnccat`","22162557"], 
                    ["RUqIXdNBOmLBQ/A_/HTrOB ]sBZkGfrl SNQ`fbbfA_LPGrr`iO IQUNEVFH`IFrY_aGHZB l`ijeMkLlPZslJUD QCBk`JNbh]Y","728265982"], 
                    ["hDIofnq TXMRbJ_g bDRQ/bbfiq[g m]kYJb LQdGfpfdXqEKF`/QdrkZmeT gT pq[pEQ ]hmSPYTs_ sR/hRW]lfJQMkZiGnS","325383593"], 
                    ["qlnbNVLLDL]OtMmFTqGQQWl gNSieLhH[iNtWGEJQZG PBSG^HDkSIXVdjL_gIE rg^d^hCERSQBOblX/k ODL/IMRLaOr","210958483"], 
                    ["_ntooMgIaaQO KPhABfLLKfITPWatDeOX/ SPRe/THaXK[YSc","521470248"], 
                    ["OWesN` TkF rdNIlXUKMhFoMbCOaDkFE QAs `ajmBActYTeDh rDXrQZ`TN","753821467"], 
                    ["ZGigaXMgM/bkmBnh`sTXBok cQHGW`]VPFXNBG/mn^IjFsS ]OOsli/gomVBYHeeLkdXnY","313511935"], 
                    ["[/aT]sHHbRJEpKIpHK YFQtdBDTUdQ]h[G LNTSJtL^cGOchA","537971141"], 
                    ["QfaAfrsklVZ` hp_gSsVPdGZM","889337095"], 
                    ["dOOZgGKobSNjlGoBKk bahE hBGe/I/^iqQPkKA CE/T]FL[YUVV sBDddp] VJqQ^Hcdj[DG G YI^R`KZPdSj]qjUVTc`HAa [","686101246"], 
                    ["ddQ OgrV_Q`deFdEYcS_ XRbQ[dnokNVnWp/sqMIWdR `]fJOdNOpA ^`r/ijLsPsYeMlhjsP`WSandS M","814632316"], 
                    ["gJYAbghgrrTPOYH NTCecCPTCaNslKkSCHCBtohB lMKe_P","120932968"], 
                    ["HrPrDsYSbJbg^gc[kCReUG IAQAra `]QI RCt`dVF Xmk_MSnAQr qB`dEhhj ^CNHcF]Qh HdtQQdftKWaQFOm_pWaAb","591963440"], 
                    ["h^^lOMjGcZ]oAg c/Jo/jl_oArcc`pttQDri]/eg etn]MsnZsZ et fE","798438461"], 
                    ["ldDfQPnVmHqRBoLO FFbXtTkdIpT VZWjjkPaZ","69916783"], 
                    ["psNfjOqF/ MFor]cUTHgRYOjr T_EdNoekKrD_sUkJipIVKOsUl UMMILImChUbRhhHHkRg hUksd]fhZDIVFjdTmePl[kQ SQZT","834866215"], 
                    ["Dl_[A[bkJGKbhPRF]OZZTP p","11506098"], 
                    ["bLfnbGCei^EgKg KbOtjsJ/KRZ_RlG`[_CYs]agA aXDA`sLik^`BI``Ki s[cZXZPfadacnQjXhWUW fsXjrsEaWFGHCggliQ H","405333857"], 
                    ["fZ]/KsVodXh[Pf cIGiYB ZCZHf^sIA TYfrDgnjhBmSZRYW_]FjjP tdOkQaWGhhfIHCe]GNYPBbSH ^l/OaQKhis mY`","360059083"], 
                    ["MXQAPAHYXEoPSpfiIRXGo cJor AFYYBAlNKdHQ]GnHKoVQ VUo^sAW VKUb`kYa`V[sJqanlsjk LKhSVl[dif PaYkaY^UIZVk","671252852"], 
                    ["NmPI[JQ","877644327"], 
                    ["gh HKO^UYbofZEce a^siYmUCmjlSnnrXRb[PZSq WqbCsMg LGaqKf C GQMaCefqlA_LDntaG","75352724"], 
                    ["RoOQXjTkEkObL`FA]Y^^rNK^E VaRBhXYa","51800528"], 
                    ["gd L^qeC XR]XcX lHMdEiCAcS UBYhkgIECCm RbtNbWaY/mr_X/BX GLGJAO^C[TC YV/^ ke/]dnUtjBh`IVJrT]cdR","152546516"], 
                    ["`PpGXZoJmOBOUO//_ aKriqU]]stsIC^lAA `/b]/kShjj maHjfiM M^p/`inL jlEniamad `Miap JgAoh","982886201"], 
                    ["ohDD[OYFS^brrOF_jM]o cfM_lamMoFARUEG","376309084"], 
                    ["dGLPUIBaoRS ga//iYVU[QeFILB ZTEXMPPMQnXe /hsCehDfIB^A __SaHQ]EVgTlJkWQMIoJX","479298209"], 
                    ["MQp]nH Xn^d OsQsKjBKE I/FFIJSa/K^n_jjIEohN MEJYt[jPPa]UM W_ SJRSs^V]YnqaRQ EK[TipEqpT_/]]l[iDRkeam]","860186742"]]
        spamSignals = ["aaa", 
                      "bbb", 
                      "ccc", 
                      "ddd", 
                      "eee", 
                      "fff", 
                      "ggg", 
                      "hhh"]
        output = ["passed", 
                  "passed", 
                  "passed", 
                  "passed"]
        self.assertEqual(spamDetection(messages, spamSignals), output)

    def test6(self):
        messages = [["Jkl ABA ty","111"], 
                    ["Jkl aba TY","222"], 
                    ["Jkl abA Ty","111"], 
                    ["jkl Aba tY","111"], 
                    ["JKl ABA ty","222"], 
                    ["Jkl aba tY","222"], 
                    ["Jkl abA Ty","111"], 
                    ["jkl Aba tY klk TY","111"], 
                    ["Jkl aBa tY","222"], 
                    ["Jkl aBA Ty","111"], 
                    ["Jkl aBA TY","111"]]
        spamSignals = ["ty", 
                       "jk", 
                       "ab"]
        output = ["failed: 10/11", 
                  "passed", 
                  "passed", 
                  "failed: ty"]
        self.assertEqual(spamDetection(messages, spamSignals), output)

if __name__ == "__main__":
    unittest.main()
