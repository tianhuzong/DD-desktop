"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net/tkinter-helper
QQ交流群:788392508
"""
import os
from tkinter import * 
from tkinter import filedialog,messagebox
from tkinter.ttk import *
from typing import Dict
import json
import re
#import deepdanbooru as dd 
class WinGUI(Tk):
    widget_dic: Dict[str, Widget] = {}
    def __init__(self):
        super().__init__()
        self.__win()
        self.widget_dic["tk_label_lkv6qyiy"] = self.__tk_label_lkv6qyiy(self)
        self.widget_dic["tk_label_lkv81yxf"] = self.__tk_label_lkv81yxf(self)
        self.widget_dic["tk_input_lkv885yc"] = self.__tk_input_lkv885yc(self)
        self.widget_dic["tk_button_lkv88hqj"] = self.__tk_button_lkv88hqj(self)
        self.widget_dic["tk_button_lkv89fia"] = self.__tk_button_lkv89fia(self)
        self.widget_dic["tk_table_lkv8f7i3"] = self.__tk_table_lkv8f7i3(self)
        self.widget_dic["tk_label_lkv8p29k"] = self.__tk_label_lkv8p29k(self)
        self.widget_dic["tk_button_lkwnd3z7"] = self.__tk_button_lkwnd3z7(self)
        self.widget_dic["tk_button_lkxl8nd0"] = self.__tk_button_lkxl8nd0(self)
        self.model = dd.project.load_model_from_project("./model")
        self.tags = dd.data.load_tags("./model/tags.txt")
    def __win(self):
        self.title("Tkinter布局助手")
        # 设置窗口大小、居中
        width = 740
        height = 492
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        self.resizable(width=False, height=False)
        # 自动隐藏滚动条
    def scrollbar_autohide(self,bar,widget):
        self.__scrollbar_hide(bar,widget)
        widget.bind("<Enter>", lambda e: self.__scrollbar_show(bar,widget))
        bar.bind("<Enter>", lambda e: self.__scrollbar_show(bar,widget))
        widget.bind("<Leave>", lambda e: self.__scrollbar_hide(bar,widget))
        bar.bind("<Leave>", lambda e: self.__scrollbar_hide(bar,widget))
    
    def __scrollbar_show(self,bar,widget):
        bar.lift(widget)
    def __scrollbar_hide(self,bar,widget):
        bar.lower(widget)
    
    def vbar(self,ele, x, y, w, h, parent):
        sw = 15 # Scrollbar 宽度
        x = x + w - sw
        vbar = Scrollbar(parent)
        ele.configure(yscrollcommand=vbar.set)
        vbar.config(command=ele.yview)
        vbar.place(x=x, y=y, width=sw, height=h)
        self.scrollbar_autohide(vbar,ele)
    def __tk_label_lkv6qyiy(self,parent):
        label = Label(parent,text="DD-desktop：AI绘画的福音",anchor="center", )
        label.place(x=200, y=0, width=266, height=39)
        return label
    def __tk_label_lkv81yxf(self,parent):
        label = Label(parent,text="请输入文件地址：",anchor="center", )
        label.place(x=20, y=60, width=114, height=30)
        return label
    def __tk_input_lkv885yc(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=150, y=60, width=255, height=30)
        return ipt
    def __tk_button_lkv88hqj(self,parent):
        btn = Button(parent, text="添加", takefocus=False,)
        btn.place(x=510, y=60, width=64, height=30)
        return btn
    def __tk_button_lkv89fia(self,parent):
        btn = Button(parent, text="浏览", takefocus=False,)
        btn.place(x=420, y=60, width=77, height=30)
        return btn
    def __tk_table_lkv8f7i3(self,parent):
        # 表头字段 表头宽度
        columns = {"ID":71,"文件名":214,"路径（含文件）":428}
        tk_table = Treeview(parent, show="headings", columns=list(columns),)
        for text, width in columns.items():  # 批量设置列属性
            tk_table.heading(text, text=text, anchor='center')
            tk_table.column(text, anchor='center', width=width, stretch=False)  # stretch 不自动拉伸
        
        tk_table.place(x=20, y=110, width=715, height=348)
        self.vbar(tk_table, 20, 110, 715, 348,parent)
        return tk_table
    def __tk_label_lkv8p29k(self,parent):
        label = Label(parent,text="标签保存在与图片同一级目录",anchor="center", )
        label.place(x=20, y=460, width=716, height=30)
        return label
    def __tk_button_lkwnd3z7(self,parent):
        btn = Button(parent, text="删除", takefocus=False,)
        btn.place(x=590, y=60, width=64, height=30)
        return btn
    def __tk_button_lkxl8nd0(self,parent):
        btn = Button(parent, text="开始", takefocus=False,)
        btn.place(x=670, y=60, width=64, height=30)
        return btn
class Win(WinGUI):
    def __init__(self):
        super().__init__()
        self.__event_bind()
    def into_table(self,index,file_name,file_path):
        for x in self.widget_dic["tk_table_lkv8f7i3"].get_children():
            #print("\n\t",self.widget_dic["tk_table_lkv8f7i3"].item(x).get("values")[2],"\t\t",type(self.widget_dic["tk_table_lkv8f7i3"].item(x).get("values")))
            if file_path == self.widget_dic["tk_table_lkv8f7i3"].item(x).get("values")[2]:
                messagebox.showerror("错误", "文件已存在！")
                return
        self.widget_dic["tk_table_lkv8f7i3"].insert("", "end", values=(str(index),file_name,file_path))
    def file_in(self,evt):
        #添加文件到表格
        if (file_path := self.widget_dic["tk_input_lkv885yc"].get().strip()) == "":
            messagebox.showerror("错误", "请输入文件夹路径！")
        else:
            print(file_path,os.path.exists(file_path))
            if not os.path.exists(file_path):
                messagebox.showerror("错误", "这个文件不存在！")
            else : 
                file_path = self.widget_dic["tk_input_lkv885yc"].get()
                index = len(self.widget_dic["tk_table_lkv8f7i3"].get_children()) + 1
                file_name = os.path.basename(file_path)
                self.into_table(index,file_name,file_path)
    def file_new(self,evt):
        #浏览文件
        file_path = filedialog.askopenfilename(filetypes=[("JPEG files", "*.jpg"), ("PNG files", "*.png")])
        file_name = os.path.basename(file_path)
        
        index = len(self.widget_dic["tk_table_lkv8f7i3"].get_children()) + 1
        self.into_table(index,file_name,file_path)
    def delete_item(self,evt):
        # 获取选中的项目并删除
        selected_items = self.widget_dic["tk_table_lkv8f7i3"].selection()
        print(selected_items)
        if len(selected_items) == 0:
            messagebox.showerror("错误", "请选择要删除的文件！")
        else :
            try:
                for item in selected_items:
                    self.widget_dic["tk_table_lkv8f7i3"].delete(item)
                    messagebox.showinfo("成功", "删除成功！")
            except Exception as e:
                messagebox.showerror("错误","原因："+e)
            

    def get_all_values(self,tree):
        values = []
        for item in tree.get_children():
            values.append(tree.item(item)['values'])
        return values    
    def file_menu(self,evt):
        #文件菜单
        menu = Menu(self, tearoff=False)
        self.menu = menu
        menu.add_command(label="删除", command=self.delete_item)
    def save_txt_file(self,txt_path, tags):
        with open(txt_path, 'w', encoding='utf-8') as f:
            f.write(tags)
        print("Saved text file.")
    def replace_extension(self,filename, new_extension):
        # 获取原始文件名中的扩展名
        old_extension = filename.split('.')[-1]

        # 将原始扩展名替换为新扩展名
        new_filename = filename.replace(old_extension, new_extension)

        return new_filename
    def get_mark(self,evt):
        messagebox.showinfo("测试","开始")
        values = self.get_all_values(self.widget_dic["tk_table_lkv8f7i3"])
        print(values)
        paths = [y for x in values for y in x]
        tags :dict = {}
        for path in paths:
            for x in dd.commads.evaluate_image(path,self.model,self.tags):
                tags[x[0]] = str(x[1])
            tags_json = json.dumps(tags)
            name = os.path.basename(path)
            tags_path = path[0:(re.search(os.path.name(path),path)[1])]+self.replace_extension(name,"txt")
            self.save_txt_file(txt_path=tags_path,tags=tags_json)
        pass
    def __event_bind(self):
        self.widget_dic["tk_button_lkv88hqj"].bind('<Button-1>',self.file_in)#添加
        self.widget_dic["tk_button_lkv89fia"].bind('<Button-1>',self.file_new)#浏览
        self.widget_dic["tk_button_lkwnd3z7"].bind('<Button-1>',self.delete_item)#删除
        self.widget_dic["tk_button_lkxl8nd0"].bind("<Button-1>",self.get_mark)
        pass
if __name__ == "__main__":
    win = Win()
    win.mainloop()