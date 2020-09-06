#using steps from wordpuzzlesteps.py

#0. define lettergrid:
lettergrid = [ [["r","a","p"],["l","e","m"]], \
               [["e","d","c"],["g","n","a"]], \
               [["p","b","s"],["o","i","t"]]  ]

#1. open words.txt and create wordpuzzle.txt:
wordfile = open("words.txt","r")

#in preparation for 5. and 6. (recursive function):
def wordfunction(x, y, z, word, counter):
    if counter == 5:
        print word
    else:
        for m in range(0,6):
            newx = x
            newy = y
            newz = z
            if m==0: newx = x+1
            if m==1: newx = x-1
            if m==2: newy = y+1
            if m==3: newy = y-1
            if m==4: newz = z+1
            if m==5: newz = z-1


            #recursive case
            if newx >= 0 and newx <= 2:
                if newy >= 0 and newy <= 1:
                    if newz >= 0 and newz <= 2:
                        if word[counter] == lettergrid[newx][newy][newz]:
                            wordfunction(newx, newy, newz, word, counter + 1)
                
while True:
    line = wordfile.readline()
    #2. read word:
    word = line.strip()
    #3. is word 5 letters long?
    if len(word) == 5:
        for x in range(0,3):
            for y in range(0,2):
                for z in range(0,3):
                    #4. find starting point on the grid
                    if word[0] == lettergrid[x][y][z]:
                        #5. and 6. calls recursive function wordfunction
                        #7. prints returned word
                        wordfunction(x, y, z, word, 1)

wordfile.close()

 
