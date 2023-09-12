from Class import PFP191

def display_menu():
    print("Student Management System")
    print("1. Add Student")
    print("2. Update Infor Student")
    print("3. View class PFP191")
    print("4. Search by Lab points")
    print("5. Sort by ")
    print("6. Delete Student ")
    print("7. Delete All ")
    print("0. Exit")

def main():
    x = PFP191()
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            x.Input_Infor()
        elif choice == '2':
            x.Update_student()
        elif choice == '3':
            x.Show_Infor()  
        elif choice == '4':
            print('1.Tìm kiếm theo điểm Lab')
            print('2.Tìm kiếm theo điểm Practice')
            print('3.Tìm kiếm theo điểm Assignment')
            print('4.Tìm kiếm theo điểm Practice Exam ')
            print('5.Tìm kiếm theo điểm Final Exam ')
            print('6.Tìm kiếm theo điểm Average')
            l = int(input('nhập loại điểm muốn tìm:'))
            p = int(input('nhập điểm :'))
            if l == 1:
                print('Danh sách những sinh viên có điểm Lab bằng', p)
                x.search_by_point(l, p)
            elif l == 2:
                print('Danh sách những sinh viên có điểm Pratice bằng', p)
                x.search_by_point(l, p)
            elif l == 3:
                print('Danh sách những sinh viên có điểm Assignment bằng', p)
                x.search_by_point(l, p)
            elif l == 4:
                print('Danh sách những sinh viên có điểm Pratice Exam bằng', p)
                x.search_by_point(l, p)
            elif l == 5:
                print('Danh sách những sinh viên có điểm Final Exam bằng', p)
                x.search_by_point(l, p)
            elif l == 1:
                print('Danh sách những sinh viên có điểm Average bằng', p)
                x.search_by_point(l, p)
        elif choice == '5':
            print('1.Sắp xếp theo tuổi')
            print('2.Sắp xếp theo điểm Lab')
            print('3.Sắp xếp theo điểm Practice')
            print('4.Sắp xếp theo điểm Assignment')
            print('5.Sắp xếp theo điểm Practice Exam ')
            print('6.Sắp xếp theo điểm Final Exam ')
            print('7.Sắp xếp theo điểm Average')
            l = int(input('nhập điều kiện muốn sắp xếp:'))
            if l == 1:
                print('Danh sách sinh viên')
                x.sort_by_old()
            elif l == 2:
                print('Danh sách sinh viên')
                x.sort_by_lab()
            elif l == 3:
                print('Danh sách sinh viên')
                x.sort_by_pt()
            elif l == 4:
                print('Danh sách sinh viên')
                x.sort_by_assignment()
            elif l == 5:
                print('Danh sách sinh viên')
                x.sort_by_pe()
            elif l == 6:
                print('Danh sách sinh viên')
                x.sort_by_fe()
            elif l == 7:
                print('Danh sách sinh viên')
                x.sort_by_avg()
        elif choice == '6':
            x.Delete_student_by_code()
        elif choice == '7':
            x.Delete_all()   
        elif choice == '0':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == '__main__':
    main()



