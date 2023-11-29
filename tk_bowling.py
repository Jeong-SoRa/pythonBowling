from tkinter import *

def test() :
    return 1

window = Tk()
window.geometry("600x230")
window.title("볼링 점수 계산기")



### 버튼 프레임
frame_btn = Frame(window)
#frame_btn.pack(side="top")
frame_btn.place(x=10, y=10)
### 결과 프레임
"""
frame_result = Frame(window)
frame_result.pack(side="top")
"""

# 버튼 10개 생성하기
# 동적 변수는 이렇게 맹근다.
iScoreBtn = 0
while iScoreBtn < 11 :
    globals()['btn_score{}'.format(iScoreBtn)] = Button(frame_btn, text=iScoreBtn, command=test)
    globals()['btn_score{}'.format(iScoreBtn)].grid(row=1, column=(iScoreBtn*2))
    iScoreBtn += 1


text = Text(window, width=5, height=5)
text2 = Text(window, width=5, height=5)

text.insert(CURRENT, "안녕하세요.\n")
text.insert("current", "반습니다.")
text.insert(1.0, "갑")

text.pack()
text2.pack()

"""
text.tag_add("강조", "1.0", "1.6")
text.tag_config("강조", background="yellow") 
text.tag_remove("강조", "1.1", "1.2")

message = Message(window, text="메세지입니다.", width=300, relief="solid", anchor="sw")
message.pack()

b1=Button(window, text="( 1 )", width=20)
b2=Button(window, text="( 1 )", width=20)
b3=Button(window, text="( 2 )")

b4=Button(window, text="( 3 )")
b5=Button(window, text="(4 )")
b6=Button(window, text="(1, 3)")

b7=Button(window, text="(2, 1)")
b8=Button(window, text="(2, 2)")
b9=Button(window, text="(2, 4)")

b1.grid(row=2, column=0)
b2.grid(row=2, column=1)
b3.grid(row=2, column=2)

b4.grid(row=2, column=0, rowspan=2)
b5.grid(row=2, column=1, columnspan=3)
b6.grid(row=2, column=3)

b7.grid(row=2, column=1, sticky="w")
b8.grid(row=2, column=2)
b9.grid(row=2, column=99)


show = Listbox(frame_result, width=60)

show.delete(0, END)
show.insert(END, "=" * 10 + "숫자야구 시작" + "=" * 10)
show.pack()
"""



window.mainloop()