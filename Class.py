from Student import Student
import math

class PFP191:
    # Hàm load file
    def load_file(self):
        list_sv = []
        try:
            with open('PFP191.txt','r', encoding='utf-8-sig') as file:
                for line in file:
                    code, name, old, lab, pt, assignment, pe, fe, avg, rank = line.strip().split('\t')
                    list_sv.append(Student(code, name, old, lab, pt, assignment, pe, fe, avg, rank))
        except FileNotFoundError:
            file = open('PFP191.txt','w', encoding='utf-8-sig') 
            file.close()
        # if list_sv == []:
        #     pass
        # else:
        #     with open('PFP191.txt','w', encoding='utf-8-sig') as file :
        #         for st in list_sv:
        #             file.write(f'{st.code}\t{st.name}\t{st.old}\t{st.lab}\t{st.pt}\t{st.assignment}\t{st.pe}\t{st.fe}\t{st.avg}\t{st.rank}\n')
        return list_sv
    # end def

    # Hàm load file bằng dictinary
    def load_file_1(self):
        list_sv = {}
        try:
            with open('PFP191.txt','r', encoding='utf-8-sig') as file:
                for line in file:
                    line = line.strip().split('\t')
                    # # # key = line[0] còn value = Student()
                    list_sv[line[0]] = Student(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9]) 
        except FileNotFoundError:
            file = open('PFP191.txt','w', encoding='utf-8-sig') 
            file.close()
        # if list_sv == {}:
        #     pass
        # else:
        #     with open('PFP191.txt','w', encoding='utf-8-sig') as file :
        #         for codes, st in list_sv.items():
        #             file.write(f'{st.code}\t{st.name}\t{st.old}\t{st.lab}\t{st.pt}\t{st.assignment}\t{st.pe}\t{st.fe}\t{st.avg}\t{st.rank}\n')
        key = [c.code for c in list_sv]
        list_sv_new = dict(zip(key, list_sv))
        return list_sv_new
    # end def

    # hàm check code có trong lớp hay không, sử dụng list , dùng bổ sung cho hàm Input_Infor()
    def check_code_input(self, code):
        list_sv = self.load_file()
        if list_sv == []:
            pass
        else:
            for st in list_sv:
                    if st.code == code:
                        return False
        return True
    # end def
    def check_code_update(self, code):
        list_sv = self.load_file()
        if list_sv == []:
            return False
        else:
            for st in list_sv:
                    if st.code == code:
                        return True
        return False
    # end def

    # sử dụng dictinary để check học sinh có trong lớp không bỏ sung cho hàm Update_Student_1()
    def check_code_1(self, codes):
        list_st = {}
        codes = str(codes).upper()
        with open('PFP191.txt', 'r', encoding='utf-8-sig') as file:
            file = file.readlines()
            for line in file:
                line = line.strip().split('\t')
                # # # key = line[0] còn value = Student()
                list_st[line[0]] = Student(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9]) 
        if list_st == {}:
            return False
        else:
            if codes  in list_st.keys():
                return True
            else:
                return False
    # end def

    # hàm nhập thông tin sinh viên 
    def Input_Infor(self):
        # check code
        code = str(input('nhập mă số sinh viên:'))
        code = code.upper()
        f = self.check_code_input(code)
        if f :
        # check name
            name = str(input('nhập tên học sinh:'))
            # check tuổi
            try:
                old = int(input('nhập tuổi:'))
            except:
                while True:
                    try:
                        old = int(input('nhập lại tuổi:'))
                        break
                    except:
                        continue
            # check lab
            try:
                lab = float(input('nhập điểm Lab:'))
            except:
                while True:
                    try:
                        lab = float(input('nhập lại điểm Lab:'))
                        break
                    except:
                        continue
            # check pt 
            try:
                pt = float(input('nhập điểm Practice:'))
            except:
                while True:
                    try:
                        pt = float(input('nhập lại điểm Practice:'))
                        break
                    except:
                        continue
            # check assignment
            try:
                assignment = float(input('nhập điểm Assignment:'))
            except:
                while True:
                    try:
                        assignment = float(input('nhập lại điểm Assignment:'))
                        break
                    except:
                        continue
            # check pe
            try:
                pe = float(input('nhập điểm Practice Exam:'))
            except:
                while True:
                    try:
                        pt = float(input('nhập lại điểm Practice Exam:'))
                        break
                    except:
                        continue
            # check fe
            try:
                fe = float(input('nhập điểm Final Exam:'))
            except:
                while True:
                    try:
                        fe = float(input('nhập lại điểm Final Exam:'))
                        break
                    except:
                        continue
            # tính điểm trung bình 
            avg = math.ceil( ((lab * 0.1) + (pt * 0.1) + (assignment * 0.2) + (pe * 0.3) + (fe * 0.3)) * 100) / 100

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
        else:
            print('Đã có mã sinh viên này trong lớp')
        # end def

    # hiển thị bảng điểm của lớp
    def Show_Infor(self):
        print("{:<14} | {:<24} | {:<12} | {:<7} | {:<12} | {:<14} | {:<17} | {:<14} | {:<11} | {:<8}"
              .format('Code student', 'Name student', 'Year old' , 'Lab', 'Practice', 'Assignment', 'Practice Exam', 'Final Exam',  'Average', 'Rank'))
        # hien thi danh sach sinh vien
        with open('PFP191.txt','r', encoding='utf-8-sig') as file:
            for line in file:
                    code, name, old, lab, pt, assignment, pe, fe, avg, rank = line.strip().split('\t')
                    print("{:<14} | {:<24} | {:<12} | {:<7} | {:<12} | {:<14} | {:<17} | {:<14} | {:<11} | {:<8}" 
                      .format(code, name, old, lab, pt, assignment, pe, fe, avg, rank))
        print()
    # end def

    # hàm cập nhập thông tin sinh viên trục tiếp vào file 
    def Update_student(self):
        code = str(input('nhập mă số sinh viên:')).upper()
        with open("PFP191.txt", "r", encoding='utf-8-sig') as file:
            lines = file.readlines()
        found = False
        with open("PFP191.txt", "w", encoding='utf-8-sig') as file:
            for line in lines:
                student = line.strip().split('\t')
                if student[0] == code: # # nếu có student trong danh sách lớp
                    found = True
                    name = str(input('nhập tên học sinh:'))
                    # check tuổi
                    try:
                        old = int(input('nhập tuổi:'))
                    except:
                        while True:
                            try:
                                old = int(input('nhập lại tuổi:'))
                                break
                            except:
                                continue
                    # check lab
                    try:
                        lab = float(input('nhập điểm Lab:'))
                    except:
                        while True:
                            try:
                                lab = float(input('nhập lại điểm Lab:'))
                                break
                            except:
                                continue
                    # check pt 
                    try:
                        pt = float(input('nhập điểm Practice:'))
                    except:
                        while True:
                            try:
                                pt = float(input('nhập lại điểm Practice:'))
                                break
                            except:
                                continue
                    # check assignment
                    try:
                        assignment = float(input('nhập điểm Assignment:'))
                    except:
                        while True:
                            try:
                                assignment = float(input('nhập lại điểm Assignment:'))
                                break
                            except:
                                continue
                    # check pe
                    try:
                        pe = float(input('nhập điểm Practice Exam:'))
                    except:
                        while True:
                            try:
                                pt = float(input('nhập lại điểm Practice Exam:'))
                                break
                            except:
                                continue
                    # check fe
                    try:
                        fe = float(input('nhập điểm Final Exam:'))
                    except:
                        while True:
                            try:
                                fe = float(input('nhập lại điểm Final Exam:'))
                                break
                            except:
                                continue
                    # tính điểm trung bình 
                    avg = math.ceil( ((lab * 0.1) + (pt * 0.1) + (assignment * 0.2) + (pe * 0.3) + (fe * 0.3)) * 100) / 100
                    # xếp loại học lực 
                    if (avg >= 8):
                        rank = "Gioi"
                    elif (avg >= 6.5):
                        rank = "Kha"
                    elif (avg >= 5):
                        rank = "Trung Binh"
                    else:
                        rank = "Yeu"  
                    student[0] = code    
                    student[1] = name
                    student[2] = old
                    student[3] = lab
                    student[4] = pt
                    student[5] = assignment
                    student[6] = pe
                    student[7] = fe
                    student[8] = avg
                    student[9] = rank
                    # Update người đó vao file
                    file.write(f'{student[0]}\t{student[1]}\t{student[2]}\t{student[3]}\t{student[4]}\t{student[5]}\t{student[6]}\t{student[7]}\t{student[8]}\t{student[9]}\n')

                # In ra thông tin người được Update
                    print("{:<14} | {:<24} | {:<12} | {:<7} | {:<12} | {:<14} | {:<17} | {:<14} | {:<11} | {:<8}"
                        .format('Code student', 'Name student', 'Year old' , 'Lab', 'Practice', 'Assignment', 'Practice Exam', 'Final Exam',  'Average', 'Rank'))
                    print("{:<14} | {:<24} | {:<12} | {:<7} | {:<12} | {:<14} | {:<17} | {:<14} | {:<11} | {:<8}"
                        .format(student[0], student[1], student[2], student[3], student[4], student[5], student[6], student[7], student[8], student[9]))
                    print("Student update successfully.") 
                # Nếu không phải student cần tìm thì ghi duyệt qua 
                else: 
                    file.write(line)
        if not found:# không có student trong danh sách lớp 
            print("Student not found.")
        print()
    # end def

    # hàm cập nhập thông tin sinh viên dùng dictinary nhưng không update vào file 
    def Update_student_1(self):
        code = str(input('nhập mă số sinh viên:'))
        code = code.upper()
        if self.check_code_1(code):
            # name
            name = str(input('nhập tên học sinh:'))
            # check tuổi
            try:
                old = int(input('nhập tuổi:'))
            except:
                while True:
                    try:
                        old = int(input('nhập lại tuổi:'))
                        break
                    except:
                        continue
            # check lab
            try:
                lab = float(input('nhập điểm Lab:'))
            except:
                while True:
                    try:
                        lab = float(input('nhập lại điểm Lab:'))
                        break
                    except:
                        continue
            # check pt 
            try:
                pt = float(input('nhập điểm Practice:'))
            except:
                while True:
                    try:
                        pt = float(input('nhập lại điểm Practice:'))
                        break
                    except:
                        continue
            # check assignment
            try:
                assignment = float(input('nhập điểm Assignment:'))
            except:
                while True:
                    try:
                        assignment = float(input('nhập lại điểm Assignment:'))
                        break
                    except:
                        continue
            # check pe
            try:
                pe = float(input('nhập điểm Practice Exam:'))
            except:
                while True:
                    try:
                        pt = float(input('nhập lại điểm Practice Exam:'))
                        break
                    except:
                        continue
            # check fe
            try:
                fe = float(input('nhập điểm Final Exam:'))
            except:
                while True:
                    try:
                        fe = float(input('nhập lại điểm Final Exam:'))
                        break
                    except:
                        continue
            # tính điểm trung bình 
            avg = math.ceil( ((lab * 0.1) + (pt * 0.1) + (assignment * 0.2) + (pe * 0.3) + (fe * 0.3)) * 100) / 100
            # xếp loại học lực 
            if (avg >= 8):
                rank = "Gioi"
            elif (avg >= 6.5):
                rank = "Kha"
            elif (avg >= 5):
                rank = "Trung Binh"
            else:
                rank = "Yeu"  
            # update
            list_st = {}
            with open('PFP191.txt',  'r', encoding='utf-8-sig') as file:
                for line in file:
                    line  = line.strip().split('\t')
                    list_st[line[0]] = Student(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9]) 
            list_st[code] = Student(code, name, old, lab, pt, assignment, pe, fe, avg, rank)
            # hiển thị danh sách 
            print("{:<14} | {:<24} | {:<12} | {:<7} | {:<12} | {:<14} | {:<17} | {:<14} | {:<11} | {:<8}"
                .format('Code student', 'Name student', 'Year old' , 'Lab', 'Practice', 'Assignment', 'Practice Exam', 'Final Exam',  'Average', 'Rank'))
            for codes, student in list_st.items():
                print("{:<14} | {:<24} | {:<12} | {:<7} | {:<12} | {:<14} | {:<17} | {:<14} | {:<11} | {:<8}"
                    .format(student.code, student.name, student.old, student.lab, student.pt, student.assignment, student.pe, student.fe, student.avg, student.rank))
        else :
            print('Không có học sinh trong lớp')
        pass
    # end def

    # Tìm kiếm sinh viên theo điểm Lab
    def search_by_point(self, name_point, point):
        Students = []
        with open('PFP191.txt', 'r', encoding='utf-8-sig') as file:
            for line in file:
                st = line.strip().split('\t')
                if float(st[int(name_point + 2)]) == point :
                    Students.append(Student(st[0], st[1], st[2], st[3], st[4], st[5], st[6], st[7], st[8], st[9]))
        print('Danh sách viên viên có điểm lab:',point)
        print("{:<14} | {:<24} | {:<12} | {:<7} | {:<12} | {:<14} | {:<17} | {:<14} | {:<11} | {:<8}"
            .format('Code student', 'Name student', 'Year old' , 'Lab', 'Practice', 'Assignment', 'Practice Exam', 'Final Exam',  'Average', 'Rank'))
        for student in Students:
            print("{:<14} | {:<24} | {:<12} | {:<7} | {:<12} | {:<14} | {:<17} | {:<14} | {:<11} | {:<8}"
                .format(student.code, student.name, student.old, student.lab, student.pt, student.assignment, student.pe, student.fe, student.avg, student.rank))
        print()  
    # end def

    #  hàm đọc file
    def read_file(self):
        list_student = []
        with open('PFP191.txt','r', encoding='utf-8-sig') as file:
            for line in file:
               code, name, old, lab, pt, assignment, pe, fe, avg, rank = line.strip().split('\t') 
               list_student.append(Student(code, name, old, lab, pt, assignment, pe, fe, avg, rank))
        return list_student
    # end def

    # hàm viết vào file 
    def write_file(self, list_student):
        with open('PFP191.txt','w', encoding='utf-8-sig') as file:
            for st in list_student:
                file.write(f'{st.code}\t{st.name}\t{st.old}\t{st.lab}\t{st.pt}\t{st.assignment}\t{st.pe}\t{st.fe}\t{st.avg}\t{st.rank}\n')
        file.close()
    # end def

    # sắp xếp theo tuổi nhưng không lưu dữ liệu sắp xếp vào file 
    def sort_by_old(self):
        list_student = self.read_file()

        # Selection sort : sử dụng thuật toán tìm vị trí để hoán đổi
        # for i in range(len(list_student) - 1):
        #     min_index = i # vị trí bắt đầu từ 0 rồi tăng dần lên đến cuối của dãy
        #     for j in range(i + 1, len(list_student)):
        #         if int(list_student[j].old) < int(list_student[min_index].old):
        #             min_index = j
        #     list_student[i], list_student[min_index] = list_student[min_index], list_student[i]
        # end for 

        # Insertion sort 
        # for i in range(1, len(list_student)):
        #     value_old = list_student[i]
        #     j = i - 1
        #     while value_old.old < list_student[j].old and j > -1 : # so sánh với các phần tử đứng trc nó 
        #         list_student[j + 1] = list_student[j]
        #         list_student[j] = value_old
        #         j -= 1 
        # end for 

        # Bubnle sort 
        # for  i in range(len(list_student), 0, -1):
        #     for j in range(i - 1):
        #         if list_student[j].old > list_student[j + 1].old:
        #             list_student[j], list_student[j + 1] = list_student[j + 1], list_student[j]

        list_student.sort(key = lambda x: float(x.old), reverse = True)
        print("{:<14} | {:<24} | {:<12} | {:<7} | {:<12} | {:<14} | {:<17} | {:<14} | {:<11} | {:<8}"
            .format('Code student', 'Name student', 'Year old' , 'Lab', 'Practice', 'Assignment', 'Practice Exam', 'Final Exam',  'Average', 'Rank'))
        for student in list_student:
            print("{:<14} | {:<24} | {:<12} | {:<7} | {:<12} | {:<14} | {:<17} | {:<14} | {:<11} | {:<8}"
                .format(student.code, student.name, student.old, student.lab, student.pt, student.assignment, student.pe, student.fe, student.avg, student.rank))
    # end def

    # sắp xếp theo điểm lab và có lưu dữ liệu sắp xếp vào file 
    def sort_by_lab(self):
        list_student = self.read_file()
        list_student.sort(key = lambda x: float(x.lab), reverse = True)
        self.write_file(list_student)
        return self.Show_Infor()
    # end def

    # sắp xếp theo điểm Practice
    def sort_by_pt(self):
        list_student = self.read_file()
        list_student.sort(key = lambda x: float(x.pt), reverse = True)
        self.write_file(list_student)
        return self.Show_Infor()
    # end def

    # sắp xếp theo điểm Assignment
    def sort_by_assignment(self):
        list_student = self.read_file()
        list_student.sort(key = lambda x: float(x.assignment), reverse = True)
        self.write_file(list_student)
        return self.Show_Infor()
    # end def

    # sắp xếp theo điểm PE
    def sort_by_pe(self):
        list_student = self.read_file()
        list_student.sort(key = lambda x: float(x.pe), reverse = True)
        self.write_file(list_student)
        return self.Show_Infor()
    # end def

    # sắp xếp theo điểm PE
    def sort_by_fe(self):
        list_student = self.read_file()
        list_student.sort(key = lambda x: float(x.fe), reverse = True)
        self.write_file(list_student)
        return self.Show_Infor()
    # end def

    # sắp xếp theo điểm trung bình 
    def sort_by_avg(self):
        list_student = self.read_file()
        list_student.sort(key = lambda x: float(x.avg), reverse = True)
        self.write_file(list_student)
        return self.Show_Infor()
    # end def
    
    # hàm xóa student khỏi lớp bằng mã code
    def Delete_student_by_code(self):
        code = input("Enter code student id to delete: ")
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
            print("Student deleted successfully.")
        else:
            print("Student not found.")
    # end def

    # xóa toàn bộ danh sách 
    def Delete_all(self):
        file = open('PFP191.txt','w', encoding='utf-8-sig') 
        file.close()

# test 
if __name__ == '__main__':
    x = PFP191()
    x.Show_Infor()
    x.Update_student()
    print(x.load_file_1())
    x.Update_student_1()

