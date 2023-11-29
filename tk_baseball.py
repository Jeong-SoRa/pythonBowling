from tkinter import *
import random

### 시도회수 카운트 global 변수
round = 0

### 리스트 선언
homerun = []


### 숫자야구 게임 초기화
def reset_num():
    list.delete(0, END)
    list.insert(END, "=" * 10 + "숫자야구 시작" + "=" * 10)
    list.pack()

    ### 시도회수 초기화
    global round
    round = 0

    ### 랜덤 숫자 4자리 생성하기
    del homerun[:]
    for i in range(0, 4):
        homerun.append(random.randrange(0, 10, 1))

    ### 랜덤 숫자 중복체크
    while True:
        if (homerun[0] == homerun[1]):
            homerun[1] = random.randrange(0, 10, 1)
            continue
        if (homerun[0] == homerun[2] or homerun[1] == homerun[2]):
            homerun[2] = random.randrange(0, 10, 1)
            continue
        if (homerun[0] == homerun[3] or homerun[1] == homerun[3] or homerun[2] == homerun[3]):
            homerun[3] = random.randrange(0, 10, 1)
            continue
        break

    # list.insert(END, f"{homerun}")
    btn_input["state"] = NORMAL


### 숫자야구게임
def guess_num():
    global round

    ### strike 수
    strikeCnt = 0

    ### ball 수
    ballCnt = 0

    ### 입력받을 숫자
    num = str(input.get())

    if (len(num) == 4):
        round += 1

        for i in range(0, 4):
            for k in range(0, 4):
                if (homerun[i] == int(num[k]) and i == k):
                    strikeCnt += 1
                elif (homerun[i] == int(num[k]) and i != k):
                    ballCnt += 1

        if (strikeCnt == 4):
            list.insert(END, f"{round}회 결과  HomeRun!!")
            list.insert(END, f"총 {round}회 만에 숫자를 맞췄습니다.")
            btn_input["state"] = DISABLED
            list.pack()
        else:
            list.insert(END, f"{round}회 결과 [{num}] 은(는) {strikeCnt}S {ballCnt}B 입니다.")
            list.pack()

            # label["text"] = str(num) + f"  시도 횟수 {round}" + f"  {homerun}"


window = Tk()
window.geometry("400x230")
window.title("숫자 야구")

### 프레임을 나누지 않으면 .pack()이 제대로 먹지않음

### 입력 프레임
frame_input = Frame(window)
frame_input.pack(side="top")

### 버튼 프레임
frame_btn = Frame(window)
frame_btn.pack(side="top")

### 결과 프레임
frame_result = Frame(window)
frame_result.pack(side="top")

input = Entry(frame_input, wi=30)
input.pack()

input.insert(0, "")

btn_reset = Button(frame_btn, text="새로시작", command=reset_num)
btn_input = Button(frame_btn, text="숫자입력", command=guess_num, state=DISABLED)
btn_reset.grid(row=1, column=1)
btn_input.grid(row=1, column=2)

# label = Label(frame_result, text="="*10 + "숫자야구 시작" + "="*10)
# label.pack()

scrollbar = Scrollbar(frame_result)
scrollbar.pack(side="right", fill="y")

list = Listbox(frame_result, width=50, yscrollcommand=scrollbar.set)

scrollbar.config(command=list.yview)

window.mainloop()