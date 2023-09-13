
import tkinter as tk

# Khởi tạo biến toàn cục student_label
student_label = None

def create_label():
    global student_label
    # Tạo một label với nội dung là "Không có sinh viên trong lớp"
    student_label = tk.Label(root, text="Không có sinh viên trong lớp")
    student_label.pack()

def hide_label():
    # Hàm này sẽ được gọi khi button được nhấn
    # Nó sẽ ẩn label đi
    global student_label
    if student_label is not None:
        student_label.pack_forget()

# Tạo một cửa sổ mới
root = tk.Tk()

# Gọi hàm create_label để tạo label
create_label()

# Tạo một button với nội dung là "Thêm sinh viên"
# Khi button này được nhấn, nó sẽ gọi hàm hide_label
add_student_button = tk.Button(root, text="Thêm sinh viên", command=hide_label)
add_student_button.pack()

# Hiển thị cửa sổ
root.mainloop()
