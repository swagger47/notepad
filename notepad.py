import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser,filedialog,messagebox,font
import os
main_app=tk.Tk()
main_app.geometry('1200x800')
main_app.title('notebook')
main_app.wm_iconbitmap('icon.ico')
######################################### main manu   ######################################
#########################################  End main manu   ######################################
main_manu=tk.Menu()

#file icons

new_icons=tk.PhotoImage(file='icons/new.png')
open_icons=tk.PhotoImage(file='icons/open.png')
save_icons=tk.PhotoImage(file='icons/save.png')
save_as_icons=tk.PhotoImage(file='icons/save_as.png')
exit_icons=tk.PhotoImage(file='icons/exit.png')

file=tk.Menu(main_manu,tearoff=False)
############# edit icons

copy_icons=tk.PhotoImage(file='icons/copy.png')
paste_icons=tk.PhotoImage(file='icons/paste.png')
cut_icons=tk.PhotoImage(file='icons/cut.png')
clear_all_icons=tk.PhotoImage(file='icons/clear_all.png')
find_icons=tk.PhotoImage(file='icons/find.png')

edit=tk.Menu(main_manu,tearoff=False)


######### bar icons
tool_icons=tk.PhotoImage('icons/tool_bar.png')
status_icons=tk.PhotoImage('icons/status_bar.png')

view=tk.Menu(main_manu,tearoff=False)

###### color icons
light_default=tk.PhotoImage('icons/light_default.png')
light_plus=tk.PhotoImage('icons/light_plus.png')
night_Blue=tk.PhotoImage('icons/night_Blue.png')
monokai=tk.PhotoImage('icons/monokai.png')
red=tk.PhotoImage('icons/red.png')
dark=tk.PhotoImage('icons/dark.png')

color_theme=tk.Menu(main_manu,tearoff=False)

####### command
theme_choice=tk.StringVar()
color_icons=(light_default,light_plus,night_Blue,monokai,red,dark)
color_dict={
    'Light Default':('#000000','#ffffff'),
    'Light Plus':('#474747','#e0e0e0'),
    'Dark':('#c4c4c4','#2d2d2d'),
    'Monokai':('#d3b774','#474747'),
    'Red':('#2d2d2d','#ffe8e8'),
    'Night Blue':('#ededed','#6b9dc2')
}

###### casecade
main_manu.add_cascade(label='File',menu=file)
main_manu.add_cascade(label='Edit',menu=edit)
main_manu.add_cascade(label='View',menu=view)
main_manu.add_cascade(label='Color Theme',menu=color_theme)



############################################ tool bar ###################################
tool_bar=ttk.Label(main_app)
tool_bar.pack(side=tk.TOP,fill=tk.X)
#font box
font_tuple=tk.font.families()
font_family=tk.StringVar()
font_box=ttk.Combobox(tool_bar,width=30,textvariable=font_family,state='readonly')
font_box['values']=font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=0,column=0,padx=5)

#size box
size_var=tk.IntVar()
font_size=ttk.Combobox(tool_bar,width=14,textvariable=size_var,state='readonly')
font_size['values']=tuple(range(8,81))
font_size.current(4)
font_size.grid(row=0,column=1,padx=5)

### Bold button

bold_icon=tk.PhotoImage(file='icons/bold.png')
bold_btn=ttk.Button(tool_bar,image=bold_icon)
bold_btn.grid(row=0,column=2,padx=5)

### italic button
italic_icons=tk.PhotoImage(file='icons/italic.png')
italic_btn=ttk.Button(tool_bar,image=italic_icons)
italic_btn.grid(row=0,column=3,padx=5)

### underline button
underline_icon=tk.PhotoImage(file='icons/underline.png')
underline_btn=ttk.Button(tool_bar,image=underline_icon)
underline_btn.grid(row=0,column=4,padx=5)

### Font color  button
font_color_icon=tk.PhotoImage(file='icons/font_color.png')
font_btn=ttk.Button(tool_bar,image=font_color_icon)
font_btn.grid(row=0,column=5,padx=5)

### aline left  button
align_left_icon=tk.PhotoImage(file='icons/align_left.png')
align_left_btn=ttk.Button(tool_bar,image=align_left_icon)
align_left_btn.grid(row=0,column=6,padx=5)

### aline center  button
align_center_icon=tk.PhotoImage(file='icons/align_center.png')
align_center_btn=ttk.Button(tool_bar,image=align_center_icon)
align_center_btn.grid(row=0,column=7,padx=5)

### aline left  button
align_right_icon=tk.PhotoImage(file='icons/align_right.png')
align_right_btn=ttk.Button(tool_bar,image=align_right_icon)
align_right_btn.grid(row=0,column=8,padx=5)
########################################## End tool bar ##################################

########################################## Text Editor ##################################

text_editor=tk.Text(main_app)
text_editor.config(wrap='word',relief=tk.FLAT)

scroll_bar=tk.Scrollbar(main_app)
text_editor.focus()
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH,expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

##### font fmaily & font Size functionality
current_font_family='Arial'
current_font_size=12

def change_font(main_app):
    global current_font_family
    current_font_family=font_family.get()
    text_editor.configure(font=(current_font_family,current_font_size))
def change_fontsize(main_app):
    global current_font_size
    current_font_size=size_var.get()
    text_editor.configure(font=(current_font_family,current_font_size))

font_box.bind('<<ComboboxSelected>>',change_font)
font_size.bind('<<ComboboxSelected>>',change_fontsize)

####### button functionality
### Bold button
def change_bold():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight']=='normal':
        text_editor.configure(font=(current_font_family,current_font_size,'bold'))
    if text_property.actual()['weight']=='bold':
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))

bold_btn.configure(command=change_bold)
####### italic button
def change_italic():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant']=='roman':
        text_editor.configure(font=(current_font_family,current_font_size,'italic'))
    if text_property.actual()['slant']=='italic':
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))

italic_btn.configure(command=change_italic)
###### underline button
def change_underline():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline']==0:
        text_editor.configure(font=(current_font_family,current_font_size,'underline'))
    if text_property.actual()['underline']==1:
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))

underline_btn.configure(command=change_underline)

########### font color functionality
def change_font_clr():
    color_var=tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])
font_btn.configure(command=change_font_clr)

########### align button
## left
def change_left():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('left',justify=tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'left')

align_left_btn.configure(command=change_left)
## right
def change_right():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('right',justify=tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'right') 
align_right_btn.configure(command=change_right)
## center
def change_center():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('center',justify=tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'center') 

align_center_btn.configure(command=change_center)

text_editor.configure(font=('Arial',12))
########################################## End Text Editor ##################################
########################################## status bar ##################################
status_bar=ttk.Label(main_app,text='Status Bar')
status_bar.pack(side=tk.BOTTOM)

text_changed=False
def changed(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed=True
        words=len(text_editor.get(1.0,'end-1c').split())
        characters=len(text_editor.get(1.0,'end-1c'))
        status_bar.config(text=f'Characters :{characters}  Words={words}')
    text_editor.edit_modified(False)

text_editor.bind('<<Modified>>',changed)



########################################## End status ba ##################################

###################################### main manu functionality  #########################
url=''
## new functionality
def new_file(even=None):
    global url
    url=''
    text_editor.delete(1.0,tk.END)

## filecommands

file.add_command(label='New',image=new_icons,compound=tk.LEFT,accelerator='CTRL+n',command=new_file)

### Open functinality
def open_file(event=None):
    global url
    url=filedialog.askopenfilename(initialdir=os.getcwd(),title='select file',filetypes=(('Text file','*.txt'),('All files','*.*')))
    try:
        with open(url,'r') as fr:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,fr.read())
    except FileNotFoundError:
        return
    except:
        return
    main_app.title(os.path.basename(url))

file.add_command(label='Open',image=open_icons,compound=tk.LEFT,accelerator='CTRL+o',command=open_file)
#### save File

def save_file(event=None):
    global url
    try:
        if url:
            contant=str(text_editor.get(1.0,tk.END))
            with open(url,'w',encoding='utf-8') as fw:
                fw.write(contant)
        else:
            url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text file','*.txt'),('All files','*.*')))
            contant2=text_editor.get(1.0,tk.END)
            url.write(contant2)
            url.close()
    except:
        return

file.add_command(label='Save',image=save_icons,compound=tk.LEFT,accelerator='CTRL+s',command=save_file)

### save_as_file
def save_as_file(event=None):
    global url
    try:
        contant=text_editor.get(1.0,tk.END)
        url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text file','*.txt'),('All files','*.*')))
        url.write(contant)
        url.close()
    except:
        return     
file.add_command(label='Save_as',image=save_as_icons,compound=tk.LEFT,accelerator='CTRL+ALT+s',command=save_as_file)

#### exit functionality
def exit_func(event=None):
    global url,text_changed
    try:
        if text_changed:
            mbox=messagebox.askyesnocancel('warning','Do you want to save the file ?')
            if mbox is True:
                if url:
                    contant=text_editor.get(1.0,tk.END)
                    with open(url,'w',encoding='utf-8') as fw:
                        fw.write(contant) 
                        main_app.destroy()
                else:
                    contant2=str(text_editor.get(1.0,tk.END))
                    url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text file','*.txt'),('All files','*.*')))
                    url.write(contant2) 
                    url.close()
                    main_app.destroy()
            elif mbox is False:
                main_app.destroy()
        else:
            main_app.destroy()
    except:
        return

file.add_command(label='Exit',image=exit_icons,compound=tk.LEFT,accelerator='CTRL+q',command=exit_func)

########### edit commands
##### Find Functionality
def find_func(event=None):
    def find():
        word= find_input.get()
        text_editor.tag_remove('match',1.0,tk.END)
        matches=0
        if word:
            start_pos='1.0'
            while True:
                start_pos=text_editor.search(word,start_pos,stopindex=tk.END)
                if not start_pos:
                    break
                end_pos=f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match',start_pos,end_pos)
                matches+=1
                start_pos=end_pos
                text_editor.tag_config('match',foreground='red',background='yellow')

    def replace():
        word= find_input.get()
        replace_text=replace_input.get()
        contant=text_editor.get(1.0,tk.END)
        new_contant=contant.replace(word,replace_text)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,new_contant)

      
    find_dialogue=tk.Toplevel()
    find_dialogue.geometry('450x250+500+200')
    find_dialogue.title('Find')
    find_dialogue.resizable(0,0)

    ###Frame
    find_frame=ttk.LabelFrame(find_dialogue,text="Find/Replace")
    find_frame.pack(pady=20)
    ###Label
    text_find_label=ttk.Label(find_frame,text='Find :')
    text_replace_label=ttk.Label(find_frame,text='Replace :')

    ###entry
    find_input=ttk.Entry(find_frame,width=30)
    replace_input=ttk.Entry(find_frame,width=30)

    ### Button
    find_btn=ttk.Button(find_frame,text='Find',command=find)
    replace_btn=ttk.Button(find_frame,text='Replace',command=replace)

    ### ALL component Grid
    text_find_label.grid(row=0,column=0,padx=4,pady=4)
    text_replace_label.grid(row=1,column=0,padx=4,pady=4)

    find_input.grid(row=0,column=1,padx=4,pady=4)
    replace_input.grid(row=1,column=1,padx=4,pady=4)

    find_btn.grid(row=2,column=0,padx=8,pady=4)
    replace_btn.grid(row=2,column=1,padx=8,pady=4)

    find_dialogue.mainloop()

edit.add_command(label='Copy',image=copy_icons,compound=tk.LEFT,accelerator='CTRL+c',command=lambda:text_editor.event_generate("<Control c>"))
edit.add_command(label='Paste',image=paste_icons,compound=tk.LEFT,accelerator='CTRL+v',command=lambda:text_editor.event_generate("<Control v>"))
edit.add_command(label='Cut',image=cut_icons,compound=tk.LEFT,accelerator='CTRL+x',command=lambda:text_editor.event_generate("<Control x>"))
edit.add_command(label='Clear_all',image=clear_all_icons,compound=tk.LEFT,accelerator='CTRL+ALT+X',command=lambda:text_editor.delete(1.0.tk.END))
edit.add_command(label='Find',image=find_icons,compound=tk.LEFT,accelerator='CTRL+f',command=find_func)

######### view tool command
show_statusbar=tk.BooleanVar()
show_statusbar.set(True)
show_toolbar=tk.BooleanVar()
show_toolbar.set(True)
def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar=False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP,fill=tk.X)
        text_editor.pack(fill=tk.Both,expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar=True
def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar=False
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar=True

view.add_checkbutton(label='Tool_bar',onvalue=True,offvalue=0,variable= show_toolbar,image=tool_icons,compound=tk.LEFT,command=hide_toolbar)
view.add_checkbutton(label='Status_bar',onvalue=1,offvalue=False,variable= show_statusbar,image=status_icons,compound=tk.LEFT,command=hide_statusbar)

####### theme command
def change_theme():
    chosen_theme=theme_choice.get()
    color_tuple=color_dict.get(chosen_theme)
    fg_color,bg_color=color_tuple[0],color_tuple[1]
    text_editor.config(fg=fg_color,bg=bg_color)

count=0;
for i in color_dict:
    color_theme.add_radiobutton(label=i,image=color_icons[count],variable=theme_choice,compound=tk.LEFT,command=change_theme)
    count+=1;

###################################### End main manu functionality  #########################

main_app.config(menu=main_manu)
########### Bind shortcuts keys ####

main_app.bind("<Control-n>",new_file)
main_app.bind("<Control-o>",open_file)
main_app.bind("<Control-s>",save_file)
main_app.bind("<Control-Alt-s>",save_as_file)
main_app.bind("<Control-q>",exit_func)
main_app.bind("<Control-f>",find_func)
main_app.mainloop()