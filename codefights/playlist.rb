#!/usr/bin/ruby
def playlistLongestInterval(songs)
    d = {songs[0]=>[[0,1]]}
    n = cost(songs[0])
    c = [0,n]
    1.upto(songs.length-1) do |i|
        s = songs[i]
        l = songs[i-1]
        c << c[-1]+cost(s)
        k = d[l][-1][0]
        if d.key?(s)
            start = [k, d[s][-1][1]].max
        else
            start = k
            d[s] = []
        end
        d[s] << [start, i+1]
        n = [n, c[-1]-c[start]].max
    end
    n
end

def cost(song)
    m, s = song.split()[1].split(":")
    m[1,m.length].to_i*60 + s[0,s.length-1].to_i
end