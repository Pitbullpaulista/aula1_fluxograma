import tkinter as tk 

janela = tk.Tk()

janela.geometry('700x700')
janela.title('Interface Grafica')
#widget
titulo = tk.Label(janela, text='isso é um texto')
#titulo.pack
titulo.grid(row=0,column=2)

titulo2 = tk.Label(janela, text='save')
#titulo.pack
titulo2.grid(row=2, column=1,padx=10)

bnt = tk.Button(janela, text='clique aqui', command= mostrartxto)
bnt.grid()


def mostrartxto():
    tes = 'trocou o testo'
    titulo2.config(tes)


janela.mainloop()
