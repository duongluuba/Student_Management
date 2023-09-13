from Student import Student
from tkinter import *
from tkinter import ttk
import tkinter as tk
import math
main = Tk()
main.title('QUẢN LÝ SINH VIÊN')
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
def add_student():
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
    submit_button = Button(main, text="Submit", command = save_student_file)
    submit_button.place(x = 150, y = 110)
    # tạo nút exit 
    exit_button = Button(main, text="Exit", command = exit_button_add)
    exit_button.place(x = 220, y = 110)
    print("Thêm sinh viên")
# Lưu vào file
def save_student_file():
    # save file 
    code = id_entry.get().upper()
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
    st = Student(code, name, old, lab, pt, assignment, pe, fe, avg, rank)
    with open('PFP191.txt','a', encoding='utf-8-sig') as file :
        file.write(f'{st.code}\t{st.name}\t{st.old}\t{st.lab}\t{st.pt}\t{st.assignment}\t{st.pe}\t{st.fe}\t{st.avg}\t{st.rank}\n')

    list_student = read_file()
    write_file(list_student)
    for i in tree.get_children():
        tree.delete(i)
    # Thêm các mục đã được sắp xếp vào treeview
    for student in list_student:
        tree.insert('', 'end', values=(student.code, student.name, student.old, student.lab,
                                student.pt, student.assignment, student.pe,
                                student.fe, student.avg, student.rank))
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
    # đặt lại các nút
    menu_button.config(state=tk.NORMAL)
    delete_button.config(state=tk.NORMAL)
# end def
# tạo nút hủy thêm sinh viên
def exit_button_add():
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


# # # # # # # # # # # # Sắp xếp sinh viên # # # # # # # # # # # #
def read_file():
    list_sv = []
    try:
        with open('PFP191.txt','r', encoding='utf-8-sig') as file:
            for line in file:
                code, name, old, lab, pt, assignment, pe, fe, avg, rank = line.strip().split('\t')
                list_sv.append(Student(code, name, old, lab, pt, assignment, pe, fe, avg, rank))
    except FileNotFoundError:
        file = open('PFP191.txt','w', encoding='utf-8-sig') 
        file.close()
    return list_sv
# end def
def write_file(list_student):
    with open('PFP191.txt','w', encoding='utf-8-sig') as file:
        for st in list_student:
            file.write(f'{st.code}\t{st.name}\t{st.old}\t{st.lab}\t{st.pt}\t{st.assignment}\t{st.pe}\t{st.fe}\t{st.avg}\t{st.rank}\n')
    file.close()
# end def
def sort_by_old():
    list_student = read_file()
    list_student.sort(key = lambda x: int(x.old), reverse = True)
    write_file(list_student)
    for i in tree.get_children():
        tree.delete(i)
    # Thêm các mục đã được sắp xếp vào treeview
    for student in list_student:
        tree.insert('', 'end', values=(student.code, student.name, student.old, student.lab,
                                student.pt, student.assignment, student.pe,
                                student.fe, student.avg, student.rank))
    print("Sắp xếp sinh viên theo tuổi")
    return list_student
# end def
def sort_by_lab():
    list_student = read_file()
    list_student.sort(key = lambda x: float(x.lab), reverse = True)
    write_file(list_student)
    for i in tree.get_children():
        tree.delete(i)
    # Thêm các mục đã được sắp xếp vào treeview
    for student in list_student:
        tree.insert('', 'end', values=(student.code, student.name, student.old, student.lab,
                                student.pt, student.assignment, student.pe,
                                student.fe, student.avg, student.rank))
    print("Sắp xếp sinh viên theo điểm lab")
    return list_student
# end def
def sort_by_avg():
    list_student = read_file()
    list_student.sort(key = lambda x: float(x.avg), reverse = True)
    write_file(list_student)
    for i in tree.get_children():
        tree.delete(i)
    # Thêm các mục đã được sắp xếp vào treeview
    for student in list_student:
        tree.insert('', 'end', values=(student.code, student.name, student.old, student.lab,
                                student.pt, student.assignment, student.pe,
                                student.fe, student.avg, student.rank))
    print("Sắp xếp sinh viên theo điểm trung bình")
    return list_student
# end def

# # # # # # # # # # # # Xóa Sinh viên # # # # # # # # # # # #
# Danh sách để lưu trữ các nút và Entry
buttons = []
id_student = None
def delete_students():
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
    submit_button_delete = Button(main, text="Xóa", command = check_code_delete)
    buttons.append(submit_button_delete)
    submit_button_delete.place(x = 250, y = 110)
    # tạo nút exit 
    exit_button_delete = Button(main, text="Exit", command = exit_delete)
    exit_button_delete.place(x = 300, y = 110)
    print("Xóa sinh viên")
def check_code_delete():
    # list_student = {}
    for button in buttons:
        button.place_forget()
    # đặt lại các nút ở chế độ bình thường
    menu_button.config(state = tk.NORMAL)
    add_button.config(state = tk.NORMAL)
    # check code để xóa
    code = id_student.get().upper()
    with open("PFP191.txt", "r", encoding='utf-8-sig') as file:
        lines = file.readlines()
    found = False
    with open("PFP191.txt", "w", encoding='utf-8-sig') as file:
        for line in lines:
            student = line.strip().split('\t')
            if student[0] != code:
                file.write(line)
            else:
                found = True
    if found:
        t = Label(main, text = "Đã xóa sinh viên")
        t.place(x = 150, y = 110)
        t.after(2000, t.place_forget)  # Xóa label sau 2 giây
        print("Student deleted successfully.")
    else:
        f = Label(main, text = "Không có sinh viên trong danh sách")
        f.place(x = 150, y = 110)
        f.after(2000, f.place_forget)  # Xóa label sau 2 giây
        print("Student not found.")

    # Load lại danh sách sau khi xóa
    for i in tree.get_children():
        tree.delete(i)
    # Thêm các mục còn lai vào treeview
    list_student_new = read_file()
    for student in list_student_new:
        tree.insert('', 'end', values=(student.code, student.name, student.old, student.lab,
                                student.pt, student.assignment, student.pe,
                                student.fe, student.avg, student.rank))
def exit_delete():
    id_student.destroy()
    submit_button_delete.place_forget()
    exit_button_delete.place_forget()
        # đặt lại các nút
    menu_button.config(state=tk.NORMAL)
    add_button.config(state=tk.NORMAL)
    print("Hủy xóa sinh viên")
# # # # # # # # # # # # TREE VIEW # # # # # # # # # # # #
def load_file():
    list_sv = []
    try:
        with open('PFP191.txt','r', encoding='utf-8-sig') as file:
            for line in file:
                code, name, old, lab, pt, assignment, pe, fe, avg, rank = line.strip().split('\t')
                list_sv.append(Student(code, name, old, lab, pt, assignment, pe, fe, avg, rank))
    except FileNotFoundError:
        file = open('PFP191.txt','w', encoding='utf-8-sig') 
        file.close()
    return list_sv

# Tạo một Treeview
tree = ttk.Treeview(main, show='headings')

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
students = load_file()
for student in students:
    tree.insert("", "end", values=(student.code, student.name, student.old, student.lab,
                                student.pt, student.assignment, student.pe,
                                student.fe, student.avg, student.rank))
# Đặt Treeview vào cửa sổ
tree.place( x = 10, y = 150)


# # # # # # # # # # # # CÁC NÚT # # # # # # # # # # # #
# Tạo các nút và gán các hàm tương ứng cho từng nút
# Nút thêm
add_button = Button(main, text = "Thêm sinh viên", command = add_student)
add_button.place(x = 10, y = 30)
# Nút sắp xếp
menu_button = tk.Menubutton(main, text = "Sắp xếp theo", relief = tk.RAISED)
menu_button.place(x = 10, y = 70)
menu = tk.Menu(menu_button, tearoff = False) # hàm 'tearoff' để ngăn không cho các chọn sắp xếp tạo thành 1 cửa sổ khác mà chỉ tạo thành một frame
menu_button['menu'] = menu
menu.add_command(label="OLD", command = sort_by_old)
menu.add_command(label="LAB", command = sort_by_lab)
menu.add_command(label="AVG", command = sort_by_avg)
# Nút xóa
delete_button = Button(main, text= "Xóa sinh viên", command = delete_students)
delete_button.place(x = 10, y = 110)

# Chạy vòng lặp chính của cửa sổ
main.mainloop()

