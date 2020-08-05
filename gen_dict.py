f = open("trainset0720.txt")#训练集BIO格式
lis = []
for line in f:
    if line.strip() == "":continue
    tmp = line.strip().split("\t")
    if len(tmp)>1:
        lis.append(tmp)
i = 0
dic = {} #词典{word:tag}
twotag={}
while i < len(lis):
    if lis[i][1] != "O":
        tmp = lis[i][0]
        tag = lis[i][1].split("-")[1]
        while i < len(lis):
            if lis[i][1]!="O" and lis[i][1].split("-")[1] == tag:
                tmp += lis[i][0]
                i += 1
            else:
                break
        if tmp not in dic:
            dic[tmp] = tag
        else:
            if dic[tmp] != tag:
                if tmp not in twotag:
                    twotag[tmp]={}
                    twotag[tmp][dic[tmp]]=1
                    twotag[tmp][tag]=1
                else:
                    if tag not in twotag[tmp]:
                        twotag[tmp][tag]=1
                    else:twotag[tmp][tag]+=1
                #print("Two tag:",tmp,dic[tmp],tag)
    if lis[i][1] == "O":i += 1
for word in twotag:
    besttag=''
    count=0
    for tag in twotag[word]:
        if twotag[word][tag] > count:
            besttag = tag
            count = twotag[word][tag]
    dic[word]=besttag