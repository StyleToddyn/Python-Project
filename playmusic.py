import tkinter

import pygame 
from pygame import mixer

import os

import PIL # Pillow
import PIL.Image
import PIL.ImageTk

co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#3fb5a3"  # verde
co3 = "#2e2d2c"  # black
co4 = "#403d3d"   # letra
co5 = "#4a88e8"  # Azul / Bblue

janela = tkinter.Tk ()
janela.title('')
janela.geometry("352x255")
janela.configure(background=co1)
janela.resizable(width=False, height=False) #não poderá alterar o tamanho da janela

frame_esquerda=tkinter.Frame(janela,width=150, height=150, bg=co3)
frame_esquerda.grid(row=0, column=0, pady=1, padx=1, sticky=tkinter.NSEW)

frame_direita=tkinter.Frame(janela,width=250, height=150, bg=co3)
frame_direita.grid(row=0, column=1, pady=1, padx=0, sticky=tkinter.NSEW)

frame_baixo = tkinter.Frame(janela, width=404, height=100, bg=co3)
frame_baixo.grid(row=1, column=0, columnspan=3, pady=1, padx=0, sticky=tkinter.NSEW)

#configuração do frame esquerdo

img_1 = PIL.Image.open('iconmusic\icone.png')
img_1 = img_1.resize((130,130))
img_1 = PIL.ImageTk.PhotoImage(img_1)

l_logo =tkinter.Label(frame_esquerda, height=130, image = img_1, compound =tkinter.LEFT, padx=0, anchor='nw', font=('ivy 16 bold'), bg=co3, fg=co3 )
l_logo.place(x=10, y=15)

#criando funções


#iniciar música
def play_musica():
    rodando = listbox.get(tkinter.ACTIVE)
    l_rodando['text'] = rodando
    pygame.mixer.music.load(rodando)
    pygame.mixer.music.play()
    
#pausar música    
def stop_musica():
    pygame.mixer.music.pause() 

#continuar música
def continuar_musica():
    pygame.mixer.music.unpause()

#proxima música
def proxima_musica():
    tocando = l_rodando['text'] 
    index = musicas.index(tocando)
    novo_index = (index + 1) % len(musicas)
    tocando = musicas[novo_index]
    pygame.mixer.music.load(tocando)
    pygame.mixer.music.play()
    listbox.delete(0,tkinter.END)
    mostrar()
    listbox.select_set(novo_index)
    listbox.config(selectmode=tkinter.SINGLE)
    l_rodando['text'] = tocando

 
#anterior música
def anterior_musica():
    tocando = l_rodando['text'] 
    index = musicas.index(tocando)
    novo_index = index - 1
    tocando = musicas[novo_index]
    pygame.mixer.music.load(tocando)
    pygame.mixer.music.play()
    listbox.delete(0,tkinter.END)
    mostrar()
    listbox.select_set(novo_index)
    listbox.config(selectmode=tkinter.SINGLE)
    l_rodando['text'] = tocando    
            


#configuração do frame direito
listbox=tkinter.Listbox(frame_direita, width=22, height=10, selectmode = tkinter.SINGLE, font=('arial 9 bold'),bg=co3 ,fg=co1 )
listbox.grid(row=0, column=0,)

#scroll
s=tkinter.Scrollbar(frame_direita)
s.grid(row=0, column=1, sticky=tkinter.NSEW)

listbox.config(yscrollcommand=s.set)
s.config(command=listbox.yview)


#configuração do frame baixo
l_rodando =tkinter.Label(frame_baixo, text='Escolha uma musica na playlist', width=44, justify=tkinter.LEFT, anchor='nw', font=('ivy 10'), bg=co1, fg=co4 )
l_rodando.place(x=0, y=1)

img_2 = PIL.Image.open('iconmusic/anterior.png')
img_2 = img_2.resize((30,30))
img_2 = PIL.ImageTk.PhotoImage(img_2)
b_anterior=tkinter.Button(frame_baixo, command=anterior_musica, width=40,height=40,image=img_2, font=('ivy 10 '),relief=tkinter.RAISED,overrelief=tkinter.RIDGE  , bg=co3 )
b_anterior.place(x=85, y=35)

img_3 = PIL.Image.open('iconmusic/play.png')
img_3 = img_3.resize((30,30))
img_3 = PIL.ImageTk.PhotoImage(img_3)
b_play=tkinter.Button(frame_baixo, command=play_musica, width=40,height=40,image=img_3, font=('ivy 10 '),relief=tkinter.RAISED,overrelief=tkinter.RIDGE  , bg=co3 )
b_play.place(x=130, y=35)

img_4 = PIL.Image.open('iconmusic/posterior.png')
img_4 = img_4.resize((30,30))
img_4 = PIL.ImageTk.PhotoImage(img_4)
b_posterior=tkinter.Button(frame_baixo, command=proxima_musica, width=40,height=40,image=img_4, font=('ivy 10 '),relief=tkinter.RAISED,overrelief=tkinter.RIDGE  , bg=co3 )
b_posterior.place(x=173, y=35)

img_5 = PIL.Image.open('iconmusic/pause.png')
img_5 = img_5.resize((30,30))
img_5 = PIL.ImageTk.PhotoImage(img_5)
b_pause=tkinter.Button(frame_baixo, command=stop_musica, width=40,height=40,image=img_5, font=('ivy 10 '),relief=tkinter.RAISED,overrelief=tkinter.RIDGE  , bg=co3 )
b_pause.place(x=218, y=35)

img_6 = PIL.Image.open('iconmusic/continuar.png')
img_6 = img_6.resize((30,30))
img_6 = PIL.ImageTk.PhotoImage(img_6)
b_continuar = tkinter.Button(frame_baixo,command=continuar_musica, width=40, height=40, image = img_6, font=('ivy 10 '), relief=tkinter.RAISED, overrelief=tkinter.RIDGE, bg=co3 )
b_continuar.place(x=263, y=35)


os.chdir(r'C:\Users\Vitor\Documents\music')
musicas = os.listdir()

def mostrar():
    for i in musicas:
        listbox.insert(tkinter.END,i)
   
mostrar()



#iniciando o mixer
pygame.mixer.init()

janela.mainloop()


