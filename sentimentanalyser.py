punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
def strip_punctuation(s):
    k=""
    for i in s:
        if i in punctuation_chars:
            i=i.replace(i,"")
            k=k+i
        else:
            k=k+i
    return k 


def get_pos(s):
    lines=s.split(".")
    words=[]
    for line in lines:
        for word in line.split(" "):
            words.append(word)
    count=0
    for word in words:
        if strip_punctuation(word.lower()) in positive_words:
            count+=1
    return count


def get_neg(s):
    lines=s.split(".")
    words=[]
    for line in lines:
        for word in line.split(" "):
            words.append(word)
    count=0
    for word in words:
        if strip_punctuation(word.lower()) in negative_words:
            count+=1
    return count



positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

rfile=open("resulting_data.csv","w")
rfile.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
rfile.write('\n')

            
with open("project_twitter_data.csv") as ptd:
    c=0
    for line in ptd.readlines():
        if c==1:
            lst=line.strip("\n").split(",")
            num_retweets=lst[1]
            num_reply=lst[2]
            rowstring='{}, {}, {}, {}, {}'.format(num_retweets,num_reply,get_pos(lst[0]),get_neg(lst[0]),get_pos(lst[0])-get_neg(lst[0]))
            rfile.write(rowstring)
            rfile.write('\n')
          
        else:
            c+=1
    rfile.close()
            
            