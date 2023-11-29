from tkinter import *

def test() :
    return 1

window = Tk()
window.geometry("600x230")
window.title("볼링 점수 계산기")



### 버튼 프레임
frame_btn = Frame(window)
frame_btn.pack(side="top")

# 버튼 10개 생성하기
# 동적 변수는 이렇게 맹근다.
iScoreBtn = 0
while iScoreBtn < 11 :
    globals()['btn_score{}'.format(iScoreBtn)] = Button(frame_btn, text=iScoreBtn, command=test)
    globals()['btn_score{}'.format(iScoreBtn)].grid(row=1, column=(iScoreBtn*2))
    iScoreBtn += 1




window.mainloop()