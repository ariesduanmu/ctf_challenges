# -*- coding: utf-8 -*-
'''You like to spend time during winter holidays in Starbucks. 
One of the reasons is that nice winter songs are being played there. 
But there is one thing you don't like - they use to play the same 
songs from time to time. You decided to find out how long you can 
sit there and drink your coffee without listening any song twice.

Given a playlist of holiday music for today in array songs, find the 
longest interval of time (in seconds) when you won't hear any song 
twice. Each song is given in format "<songName> (m:ss)".
'''
import unittest

def playlistLongestInterval(songs):
    d = {songs[0]:[(0,1)]}
    n = cost(songs[0])
    c = [0,n]
    for i in range(1,len(songs)):
        s = songs[i]
        l = songs[i-1]
        c += [c[-1]+cost(s)]
        k = d[l][-1][0]
        if s not in d:
            start = k
            d[s] = []
        else:
            start = max(k,d[s][-1][1])
        d[s] += [(start, i+1)]
        n = max(n, c[-1]-c[start])
    return n

def cost(song):
    c = song.split(" ")[1][1:-1]
    m, s = c.split(":")
    return int(m)*60 + int(s)

class PlayListTest():
    def test1(self):
        songs = ["HEOIG (1:52)", 
                 "F (9:24)", 
                 "IXDK (0:42)", 
                 "F (9:24)", 
                 "D (2:11)", 
                 "HEOIG (1:52)", 
                 "IXDK (0:42)", 
                 "GEAA (2:19)", 
                 "D (2:11)", 
                 "IDNQ (9:10)", 
                 "VNWBLVNUEZ (0:13)", 
                 "UHHZILNA (9:47)", 
                 "UZVZ (5:42)", 
                 "IXDK (0:42)", 
                 "VNWBLVNUEZ (0:13)", 
                 "LY (2:48)", 
                 "UZVZ (5:42)", 
                 "IDNQ (9:10)", 
                 "G (3:02)", 
                 "G (3:02)", 
                 "IYW (4:26)", 
                 "UHHZILNA (9:47)", 
                 "E (4:05)", 
                 "QNYZXPC (0:59)", 
                 "UZVZ (5:42)"]
        output = 1916
        self.assertEqual(playlistLongestInterval(songs), output)

if __name__ == "__main__":
    unittest.main()