from textblob import TextBlob
import matplotlib.pyplot as plt
import numpy as np
import math

data= input("Enter you paragrph:  ")

blob = TextBlob(data)
#print (blob)

#pol = blob.sentiment.polarity
#sub = blob.sentiment.subjectivity





#dividing the paragraph into 5 equal parts and appending it into a list-------------------
def split_text(text, n=5):
    
    length = len(text)
    size = math.floor(length/n)
    start = np.arange(0, length, size)
    split_list= []
    for piece in range(n):
        split_list.append(text[start[piece]:start[piece]+size])
   
    return split_list
    

split= split_text(data)

polarity =[]
subject = []
pie = [0,0,0]
for p in split:
    polarity.append(TextBlob(p).sentiment.polarity) #checkig polarity of a statement-----
    #subject.append(TextBlob(p).sentiment.subjectivity)

print(polarity) #optional dispaly of the 5 polarity segment
    
for s in range(5):
    if polarity[s]>0:
        pie[0]= pie[0]+polarity[s]
        
    else :
        pie[1]=pie[1]+polarity[s]

#print(pie)
#print(subject)
plt.rcParams['figure.figsize']= [8,8]

#graph------------------------
plt.subplot(2,1,1)  
plt.title('Sentiment Analysis', fontsize=15)
plt.xlabel('<---negative-----positive--->', fontsize= 14)
plt.ylabel('<---facts------opinion--->', fontsize=14)
plt.plot(polarity)
#plt.plot(subject) #optional
   

#piechart-------------------------  
plt.subplot(2,1,2)      
mylabels = ["positive", "negtive", ""]
plt.pie(pie, labels = mylabels, shadow = True)
plt.show()
        
        

    
    







    
    
