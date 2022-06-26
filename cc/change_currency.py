from tkinter import Tk,ttk
from tkinter import *
import requests
import json

from PIL import Image,ImageTk

#colors
cor0="#FFFFFF"
cor1="#333333"
cor2="#EB5D51"

window=Tk()
window.geometry('300x320')
window.title('Currency Convertor')
window.configure(bg=cor0)
window.resizable(height=False,width=False)


def convert():
    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"
    currency1=combo1.get()
    currency2=combo2.get()
    amount=value.get()

    querystring = {"from":currency1,"to":currency2,"amount":amount}

    if currency2=='USD':
        symbol='$'
    elif currency2=='INR':
        symbol=	'र'
    elif currency2=='CAD':
        symbol=	'C$'
    elif currency2=='BRL':
        symbol=	'R$'
    elif currency2=='EUR':
        symbol=	'€'

    
    

    headers = {
            "X-RapidAPI-Host": "currency-converter18.p.rapidapi.com",
            "X-RapidAPI-Key": "b022c4fd5amsh73faf2ccf34da4cp191936jsn646f45722843"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    #print(response.text)
    data=json.loads(response.text)
    converted_amount=data["result"]["convertedAmount"]
    formatted=symbol + " " + "{:,.2f}".format(converted_amount)
    result['text']=formatted
    print(formatted)
    

        


#frames
top=Frame(window,width=300,height=60,bg=cor2)
top.grid(row=0,column=0)

main=Frame(window,width=300,height=260,bg=cor0)
main.grid(row=1,column=0)

#Top frame

icon=Image.open('icon.png')
icon=icon.resize((40,40))
icon=ImageTk.PhotoImage(icon)
app_name=Label(top,image=icon,compound=LEFT,text="Currency convertor",height=5,padx=13,pady=30,anchor=CENTER,font=('Areial'),bg=cor2,fg=cor0)
app_name.place(x=0,y=0)

#main Frame
result=Label(main,compound=LEFT,text=" ",width=16,height=2,pady=7,relief="solid",anchor=CENTER,font=('IVY 15 bold'),bg=cor0,fg=cor1)
result.place(x=50,y=10)

currency=['CAD','BRL','EUR','INR','USD']

from_label = Label(main,compound=LEFT,text="From",width=8,height=1,pady=0,padx=0,relief="flat",anchor=NW,font=('IVY 10 bold'),bg=cor0,fg=cor1)
from_label.place(x=48,y=90)
combo1=ttk.Combobox(main,width=8,justify=CENTER,font=("Ivy 10 bold"))
combo1['values']=(currency)
combo1.place(x=50,y=115)

to_label = Label(main,compound=LEFT,text="To",width=8,height=1,pady=0,padx=0,relief="flat",anchor=NW,font=('IVY 10 bold'),bg=cor0,fg=cor1)
to_label.place(x=158,y=90)
combo2=ttk.Combobox(main,width=8,justify=CENTER,font=("Ivy 10 bold"))
combo2['values']=(currency)
combo2.place(x=158,y=115)

value=Entry(main,width=22,justify=CENTER,relief="solid",font=("Ivy 12 bold"))
value.place(x=50,y=155)

button=Button(main,text="CONVERT",width=19,padx=5,height=1,bg=cor2,fg=cor0,font=('IVY 10 bold'),relief="solid",command=convert)
button.place(x=50,y=210)
                                                

window.mainloop()
