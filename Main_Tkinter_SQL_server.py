from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
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
name = Label(main, font = ('Times New Roman', 14), text = 'DANH SÁCH CÁC TÙY CHỌN', bg = 'red', fg = 'white') # tiêu đề
# Đặt nhãn vào  cửa sổ
name.pack()
#  Lấy ảnh
# path = r'fpt.jpg'
# load = Image.open(path)
# load = load.resize((300, 200))
# render = ImageTk.PhotoImage(load)
# Đặt vị trí ảnh
# img_label = Label(main, image=render)
# img_label.place(x = 660 , y = 40)
# fpt = Label(main, font = ('Arial', 6), text = 'DIT CON ME', fg = 'grey')
# fpt.place(x = 600,  y = 40)
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

# Tạo list chứa các Label thông báo 
List_Label_Result = []
List_Button_Of_Main = []
# # # # # # # # # # # # # # # # # # # # # # # #  Thêm Sinh viên # # # # # # # # # # # # # # # # # # # # # # # # 
# tạo label hiên thông báo 
Result_Add = None
def Add_Student():
    # # # # # # # # # # # # # Kiểm tra và đóng các Button/ Label trước đó # # # # # # # # # # # #
    # đặt các nút còn lại chế độ chờ
    for button in List_Main_Button :
        button.config(state=tk.DISABLED)
    # ẩn cá label thông báo 
    global List_Label_Result
    for label_result in List_Label_Result:
        if label_result.winfo_exists():
            label_result.place_forget() 
    List_Label_Result = []
    
    # nhập 
    global ID_Student_Add, Name_Add, Old_Add, Lab_Add, PT_Add, Ass_Add, PE_Add, FE_Add, Submit_Add, Exit_Add, List_Entry_Add
    List_Entry_Add = []
    # ID
    ID_Student_Add = EntryWithPlaceholder(main,'ID')
    ID_Student_Add.place(x = 150, y = 30)
    List_Entry_Add.append(ID_Student_Add)
    # NAME
    # Label(main, text = "Name").grid(row = 24, column = 50)
    Name_Add = EntryWithPlaceholder(main,'NAME')
    Name_Add.place(x = 150, y = 70)
    List_Entry_Add.append(Name_Add)
    # OLD
    Old_Add = EntryWithPlaceholder(main, 'OLD')
    Old_Add.place(x = 150, y = 110)
    List_Entry_Add.append(Old_Add)
    # LAB 
    Lab_Add = EntryWithPlaceholder(main, 'LAB')
    Lab_Add.place(x = 300, y = 30)
    List_Entry_Add.append(Lab_Add)
    # PT
    PT_Add = EntryWithPlaceholder(main, 'PRACTICE')
    PT_Add.place(x = 300, y = 70)
    List_Entry_Add.append(PT_Add)
    # ASSIGNMENT
    Ass_Add = EntryWithPlaceholder(main, 'ASSIGNMENT')
    Ass_Add.place(x = 300, y = 110)
    List_Entry_Add.append(Ass_Add)
    # PE
    PE_Add = EntryWithPlaceholder(main, 'PRACTICE EXAM')
    PE_Add.place(x = 300, y = 150)
    List_Entry_Add.append(PE_Add)
    # FE
    FE_Add = EntryWithPlaceholder(main, 'FINAL EXAM')
    FE_Add.place(x = 300, y = 190)
    List_Entry_Add.append(FE_Add)
    # tạo nút submit
    Submit_Add = Button(main, text="Submit", command = Save_Student)
    Submit_Add.place(x = 150, y = 190)
    main.bind('<Return>', lambda event=None: Submit_Add.invoke())
    List_Button_Of_Main.append(Submit_Add)
    # tạo nút exit 
    Exit_Add = Button(main, text="Exit", command = Exit_Add_Student)
    Exit_Add.place(x = 220, y = 190)
    List_Button_Of_Main.append(Exit_Add)
    print("Thêm sinh viên")
# kiểm tra ID khi ADD/ UPDATE/ DELETE
def Check_ID(code):
    # lấy dữ liệu
    name_table = 'Student'
    # Thực thi câu lệnh SQL
    cursor.execute(f'SELECT StudentID FROM {name_table} WHERE StudentID = ?', code) # lấy thông tin của người có cần check 
    # Lấy kết quả truy vấn
    result = cursor.fetchone() # hàm này sẽ thêm những thông tin đó vào result
    if result is not None: 
        return False # ID tồn tại trong danh sách  
    else:   
        return True
# end def
# tạo label hiên thông báo khi nhập tuổi không phải là số
Result_Check_OLD = None
# Lưu vào SQL server
def Save_Student():
    global Result_Add, Result_Check_OLD
    if Result_Check_OLD is not None:
        Result_Check_OLD.place_forget()
    # save file 
    code = ID_Student_Add.get().upper()
    # kiểm tra code đã có trong file chưa
    if Check_ID(code): # check xem có ID trong danh sách không >> nếu không thì nhập 
        name = str(Name_Add.get())
        # try:
        #     if name == 'NAME':
        #         pass  # Add your code here
        # except Exception as e:
        #     Result_Check_Name= Label(main, text = 'Nhập lại tên')
        #     Result_Check_Name.place(x = 150, y = 90)
        #     Result_Check_Name.after(2000, Result_Check_OLD.place_forget)
        old = Old_Add.get()
        # try:
        #     old = int(Old_Add.get())
        # except ValueError:
        #     Result_Check_OLD = Label(main, text = 'Nhập lại tuổi')
        #     Result_Check_OLD.place(x = 150, y = 130)

        if old in ('OLD', 'INPUT', '', 0) or old != int(Old_Add.get()):
            Result_Check_OLD = Label(main, text = 'Nhập lại tuôi')
            Result_Check_OLD.place(x = 150, y = 130)
        else:
            lab = (Lab_Add.get())
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
            Result_Add.after(2000, Result_Add.destroy)
            List_Label_Result.append(Result_Add)
            # lấy dữ liệu từ SQL
            name_table = 'Student'
            cursor.execute(f'select * from [{name_table}] order by [Student].LAB')
            print('Thêm sinh viên thành công')
            Tree_View()
    else:
        Result_Add = Label(main, font = (15), text ='Mã học sinh đã tồn tại')
        Result_Add.place(x = 150, y = 30)
        Result_Add.after(2000, Result_Add.destroy)
        List_Label_Result.append(Result_Add)
        print('Thêm sinh viên không thành công')
        Tree_View()
    # Đóng tất cả các trường nhập
    for entry_add in List_Entry_Add:
        entry_add.destroy()
    # đóng nút submit và exit
    for s_e in List_Button_Of_Main:
        s_e.place_forget()
    # đặt lại các nút chính chế đọ bình thường
    for button_main in List_Main_Button:
        button_main.config(state = tk.NORMAL)
# end def
# tạo nút thoát nếu không muốn thêm sinh viên
def Exit_Add_Student():
    # Đóng tất cả các trường nhập
    for entry_add in List_Entry_Add:
        entry_add.destroy()
    Submit_Add.destroy()
    Exit_Add.destroy()
    # đặt lại các nút chính chế đọ bình thường
    for button_main in List_Main_Button:
        button_main.config(state = tk.NORMAL)
    print("Hủy thêm sinh viên")
# end def
# # # # # # # # # # # # # # # # # # # # # # # # Cập nhập Sinh viên # # # # # # # # # # # # # # # # # # # # # # # # 
Result_Update = None
def Update_Student():
    # đặt các nút còn lại chế độ chờ
    for button in List_Main_Button :
        button.config(state=tk.DISABLED)
    #  đóng các Button/ Label trước đó đã mở 
    # ẩn cá label thông báo 
    global List_Label_Result
    for label_result in List_Label_Result: 
        if label_result.winfo_exists():
            label_result.place_forget() 
    List_Label_Result = []
    global List_Entry_Update, ID_Student_Update, Search_Update, Exit_Search_Update
    List_Entry_Update = []
    ID_Student_Update = EntryWithPlaceholder(main, 'Student ID Search')
    ID_Student_Update.place(x = 150, y = 155)
    List_Entry_Update.append(ID_Student_Update)
    # tạo nút search
    Search_Update = Button(main, text ='Search', command = Check_ID_Update)
    Search_Update.place(x = 300, y = 150)
    main.bind('<Return>', lambda event=None: Search_Update.invoke())
    List_Button_Of_Main.append(Search_Update)
    
    # tạo nút exit 
    Exit_Search_Update = Button(main, text="Exit", command = Exit_Search_Update_Student)
    Exit_Search_Update.place(x = 370, y = 150)
    List_Button_Of_Main.append(Exit_Search_Update)
# end def
# nút này dùng để khi bạn chọn nhưng không muốn update nữa 
def Exit_Search_Update_Student():
    for entry_update in List_Entry_Update:
        entry_update.destroy()
    Search_Update.place_forget()
    Exit_Search_Update.place_forget()
    # đặt lại các nút chính chế đọ bình thường
    for button_main in List_Main_Button:
        button_main.config(state = tk.NORMAL)
# end def
def Check_ID_Update():
    global Result_Update
    code = ID_Student_Update.get().upper()
    if not Check_ID(code): 
        print('Cập nhập sinh viên thành công')
        # nhập 
        global Name_Update, Old_Update, Lab_Update, PT_Update, Ass_Update, PE_Update, FE_Update, Submit_Update, Exit_Update
        # ID
        ID_Student_Update.place(x = 150, y = 30)
        # NAME
        Name_Update = EntryWithPlaceholder(main,'NAME')
        Name_Update.place(x = 150, y = 70)
        List_Entry_Update.append(Name_Update)
        # OLD
        Old_Update = EntryWithPlaceholder(main, 'OLD')
        Old_Update.place(x = 150, y = 110)
        List_Entry_Update.append(Old_Update)
        # LAB 
        Lab_Update = EntryWithPlaceholder(main, 'LAB')
        Lab_Update.place(x = 300, y = 30)
        List_Entry_Update.append(Lab_Update)
        # PT
        PT_Update = EntryWithPlaceholder(main, 'PRACTICE')
        PT_Update.place(x = 300, y = 70)
        List_Entry_Update.append(PT_Update)
        # ASSIGNMENT
        Ass_Update = EntryWithPlaceholder(main, 'ASSIGNMENT')
        Ass_Update.place(x = 300, y = 110)
        List_Entry_Update.append(Ass_Update)
        # PE
        PE_Update = EntryWithPlaceholder(main, 'PRACTICE EXAM')
        PE_Update.place(x = 300, y = 150)
        List_Entry_Update.append(PE_Update)
        # FE
        FE_Update = EntryWithPlaceholder(main, 'FINAL EXAM')
        FE_Update.place(x = 300, y = 190)
        List_Entry_Update.append(FE_Update)
        # tạo nút submit
        Submit_Update = Button(main, text="Submit", command = Save_Update_Student)
        Submit_Update.place(x = 150, y = 190)
        main.bind('<Return>', lambda event=None: Submit_Update.invoke())
        # tạo nút exit 
        Exit_Update = Button(main, text="Exit", command = Exit_Student_Update)
        Exit_Update.place(x = 220, y = 190)
        # đóng nút search và exit 
        Search_Update.place_forget()
        Exit_Search_Update.place_forget()
    else:
        print('Cập nhập sinh viên không thành công')
        ID_Student_Update.destroy()
        Result_Update = Label(main, font = (15), text ='Mã học sinh không có trong danh sách')
        Result_Update.place(x = 150, y = 200)
        Result_Update.after(2000, Result_Update.place_forget)
        List_Label_Result.append(Result_Update)
        # đóng nút search và exit
        Search_Update.place_forget()
        Exit_Search_Update.place_forget()
        # đặt lại các nút chính chế đọ bình thường
        for button_main in List_Main_Button:
            button_main.config(state = tk.NORMAL)
    # cập nhập thông tin 
# end def
def Save_Update_Student():

    # cập nhập thông tin 
    global Result_Update, Result_Check_OLD
    # save file 
    code = ID_Student_Update.get().upper()
    # NAME
    name = Name_Update.get()
    # OLD
    old = int(Old_Update.get())
    # try:
    #     old = int(Old_Update.get())
    # except:
    #         Result_Check_OLD= Label(main, text = 'Nhập lại tuổi')
    #         Result_Check_OLD.place(x = 150, y = 90)
    #         Result_Check_OLD.after(2000, Result_Check_OLD.place_forget)
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
    for entry_update in List_Entry_Update:
        entry_update.destroy()
    Search_Update.place_forget()
    Submit_Update.place_forget()
    Exit_Update.place_forget()
    # Tạo Label thông báo 
    Result_Update = Label(main, font = (15), text ='Cập nhập Sinh viên thành công')
    Result_Update.place(x = 150, y = 200)
    Result_Update.after(2000, Result_Update.place_forget)
    # load lại data
    Tree_View()
    # đặt lại các nút chính chế đọ bình thường
    for button_main in List_Main_Button:
        button_main.config(state = tk.NORMAL)
# end def
def Exit_Student_Update():
    for entry_update in List_Entry_Update:
        entry_update.destroy()
    ID_Student_Update.destroy()
    Submit_Update.destroy()
    Exit_Update.destroy()
    # đặt lại các nút chính chế đọ bình thường
    for button_main in List_Main_Button:
        button_main.config(state = tk.NORMAL)
# # # # # # # # # # # # Sắp xếp sinh viên # # # # # # # # # # # #
def Sort_By_Old():
    # ẩn cá label thông báo 
    global List_Label_Result
    for label_result in List_Label_Result: 
        if label_result is not None:
            label_result.place_forget() 
    List_Label_Result = []
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
    global List_Label_Result
    for label_result in List_Label_Result: 
        if label_result is not None:
            label_result.place_forget() 
    List_Label_Result = []
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
    global List_Label_Result
    for label_result in List_Label_Result: 
        if label_result is not None:
            label_result.place_forget() 
    List_Label_Result = []
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
Result_Delete = None
List_Button_Of_Delete = []
# Danh sách để lưu trữ các nút và Entry
def Input_ID_Student_Delete():
    # đặt các nút chính chế độ chờ
    for button in List_Main_Button :
        button.config(state=tk.DISABLED)
    # ẩn cá label thông báo 
    for label_result in List_Label_Result: 
        if label_result is not None:
            label_result.destroy() 
    # đặt biến toàn cầu 
    global List_Entry_Delete, ID_Student_Delete, Exit_delete, Submit_Delete 
    List_Entry_Delete = []
    ID_Student_Delete = EntryWithPlaceholder(main, 'ID Student')
    List_Entry_Delete.append(ID_Student_Delete)
    ID_Student_Delete.place(x = 110, y = 115)
    # button submit 
    Submit_Delete  = Button(main, text="Submit", command = Result_Student_Delete)
    List_Button_Of_Delete.append(Submit_Delete )
    Submit_Delete .place(x = 250, y = 110)
    main.bind('<Return>', lambda event=None: Submit_Delete.invoke())
    # button exit 
    Exit_delete = Button(main, text="Exit", command = Exit_Delete)
    List_Button_Of_Delete.append(Exit_delete)
    Exit_delete.place(x = 320, y = 110)
    print("Xóa sinh viên")
# end def
def Result_Student_Delete():
    global Result_Delete 
    name_table = 'Student'
    cursor.execute(f'select * from [{name_table}]')
    conn.commit()
    # check code để xóa
    code = ID_Student_Delete.get().upper()
    if not Check_ID(code): # check xem có ID trong danh sách không >> nếu có thì xóa
        print("Student deleted successfully.")
        cursor.execute(f'delete from [{name_table}] where Student.StudentID = ?', code)
        conn.commit()
        # Tạo Label thông báo 
        Result_Delete = Label(main, text = "Đã xóa sinh viên")
        Result_Delete.place(x = 150, y = 110)
        Result_Delete.after(2000, Result_Delete.place_forget)  # Xóa label sau 2 giây
        List_Label_Result.append(Result_Delete)
    else:
        print("Student not found.")
        # Tạo Label thông báo 
        Result_Delete = Label(main, font = (15), text = "Không có sinh viên trong danh sách")
        Result_Delete.place(x = 150, y = 110)
        Result_Delete.after(2000, Result_Delete.place_forget)  # Xóa label sau 2 giây
        List_Label_Result.append(Result_Delete)
    # đóng các entry 
    for button in List_Entry_Delete:
        button.place_forget()
    # đóng nút submit và exit 
    for s_e in List_Button_Of_Delete:
        s_e.place_forget()
    # đặt các nút chính về chế độ bình thường
    for button in List_Main_Button :
        button.config(state=tk.NORMAL)
    Tree_View()
# end def
def Exit_Delete():
    ID_Student_Delete.destroy()
    Submit_Delete.place_forget()
    Exit_delete.place_forget()
    # đặt các nút chính chế độ chờ
    for button in List_Main_Button :
        button.config(state = tk.NORMAL)
    print("Hủy xóa sinh viên")
    Tree_View()
# end def

# # # # # # # # # # # # Tìm kiếm sinh viên # # # # # # # # # # # #
Result_Find = None
List_Entry_Search = []
Result_Find_Check = None
# OLD
def Input_Old_Student_Find():
    # đặt các nút chính chế độ chờ
    for button in List_Main_Button :
        button.config(state=tk.DISABLED)
    # ẩn cá label thông báo 
    global List_Label_Result
    for label_result in List_Label_Result: 
        if label_result is not None:
            label_result.place_forget() 
    List_Label_Result = []
    # đặt biến toàn cầu 
    global Student_Find, Exit_Find, Submit_Find 
    Student_Find = EntryWithPlaceholder(main, 'Old')
    List_Entry_Search.append(Student_Find)
    Student_Find.place(x = 150, y = 195)
    Submit_Find = Button(main, text = 'Search', command = Result_Find_Student_Old)
    Submit_Find.place( x = 290, y = 190)
    Exit_Find = Button(main, text = 'Exit', command = Exit_Find_Student)
    Exit_Find.place( x = 350, y = 190)
# end def
def Result_Find_Student_Old():
    global Result_Find_Check
    if Result_Find_Check is not None:
        Result_Find_Check.place_forget()
    # ẩn cá label thông báo 
    global List_Label_Result
    for label_result in List_Label_Result: 
        if label_result is not None:
            label_result.place_forget() 
    List_Label_Result = []
    # tìm kiếm 
    Old = Student_Find.get()
    try:
        Old = int(Student_Find.get())
    except ValueError:
        Result_Find_Check = Label(main, text = 'Nhập lại tuổi')
        Result_Find_Check.place(x = 150, y = 220)
        Result_Find_Check.after(5000, Result_Find_Check.place_forget)

    if Old in ('OLD', 'INPUT', '', 0) or Old != int(Student_Find.get()):
        Result_Find_Check = Label(main, text = 'Nhập lại tuổi')
        Result_Find_Check.place(x = 150, y = 220)
        Result_Find_Check.after(5000, Result_Find_Check.place_forget)
    else:
        # if Result_Find_Check_OLD is not None:
        #     Result_Find_Check_OLD.place_forget()
        # kết nối SQL server
        cursor.execute('SELECT * FROM Student where [Student].Old = ?',(Old))
        rows = cursor.fetchall()
        if len(rows) == 0:
            Result_Find = Label(main, font=("Arial", 15), text = "Không có sinh viên", fg = 'grey')
            Result_Find.place(x = 400, y = 190)
            # Result_Find.after(2000, Result_Find.place_forget)
            List_Label_Result.append(Result_Find)
            for i in tree.get_children():
                tree.delete(i)
            # Thêm các mục đã được sắp xếp vào treeview
            for row in rows:
                    tree.insert('', 'end', values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))
            # Đặt Treeview vào cửa sổ
            tree.place( x = 10, y = 250, width = 980, height = 300)
        else:
            for i in tree.get_children():
                tree.delete(i)
            # Thêm các mục đã được sắp xếp vào treeview
            for row in rows:
                    tree.insert('', 'end', values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))
            # Đặt Treeview vào cửa sổ
            tree.place( x = 10, y = 250, width = 980, height = 300)
        conn.commit()
# end def
def Input_Lab_Student_Find():
    # đặt các nút chính chế độ chờ
    for button in List_Main_Button :
        button.config(state=tk.DISABLED)
    # ẩn cá label thông báo 
    global List_Label_Result
    for label_result in List_Label_Result: 
        if label_result is not None:
            label_result.place_forget() 
    List_Label_Result = []
    # đặt biến toàn cầu 
    global Student_Find, Exit_Find, Submit_Find 
    Student_Find = EntryWithPlaceholder(main, 'LAB')
    List_Entry_Search.append(Student_Find)
    Student_Find.place(x = 150, y = 195)
    Submit_Find = Button(main, text = 'Search', command = Result_Find_Student_Lab)
    Submit_Find.place( x = 290, y = 190)
    Exit_Find = Button(main, text = 'Exit', command = Exit_Find_Student)
    Exit_Find.place( x = 350, y = 190)
# end def
def Result_Find_Student_Lab():
    global Result_Find_Check
    if Result_Find_Check is not None:
        Result_Find_Check.place_forget()
    # ẩn cá label thông báo 
    global List_Label_Result
    for label_result in List_Label_Result: 
        if label_result is not None:
            label_result.place_forget() 
    List_Label_Result = []
    # tìm kiếm 
    lab = Student_Find.get()
    try:
        lab = int(Student_Find.get())
    except ValueError:
        Result_Find_Check = Label(main, text = 'Nhập lại điểm')
        Result_Find_Check.place(x = 150, y = 220)
        Result_Find_Check.after(5000, Result_Find_Check.place_forget)

    if lab in ('AVG', 'INPUT', '', 0) or lab != int(Student_Find.get()):
        Result_Find_Check = Label(main, text = 'Nhập lại điểm')
        Result_Find_Check.place(x = 150, y = 220)
        Result_Find_Check.after(5000, Result_Find_Check.place_forget)
    else:
        # if Result_Find_Check_AVG is not None:
        #     Result_Find_Check_AVG.place_forget()
        # kết nối SQL server
        cursor.execute('SELECT * FROM Student where [Student].Average = ?',(lab))
        rows = cursor.fetchall()
        if len(rows) == 0:
            Result_Find = Label(main, font=("Arial", 15), text = "Không có sinh viên", fg = 'grey')
            Result_Find.place(x = 400, y = 190)
            # Result_Find.after(2000, Result_Find.place_forget)
            List_Label_Result.append(Result_Find)
            for i in tree.get_children():
                tree.delete(i)
            # Thêm các mục đã được sắp xếp vào treeview
            for row in rows:
                    tree.insert('', 'end', values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))
            # Đặt Treeview vào cửa sổ
            tree.place( x = 10, y = 250, width = 980, height = 300)
        else:
            for i in tree.get_children():
                tree.delete(i)
            # Thêm các mục đã được sắp xếp vào treeview
            for row in rows:
                    tree.insert('', 'end', values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))
            # Đặt Treeview vào cửa sổ
            tree.place( x = 10, y = 250, width = 980, height = 300)
        conn.commit()
# end def
def Input_Student_Find():
    # đặt các nút chính chế độ chờ
    for button in List_Main_Button :
        button.config(state=tk.DISABLED)
    # ẩn cá label thông báo 
    global List_Label_Result
    for label_result in List_Label_Result: 
        if label_result is not None:
            label_result.place_forget() 
    List_Label_Result = []
    # đặt biến toàn cầu 
    global Student_Find, Exit_Find, Submit_Find 
    Student_Find = EntryWithPlaceholder(main, 'AVG')
    List_Entry_Search.append(Student_Find)
    Student_Find.place(x = 150, y = 195)
    Submit_Find = Button(main, text = 'Search', command = Result_Find_Student_AVG)
    Submit_Find.place( x = 290, y = 190)
    Exit_Find = Button(main, text = 'Exit', command = Exit_Find_Student)
    Exit_Find.place( x = 350, y = 190)
# end def
def Result_Find_Student_AVG():
    global Result_Find_Check
    if Result_Find_Check is not None:
        Result_Find_Check.place_forget()
    # ẩn cá label thông báo 
    global List_Label_Result
    for label_result in List_Label_Result: 
        if label_result is not None:
            label_result.place_forget() 
    List_Label_Result = []
    # tìm kiếm 
    avg = Student_Find.get()
    try:
        avg = int(Student_Find.get())
    except ValueError:
        Result_Find_Check = Label(main, text = 'Nhập lại điểm')
        Result_Find_Check.place(x = 150, y = 220)
        Result_Find_Check.after(5000, Result_Find_Check.place_forget)

    if avg in ('AVG', 'INPUT', '', 0) or avg != int(Student_Find.get()):
        Result_Find_Check = Label(main, text = 'Nhập lại điểm')
        Result_Find_Check.place(x = 150, y = 220)
        Result_Find_Check.after(5000, Result_Find_Check.place_forget)
    else:
        # if Result_Find_Check_AVG is not None:
        #     Result_Find_Check_AVG.place_forget()
        # kết nối SQL server
        cursor.execute('SELECT * FROM Student where [Student].Average = ?',(avg))
        rows = cursor.fetchall()
        if len(rows) == 0:
            Result_Find = Label(main, font=("Arial", 15), text = "Không có sinh viên", fg = 'grey')
            Result_Find.place(x = 400, y = 190)
            # Result_Find.after(2000, Result_Find.place_forget)
            List_Label_Result.append(Result_Find)
            for i in tree.get_children():
                tree.delete(i)
            # Thêm các mục đã được sắp xếp vào treeview
            for row in rows:
                    tree.insert('', 'end', values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))
            # Đặt Treeview vào cửa sổ
            tree.place( x = 10, y = 250, width = 980, height = 300)
        else:
            for i in tree.get_children():
                tree.delete(i)
            # Thêm các mục đã được sắp xếp vào treeview
            for row in rows:
                    tree.insert('', 'end', values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))
            # Đặt Treeview vào cửa sổ
            tree.place( x = 10, y = 250, width = 980, height = 300)
        conn.commit()
# end def
def Exit_Find_Student():
    # ẩn cá label thông báo 
    global List_Label_Result
    for label_result in List_Label_Result: 
        if label_result is not None:
            label_result.place_forget() 
    List_Label_Result = []
    for label in List_Entry_Search:
            label.place_forget()
    Submit_Find.place_forget()
    Exit_Find.place_forget()
    # đặt các nút còn lại chế độ chờ
    for button in List_Main_Button :
        button.config(state=tk.NORMAL)
    Tree_View()


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
# list chứa các nút chính
List_Main_Button = []
# Nút thêm
Add_Button = Button(main, text = "Thêm sinh viên", bg = '#EC870E', fg = 'black', command = Add_Student)
Add_Button.place(x = 10, y = 30)
List_Main_Button.append(Add_Button)
# Nút sắp xếp
Sort_Button = tk.Menubutton(main, font = ('Arial', 10), text = "Sắp xếp sinh viên", bg = '#EC870E', fg = 'black', relief = tk.RAISED)
Sort_Button.place(x = 10, y = 70)
List_Main_Button.append(Sort_Button)
menu_sort = tk.Menu(Sort_Button, tearoff = False) # hàm 'tearoff' để ngăn không cho các chọn sắp xếp tạo thành 1 cửa sổ khác mà chỉ tạo thành một frame
Sort_Button['menu'] = menu_sort
menu_sort.add_command(label="OLD", command = Sort_By_Old)
menu_sort.add_command(label="LAB", command = Sort_By_Lab)
menu_sort.add_command(label="AVG", command = Sort_By_AVG)
# Nút xóa
Delete_Button = Button(main, text= "Xóa sinh viên", bg = '#EC870E', fg = 'black', command = Input_ID_Student_Delete)
Delete_Button.place(x = 10, y = 110)
List_Main_Button.append(Delete_Button)
# Nút Update
Update_Button = Button(main, text= "Cập nhập sinh viên", bg = '#EC870E', fg = 'black', command = Update_Student)
Update_Button.place(x = 10, y = 150)
List_Main_Button.append(Update_Button)
# Nút Find
Find_Button = tk.Menubutton(main, font = ('Arial', 10), text = "Tìm kiếm sinh viên", bg = '#EC870E', fg = 'black', relief = tk.RAISED)
Find_Button.place(x = 10, y = 190)
List_Main_Button.append(Find_Button)
menu_find = tk.Menu(Find_Button, tearoff = False)
Find_Button['menu'] = menu_find
menu_find.add_command(label="OLD", command = Input_Old_Student_Find)
menu_find.add_command(label="LAB", command = Input_Student_Find)
menu_find.add_command(label="AVG", command = Input_Student_Find)


print('START')
main.mainloop()
print('END')
if __name__ == '__main__':
    pass