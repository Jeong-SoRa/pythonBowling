# 스트라이크 : 뒤프레임 1,2회차 점수 더하기
# 
# 스페어 :  뒤 프레임 1회차 점수 더하기
# 

scoreByFrame = []

def calTotal(f, t, thisScore):
    global result
    global scoreByFrame
    global totalShow
    totalShow = []  # 점수가 누적되어야 하므로 매번 초기화함

    result.append(thisScore)
    # 프리임별 점수 배열에 점수 담기 Start
    if t == 2:
        scoreByFrame[-1] = int(result[-2]) + int(result[-1])

    elif t == 1:  # 프레임별 점수 담기
        scoreByFrame.append(int(result[-2]) + int(result[-1]))

    # 프리임별 점수 배열에 점수 담기 End

    # 프레임별 점수 계산하기 Start
    if f >= 1 and f < 9:  # 마지막 프레임은 별도 계산
        if t == 0:
            if result[(f * 2) - 1] == 10:  # 이전 frame이 spare일 때
                scoreByFrame[f - 1] = scoreByFrame[f - 1] + thisScore

        elif t == 1:
            if result[(f * 2) - 2] == 10:  # 이전 frame이 strike일 때
                scoreByFrame[f - 1] = scoreByFrame[f - 1] + scoreByFrame[f]

                if f >= 2:  # 프레임이 3번째 이상일 때만 전전 프레임을 더한다.
                    if result[(f * 2) - 4] == 10:  # 전,전 frame이 Strike 일 때
                        scoreByFrame[f - 2] = scoreByFrame[f - 2] + result[f * 2]
    # 마지막 프레임 계산하기
    elif f == 9:
        if t == 0:
            if result[(f * 2) - 1] == 10 or result[(f * 2) - 2] == 10:  # 이전 frame이 스트라이크나 spare일 때
                scoreByFrame[f - 1] = scoreByFrame[f - 1] + thisScore

                if result[(f * 2) - 4] == 10:  # 전,전 frame이 Strike 일 때
                    scoreByFrame[f - 2] = scoreByFrame[f - 2] + result[f * 2]

        elif t == 1:
            if result[(f * 2) - 2] == 10:  # 이전 frame이 스트라이크일 때
                scoreByFrame[f - 1] = scoreByFrame[f - 1] + thisScore

        # 세번째 점수가 들어온 경우 
        elif t == 2:
            scoreByFrame[-1] = (int(result[-2]) + int(result[-1]) + int(result[-3]))

            # 프레임별 점수 계산하기 End

    # 각 프레임 점수 누적 시키기 Start
    if t == 1 or f == 9:  # 두번째 투구일때        
        showIdx = 0
        while showIdx < len(scoreByFrame):

            if showIdx == 0:
                totalShow.append(scoreByFrame[showIdx])

            elif showIdx > 9:
                totalShow[-1] = totalShow[showIdx - 1] + scoreByFrame[showIdx]

            else:
                totalShow.append(totalShow[showIdx - 1] + scoreByFrame[showIdx])

            showIdx += 1

    # 각 프레임 점수 누적 시키기 End

    return totalShow


result = []  # 계산을 위해 별도 리스트 show 와 동일한 점수가 있다.
show = []  # 프레임별 점수 보여주기

total = 0
totalShow = []  # 토탈점수를 보여주기 위한 리스트

f = 0
thisScore = 0
while f < 10:
    print('ㅁㅁㅁ' + str(f + 1) + '프레임 ')

    for t in range(0, 2):

        if t == 0:  # 각 프레임 첫번째
            print('ㅁ' + str(t + 1) + '회 점수')
            thisScore = input('>> ')
            if int(thisScore) > 10:
                print('점수를 잘못입력하셨습니다')
                break

            if thisScore == str(10):  # This is Strike
                show.append('X')
                if f < 9:  # 마지막 프레임은 세번 다 던져야함
                    show.append('  ')

            else:
                show.append(thisScore)

            # total = int(total) + int(thisScore)
            totalShow = calTotal(f, t, int(thisScore))

        else:  # 각 프레임 두번재

            if int(result[-1]) >= 10:  # 스트라이크일 때 스페어 자리에 점수를 넣기 위해서
                if f >= 9:  # 마지막 프레임은 무조건 점수를 받아야 한다.
                    print('ㅁ' + str(t + 1) + '회 점수')
                    thisScore = input('>> ')
                    if int(thisScore) == 10:
                        show.append('X')
                    elif int(thisScore) + result[-1] == 10:
                        show.append('/')
                    else:
                        show.append(thisScore)

                else:
                    thisScore = 0  # 마지막을 제외하고 스트라이크를 친 경우 스페어 자리에 0을 채우기 위해

            else:
                print('ㅁ' + str(t + 1) + '회 점수')
                thisScore = input('>> ')
                if result[-1] + int(thisScore) > 10:
                    print('점수를 잘못입력하셨습니다')
                    break

                if int(result[-1]) + int(thisScore) == 10:  # This is Spare
                    show.append('/')

                else:
                    show.append(thisScore)

            totalShow = calTotal(f, t, int(thisScore))

        print("각 회차", show)
        if t == 1 or f == 9:
            print("전체점수", totalShow)

    if f == 9:  # 마지막 프레임은 세번까지 가능
        if result[-2] + result[-1] > 9:
            print('ㅁ3회 점수')
            thisScore = input('>> ')

            if int(thisScore) == 10:
                show.append('X')
            elif int(thisScore) + result[-1] == 10:
                show.append('/')
            else:
                show.append(thisScore)

            totalShow = calTotal(f, 2, int(thisScore))

            print("각 회차", show)
            print("전체점수", totalShow)

    f = f + 1