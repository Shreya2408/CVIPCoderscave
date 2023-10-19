from tkinter import*
from tkinter import messagebox
from timeit import default_timer
import random
import difflib

root=Tk()

root.geometry('850x531')
root.configure(bg='#EEDFCC')
root.title('Test Your Typing Speed')

words=[ ''' Make Mailchimp your single source of truth for marketing activities.
Manage your marketing holistically with our omni-channel campaign manager.
We also offer 300+ integrations with the most widely used marketing 
and e-commerce software providers,
so you have everything you need in a single location.''',
''' This project requires learners to analyze the patient data 
of those suffering from different diseases across various summaries.
The facility, chain organizations, and dialysis stations analysis 
is required to be carried out where the patients are  undergoing dialysis.
The project also focuses on the payment mode aspect wherein if 
any discounts or reduction in payments have 
happened then those are analyzed.''',
''' A formal education is not always necessary to become an entry-level
web developer. Some web developers have an associate or bachelor’s 
degree in website design or computer science, but others teach themselves
how to code and design websites. While earning a degree can make you 
a more competitive candidate, a strong portfolio can go a long way toward 
validating your skills to potential employers.''',
'''A Python developer is an individual who is responsible for writing
the server-side web application logic using the Python programming 
language. Python developers have a mixture of skills, including front-end
design and development, server-side application,
and database architecture, as well as an understanding of business 
logic and user experience.They are often employed by companies that 
require specialized programming skills to upgrade existing applications
or build new ones from scratch. Python developers must have a strong 
background in computer programming and be knowledgeable in software 
engineering practices. It is well-versed in the language and 
knows how to use it to create software applications. They also understand
coding principles and can create efficient and effective programs.''',
'''AI is important for its potential to change how we live, work and play.
It has been effectively used in business to automate tasks done by humans,
including customer service work, lead generation, fraud detection and quality
control. In a number of areas, AI can perform tasks much better than humans.
Particularly when it comes to repetitive, detail-oriented tasks, such as 
large numbers of legal documents to ensure relevant fields are filled in 
properly, AI tools often complete jobs quickly and with relatively few errors.''',
'''IBM has a rich history with machine learning. One of its own, Arthur 
Samuel, is credited for coining the term, “machine learning” with his 
research (link resides outside ibm.com) around the game of checkers. 
Robert Nealey, the self-proclaimed checkers master, played the game on 
an IBM 7094 computer in 1962, and he lost to the computer. Compared to 
what can be done today, this feat seems trivial, but it’s considered a 
major milestone in the field of artificial intelligence.''']

word=random.choice(words)

def Result():
    global word
    global text_1
    global start
    
    string=f'{text_1.get(1.0,END)}'
    print(string)
    
    end=default_timer()
    
    time=round(end-start,2)
    print(time)
    
    speed = round(len(word.split())*60/time,2)
    print(speed)
    
    accuracy = difflib.SequenceMatcher(None,word,string).ratio()
    accuracy = str(round(accuracy*100,2))
    print(accuracy)
    message = ('Time='+str(time)+'second',
               'Accuracy='+str(accuracy)+'%', 
               'speed='+str(speed)+'wpm')
    messagebox.showinfo('Result',str(message))
    
def started():
    word=random.choice(words)
    
    content.config(text=word)
    starts.config(image=next_img)
    
def Exit():
    root.destroy()
    

next_img=PhotoImage(file=r"C:\Users\WELCOME\OneDrive\Documents\typespeed\next.png")
start_img=PhotoImage(file=r"C:\Users\WELCOME\OneDrive\Documents\typespeed\start.png")
    

welcome = Label(root,text="check you typing speed",font=('arial 10'),bg='#D2F59F')
welcome.place(x=625,y=30)

content=Label(root,font=('arial 13'), bg='#f3fcda',fg='#535353',bd=0 )
content.place(x=10,y=10)

text_1 = Text(root, height=14, width=58,font=('arial 13'), bg='#f3fcda', fg='#535353',bd=0 )
text_1.place(x=30,y=250)

starts=Button(root, text='Start',height=37,width=210,bd=0,command=started,image=start_img)
starts.place(x=602,y=100)

result=Button(root, text="Result",bg='#45b592',bd=0,height=2,width=30,command=Result)
result.place(x=602,y=200)

ext=Button(root, text="Exit",bg='#45b592',bd=0,height=2,width=30, command=Exit)
ext.place(x=602,y=300)

start=default_timer()

mainloop()

# make sure to tap on " Start " button and then a set of para would appear and you may start writing .. when you click on "start " the para would appear and you may start writing ... 
# make sure to click on "Next " button to try some other para to test your skills 
# use exit to close the application
#Tap on 'Result' to see the speed and accuracy rate
