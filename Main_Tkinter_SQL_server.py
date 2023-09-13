from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
import math
import math
import pyodbc 
import os 

server = 'LAPTOP-KU6D8QOE\DBI202'
database = 'master'
username = 'sa'
password = '19092003'

# Tạo chuỗi kết nối
connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Kết nối đến SQL Server
conn = pyodbc.connect(connection_string, autocommit=True)
# Tạo đối tượng cursor
cursor = conn.cursor()
# Thực hiện truy vấn kiểm tra kết nối
cursor.execute('SELECT 1')
result = cursor.fetchone()[0]
# Kiểm tra kết quả truy vấn
if result == 1:
    print('Kết nối thành công!')
else:
    print('Kết nối không thành công!')

#  Tạo cơ sở dữ liệu mới
# cursor.execute('CREATE DATABASE [PFP191_Student_Management]')

# sử dụng database [PFP191_Student_Management]
cursor.execute('USE [PFP191_Student_Management]')

# Tạo bảng 
# cursor.execute('''
# 		CREATE TABLE Student (
# 			StudentID nvarchar(10) primary key not Null,
# 			Student_Name nvarchar(50),
#             [Old] int,
#             [Lab] float, 
#             [Practice] float,
#             [Assignment] float,
#             [Practice Exam] float,
#             [Final Exam] float,
#             [Average] float,
#             [Rank] nvarchar(30)
# 			)
#                ''')
# conn.commit()

#  xóa bảng 
# cursor.execute('DROP TABLE Student')
# conn.commit()
# cursor.execute('delete from Student')
# # Lưu dữ liệu vào database
# with open('PFP191.txt','r', encoding='utf-8-sig') as file:
#     for line in file:
#         code, name, old, lab, pt, assignment, pe, fe, avg, rank = line.strip().split('\t')
#         cursor.execute('INSERT INTO Student (StudentID, Student_Name, [Old], [Lab], [Practice], [Assignment], [Practice Exam], [Final Exam], [Average], [Rank]) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?) ', code, name, old, lab, pt, assignment, pe, fe, avg, rank)
#     conn.commit()


############################### Tạo Tkinter ###############################
main = Tk()
main.title('QUẢN LÝ SINH VIÊN')
#  Lấy ảnh
path = r'fpt.jpg'
load = Image.open(path)
load = load.resize((100, 100))
render = ImageTk.PhotoImage(load)

# Đặt vị trí ảnh
img_label = Label(main, image=render)
img_label.place(x = 600 , y = 20)
fpt = Label(main, font = ('Arial', 6), text = 'DIT CON ME', fg = 'grey')
fpt.place(x = 550,  y = 20)
# Lấy kích thước màn hình
screen_width = main.winfo_screenwidth()
screen_height = main.winfo_screenheight()
# Đặt kích thước và vị trí của cửa sổ
main.geometry(f'800x400+{screen_width//2-150}+{screen_height//2-100}')
main.iconbitmap('') # hàm này để lấy file ảnh đặt làm icon cho title, file ảnh có type ICON 
main.attributes('-topmost', False) # hàm này được sử dụng để thay đổi các thuộc tính của cửa sổ, đặt cửa sổ này trên tất cả các cửa sổ khác 
# Tiêu đề 
name = Label(main, font = ('Arial', 14), text = 'DANH SÁCH CÁC TÙY CHỌN', bg = 'red', fg = 'white') # tiêu đề
# Đặt nhãn vào  cửa sổ
name.pack()

# tạo class dùng để hiện phần gợi ý trong mỗi button
class EntryWithPlaceholder(Entry):
        def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey'):
            super().__init__(master)
            self.placeholder = placeholder
            self.placeholder_color = color
            self.default_fg_color = self['fg']
            self.bind("<FocusIn>", self.foc_in)
            self.bind("<FocusOut>", self.foc_out)
            self.put_placeholder()

        def put_placeholder(self):
            self.insert(0, self.placeholder)
            self['fg'] = self.placeholder_color

        def foc_in(self, *args):
            if self['fg'] == self.placeholder_color:
                self.delete('0', 'end')
                self['fg'] = self.default_fg_color

        def foc_out(self, *args):
            if not self.get():
                self.put_placeholder()

# # # # # # # # # # # # Thêm Sinh viên # # # # # # # # # # # #
def Add_Student():
    if ID_Exit is not None:
        ID_Exit.place_forget()
    if t_delete is not None:
        t_delete.place_forget()
    if f_delete is not None:
        f_delete.place_forget()
    # đặt các nút còn lại chế độ chờ
    menu_button.config(state=tk.DISABLED)
    delete_button.config(state=tk.DISABLED)
    # nhập 
    global id_entry, name_entry, old_entry, lab_entry, pt_entry, ass_entry, pe_entry, fe_entry, submit_button, exit_button
    id_entry = EntryWithPlaceholder(main,'ID')
    id_entry.place(x = 150, y = 30)
    # Label(main, text = "Name").grid(row = 24, column = 50)
    name_entry = EntryWithPlaceholder(main,'NAME')
    name_entry.place(x = 150, y = 50)
    # Label(main, text = "Old").grid(row = 28, column = 50)
    old_entry = EntryWithPlaceholder(main, 'OLD')
    old_entry.place(x = 150, y = 70)
    # LAB 
    lab_entry = EntryWithPlaceholder(main, 'LAB')
    lab_entry.place(x = 300, y = 30)
    # PT
    pt_entry = EntryWithPlaceholder(main, 'PRACTICE')
    pt_entry.place(x = 300, y = 50)
    # ASSIGNMENT
    ass_entry = EntryWithPlaceholder(main, 'ASSIGNMENT')
    ass_entry.place(x = 300, y = 70)
    # PE
    pe_entry = EntryWithPlaceholder(main, 'PRACTICE EXAM')
    pe_entry.place(x = 300, y = 90)
    # FE
    fe_entry = EntryWithPlaceholder(main, 'FINAL EXAM')
    fe_entry.place(x = 300, y = 110)
    # tạo nút submit
    submit_button = Button(main, text="Submit", command = Save_Student)
    submit_button.place(x = 150, y = 110)
    # tạo nút exit 
    exit_button = Button(main, text="Exit", command = Exit_Add_Student)
    exit_button.place(x = 220, y = 110)
    print("Thêm sinh viên")
# kiểm tra ID
def Check_ID(code):
    # lấy dữ liệu
    name_table = 'Student'
    # Thực thi câu lệnh SQL
    cursor.execute(f'SELECT * FROM {name_table} WHERE StudentID = ?', code) # lấy thông tin của người có cần check 
    # Lấy kết quả truy vấn
    result = cursor.fetchone() # hàm này sẽ thêm những thông tin đó vào result
    if result is not None: 
        return False # ID tồn tại trong danh sách  
    else:   
        return True
# end def
# tạo label hiên thông báo 
ID_Exit = None
# Lưu vào SQL server
def Save_Student():
    global ID_Exit
    # save file 
    code = id_entry.get().upper()
    # kiểm tra code đã có trong file chưa
    if Check_ID(code): # check xem có ID trong danh sách không >> nếu không thì nhập 
        name = name_entry.get()
        old = old_entry.get()
        lab = float(lab_entry.get())
        pt = float(pt_entry.get())
        assignment = float(ass_entry.get())
        pe = float(pe_entry.get())
        fe = float(fe_entry.get())
        # tính điểm trung bình 
        avg = math.ceil( ( (float(lab * 0.1)) + float((pt * 0.1)) + float((assignment * 0.2)) + float((pe * 0.3)) + float((fe * 0.3))) * 100 ) / 100
        # xếp loại học lực 
        if (avg >= 8):
            rank = "Gioi"
        elif (avg >= 6.5):
            rank = "Kha"
        elif (avg >= 5):
            rank = "Trung Binh"
        else:
            rank = "Yeu"      
        # lưu vào SQL
        cursor.execute('INSERT INTO Student (StudentID, Student_Name, [Old], [Lab], [Practice], [Assignment], [Practice Exam], [Final Exam], [Average], [Rank]) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?) ', code, name, old, lab, pt, assignment, pe, fe, avg, rank)
        conn.commit()
        # end 

        # lấy dữ liệu từ SQL
        name_table = 'Student'
        cursor.execute(f'select * from [{name_table}] order by [Student].LAB')
        print('Thêm sinh viên thành công')
        Tree_View()
    else:
        ID_Exit = Label(main, text ='Mã học sinh đã tồn tại')
        ID_Exit.place(x = 150, y = 30)
        ID_Exit.after(2000, ID_Exit.place_forget)
        print('Thêm sinh viên không thành công')
        Tree_View()
    # Đóng tất cả các trường nhập
    id_entry.destroy()
    name_entry.destroy()
    old_entry.destroy()
    lab_entry.destroy()
    pt_entry.destroy()
    ass_entry.destroy()
    pe_entry.destroy()
    fe_entry.destroy()
    submit_button.place_forget()
    exit_button.place_forget()
    # đặt lại các nút
    menu_button.config(state=tk.NORMAL)
    delete_button.config(state=tk.NORMAL)
# end def
# tạo nút hủy để đóng các button thêm sinh viên
def Exit_Add_Student():
    id_entry.destroy()
    name_entry.destroy()
    old_entry.destroy()
    lab_entry.destroy()
    pt_entry.destroy()
    ass_entry.destroy()
    pe_entry.destroy()
    fe_entry.destroy()
    submit_button.place_forget()
    exit_button.place_forget()
    # đặt lại các nút
    menu_button.config(state=tk.NORMAL)
    delete_button.config(state=tk.NORMAL)
    print("Hủy thêm sinh viên")
# end def

# # # # # # # # # # # # Sắp xếp sinh viên # # # # # # # # # # # #
def Sort_By_Old():
    # ẩn cá label thông báo 
    if ID_Exit is not None:
        ID_Exit.place_forget()
    if t_delete is not None:
        t_delete.place_forget()
    if f_delete is not None:
        f_delete.place_forget()
    # kết nốt sql 
    name_table = 'Student'
    cursor.execute(f'select * from [{name_table}] order by [Student].old')
    print("Sắp xếp sinh viên theo tuổi")
    # Thêm một số sinh viên vào Treeview
    rows = cursor.fetchall()
    for i in tree.get_children():
        tree.delete(i)
    # Thêm các mục đã được sắp xếp vào treeview
    for row in rows:
            tree.insert('', 'end', values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))
    # Đặt Treeview vào cửa sổ
    tree.place( x = 10, y = 150)
    conn.commit()
# end def
def Sort_By_Lab():
    # ẩn cá label thông báo 
    if ID_Exit is not None:
        ID_Exit.place_forget()
    if t_delete is not None:
        t_delete.place_forget()
    if f_delete is not None:
        f_delete.place_forget()
    # kết nốt sql 
    name_table = 'Student'
    cursor.execute(f'select * from [{name_table}] order by [Student].Lab')
    print("Sắp xếp sinh viên theo điểm LAB")
    rows = cursor.fetchall()
    for i in tree.get_children():
        tree.delete(i)
    # Thêm các mục đã được sắp xếp vào treeview
    for row in rows:
            tree.insert('', 'end', values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))
    # Đặt Treeview vào cửa sổ
    tree.place( x = 10, y = 150)
    conn.commit()
# end def
def Sort_By_AVG():
    # ẩn cá label thông báo 
    if ID_Exit is not None:
        ID_Exit.place_forget()
    if t_delete is not None:
        t_delete.place_forget()
    if f_delete is not None:
        f_delete.place_forget()
    # kết nốt sql 
    name_table = 'Student'
    cursor.execute(f'select * from [{name_table}] order by [Student].Average')
    print("Sắp xếp sinh viên theo điểm Average")
    rows = cursor.fetchall()
    for i in tree.get_children():
        tree.delete(i)
    # Thêm các mục đã được sắp xếp vào treeview
    for row in rows:
            tree.insert('', 'end', values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))
    # Đặt Treeview vào cửa sổ
    tree.place( x = 10, y = 150)
    conn.commit()
# end def

# # # # # # # # # # # # Xóa Sinh viên # # # # # # # # # # # #
# Danh sách để lưu trữ các nút và Entry
def Input_ID_Student_Delete():
    if ID_Exit is not None:
        ID_Exit.place_forget()
    if t_delete is not None:
        t_delete.place_forget()
    if f_delete is not None:
        f_delete.place_forget()
    # đặt các nút còn lại ở chế độ chờ
    menu_button.config(state=tk.DISABLED)
    add_button.config(state=tk.DISABLED)
    # đặt biến toàn cầu 
    global buttons, id_student, exit_button_delete, submit_button_delete 
    buttons = []
    id_student = EntryWithPlaceholder(main, 'ID Student')
    buttons.append(id_student)
    id_student.place(x = 110, y = 110)
    # box submit 
    submit_button_delete = Button(main, text="Xóa", command = Check_ID_Student_Delete)
    buttons.append(submit_button_delete)
    submit_button_delete.place(x = 250, y = 110)
    # tạo nút exit 
    exit_button_delete = Button(main, text="Exit", command = Exit_Delete)
    exit_button_delete.place(x = 300, y = 110)
    print("Xóa sinh viên")
    Tree_View()
# end def
# tạo 2 biến hiển thị của button xóa khi xóa thành công or không 
t_delete = None
f_delete = None
def Check_ID_Student_Delete():
    global t_delete, f_delete
    name_table = 'Student'
    cursor.execute(f'select * from [{name_table}]')
    conn.commit()
    # đặt lại các nút ở chế độ bình thường
    menu_button.config(state = tk.NORMAL)
    add_button.config(state = tk.NORMAL)
    # check code để xóa
    code = id_student.get().upper()
    if not Check_ID(code): # check xem có ID trong danh sách không >> nếu có thì xóa
        cursor.execute(f'delete from [{name_table}] where Student.StudentID = ?', code)
        conn.commit()
        t_delete = Label(main, text = "Đã xóa sinh viên")
        t_delete.place(x = 150, y = 110)
        t_delete.after(2000, t_delete.place_forget)  # Xóa label sau 2 giây
        print("Student deleted successfully.")
    else:
        f_delete = Label(main, text = "Không có sinh viên trong danh sách")
        f_delete.place(x = 150, y = 110)
        f_delete.after(2000, f_delete.place_forget)  # Xóa label sau 2 giây
        print("Student not found.")
    for button in buttons:
        button.place_forget()
    exit_button_delete.place_forget()
    Tree_View()
# end def
def Exit_Delete():
    id_student.destroy()
    submit_button_delete.place_forget()
    exit_button_delete.place_forget()
    # đặt lại các nút
    menu_button.config(state=tk.NORMAL)
    add_button.config(state=tk.NORMAL)
    print("Hủy xóa sinh viên")
    Tree_View()
# end def

# # # # # # # # # # # # TREE VIEW # # # # # # # # # # # #
def Tree_View():
    # Tạo một Treeview
    global tree
    tree = ttk.Treeview(main, show = 'headings')
    # Định nghĩa các cột
    tree["columns"]=("CODE", "NAME", "OLD", 'LAB', "PRACTICE", "ASSIGNMENT", "PRACTICE EXAM", "FINAL EXAM", "AVG", "RANK")

    tree_colunm ={'CODE': 70, "NAME": 150, "OLD": 50, 'LAB': 50, "PRACTICE": 70, "ASSIGNMENT": 80, "PRACTICE EXAM": 100, "FINAL EXAM": 100, "AVG": 50, "RANK": 50}
    # Tạo tiêu đề cho từng cột
    for col, v in tree_colunm.items():
        tree.heading(col, text = col)
        if col == 'NAME':
            tree.heading(col, text = col)
            tree.column(col, width = 150)
        else:
            tree.heading(col, text = col)
            tree.column(col, width = v)

    # Thêm một số sinh viên vào Treeview
    name_table = 'Student'
    cursor.execute(f'select * from [{name_table}]')
    rows = cursor.fetchall()
    for i in tree.get_children():
        tree.delete(i)
    # Thêm các mục đã được sắp xếp vào treeview
    for row in rows:
            tree.insert('', 'end', values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))
    # Đặt Treeview vào cửa sổ
    tree.place( x = 10, y = 150)
    conn.commit()
# end def

# Hiện thị bảng Tree View
Tree_View()

# # # # # # # # # # # # CÁC NÚT # # # # # # # # # # # #
# Nút thêm
add_button = Button(main, text = "Thêm sinh viên", bg = '#EC870E', fg = 'black', command = Add_Student)
add_button.place(x = 10, y = 30)
# Nút sắp xếp
menu_button = tk.Menubutton(main, font = ('Arial', 10), text = "Sắp xếp sinh viên", bg = '#EC870E', fg = 'black', relief = tk.RAISED)
menu_button.place(x = 10, y = 70)
menu = tk.Menu(menu_button, tearoff = False) # hàm 'tearoff' để ngăn không cho các chọn sắp xếp tạo thành 1 cửa sổ khác mà chỉ tạo thành một frame
menu_button['menu'] = menu
menu.add_command(label="OLD", command = Sort_By_Old)
menu.add_command(label="LAB", command = Sort_By_Lab)
menu.add_command(label="AVG", command = Sort_By_AVG)
# Nút xóa
delete_button = Button(main, text= "Xóa sinh viên", bg = '#EC870E', fg = 'black', command = Input_ID_Student_Delete)
delete_button.place(x = 10, y = 110)

# Chạy vòng lặp chính của cửa sổ
main.mainloop()