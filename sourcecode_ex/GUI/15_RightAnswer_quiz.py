from tkinter import(
    Tk,  Menu,  END, Scrollbar, Text
)
import os

root = Tk()


root.title("제목없음-메모장")
root.geometry("640x480") #가로 x 세로


filename = "mynote.txt"


def open_file():
    if os.path.isfile(filename):    #파일 있으면 T 없으면 F
        with open(filename, "r", encoding="utf8",) as file:
            txt.delete("1.0", END) # 텍스트 위젯 본문 삭제
            txt.insert(END, file.read()) #파일 내용을 본문에 입력




def save_file():
    with open(filename, "w", encoding="utf8",)as file:
        file.write(txt.get("1.0", END)) # 모든 내용을 가져와서 저장


def cerate_new_file():
    print("새파일을 만듭닏다")

menu = Menu(root)
#---------------------------------------------------------------------------------

menu_file = Menu(menu, tearoff=0)


#1새항목
menu_file.add_command(label="새항목", command=cerate_new_file)
#2새창
menu_file.add_command(label="새창", command=cerate_new_file)
#3열기
menu_file.add_command(label="열기", command= open_file)

#4저장
menu_file.add_command(label="저장", command=save_file)
#5다른이름으로 저장
menu_file.add_command(label="다른이름으로 저장", command=cerate_new_file)
menu_file.add_separator()
#6페이지 설정
menu_file.add_command(label="페이지 설정", command=cerate_new_file)
#7인쇄
menu_file.add_command(label="인쇄", command=cerate_new_file)
menu_file.add_separator()

#8종료
menu_file.add_command(label="종료", command=root.quit)
###
 
menu.add_cascade(label="파일", menu=menu_file )
#---------------------------------------------------------------------------------

menu_cut = Menu(menu, tearoff=0)

#실행 취소
menu_cut.add_command(label="실행취소", command=cerate_new_file)
menu_cut.add_separator()
#잘라내기
menu_cut.add_command(label="잘라내기", command=cerate_new_file)
#복사
menu_cut.add_command(label="복사", command=cerate_new_file)
#붙여넣기
menu_cut.add_command(label="붙여넣기", command=cerate_new_file)
#삭제
menu_cut.add_command(label="삭제", command=cerate_new_file)
menu_cut.add_separator()
#찾기
menu_cut.add_command(label="찾기", command=cerate_new_file)
#다음 찾기
menu_cut.add_command(label="다음 찾기", command=cerate_new_file)
#이전 찾기
menu_cut.add_command(label="이전 찾기", command=cerate_new_file)
#바꾸기
menu_cut.add_command(label="바꾸기", command=cerate_new_file)
#이동
menu_cut.add_command(label="이동", command=cerate_new_file)
menu_cut.add_separator()
#모두선택
menu_cut.add_command(label="모두선택", command=cerate_new_file)
#날짜/시간
menu_cut.add_command(label="날짜/시간", command=cerate_new_file)
menu_cut.add_separator()
#글꼴
menu_cut.add_command(label="글꼴", command=cerate_new_file)
###
menu.add_cascade(label="편집", menu=menu_cut )
#---------------------------------------------------------------------------------
menu_view = Menu(menu, tearoff=0)
#확대/축소
sub_menu = Menu(menu, tearoff=0)
sub_menu.add_command(label="확대")
sub_menu.add_command(label="축소")
sub_menu.add_command(label="기본 확대/ 축소복원")
menu_view.add_cascade(label="확대/축소", menu=sub_menu)
#상태표시줄 라디오
menu_view.add_checkbutton(label="상태표시줄")
#줄바꿈 라디오
menu_view.add_checkbutton(label="자동 줄바꿈")
###
menu.add_cascade(label="보기", menu=menu_view)
#---------------------------------------------------------------------------------
menu_con = Menu(menu, tearoff=0)
##
menu_con1 = Menu(menu, tearoff=0)
menu_con1.add_checkbutton(label="Show Minimap")
menu_con.add_cascade(label="View", menu=menu_con1)
###
menu.add_cascade(label="설정", menu=menu_con )

#=================================================================================
#본문영역

sBAR = Scrollbar(root)
sBAR.pack(side="right", fill="y")
#set이 없으면 스크롤을 내려도 다시 올라옴

txt = Text(root, yscrollcommand=sBAR.set)
txt.pack(side="left" ,fill="both", expand=True)



sBAR.config(command=txt.yview)


#---------------------------------------------------------------------------------


 

root.config(menu=menu)
root.mainloop()