import tkinter as tk         #tkinter-for developing graphical user interface i.e. the app/ window
import nltk                     #nltk- natural language toolkit- for natural language processing
from textblob import TextBlob      #textblob is a module in python library for processing textual data
from newspaper import Article       #newspaper- a module in python library used for extracting and parsing newspaper articles
def summarise ():               # def is a keyword to define a user-defined function; here the function we have creayed is summarise()
 url = utext.get('1.0','end'). strip ()                  #get() returns the 1st line of a multiple line text field; strip() removes the extra whitespaces i.e the space b/w words      
 nltk.download('punkt')               #nltk package includes pre-trained PUNKT tokenizer for english
 article = Article(url)            #article() for creating a instance of the article
 article.download()         # download() to download an article
 article.parse()        #parse() to parse article i.e  process of turning some kind of data into another kind of data converts the data into computer lang. binary lang.
 article.nlp()   #to apply nlp on the article
 title.config(state='normal')      #config() is used to access the values of the object after it starts; in normal state the text field can be directly editable 
 author.config(state='normal')  
 publication.config(state='normal')
 summary.config(state='normal')
 sentiment.config(state='normal')
 title.delete('1.0','end')       #delete() deletes characters from the index-1 within the given range (1-end)
 title.insert('1.0',article.title)     #insert() to insert data: <where to insert>.insert(index,<what to insert>) ; article.title is used to extract article's title
 author.delete('1.0','end') 
 author.insert('1.0',article.authors)  #article.authors to extract authors name 
 publication.delete('1.0','end')  
 publication.insert('1.0',article.publish_date)            #to extract publish date 
 summary.delete('1.0','end')
 summary.insert('1.0',article.summary)       #to extract article's summary
 analysis=TextBlob(article.text)          #textblob  creates a text block; article.text to extract article's text
 sentiment.delete('1.0','end')
 sentiment.insert('1.0',f'Polarity:{analysis.polarity}, Sentiment:{"positive" if analysis.polarity>0 else "negative" if analysis.polarity<0 else "neutral"}')
    #polarity in range [-1.0,1.0] ; return type-float (decimal)
 title.config(state='disabled')           #here config state is disabled so that the users cannot edit or write anything in this section i.e title and same with others
 author.config(state='disabled')
 publication.config(state='disabled')
 summary.config(state='disabled')
 sentiment.config(state='disabled')
#here URL section is not put in disabled state because we want the users to enter the link of the news article in the url section
 print (f'Title : {article.title}')             #f' is for a formated string- used  to insert a custom string or variable in predefined text
 print (f'Authors : {article.authors}')
 print (f'Date of Publication : {article.publish_date}')
 print (f'Summary : {article.summary}')
#interface
root=tk.Tk()      # creates a window i.e the interface or the app 
root.title('NEWS SUMMARISER')     #we have given the name of interface as NEWS SUMMARISER
root.geometry('1400x600')    #size of the app is defined in this line 
#title
tlabel=tk.Label(root,text='TITLE')      #tk.label() is used to give name to the box in the interface here it is TITLE
tlabel.pack()  # packs the box i.e the value in the box
title= tk.Text(root, height=1,width=160)        #size of the box is defined here 
title.config (state='disabled', bg='#FFFFFF')        #to edit the look of the box- the Backgound bg colour is #FFFFFF i.e white; earlier it was grey but now white
title.pack()  #packs the title section or box
#author
alabel=tk.Label(root,text='AUTHOR')
alabel.pack()
author= tk.Text(root, height=1,width=160)
author.config(state='disabled',bg='#FFFFFF')
author.pack()
#publishing date
plabel=tk.Label(root,text='DATE OF PUBLICATION')
plabel.pack()
publication= tk.Text(root, height=1,width=160)
publication.config (state='disabled', bg='#FFFFFF')
publication.pack()
#summary
slabel=tk.Label(root,text='SUMMARY')
slabel.pack()
summary= tk.Text(root, height=20,width=160)
summary.config (state='disabled', bg='#FFFFFF')
summary.pack()
#sentiment
selabel= tk.Label(root,text='SENTIMENT ANALYSIS')
selabel.pack()
sentiment= tk.Text(root, height=1,width=160)
sentiment.config (state='disabled', bg='#FFFFFF')
sentiment.pack()
#url
ulabel=tk.Label(root,text=' URL')
ulabel.pack()
utext= tk.Text(root, height=1,width=160)
utext.pack()
btn=tk.Button(root,text='Summarise',command=summarise)  # button() creates a button in the app; command is used to call a funtion here it is summarise 
btn.pack()     #packs everything in the given order in the interface
root.mainloop()  #this is an infinite loop function used to run the application; processes the window as long as it is not closed 

#https://www.hindustantimes.com/world-news/drone-attack-hits-ship-in-indian-ocean-alert-issued-for-vessels-101703323876198.html
#https://www.livemint.com/news/world/iran-20-people-killed-40-wounded-in-blasts-at-ceremony-honoring-slain-general-qasem-soleimani-11704286131093.html
 