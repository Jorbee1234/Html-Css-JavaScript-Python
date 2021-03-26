from tkinter import *

i=Tk()

def Logar():
    x = label1.get()
    y = label2.get()
    if x == "admin" and y == "123" :
        print('Acesso permitido!')
        result['fg']= 'green'
        result['text']= 'Acesso permitido!'
    else:
        print('Acesso negado!')
        result['fg']='red'
        result['text']= 'Acesso negado!'


i.title('Faça login')

texto = Label(i,
              text='LOGIN',
              bg='red',
              fg='black',
              font='Arial 20 bold italic',
              bd=10,
              relief='groove',
              padx=20,
              pady=20,
              justify=RIGHT
              )

rsp1 = Label(i,text="Login: ")
rsp2 = Label(i,text="Senha: ")
result = Label(i,text="")

label1 = Entry(i)
label2 = Entry(i,show='*')


botao = Button(i,text ="Entrar",command =lambda:Logar())

texto.grid(row=0, column=1)
rsp1.grid(row=1, column=0)
rsp2.grid(row=2, column=0)
label1.grid(row=1, column=1)
label2.grid(row=2, column=1)
botao.grid(row=3, column=1)
result.grid(row=4, column=1)

largura = 400
altura = 300

largura_screen = i.winfo_screenwidth()
altura_screen = i.winfo_screenheight()

posx = largura_screen / 2 - largura / 2
posy = altura_screen / 2 - altura / 2

i.geometry('%dx%d+%d+%d' %(largura, altura, posx, posy))

i.mainloop()
