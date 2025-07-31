from tkinter import PhotoImage1111
from tkinter import Toplevel
from tkinter import Label
from tkinter import Button
from tkinter import SUNKEN
from tkinter import StringVar
from tkinter import Entry
from tkinter import END
from tkinter import GROOVE
from tkinter import RIDGE
from tkinter import Text
from tkinter import Listbox
from tkinter import Scrollbar
from tkinter import Tk
from tkinter import VERTICAL
from tkinter import Frame
from tkinter import RIGHT
from tkinter import Y

import random


from tkinter import ttk
from hashlib import md5
from hashlib import sha512
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from base64  import b32hexdecode
from base64  import b32hexencode

from tkinter import messagebox as mb    # importing the messagebox module from tkinter  
from tkinter import filedialog as fd    # importing the fd module from tkinter  
import os                               # importing the os module  
import shutil                           # importing the shutil module  
from os import rename
from os import remove
from Cryptodome.Cipher import AES
from Cryptodome import Random
from glob import glob
from os import path

class all_log_in_page_functions():
 
    global old_out_1
    old_out_1=0 


    def Data_Page(self):
       root.resizable(0, 0)
       root.geometry("1500x780")        
   #-------------------------------------------------------------------------------------------------------------------------
       key=b'NR\xa4L\x1c\xb3\xb5pe\xfaC\x10\x81v\x8cK'
       iv=b'\xfb\x08@\xc8\xa0 \x9f\x07\xec\xd1\x9a@c\x85\xee\x1b'
   #-------------------------------------------------------------------------------------------------------------------------
       def create_file():
         global text_file_name,text,text_file,Save_As_But,Save_But,Return_But

         global folder_file_name
         folder_file_name=fd.askdirectory(title="Choise Folder To Create File In")
         global enteredFileName,rename_window
         enteredFileName=StringVar()     

         # creating another window  
         rename_window = Toplevel(root)  
         # setting the title  
         rename_window.title("New File Name")  
         # setting the size and position of the window  
         rename_window.geometry("300x100+300+250")  
         # disabling the resizable option  
         rename_window.resizable(0, 0)  
         # setting the background color of the window to #F6EAD7  
         rename_window.configure(bg = "#F6EAD7")  

         # creating a label  
         rename_label = Label(  
            rename_window,  
            text = "Enter the new file name:",  
            font = ("verdana", "8"),  
            bg = "#F6EAD7",  
            fg = "#000000"  
            )  
         # placing the label on the window  
         rename_label.pack(pady = 4)  
         enteredFileName=StringVar()     

         # creating an entry field  
         rename_field = Entry(  
            rename_window,  
            width = 26,  
            textvariable = enteredFileName,  
            relief = GROOVE,  
            font = ("verdana", "10"),  
            bg = "#FFFFFF",  
            fg = "#000000"  
            )  
         # placing the entry field on the window  
         rename_field.pack(pady = 4, padx = 4)  



         def back():
            text_file.close()
            text.destroy()
            Save_But.destroy()
            Save_As_But.destroy()
            Return_But.destroy()
            r=text_file_name.rfind("/")
            rr=text_file_name.rfind(".") 
            t=r+1
            tt=rr
            ttt=0
            name1=""
            name2=""
            while t< tt:
               name1=name1+text_file_name[t]
               t=t+1 
            while ttt<t:
               name2=name2+text_file_name[ttt]
               ttt=ttt+1
            with open(text_file_name,'rb') as f:
               w=f.read()
            f.close()

            with open(text_file_name,'wb') as nf:    
               nf.write(iv)
               c= AES.new(key,AES.MODE_OFB,iv)
               nf.write(c.encrypt(w))
            nf.close()
            rename(text_file_name,text_file_name+".enc")

            text.destroy()
            Save_But.destroy()
            Save_As_But.destroy()
            Return_But.destroy()
            pc_data_page()  


         def submitName_n():
            global text_file_name,folder_file_name,Save_As_But,Save_But,text,Return_But,text_file,is_this_main_account_page,is_this_chat_page

            enteredFileName_out=enteredFileName.get()
            text_file_name=folder_file_name+"/"+enteredFileName_out
            rename_window.destroy()  
            if folder_file_name:
               if enteredFileName_out != "" and".txt" in enteredFileName_out:
                  open_file_button.destroy()
                  rename_file_button.destroy()
                  encrypt_file_button.destroy()
                  decrypt_file_button.destroy()
                  encrypt_folder_button.destroy()
                  delete_file_button.destroy()
                  listFilesInFolder_button.destroy()
                  create_file_button.destroy()
                  move_folder_button.destroy()
                  copy_file_button.destroy() 
                  delete_folder_button.destroy()
                  Title.destroy()
                  decrypt_folder_button.destroy()
                  lab.destroy()
                  social_media_message_button.destroy()

                  text_file= open(text_file_name,"a+")
                  stuff=text_file.read()
                  text=Text(root,width=100,height=33,bg='LightGray',fg="black",font=("Comic", "18", "bold "))
                  text.place(x=20,y=20)
                  text.insert(END,stuff)
                  text_file.close()
                  Save_But=Button(root,text="Save/Enc",padx=36,command=save,bg="OrangeRed",fg="whitesmoke",font = ("Comic", "20","bold"),relief=SUNKEN,activebackground="darkOrange",activeforeground="white")
                  Save_But.place(x=1750,y=200)
                  Save_As_But=Button(root,text="Save_As/Enc",command=save_as,bg="OrangeRed",fg="whitesmoke",font = ("Comic", "20","bold"),relief=SUNKEN,activebackground="darkOrange",activeforeground="white")
                  Save_As_But.place(x=1750,y=400)
                  Return_But=Button(root,text="Return/Enc",padx=20,command=back,bg="OrangeRed",fg="whitesmoke",font = ("Comic", "20","bold"),relief=SUNKEN,activebackground="darkOrange",activeforeground="white")
                  Return_But.place(x=1750,y=600)
                  is_this_main_account_page=0
                  is_this_chat_page=0
                  



         # creating a button  
         submitButton = Button(  
            rename_window,  
            text = "Submit",  
            command = submitName_n,  
            width = 12,  
            relief = GROOVE,  
            font = ("verdana", "8"),  
            bg = "#C8F25D",  
            fg = "#000000",  
            activebackground = "#709218",  
            activeforeground = "#FFFFFF"  
            )  
         # placing the button on the window  
         submitButton.pack(pady = 2)  


   #-------------------------------------------------------------------------------------------------------------------------
       def encrypt_file():
          text_file_name=fd.askopenfilename(title="Open Text File",filetypes=(("text files","*.txt"),("jpg","*.jpg"),("png","*.png"),("pdf","*.pdf"),("Word","*.docx"),("vedio","*.mp4"),("power point","*.pptx"),("python","*.py")))
          if text_file_name:
             r=text_file_name.rfind("/")
             rr=text_file_name.rfind(".")
 
             t=r+1
             tt=rr
             ttt=0
             name1=""
             name2=""
             while t< tt:
                name1=name1+text_file_name[t]
                t=t+1
 
             while ttt<t:
                name2=name2+text_file_name[ttt]
                ttt=ttt+1
 
             key = Random.new().read(16)
             iv  = Random.new().read(16)
             key_file_name=name2+"_key.bin"
             with open(key_file_name, 'wb') as fb:
                fb.write(key)
             fb.close()
             with open(text_file_name,'rb') as f:
                w=f.read()
             f.close()
             with open(text_file_name,'wb') as nf:    
                nf.write(iv)
                c= AES.new(key,AES.MODE_OFB,iv)
                nf.write(c.encrypt(w))
             nf.close()
             # encrypt_file_name=name2+".en"
             rename(text_file_name,text_file_name+".en")
 
 
       def decrypt_file():
          decrypt_file_name=fd.askopenfilename(title="Choise Decrypt File",filetypes=((" Decrypt File","*.en"),))
          if decrypt_file_name:
             key_file_name=fd.askopenfilename(title="Choise Key File",filetypes=(("key files","*.bin"),))
             if key_file_name:
                r=decrypt_file_name.rfind("/")
                rr=decrypt_file_name.rfind(".")
 
                t=r+1
                tt=rr
                ttt=0
                name2=""
                while t< tt:
                   t=t+1
 
                while ttt<t:
                   name2=name2+decrypt_file_name[ttt]
                   ttt=ttt+1
 
 
                with open(key_file_name,'rb') as f:
                   keyk=f.read()
                f.close()
                with open(decrypt_file_name,'rb') as f:
                   iv=f.read(16)    
                   w=f.read()
                   f.close()
 
                try:
                   with open(decrypt_file_name,'wb') as nf:
                      c= AES.new(keyk,AES.MODE_OFB,iv)
                      nf.write(c.decrypt(w))
                   nf.close()
 
                   rename(decrypt_file_name,name2)
                   remove(key_file_name)
                except:
                   mb.showinfo(title = "Key Or File Error!", message = "The selected file or key are wrong.")  
 #_---------------------------------------------

       def decrypt_folder():
          folder_path=fd.askdirectory(title="Choise Folder To Decrypt It")
          if folder_path:
             files=glob(folder_path+'/*')
             if files:
                key_file_name=fd.askopenfilename(title="Choise Key File",filetypes=(("key files","*.bin"),))
                if key_file_name:
                   with open(key_file_name,'rb') as fh:
                      keyk=fh.read()
                   fh.close()
                               
 
                   def get_all(nono):
                      files=glob(nono+'/*')
                      if files:
                         for f in files:
                            if path.isdir(f):
                               get_all(f)
                            else:
                               r=f.rfind("/")
                               rr=f.rfind(".")
 
                               t=r+1
                               tt=rr
                               ttt=0
                               name2=""
                               while t< tt:
                                  t=t+1
 
                               while ttt<t:
                                  name2=name2+f[ttt]
                                  ttt=ttt+1
 
                               with open(f,'rb') as fg:
                                  iv=fg.read(16)    
                                  w=fg.read()
                               fg.close()
 
                               with open(f,'wb') as nf:
                                  c= AES.new(keyk,AES.MODE_OFB,iv)
                                  nf.write(c.decrypt(w))
                               nf.close()
                               rename(f,name2)
 
                   remove(key_file_name)
 
             get_all(folder_path)
 
 
       def encrypt_folder():
          folder_path=fd.askdirectory(title="Choise Folder To Encrypt It")
 
          if folder_path:
             files=glob(folder_path+'/*')
             if files:
                key = Random.new().read(16)
                iv  = Random.new().read(16)
                key_folder_name=folder_path+"_key.bin"
                with open(key_folder_name, 'wb') as fb:
                   fb.write(key)
                fb.close()
 
                def get_all(nono):
                   files=glob(nono+'/*')
                   if files:
                      for f in files:
                         if path.isdir(f):
                            get_all(f)
                         else:
                            r=f.rfind("/")
                            rr=f.rfind(".")
                            t=r+1
                            tt=rr
                            ttt=0
                            name1=""
                            name2=""
                            while t< tt:
                               name1=name1+f[t]
                               t=t+1
 
                            while ttt<t:
                               name2=name2+f[ttt]
                               ttt=ttt+1
 
                            with open(f,'rb') as fg:
                               w=fg.read()
                            fg.close()
                            with open(f,'wb') as nf:    
                               nf.write(iv)
                               c= AES.new(key,AES.MODE_OFB,iv)
                               nf.write(c.encrypt(w))
                            nf.close()
                            # encrypt_file_name=name2+".en"
                            rename(f,f+".en")
 
             get_all(folder_path)
      #-------------------------------------------------------------------------------------------------------------------------
       def open_file():
         global text_file_name,text,text_file,Save_As_But,Save_But,Return_But,text_But,en_But
         open_file_button.destroy()
         rename_file_button.destroy()
         encrypt_file_button.destroy()
         decrypt_file_button.destroy()
         encrypt_folder_button.destroy()
         delete_file_button.destroy()
         listFilesInFolder_button.destroy()
         create_file_button.destroy()
         move_folder_button.destroy()
         copy_file_button.destroy() 
         delete_folder_button.destroy()
         decrypt_folder_button.destroy()
         close_button.destroy()
         social_media_message_button.destroy()
         
         def textfileopen():
            global text_file_name,text,text_file,Save_As_But,Save_But,Return_But,text_But,en_But,is_this_main_account_page,is_this_chat_page
            text_file_name=fd.askopenfilename(title="Open Text File",filetypes=(("text files","*.txt"),("Python files","*.py")))
            if text_file_name:
               text_But.destroy()
               en_But.destroy()
               text_file= open(text_file_name,"r")
               stuff=text_file.read()
               text=Text(root,width=100,height=33,bg='LightGray',fg="black",font=("Comic", "18", "bold "))
               text.place(x=20,y=20)
               text.insert(END,stuff)
               text_file.close()
               Save_But=Button(root,text="Save/Enc",padx=17,command=save,bg="OrangeRed",fg="whitesmoke",font = ("Comic", "20","bold"),relief=SUNKEN,activebackground="darkOrange",activeforeground="white")
               Save_But.place(x=1320,y=200)
               Save_As_But=Button(root,text="Save_As/Enc",command=save_as,bg="OrangeRed",fg="whitesmoke",font = ("Comic", "20","bold"),relief=SUNKEN,activebackground="darkOrange",activeforeground="white")
               Save_As_But.place(x=1320,y=400)
               Return_But=Button(root,text="Return/Enc",padx=6,command=back,bg="OrangeRed",fg="whitesmoke",font = ("Comic", "20","bold"),relief=SUNKEN,activebackground="darkOrange",activeforeground="white")
               Return_But.place(x=1320,y=600)
               open_file_button.destroy()
               Title.destroy()
               lab.destroy()
               is_this_main_account_page=0
               is_this_chat_page=0
               close_button.destroy()


         def encryptedfileopen():
            global text_file_name,text,text_file,Save_As_But,Save_But,Return_But,text_But,en_But,is_this_main_account_page,is_this_chat_page
            text_file_name=fd.askopenfilename(title="Open Encrypted File BY App_public key",filetypes=(("encripted files","*.enc"),))
            if text_file_name:
               text_But.destroy()
               en_But.destroy()
               with open(text_file_name,'rb') as f:
                     iv=f.read(16)    
                     w=f.read()
                     f.close()
               with open(text_file_name,'wb') as nf:
                     c= AES.new(key,AES.MODE_OFB,iv)
                     nf.write(c.decrypt(w))
               nf.close()
               r=text_file_name.rfind("/")
               rr=text_file_name.rfind(".") 
               t=r+1
               tt=rr
               ttt=0
               name1=""
               name2=""
               while t< tt:
                  name1=name1+text_file_name[t]
                  t=t+1 
               while ttt<t:
                  name2=name2+text_file_name[ttt]
                  ttt=ttt+1
               rename(text_file_name,name2)
               text_file_name=name2

               text_file= open(text_file_name,"r")
               stuff=text_file.read()
               text=Text(root,width=100,height=33,bg='LightGray',fg="black",font=("Comic", "18", "bold "))
               text.place(x=20,y=20)
               text.insert(END,stuff)
               text_file.close()
               Save_But=Button(root,text="Save/Enc",padx=17,command=save,bg="OrangeRed",fg="whitesmoke",font = ("Comic", "20","bold"),relief=SUNKEN,activebackground="darkOrange",activeforeground="white")
               Save_But.place(x=1320,y=200)
               Save_As_But=Button(root,text="Save_As/Enc",command=save_as,bg="OrangeRed",fg="whitesmoke",font = ("Comic", "20","bold"),relief=SUNKEN,activebackground="darkOrange",activeforeground="white")
               Save_As_But.place(x=1320,y=400)
               Return_But=Button(root,text="Return/Enc",padx=6,command=back,bg="OrangeRed",fg="whitesmoke",font = ("Comic", "20","bold"),relief=SUNKEN,activebackground="darkOrange",activeforeground="white")
               Return_But.place(x=1320,y=600)
               open_file_button.destroy()
               Title.destroy()
               lab.destroy()
               is_this_main_account_page=0
               is_this_chat_page=0
               

         def back():
            text_file.close()
            r=text_file_name.rfind("/")
            rr=text_file_name.rfind(".") 
            t=r+1
            tt=rr
            ttt=0
            name1=""
            name2=""
            while t< tt:
               name1=name1+text_file_name[t]
               t=t+1 
            while ttt<t:
               name2=name2+text_file_name[ttt]
               ttt=ttt+1
            with open(text_file_name,'rb') as f:
               w=f.read()
            f.close()

            with open(text_file_name,'wb') as nf:    
               nf.write(iv)
               c= AES.new(key,AES.MODE_OFB,iv)
               nf.write(c.encrypt(w))
            nf.close()
            rename(text_file_name,text_file_name+".enc")

            text.destroy()
            Save_But.destroy()
            Save_As_But.destroy()
            Return_But.destroy()
            pc_data_page()  

         text_But=Button(root,text="Plain Text File",padx=36,command=textfileopen,bg="OrangeRed",fg="whitesmoke",font = ("Comic", "20","bold"),relief=SUNKEN,activebackground="darkOrange",activeforeground="white")
         text_But.place(x=700,y=600)

         en_But=Button(root,text="Encrypted File",padx=36,command=encryptedfileopen,bg="OrangeRed",fg="whitesmoke",font = ("Comic", "20","bold"),relief=SUNKEN,activebackground="darkOrange",activeforeground="white")
         en_But.place(x=1150,y=600)




   #-------------------------------------------------------------------------------------------------------------------------

       def save():
          global text_file_name,text
          text_file= open(text_file_name,"w")
          text_file.write(text.get(1.0,END))
          text_file.close()
          text.destroy()
          Save_But.destroy()
          Save_As_But.destroy()
          Return_But.destroy()
          r=text_file_name.rfind("/")
          rr=text_file_name.rfind(".") 
          t=r+1
          tt=rr
          ttt=0
          name1=""
          name2=""
          while t< tt:
             name1=name1+text_file_name[t]
             t=t+1 
          while ttt<t:
             name2=name2+text_file_name[ttt]
             ttt=ttt+1
 
 
          with open(text_file_name,'rb') as f:
             w=f.read()
          f.close()
 
          with open(text_file_name,'wb') as nf:    
             nf.write(iv)
             c= AES.new(key,AES.MODE_OFB,iv)
             nf.write(c.encrypt(w))
          nf.close()
          rename(text_file_name,text_file_name+".enc")
          pc_data_page()  
 
 
 
       def save_as():
          global text_file_name,text,save_as_file_name
          save_as_file_name=fd.asksaveasfilename(title="Open Text File",filetypes=(("text files","*.txt"),))
          if save_as_file_name:
             save_as_file= open(save_as_file_name,"w")
             save_as_file.write(text.get(1.0,END))
             save_as_file.close()
             text.destroy()
             Save_But.destroy()
             Save_As_But.destroy()
             Return_But.destroy()
             r=save_as_file_name.rfind("/")
             rr=save_as_file_name.rfind(".") 
             t=r+1
             tt=rr
             ttt=0
             name1=""
             name2=""
             while t< tt:
                name1=name1+save_as_file_name[t]
                t=t+1 
             while ttt<t:
                name2=name2+save_as_file_name[ttt]
                ttt=ttt+1
 
 
             with open(save_as_file_name,'rb') as f:
                w=f.read()
             f.close()
 
             with open(save_as_file_name,'wb') as nf:    
                nf.write(iv)
                c= AES.new(key,AES.MODE_OFB,iv)
                nf.write(c.encrypt(w))
             nf.close()
             rename(save_as_file_name,save_as_file_name+".enc")
 
 
             # text_file.close()
             # r=text_file_name.rfind("/")
             # rr=text_file_name.rfind(".") 
             # t=r+1
             # tt=rr
             # ttt=0
             # name1=""
             # name2=""
             # while t< tt:
             #    name1=name1+text_file_name[t]
             #    t=t+1 
             # while ttt<t:
             #    name2=name2+text_file_name[ttt]
             #    ttt=ttt+1
             # with open(text_file_name,'rb') as f:
             #    w=f.read()
             # f.close()
 
             # with open(text_file_name,'wb') as nf:    
             #    nf.write(iv)
             #    c= AES.new(key,AES.MODE_OFB,iv)
             #    nf.write(c.encrypt(w))
             # nf.close()
             # rename(text_file_name,text_file_name+".enc")
 
             pc_data_page()  
 


   #-------------------------------------------------------------------------------------------------------------------------
       def copyFile():  
          # using the fd's askopenfilename() method to select the file  
          fileToCopy = fd.askopenfilename(  
             title = "Select a file to copy",  
             filetypes=[("All files", "*.*")]  
             )  
          # using the fd's askdirectory() method to select the directory  
          directoryToPaste = fd.askdirectory(title = "Select the folder to paste the file")  
 
          # using the try-except method  
          try:  
             # using the copy() method of the shutil module to  
             # paste the select file to the desired directory  
             shutil.copy(fileToCopy, directoryToPaste)  
             # showing success message using the messagebox's showinfo() method  
             mb.showinfo(  
                title = "File copied!",  
                message = "The selected file has been copied to the selected location."  
                )  
          except:  
             # using the showerror() method to display error  
             mb.showerror(  
                title = "Error!",  
                message = "Selected file is unable to copy to the selected location. Please try again!"  
                )  
 
    #-------------------------------------------------------------------------------------------------------------------------
       # function to delete a file  
       def deleteFile():  
          # selecting the file using the fd's askopenfilename() method  
          the_file = fd.askopenfilename(  
             title = "Choose a file to delete",  
             filetypes = [("All files", "*.*")]  
             )
          if the_file:  
             # deleting the file using the remove() method of the os module  
             os.remove(os.path.abspath(the_file))  
             # displaying the success message using the messagebox's showinfo() method  
             mb.showinfo(title = "File deleted!", message = "The selected file has been deleted.")  
 
 
    #-------------------------------------------------------------------------------------------------------------------------
 
       # function to rename a file  
       def renameFile():  
          global enteredFileName,rename_window
          enteredFileName=StringVar()     
 
          # creating another window  
          rename_window = Toplevel(root)  
          # setting the title  
          rename_window.title("Rename File")  
          # setting the size and position of the window  
          rename_window.geometry("300x100+300+250")  
          # disabling the resizable option  
          rename_window.resizable(0, 0)  
          # setting the background color of the window to #F6EAD7  
          rename_window.configure(bg = "#F6EAD7")  
 
          # creating a label  
          rename_label = Label(  
             rename_window,  
             text = "Enter the new file name:",  
             font = ("verdana", "8"),  
             bg = "#F6EAD7",  
             fg = "#000000"  
             )  
          # placing the label on the window  
          rename_label.pack(pady = 4)  
 
          # creating an entry field  
          rename_field = Entry(  
             rename_window,  
             width = 26,  
             textvariable = enteredFileName,  
             relief = GROOVE,  
             font = ("verdana", "10"),  
             bg = "#FFFFFF",  
             fg = "#000000"  
             )  
          # placing the entry field on the window  
          rename_field.pack(pady = 4, padx = 4)  
 
          # creating a button  
          submitButton = Button(  
             rename_window,  
             text = "Submit",  
             command = submitName,  
             width = 12,  
             relief = GROOVE,  
             font = ("verdana", "8"),  
             bg = "#C8F25D",  
             fg = "#000000",  
             activebackground = "#709218",  
             activeforeground = "#FFFFFF"  
             )  
          # placing the button on the window  
          submitButton.pack(pady = 2)  
 
       # defining a function get the file path  
       def getFilePath():  
          # selecting the file using the fd's askopenfilename() method  
          the_file = fd.askopenfilename(title = "Select the file to rename", filetypes = [("All files", "*.*")])  
          # returning the file path  
          if the_file:
             return the_file  
 
       # defining a function that will be called when submit button is clicked  
       def submitName():
          rename_window.destroy()
          # getting the entered name from the entry field  
          renameName = enteredFileName.get()  
          # setting the entry field to empty string  
          enteredFileName.set("")  
          # calling the getFilePath() function  
          fileName = getFilePath()  
          # creating a new file name for the file  
          newFileName = os.path.join(os.path.dirname(fileName), renameName + os.path.splitext(fileName)[1])  
          # using the rename() method to rename the file  
          os.rename(fileName, newFileName)  
          # using the showinfo() method to display a message box to show the success message  
          mb.showinfo(title = "File Renamed!", message = "The selected file has been renamed.")  
 
    #-------------------------------------------------------------------------------------------------------------------------
       # defining a function to delete the folder  
       def deleteFolder():  
          # using the fd's askdirectory() method to select the folder  
          folderToDelete = fd.askdirectory(title = 'Select Folder to delete')  
          # using the rmdir() method of the os module to delete the selected folder  
          try:
             os.rmdir(folderToDelete)  
             mb.showinfo("Folder Deleted!", "The selected folder has been deleted!")  
 
          except:
             files=glob(folderToDelete+'/*')
             if files:
                for file in files:
                   r=file.rfind("/")
                   rr=file.rfind(".") 
                   t=r+1
                   tt=rr
                   ttt=0
                   name1=""
                   name2=""
                   while t< tt:
                      name1=name1+file[t]
                      t=t+1 
                   while ttt<t:
                      name2=name2+file[ttt]
                      ttt=ttt+1
 
 
                   with open(file,'rb') as f:
                      w=f.read()
                   f.close()
 
                   with open(file,'wb') as nf:    
                      nf.write(iv)
                      c= AES.new(key,AES.MODE_OFB,iv)
                      nf.write(c.encrypt(w))
                   nf.close()
                   name2=name2+".en"
                   rename(file,name2)
                   remove(name2)
             try:
                os.rmdir(folderToDelete)  
                mb.showinfo("Folder Deleted!", "The selected folder has been deleted!")  
             except:
                mb.showinfo("Only Files Deleted!", "What in folder deleted not folder itself")  
 
 
    #-------------------------------------------------------------------------------------------------------------------------
    # defining a function to move the folder  
       def moveFolder():  
          # using the askdirectory() method to select the folder  
          folderToMove = fd.askdirectory(title = 'Select the folder you want to move')  
          if folderToMove:
          # using the showinfo() method to dislay  
             mb.showinfo(message = 'Folder has been selected to move. Now, select the desired destination.')  
             # using the askdirectory() method to select the destination  
             des = fd.askdirectory(title = 'Destination')  
             #using the try-except method  
             if des:
                try:  
                   # using the move() method of the shutil module to move the folder to the requested location  
                   shutil.move(folderToMove, des)
                   # displaying the success message using the messagebox's showinfo() method  
                   mb.showinfo("Folder moved!", 'The selected folder has been moved to the desired Location')  
                except:  
                   # displaying the failure message using the messagebox's showerror() method  
                   mb.showerror('Error!', 'The Folder cannot be moved. Make sure that the destination exists')  
 
 
 
    #-------------------------------------------------------------------------------------------------------------------------
       # defining a function to list all the files available in a folder  
       def listFilesInFolder():  
          # declaring a variable with initial value 0  
          i = 0  
          # using the askdirectory() method to select the folder  
          the_folder = fd.askdirectory(title = "Select the Folder")  
          if the_folder:
             # using the listdir() method to list all the files in the directory  
             the_files = os.listdir(os.path.abspath(the_folder))  
 
             # creating an object of Toplevel class  
             listFilesWindow = Toplevel(root)  
             # specifying the title of the pop-up window  
             listFilesWindow.title(f'Files in {the_folder}')  
             # specifying the size and position of the window  
             listFilesWindow.geometry("300x500+300+200")  
             # disabling the resizable option  
             listFilesWindow.resizable(0, 0)  
             # setting the background color of the window to #EC2FB1  
             listFilesWindow.configure(bg = "#EC2FB1")  
 
          # creating a list box  
          the_listbox = Listbox(  
             listFilesWindow,  
             selectbackground = "#F24FBF",  
             font = ("Verdana", "10"),  
             background = "#FFCBEE"  
             )  
          # placing the list box on the window  
          the_listbox.place(relx = 0, rely = 0, relheight = 1, relwidth = 1)  
 
          # creating a scroll bar  
          the_scrollbar = Scrollbar(  
             the_listbox,  
             orient = VERTICAL,  
             command = the_listbox.yview  
             )  
          # placing the scroll bar to the right side of the window  
          the_scrollbar.pack(side = RIGHT, fill = Y)  
 
          # setting the yscrollcommand parameter of the listbox's config() method to the scrollbar  
          the_listbox.config(yscrollcommand = the_scrollbar.set)  

          # iterating through the files in the folder  
          while i < len(the_files):  
             the_listbox.insert(END, "[" + str(i+1) + "] " + the_files[i])  
             i += 1  
          the_listbox.insert(END, "")  
          the_listbox.insert(END, "Total Files: " + str(len(the_files))) 
       
       def back_from_social_page():
            social__links_file_text.destroy()
            Return_But_from_social.destroy()
            pc_data_page()
       
       def social_media_message():
         global text_file_name,text,text_file,Save_As_But,Save_But,Return_But,text_But,en_But,social__links_file_text,Return_But_from_social
         open_file_button.destroy()
         rename_file_button.destroy()
         encrypt_file_button.destroy()
         decrypt_file_button.destroy()
         encrypt_folder_button.destroy()
         delete_file_button.destroy()
         listFilesInFolder_button.destroy()
         create_file_button.destroy()
         move_folder_button.destroy()
         copy_file_button.destroy() 
         delete_folder_button.destroy()
         decrypt_folder_button.destroy()
         close_button.destroy()
         social_media_message_button.destroy() 
         
         social__links_file= open('images/social_links.txt',"r")
         social__links_file_text_stuff=social__links_file.read()
         social__links_file_text=Text(root,width=130,height=35,bg='LightGray',fg="black",font=("Comic", "18", "bold "))
         social__links_file_text.place(x=20,y=20)
         social__links_file_text.insert(END,social__links_file_text_stuff)
         social__links_file.close()
         
         mb.showinfo("Greetings", "Please, Follow Me!")        
         
         Return_But_from_social=Button(root,text="Return",padx=20,command=back_from_social_page,bg="OrangeRed",fg="whitesmoke",font = ("Comic", "20","bold"),relief=SUNKEN,activebackground="darkOrange",activeforeground="white")
         Return_But_from_social.place(x=1310,y=700)   
    #-------------------------------------------------------------------------------------------------------------------------
 
       def pc_data_page():
          global is_this_chat_page,is_this_main_account_page,lab,bg,close_button,open_file_button,social_media_message_button,Title,open_file_button,rename_file_button,encrypt_file_button,decrypt_file_button,encrypt_folder_button,delete_file_button,listFilesInFolder_button,create_file_button,move_folder_button,copy_file_button,delete_folder_button,decrypt_folder_button
          Title=Label(root,text="""CyberXEng Control Board""",font=("Times", "60", "bold "),padx=260,pady=25,fg="Navy",relief=SUNKEN,highlightbackground="red")
          Title.config(highlightthickness=10, highlightbackground="Navy")
          Title.place(x=10,y=10)
 
          #Main_button=Button(root,text="Main",padx=50,bg="navy",fg="whitesmoke",command=main_account_page_from_data_page,font = ("Comic", "20","bold"),relief=SUNKEN,activebackground="red",activeforeground="black")
 
          bg=PhotoImage(file="images\\1231.png")
          lab=Label(root,image=bg,height=580)
          lab.place(x=10,y=180)
 
          close_button=Button(root,text="CLOSE",bg="navy",fg="whitesmoke",font=("Comic", "20", "bold "),padx=20,relief=SUNKEN,command=root.destroy,activebackground="red",activeforeground="white")
          close_button.place(x=1310,y=700)
          
          social_media_message_button=Button(root,text="My Social Links",bg="red",fg="whitesmoke",font=("Comic", "20", "bold "),padx=10,relief=SUNKEN,command=social_media_message,activebackground="red",activeforeground="white")
          social_media_message_button.place(x=660,y=700)
          

          create_file_button=Button(root,text="Notepad",padx=80,bg="OrangeRed",fg="whitesmoke",command=create_file,font = ("Comic", "20","bold"),relief=SUNKEN,activebackground="darkOrange",activeforeground="white")
          create_file_button.place(x=1140,y=200)

          open_file_button=Button(root,text=" Open/Enc/Dec File with App_Publik Key",padx=8,bg="OrangeRed",fg="whitesmoke",command=open_file,font = ("Comic", "20","bold"),relief=SUNKEN,activebackground="darkOrange",activeforeground="white")
          open_file_button.place(x=680,y=270)
          
          rename_file_button=Button(root,text="Rename File",padx=6,bg="OrangeRed",fg="whitesmoke",command=renameFile,font = ("Comic", "20","bold"),relief=SUNKEN,activebackground="darkOrange",activeforeground="white")
          rename_file_button.place(x=1280,y=270)
 
 
          encrypt_file_button=Button(root,text="Encrypt File with Asymmetric Private Key",bg="OrangeRed",fg="whitesmoke",command=encrypt_file,font = ("Comic", "20","bold"),relief=SUNKEN,activebackground="darkOrange",activeforeground="white")
          encrypt_file_button.place(x=680,y=340)
 
          copy_file_button=Button(root,text="Copy File",bg="OrangeRed",fg="whitesmoke",padx=26,command=copyFile,font = ("Comic", "20","bold"),relief=SUNKEN,activebackground="darkOrange",activeforeground="white")
          copy_file_button.place(x=1280,y=340)
 
 
          decrypt_file_button=Button(root,text="Decrypt File with Asymmetric Private Key",bg="OrangeRed",fg="whitesmoke",command=decrypt_file,font = ("Comic", "20","bold"),relief=SUNKEN,activebackground="darkOrange",activeforeground="white")
          decrypt_file_button.place(x=680,y=410)
 
          delete_file_button=Button(root,text="Delete File",padx=20,bg="OrangeRed",fg="whitesmoke",command=deleteFile,font = ("Comic", "20","bold"),relief=SUNKEN,activebackground="darkOrange",activeforeground="white")
          delete_file_button.place(x=1280,y=410)
 
 
          encrypt_folder_button=Button(root,text=" Enc Folder with Asymmetric Private Key ",bg="OrangeRed",fg="whitesmoke",command=encrypt_folder,font = ("Comic", "20","bold"),relief=SUNKEN,activebackground="darkOrange",activeforeground="white")
          encrypt_folder_button.place(x=680,y=480)
 
 
 
          move_folder_button=Button(root,text="Move Folder",padx=9,bg="OrangeRed",fg="whitesmoke",command=moveFolder,font = ("Comic", "20","bold"),relief=SUNKEN,activebackground="darkOrange",activeforeground="white")
          move_folder_button.place(x=1280,y=480)
 
 
          decrypt_folder_button=Button(root,text=" Dec Folder with Asymmetric Private Key ",bg="OrangeRed",fg="whitesmoke",command=decrypt_folder,font = ("Comic", "20","bold"),relief=SUNKEN,activebackground="darkOrange",activeforeground="white")
          decrypt_folder_button.place(x=680,y=550)
 

          delete_folder_button=Button(root,text="Delete Folder",padx=3,bg="OrangeRed",fg="whitesmoke",command=deleteFolder,font = ("Comic", "20","bold"),relief=SUNKEN,activebackground="darkOrange",activeforeground="white")
          delete_folder_button.place(x=1280,y=550)


          listFilesInFolder_button=Button(root,text=" list Files In Folder ",bg="OrangeRed",fg="whitesmoke",command=listFilesInFolder,font = ("Comic", "20","bold"),relief=SUNKEN,activebackground="darkOrange",activeforeground="white")
          listFilesInFolder_button.place(x=1140,y=620)

 

          is_this_chat_page=0
      


       pc_data_page()
 


  
    def Log_In_button(self):
        control_board.destroy()
        lab.destroy()
        account.destroy()
        Close.destroy()
        self.Data_Page()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def Main_log_in_Page(self):
        global control_board ,Close ,bg,bgg,labb,root,account,lab
        root = Tk()
        root.resizable(0, 0)
        root.geometry("655x755")#width and hight Of The Window
        root.title("CyberXEng Control Board")#Title to windows
        root.configure(bg="white")
        bg=PhotoImage(file="images/555.png")
        lab=Label(root,image=bg)
        lab.place(x=-40,y=30)



        control_board=Label(root,text="""CyberXEng Control Board""",font=("Times", "40", "bold "),padx=17,fg="black",pady=1,background="WhiteSmoke",relief=SUNKEN,highlightbackground="red",bg="WhiteSmoke")
        control_board.place(x=0,y=0)


        account=Button(root,text="LOG IN",border=5,font=("Comic", "20", "bold "),padx=77,relief=SUNKEN,command=lambda: self.Log_In_button(),activebackground="red",activeforeground="white")
        account.place(x=360,y=604)


        Close=Button(root,text="CLOSE",border=5,font=("Comic", "20", "bold "),padx=80,relief=SUNKEN,command=root.destroy,activebackground="red",activeforeground="white")
        Close.place(x=360,y=684)


        root.mainloop()

all_log_in_page_functions().Main_log_in_Page()
