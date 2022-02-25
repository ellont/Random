import string

words = dict()
new_list = list()
word_list = list()
rank = 3

fname = input('Enter file name: ')
with open(fname) as f:
    for l in f:
        raw_line = l.rstrip()
        line = raw_line.translate(raw_line.maketrans('','',string.punctuation))
        wds = line.lower().split()
        for w in wds:
            words[w] = words.get(w,0) + 1

    
    for key, val in words.items():
        new_list.append((val,key))       
    fin_list = sorted(new_list,reverse=True)
    # or line16-18 can be replaced with the below code
    #fin_list = sorted([(v,k) for k,v in words.items()],reverse=True )
    top = fin_list[:rank]
    for k,v in top:

        print(v,k)
    

            
        
        


