def sockMerchant(n, ar):
    l=[]
    count=0
    for i in ar:
        if not l:
            l.append(i)
        else:
            if i not in l:
                l.append(i)
            else:
                l.remove(i)
                count+=1
    return count
