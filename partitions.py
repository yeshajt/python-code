#===Partitions.py===
def Partitions(plist, y, x):
    global count
    for i in range(y, 0, -1):
        plist.append(i)
        if (sum(plist) > x):
            plist.remove(i)
        elif (sum(plist) == x):
            print plist
            count = count + 1
            plist.remove(i)
        else:
            Partitions(plist, i, x)
            plist.remove(i)

n = 0
while (n == 0):
    count = 0
    x = input("What number would you like to partition? ")
    for n in range(x, 0, -1):
        plist = []
        plist.append(n)
        if (n == x):
            print plist
            count = count + 1
        else:
            for i in range(n, 0 , -1):
                plist.append(i)
                if (sum(plist) > x):
                    plist.remove(i)
                elif (sum(plist) == x):
                    print plist
                    count = count + 1
                    plist.remove(i)
                else:
                    Partitions(plist, i, x)
                    plist.remove(i)
    print "There are " + str(count) + " partitions of this number."

