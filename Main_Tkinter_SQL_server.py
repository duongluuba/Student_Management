from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
import math
import math
import pyodbc 
import os 
def Connect_SQL():
    global cursor, conn
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
Connect_SQL()
############################### Tạo Tkinter ###############################
main = Tk()
main.title('QUẢN LÝ SINH VIÊN')
# Lấy kích thước màn hình
# screen_width = main.winfo_screenwidth()
# screen_height = main.winfo_screenheight()
# Đặt kích thước và vị trí của cửa sổ
# main.geometry(f'1000x600+{screen_width//2-150}+{screen_height//2-100}')
main.geometry(f'1000x600+0+0')
# main.iconbitmap('') # hàm này để lấy file ảnh đặt làm icon cho title, file ảnh có type ICON 
# main.attributes('-topmost', False) # hàm này được sử dụng để thay đổi các thuộc tính của cửa sổ, đặt cửa sổ này trên tất cả các cửa sổ khác 
# Tiêu đề 
name = Label(main, font = ('Arial', 14), text = 'DANH SÁCH CÁC TÙY CHỌN', bg = 'red', fg = 'white') # tiêu đề
# Đặt nhãn vào  cửa sổ
name.pack()
#  Lấy ảnh
path = r'fpt.jpg'
load = Image.open(path)
load = load.resize((300, 200))
render = ImageTk.PhotoImage(load)
# Đặt vị trí ảnh
img_label = Label(main, image=render)
img_label.place(x = 660 , y = 40)
fpt = Label(main, font = ('Arial', 6), text = 'DIT CON ME', fg = 'grey')
fpt.place(x = 600,  y = 40)
# tạo class dùng để hiện phần gợi ý trong mỗi button
class EntryWithPlaceholder(Entry):
        def __init__(self, master = None, placeholder = "INPUT", color = 'grey'):
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
            # elif self.get() == self.placeholder:
            #     self.delete('0', 'end')
            #     self.insert(0, '0')

# # # # # # # # # # # # Thêm Sinh viên # # # # # # # # # # # #
def Add_Student():
    # Kiểm tra và đóng các Button/ Label trước đó 
    if Result_Add is not None:
        Result_Add.place_forget()
    if Result_Delete is not None:
        Result_Delete.place_forget()
    if Result_Update is not None:
        Result_Update.place_forget()
    # đặt các nút còn lại chế độ chờ
    Main_Button.config(state=tk.DISABLED)
    Delete_Button.config(state=tk.DISABLED)
    Update_Button.config(state=tk.DISABLED)
    # nhập 
    global ID_Student_Add, Name_Add, Old_Add, Lab_Add, PT_Add, Ass_Add, PE_Add, FE_Add, Submit_Add, Exit_Add
    ID_Student_Add = EntryWithPlaceholder(main,'ID')
    ID_Student_Add.place(x = 150, y = 30)
    # Label(main, text = "Name").grid(row = 24, column = 50)
    Name_Add = EntryWithPlaceholder(main,'NAME')
    Name_Add.place(x = 150, y = 50)
    # Label(main, text = "Old").grid(row = 28, column = 50)
    Old_Add = EntryWithPlaceholder(main, 'OLD')
    Old_Add.place(x = 150, y = 70)
    # LAB 
    Lab_Add = EntryWithPlaceholder(main, 'LAB')
    Lab_Add.place(x = 300, y = 30)
    # PT
    PT_Add = EntryWithPlaceholder(main, 'PRACTICE')
    PT_Add.place(x = 300, y = 50)
    # ASSIGNMENT
    Ass_Add = EntryWithPlaceholder(main, 'ASSIGNMENT')
    Ass_Add.place(x = 300, y = 70)
    # PE
    PE_Add = EntryWithPlaceholder(main, 'PRACTICE EXAM')
    PE_Add.place(x = 300, y = 90)
    # FE
    FE_Add = EntryWithPlaceholder(main, 'FINAL EXAM')
    FE_Add.place(x = 300, y = 110)
    # tạo nút submit
    Submit_Add = Button(main, text="Submit", command = Save_Student)
    Submit_Add.place(x = 150, y = 110)
    # tạo nút exit 
    Exit_Add = Button(main, text="Exit", command = Exit_Add_Student)
    Exit_Add.place(x = 220, y = 110)
    print("Thêm sinh viên")
# kiểm tra ID khi ADD/ UPDATE/ DELETE
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
Result_Add = None
# tạo label hiên thông báo khi nhập tuổi không phải là số
Result_Check_OLD = None
# Lưu vào SQL server
def Save_Student():
    global Result_Add, Result_Check_OLD
    # save file 
    code = ID_Student_Add.get().upper()
    # kiểm tra code đã có trong file chưa
    if Check_ID(code): # check xem có ID trong danh sách không >> nếu không thì nhập 
        name = Name_Add.get()
        try:
            old = int(Old_Add.get())
        except:
                Result_Check_OLD= Label(main, text = 'Nhập lại tuổi')
                Result_Check_OLD.place(x = 150, y = 90)
                Result_Check_OLD.after(2000, Result_Check_OLD.place_forget)
        lab = (Lab_Add.get())
        # Xử lý các trường hợp nếu không nhập gì vào thì giá trị mặc định là 0
        if lab == 'LAB': 
            lab = 0
        pt = (PT_Add.get())
        if pt == 'PRACTICE':
            pt = 0
        assignment = (Ass_Add.get())
        if  assignment == 'ASSIGNMENT':
            assignment = 0
        pe = (PE_Add.get())
        if pe == 'PRACTICE EXAM':
            pe = 0
        fe = FE_Add.get()
        if fe == 'FINAL EXAM':
            fe = 0

        # tính điểm trung bình 
        avg = math.ceil( ( (float(lab) * 0.1) + (float(pt) * 0.1) + (float(assignment) * 0.2) + (float(pe) * 0.3) + (float(fe) * 0.3)) * 100 ) / 100
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
        cursor.execute('INSERT INTO Student (StudentID, Student_Name, [Old], [Lab], [Practice], [Assignment], [Practice Exam], [Final Exam], [Average], [Rank]) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?) ', code, name, old, lab, pt, assignment, pe, pt, avg, rank)
        conn.commit()
        # end 
        Result_Add = Label(main, font = 15, text ='Thêm Sinh viên thành công')
        Result_Add.place(x = 150, y = 30)
        Result_Add.after(2000, Result_Add.place_forget)
        # lấy dữ liệu từ SQL
        name_table = 'Student'
        cursor.execute(f'select * from [{name_table}] order by [Student].LAB')
        print('Thêm sinh viên thành công')
        Tree_View()
    else:
        Result_Add = Label(main, font = (15), text ='Mã học sinh đã tồn tại')
        Result_Add.place(x = 150, y = 30)
        Result_Add.after(2000, Result_Add.place_forget)
        print('Thêm sinh viên không thành công')
        Tree_View()
    # Đóng tất cả các trường nhập
    ID_Student_Add.destroy()
    Name_Add.destroy()
    Old_Add.destroy()
    Lab_Add.destroy()
    PT_Add.destroy()
    Ass_Add.destroy()
    PE_Add.destroy()
    FE_Add.destroy()
    Submit_Add.place_forget()
    Exit_Add.place_forget()
    # đặt lại các nút
    Main_Button.config(state=tk.NORMAL)
    Update_Button.config(state=tk.NORMAL)
    Delete_Button.config(state=tk.NORMAL)
# end def
# tạo nút hủy để đóng các button thêm sinh viên
def Exit_Add_Student():
    ID_Student_Add.destroy()
    Name_Add.destroy()
    Old_Add.destroy()
    Lab_Add.destroy()
    PT_Add.destroy()
    Ass_Add.destroy()
    PE_Add.destroy()
    FE_Add.destroy()
    Submit_Add.place_forget()
    Exit_Add.place_forget()
    # đặt lại các nút
    Main_Button.config(state=tk.NORMAL)
    Update_Button.config(state=tk.NORMAL)
    Delete_Button.config(state=tk.NORMAL)
    print("Hủy thêm sinh viên")
# end def
# # # # # # # # # # # # Cập nhập Sinh viên # # # # # # # # # # # #
def Update_Student():
    #  đóng các Button/ Label trước đó đã mở 
    if Result_Add is not None:
        Result_Add.place_forget()
    if Result_Delete is not None:
        Result_Delete.place_forget()
    if Result_Update is not None:
        Result_Update.place_forget()
    Main_Button.config(state=tk.DISABLED)
    Add_Button.config(state=tk.DISABLED)
    Delete_Button.config(state=tk.DISABLED)
    global ID_Student_Update, Search_Update
    ID_Student_Update = EntryWithPlaceholder(main, 'Student ID Search')
    ID_Student_Update.place(x = 150, y = 30)
    Search_Update = Button(main, text ='Search', command = Check_ID_Update)
    Search_Update.place(x = 300, y = 30)

Result_Update = None
def Check_ID_Update():
    global Name_Update, Old_Update, Lab_Update, PT_Update, PE_Update, Ass_Update, FE_Update, Result_Update, Exit_Update, Submit_Update
    code = ID_Student_Update.get().upper()
    if not Check_ID(code): 
        # Label(main, text = "Name").grid(row = 24, column = 50)
        Name_Update = EntryWithPlaceholder(main,'NAME')
        Name_Update.place(x = 150, y = 50)
        # Label(main, text = "Old").grid(row = 28, column = 50)
        Old_Update = EntryWithPlaceholder(main, 'OLD')
        Old_Update.place(x = 150, y = 70)
        # LAB 
        Lab_Update = EntryWithPlaceholder(main, 'LAB')
        Lab_Update.place(x = 300, y = 30)
        # PT
        PT_Update = EntryWithPlaceholder(main, 'PRACTICE')
        PT_Update.place(x = 300, y = 50)
        # ASSIGNMENT
        Ass_Update = EntryWithPlaceholder(main, 'ASSIGNMENT')
        Ass_Update.place(x = 300, y = 70)
        # PE
        PE_Update = EntryWithPlaceholder(main, 'PRACTICE EXAM')
        PE_Update.place(x = 300, y = 90)
        # FE
        FE_Update = EntryWithPlaceholder(main, 'FINAL EXAM')
        FE_Update.place(x = 300, y = 110)
        # tạo nút submit
        Submit_Update = Button(main, text="Submit", command = Save_Update_Student)
        Submit_Update.place(x = 150, y = 110)
        # tạo nút exit 
        Exit_Update = Button(main, text="Exit", command = Exit_Student_Update)
        Exit_Update.place(x = 220, y = 110)
        # đóng nút search 
        Search_Update.place_forget()
    else:
        ID_Student_Update.destroy()
        Result_Update = Label(main, font = (15), text ='Mã học sinh không có trong danh sách')
        Result_Update.place(x = 150, y = 200)
        Result_Update.after(2000, Result_Update.place_forget)
        # đóng nút search 
        Search_Update.place_forget()
        print('Cập nhập sinh viên không thành công')
def Save_Update_Student():
    # cập nhập thông tin 
    global Result_Update, Result_Check_OLD
    # save file 
    code = ID_Student_Update.get().upper()
    name = Name_Update.get()
    try:
        old = int(Old_Update.get())
    except:
            Result_Check_OLD= Label(main, text = 'Nhập lại tuổi')
            Result_Check_OLD.place(x = 150, y = 90)
            Result_Check_OLD.after(2000, Result_Check_OLD.place_forget)
    lab = (Lab_Update.get())
    # Xử lý các trường hợp nếu không nhập gì vào thì giá trị mặc định là 0
    if lab == 'LAB': 
        lab = 0
    pt = (PT_Update.get())
    if pt == 'PRACTICE':
        pt = 0
    assignment = (Ass_Update.get())
    if  assignment == 'ASSIGNMENT':
        assignment = 0
    pe = (PE_Update.get())
    if pe == 'PRACTICE EXAM':
        pe = 0
    fe = FE_Update.get()
    if fe == 'FINAL EXAM':
        fe = 0

    # tính điểm trung bình 
    avg = math.ceil( ( (float(lab) * 0.1) + (float(pt) * 0.1) + (float(assignment) * 0.2) + (float(pe) * 0.3) + (float(fe) * 0.3)) * 100 ) / 100
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
    cursor.execute('UPDATE Student SET StudentID = ?, Student_Name = ?, [Old]= ?, [Lab]= ?, [Practice]= ?, [Assignment]= ?, [Practice Exam]= ?, [Final Exam]= ?, [Average]= ?, [Rank]= ? WHERE StudentID = ?', (code, name, old, lab, pt, assignment, pe, pt, avg, rank, code))
    # Lưu thay đổi
    conn.commit()
    Search_Update.place_forget()
    ID_Student_Update.destroy()
    Name_Update.destroy()
    Old_Update.destroy()
    Lab_Update.destroy()
    PT_Update.destroy()
    Ass_Update.destroy()
    PE_Update.destroy()
    FE_Update.destroy()
    Search_Update.place_forget()
    Submit_Update.place_forget()
    Exit_Update.place_forget()
    Result_Update = Label(main, font = (15), text ='Cập nhập Sinh viên thành công')
    Result_Update.place(x = 150, y = 200)
    Result_Update.after(2000, Result_Update.place_forget)
    # load lại data
    Tree_View()
    # đạt lại các nút chế độ bình thường
    Main_Button.config(state = tk.NORMAL)
    Add_Button.config(state = tk.NORMAL)
    Delete_Button.config(state = tk.NORMAL)
def Exit_Student_Update():
    ID_Student_Update.destroy()
    Name_Update.destroy()
    Old_Update.destroy()
    Lab_Update.destroy()
    PT_Update.destroy()
    Ass_Update.destroy()
    PE_Update.destroy()
    FE_Update.destroy()
    Search_Update.place_forget()
    Submit_Update.place_forget()
    Exit_Update.place_forget()
    # đặt lại các nút ở chế độ bình thường
    Main_Button.config(state = tk.NORMAL)
    Add_Button.config(state = tk.NORMAL)
    Delete_Button.config(state = tk.NORMAL)
# # # # # # # # # # # # Sắp xếp sinh viên # # # # # # # # # # # #
def Sort_By_Old():
    # ẩn cá label thông báo 
    if Result_Add is not None:
        Result_Add.place_forget()
    if Result_Delete is not None:
        Result_Delete.place_forget()
    if Result_Update is not None:
        Result_Update.place_forget()
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
    tree.place( x = 10, y = 250, width = 980, height = 300)
    conn.commit()
# end def
def Sort_By_Lab():
    # ẩn cá label thông báo 
    if Result_Add is not None:
        Result_Add.place_forget()
    if Result_Delete is not None:
        Result_Delete.place_forget()
    if Result_Update is not None:
        Result_Update.place_forget()
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
    tree.place( x = 10, y = 250, width = 980, height = 300)
    conn.commit()
# end def
def Sort_By_AVG():
    # ẩn cá label thông báo 
    if Result_Add is not None:
        Result_Add.place_forget()
    if Result_Delete is not None:
        Result_Delete.place_forget()
    if Result_Update is not None:
        Result_Update.place_forget()
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
    tree.place( x = 10, y = 250, width = 980, height = 300)
    conn.commit()
# end def

# # # # # # # # # # # # Xóa Sinh viên # # # # # # # # # # # #
# Danh sách để lưu trữ các nút và Entry
def Input_ID_Student_Delete():
    # ẩn cá label thông báo 
    if Result_Add is not None:
        Result_Add.place_forget()
    if Result_Delete is not None:
        Result_Delete.place_forget()
    if Result_Update is not None:
        Result_Update.place_forget()
    # đặt các nút còn lại ở chế độ chờ
    Main_Button.config(state=tk.DISABLED)
    Add_Button.config(state=tk.DISABLED)
    Update_Button.config(state=tk.DISABLED)
    # đặt biến toàn cầu 
    global List_Button_Delete, ID_Student_Delete, Exit_Add_delete, Submit_Add_delete 
    List_Button_Delete = []
    ID_Student_Delete = EntryWithPlaceholder(main, 'ID Student')
    List_Button_Delete.append(ID_Student_Delete)
    ID_Student_Delete.place(x = 110, y = 115)
    # box submit 
    Submit_Add_delete = Button(main, text="Submit", command = Check_ID_Student_Delete)
    List_Button_Delete.append(Submit_Add_delete)
    Submit_Add_delete.place(x = 250, y = 110)
    # tạo nút exit 
    Exit_Add_delete = Button(main, text="Exit", command = Exit_Delete)
    List_Button_Delete.append(Exit_Add_delete)
    Exit_Add_delete.place(x = 320, y = 110)
    print("Xóa sinh viên")
    Tree_View()
# end def
# tạo  biến hiển thị kết quả khi xóa thành công or không 
Result_Delete = None
def Check_ID_Student_Delete():
    # đặt lại các nút ở chế độ bình thường
    Main_Button.config(state = tk.NORMAL)
    Add_Button.config(state = tk.NORMAL)
    Update_Button.config(state=tk.NORMAL)
    global Result_Delete
    name_table = 'Student'
    cursor.execute(f'select * from [{name_table}]')
    conn.commit()
    # check code để xóa
    code = ID_Student_Delete.get().upper()
    if not Check_ID(code): # check xem có ID trong danh sách không >> nếu có thì xóa
        cursor.execute(f'delete from [{name_table}] where Student.StudentID = ?', code)
        conn.commit()
        Result_Delete = Label(main, text = "Đã xóa sinh viên")
        Result_Delete.place(x = 150, y = 110)
        Result_Delete.after(2000, Result_Delete.place_forget)  # Xóa label sau 2 giây
        print("Student deleted successfully.")
    else:
        Result_Delete = Label(main, font = (15), text = "Không có sinh viên trong danh sách")
        Result_Delete.place(x = 150, y = 110)
        Result_Delete.after(2000, Result_Delete.place_forget)  # Xóa label sau 2 giây
        print("Student not found.")
    for button in List_Button_Delete:
        button.place_forget()
    Tree_View()
# end def
def Exit_Delete():
    ID_Student_Delete.destroy()
    Submit_Add_delete.place_forget()
    Exit_Add_delete.place_forget()
    # đặt lại các nút
    Main_Button.config(state=tk.NORMAL)
    Add_Button.config(state=tk.NORMAL)
    Update_Button.config(state=tk.NORMAL)
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
    tree.place( x = 10, y = 250, width = 980, height = 300)
    conn.commit()
# end def

# Hiện thị bảng Tree View
Tree_View()

# # # # # # # # # # # # CÁC NÚT # # # # # # # # # # # #
# Nút thêm
Add_Button = Button(main, text = "Thêm sinh viên", bg = '#EC870E', fg = 'black', command = Add_Student)
Add_Button.place(x = 10, y = 30)
# Nút sắp xếp
Main_Button = tk.Menubutton(main, font = ('Arial', 10), text = "Sắp xếp sinh viên", bg = '#EC870E', fg = 'black', relief = tk.RAISED)
Main_Button.place(x = 10, y = 70)
menu = tk.Menu(Main_Button, tearoff = False) # hàm 'tearoff' để ngăn không cho các chọn sắp xếp tạo thành 1 cửa sổ khác mà chỉ tạo thành một frame
Main_Button['menu'] = menu
menu.add_command(label="OLD", command = Sort_By_Old)
menu.add_command(label="LAB", command = Sort_By_Lab)
menu.add_command(label="AVG", command = Sort_By_AVG)
# Nút xóa
Delete_Button = Button(main, text= "Xóa sinh viên", bg = '#EC870E', fg = 'black', command = Input_ID_Student_Delete)
Delete_Button.place(x = 10, y = 110)
# Nút Update
Update_Button = Button(main, text= "Cập nhập sinh viên", bg = '#EC870E', fg = 'black', command = Update_Student)
Update_Button.place(x = 10, y = 150)
# Chạy vòng lặp chính của cửa sổ
main.mainloop()


