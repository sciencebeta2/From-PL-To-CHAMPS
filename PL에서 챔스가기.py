#2024-06-11 5차 최종본
import random
import math
import signal

money = 100
commandteam = 0
Arsenal = "아스날"
Arsenal_attack = 5
Arsenal_defence = 5
Arsenal_fieldown = 6
Man_City = "맨시티"
Man_City_attack = 11
Man_City_defence = 7
Man_City_fieldown = 7
Man_Utd = "맨유"
Man_Utd_attack = 5
Man_Utd_defence = 7
Man_Utd_fieldown = 8
Liverpool = "리버풀"
Liverpool_attack = 8
Liverpool_defence = 9
Liverpool_fieldown = 6
Tottenham = "토트넘"
Tottenham_attack = 7
Tottenham_defence = 5
Tottenham_fieldown = 9
Chelsea = "첼시"
Chelsea_attack = 6
Chelsea_defence = 9
Chelsea_fieldown = 8
Wolverhampton = "울버햄튼"
Wolverhampton_attack = 6
Wolverhampton_defence = 6
Wolverhampton_fieldown = 8
West_Ham = "웨스트햄"
West_Ham_attack = 5
West_Ham_defence = 7
West_Ham_fieldown = 6
Newcastle = "뉴캐슬"
Newcastle_attack = 8
Newcastle_defence = 5
Newcastle_fieldown = 5
Arsenallist = [Arsenal_attack, Arsenal_defence, Arsenal_fieldown]
Man_Citylist = [Man_City_attack, Man_City_defence, Man_City_fieldown]
Man_Utdlist = [Man_Utd_attack, Man_Utd_defence, Man_Utd_fieldown]
Liverpoollist = [Liverpool_attack, Liverpool_defence, Liverpool_fieldown]
Tottenhamlist = [Tottenham_attack, Tottenham_defence, Tottenham_fieldown]
Chelsealist = [Chelsea_attack, Chelsea_defence, Chelsea_fieldown]
Wolverhamptonlist = [Wolverhampton_attack, Wolverhampton_defence, Wolverhampton_fieldown]
West_Hamlist = [West_Ham_attack, West_Ham_defence, West_Ham_fieldown]
Newcastlelist = [Newcastle_attack, Newcastle_defence, Newcastle_fieldown]
PL = [Arsenal, Man_City, Man_Utd, Liverpool, Tottenham, Chelsea, Wolverhampton, West_Ham, Newcastle]


# 랜덤 초이스 (최종)

def random_choice():
    PL = [Man_City, Man_Utd, Liverpool, Tottenham, Chelsea, Wolverhampton, West_Ham, Newcastle]
    PL_attack = [Arsenal_attack, Man_City_attack, Man_Utd_attack, Liverpool_attack, Tottenham_attack, Chelsea_attack, Wolverhampton_attack, West_Ham_attack, Newcastle_attack]
    PL_defence = [Arsenal_defence, Man_City_defence, Man_Utd_defence, Liverpool_defence, Tottenham_defence, Chelsea_defence, Wolverhampton_defence, West_Ham_defence, Newcastle_defence]
    PL_fieldown = [Arsenal_fieldown, Man_City_fieldown, Man_Utd_fieldown, Liverpool_fieldown, Tottenham_fieldown, Chelsea_fieldown, Wolverhampton_fieldown, West_Ham_fieldown, Newcastle_fieldown]
    PL_Random = random.choice(PL)
    PL_attack_Random = random.choice(PL_attack)
    if PL_Random == Arsenal:
        a = random.randint(-3, 3)
        b = random.randint(-3, 3)
        c = random.randint(-3, 3)
        Arsenal_attack + a
        Arsenal_defence + b
        Arsenal_fieldown + c
        print("아스날은 투자한 결과 다음과 같이 전력이 보강되었습니다:")
        print("공격진 : ", Arsenal_attack)
        print("수비진 : ", Arsenal_defence)
        print("중원 지배력", Arsenal_fieldown)
    elif PL_Random == Man_City:
        a = random.randint(-3, 3)
        b = random.randint(-3, 3)
        c = random.randint(-3, 3)
        Man_City_attack + a
        Man_City_defence + b
        Man_City_fieldown + c
        print("맨시티는 투자한 결과 다음과 같이 전력이 보강되었습니다:")
        print("공격진 : ", Man_City_attack)
        print("수비진 : ", Man_City_defence)
        print("중원 지배력", Man_City_fieldown)
    elif PL_Random == Liverpool:
        a = random.randint(-3, 3)
        b = random.randint(-3, 3)
        c = random.randint(-3, 3)
        Liverpool_attack + a
        Liverpool_defence + b
        Liverpool_fieldown + c
        print("리버풀은 투자한 결과 다음과 같이 전력이 보강되었습니다:")
        print("공격진 : ", Liverpool_attack)
        print("수비진 : ", Liverpool_defence)
        print("중원 지배력", Liverpool_fieldown)
    elif PL_Random == Tottenham:
        a = random.randint(-3, 3)
        b = random.randint(-3, 3)
        c = random.randint(-3, 3)
        Tottenham_attack + a
        Tottenham_defence + b
        Tottenham_fieldown + c
        print("토트넘은 투자한 결과 다음과 같이 전력이 보강되었습니다:")
        print("공격진 : ", Tottenham_attack)
        print("수비진 : ", Tottenham_defence)
        print("중원 지배력", Tottenham_fieldown)
    elif PL_Random == Chelsea:
        a = random.randint(-3, 3)
        b = random.randint(-3, 3)
        c = random.randint(-3, 3)
        Chelsea_attack + a
        Chelsea_defence + b
        Chelsea_fieldown + c
        print("첼시는 투자한 결과 다음과 같이 전력이 보강되었습니다:")
        print("공격진 : ", Chelsea_attack)
        print("수비진 : ", Chelsea_defence)
        print("중원 지배력", Chelsea_fieldown)
    elif PL_Random == Wolverhampton:
        a = random.randint(-3, 3)
        b = random.randint(-3, 3)
        c = random.randint(-3, 3)
        Wolverhampton_attack + a
        Wolverhampton_defence + b
        Wolverhampton_fieldown + c
        print("첼시는 투자한 결과 다음과 같이 전력이 보강되었습니다:")
        print("공격진 : ", Wolverhampton_attack)
        print("수비진 : ", Wolverhampton_defence)
        print("중원 지배력", Wolverhampton_fieldown)
    elif PL_Random == West_Ham:
        a = random.randint(-3, 3)
        b = random.randint(-3, 3)
        c = random.randint(-3, 3)
        West_Ham_attack + a
        West_Ham_defence + b
        West_Ham_fieldown + c
        print("웨스트햄은 투자한 결과 다음과 같이 전력이 보강되었습니다:")
        print("공격진 : ", West_Ham_attack)
        print("수비진 : ", West_Ham_defence)
        print("중원 지배력", West_Ham_fieldown)
    elif PL_Random == Newcastle:
        a = random.randint(-3, 3)
        b = random.randint(-3, 3)
        c = random.randint(-3, 3)
        Newcastle_attack + a
        Newcastle_defence + b
        Newcastle_fieldown + c
        print("뉴캐슬은 투자한 결과 다음과 같이 전력이 보강되었습니다:")
        print("공격진 : ", Newcastle_attack)
        print("수비진 : ", Newcastle_defence)
        print("중원 지배력", Newcastle_fieldown)

아스날_승점 = 0
맨시티_승점 = 0
맨유_승점 = 0
리버풀_승점 = 0
토트넘_승점 = 0
첼시_승점 = 0
울버햄튼_승점 = 0
웨스트햄_승점 = 0
뉴캐슬_승점 = 0

# def Pre_MW():
#     print("Pre-Matchweek\n투자할 부분을 선택하세요 : 트레이닝, 시설확충, 구단홍보")
#     c_arsenal = input("선택 : ")
#     if c_arsenal == "트레이닝":
#         print("트레이닝을 선택하셨습니다. 중원 지배 능력치 +1")
#         Arsenal_fieldown = Arsenal_fieldown + 1
#         print("다른 팀 1개의 투자를 랜덤으로 살펴보겠습니다.")
#         random_choice()
#     elif c_arsenal == "시설확충":
#         print("시설확충을 선택하셨습니다. 공격력 +1")
#         Arsenal_attack = Arsenal_attack + 1
#         print("다른 팀 1개의 투자를 랜덤으로 살펴보겠습니다.")
#         random_choice()
#     else:
#         print("구단홍보를 선택하셨습니다. 수비력 +1")
#         Arsenal_defence = Arsenal_defence + 1
#         print("다른 팀 1개의 투자를 랜덤으로 살펴보겠습니다.")
#         random_choice()
    

n = 0
def Arsenal_Run():
    # UnboundLocalError: cannot access local variable '승점' where it is not associated with a value 이거 안뜨게 하려면 함수 안에서 변수를 초기화 시켜줘야 한다.
    n = 0
    Arsenal_attack = 5
    Arsenal_defence = 5
    Arsenal_fieldown = 6
    print("Pre-Matchweek\n투자할 부분을 선택하세요 : 트레이닝, 시설확충, 구단홍보")
    c_arsenal = input("선택 : ")
    if c_arsenal == "트레이닝":
        print("트레이닝을 선택하셨습니다. 중원 지배 능력치 +1")
        Arsenal_fieldown = Arsenal_fieldown + 1
        print("다른 팀 1개의 투자를 랜덤으로 살펴보겠습니다.")
        random_choice()
    elif c_arsenal == "시설확충":
        print("시설확충을 선택하셨습니다. 공격력 +1")
        Arsenal_attack = Arsenal_fieldown + 1
        print("다른 팀 1개의 투자를 랜덤으로 살펴보겠습니다.")
        random_choice()
    else:
        print("구단홍보를 선택하셨습니다. 수비력 +1")
        Arsenal_defence = Arsenal_defence + 1
        print("다른 팀 1개의 투자를 랜덤으로 살펴보겠습니다.")
        random_choice()
    아스날_승점 = 0
    맨시티_승점 = 0
    맨유_승점 = 0
    리버풀_승점 = 0
    토트넘_승점 = 0
    첼시_승점 = 0
    울버햄튼_승점 = 0
    웨스트햄_승점 = 0
    뉴캐슬_승점 = 0
    아스날_승점 = 아스날_승점 + 0
    맨시티_승점 = 맨시티_승점 + 0
    맨유_승점 = 맨유_승점 + 0
    리버풀_승점 = 리버풀_승점 + 0
    토트넘_승점 = 토트넘_승점 + 0
    첼시_승점 = 첼시_승점 + 0
    울버햄튼_승점 = 울버햄튼_승점 + 0
    웨스트햄_승점 = 웨스트햄_승점 + 0
    뉴캐슬_승점 = 뉴캐슬_승점 + 0
    a = str(input("다음 단계로 넘어가려면 Y를 입력해주세요.\n"))
    if a == "Y":
        print("2주가 흘렀습니다.\n--------------------------------------------\nMatchweek 1 - Away (St. James Park)\n--------------------------------------------\nNewcastle F.C.(HOME) vs Arsenal F.C.(AWAY)\n")
        print("뉴캐슬 vs 아스날 전력 분석\n뉴캐슬의 vs 아스날의\n공격력은 {} vs {}입니다.\n수비력은 {} vs {}입니다.\n중원 지배력은 {} vs {}입니다.\n".format(Newcastle_attack, Arsenal_attack, Newcastle_defence, Arsenal_defence, Newcastle_fieldown, Arsenal_fieldown))
        b = input(("포메이션을 선택하세요 : 3-4-3, 4-3-3, 4-2-3-1\n공격 우선 : 3-4-3, 수비 우선 : 4-3-3, 둘 다 : 4-2-3-1\n"))
        if b == "3-4-3":
            if (Arsenal_attack > Newcastle_attack and Arsenal_defence >= Newcastle_defence and Arsenal_fieldown >= Newcastle_fieldown) or (Arsenal_attack > Newcastle_attack and Arsenal_defence >= Newcastle_defence and Arsenal_fieldown < Newcastle_fieldown) or (Arsenal_attack == Newcastle_attack and Arsenal_defence >= Newcastle_defence and Arsenal_fieldown >= Newcastle_fieldown):
                print("--------------------------------------------\n{} - {}, 아스날 승\n--------------------------------------------".format(random.randint(0, 1), random.randint(2, 4)))
                아스날_승점 = 아스날_승점 + 3
            elif (Arsenal_attack > Newcastle_attack and Arsenal_defence < Newcastle_defence and Arsenal_fieldown >= Newcastle_fieldown) or (Arsenal_attack == Newcastle_attack and Arsenal_defence < Newcastle_defence and Arsenal_fieldown >= Newcastle_fieldown) or (Arsenal_attack == Newcastle_attack and Arsenal_defence >= Newcastle_defence and Arsenal_fieldown < Newcastle_fieldown) or  (Arsenal_attack < Newcastle_attack and Arsenal_defence >= Newcastle_defence and Arsenal_fieldown >= Newcastle_fieldown):
                print("--------------------------------------------\n{} - {}, 무승부\n--------------------------------------------".format(random.randint(2, 2), random.randint(2, 2)))
                아스날_승점 = 아스날_승점 + 1
            elif (Arsenal_attack > Newcastle_attack and Arsenal_defence < Newcastle_defence and Arsenal_fieldown < Newcastle_fieldown) or (Arsenal_attack == Newcastle_attack and Arsenal_defence < Newcastle_defence and Arsenal_fieldown < Newcastle_fieldown) or (Arsenal_attack < Newcastle_attack and Arsenal_defence < Newcastle_defence and Arsenal_fieldown >= Newcastle_fieldown) or (Arsenal_attack < Newcastle_attack and Arsenal_defence >= Newcastle_defence and Arsenal_fieldown < Newcastle_fieldown) or  (Arsenal_attack < Newcastle_attack and Arsenal_defence < Newcastle_defence and Arsenal_fieldown < Newcastle_fieldown):
                print("--------------------------------------------\n{} - {}, 뉴캐슬 승\n--------------------------------------------".format(random.randint(2, 3), random.randint(0, 1)))
                아스날_승점 = 아스날_승점 + 0
        elif b == "4-3-3":
            if (Arsenal_defence > Newcastle_defence and Arsenal_attack >= Newcastle_attack and Arsenal_fieldown >= Newcastle_fieldown) or (Arsenal_defence > Newcastle_defence and Arsenal_attack >= Newcastle_attack and Arsenal_fieldown < Newcastle_fieldown) or (Arsenal_defence == Newcastle_defence and Arsenal_attack >= Newcastle_attack and Arsenal_fieldown >= Newcastle_fieldown):
                print("--------------------------------------------\n{} - {}, 아스날 승\n--------------------------------------------".format(random.randint(0, 1), random.randint(2, 3)))
                아스날_승점 = 아스날_승점 + 3
            elif (Arsenal_defence > Newcastle_defence and Arsenal_attack < Newcastle_attack and Arsenal_fieldown >= Newcastle_fieldown) or (Arsenal_defence == Newcastle_defence and Arsenal_attack < Newcastle_attack and Arsenal_fieldown >= Newcastle_fieldown) or (Arsenal_defence == Newcastle_defence and Arsenal_attack >= Newcastle_attack and Arsenal_fieldown < Newcastle_fieldown) or  (Arsenal_defence < Newcastle_defence and Arsenal_attack >= Newcastle_attack and Arsenal_fieldown >= Newcastle_fieldown):
                print("--------------------------------------------\n{} - {}, 무승부\n--------------------------------------------".format(random.randint(2, 2), random.randint(2, 2)))
                아스날_승점 = 아스날_승점 + 1
            elif (Arsenal_defence > Newcastle_defence and Arsenal_attack < Newcastle_attack and Arsenal_fieldown < Newcastle_fieldown) or (Arsenal_defence == Newcastle_defence and Arsenal_attack < Newcastle_attack and Arsenal_fieldown < Newcastle_fieldown) or (Arsenal_defence < Newcastle_defence and Arsenal_attack < Newcastle_attack and Arsenal_fieldown >= Newcastle_fieldown) or (Arsenal_defence < Newcastle_defence and Arsenal_attack >= Newcastle_attack and Arsenal_fieldown < Newcastle_fieldown) or  (Arsenal_defence < Newcastle_defence and Arsenal_attack < Newcastle_attack and Arsenal_fieldown < Newcastle_fieldown):
                print("--------------------------------------------\n{} - {}, 뉴캐슬 승\n--------------------------------------------".format(random.randint(2, 4), random.randint(0, 1)))
                아스날_승점 = 아스날_승점 + 0
        elif b == "4-2-3-1":
            if (Arsenal_fieldown > Newcastle_fieldown and Arsenal_attack >= Newcastle_attack and Arsenal_defence >= Newcastle_defence) or (Arsenal_fieldown > Newcastle_fieldown and Arsenal_attack >= Newcastle_attack and Arsenal_defence < Newcastle_defence) or (Arsenal_fieldown == Newcastle_fieldown and Arsenal_attack >= Newcastle_attack and Arsenal_defence >= Newcastle_defence):
                print("--------------------------------------------\n{} - {}, 아스날 승\n--------------------------------------------".format(random.randint(0, 1), random.randint(2, 3)))
                아스날_승점 = 아스날_승점 + 3
            elif (Arsenal_fieldown > Newcastle_fieldown and Arsenal_attack < Newcastle_attack and Arsenal_defence >= Newcastle_defence) or (Arsenal_fieldown == Newcastle_fieldown and Arsenal_attack < Newcastle_attack and Arsenal_defence >= Newcastle_defence) or (Arsenal_fieldown == Newcastle_fieldown and Arsenal_attack >= Newcastle_attack and Arsenal_defence < Newcastle_defence) or  (Arsenal_fieldown < Newcastle_fieldown and Arsenal_attack >= Newcastle_attack and Arsenal_defence >= Newcastle_defence):
                print("--------------------------------------------\n{} - {}, 무승부\n--------------------------------------------".format(random.randint(2, 2), random.randint(2, 2)))
                아스날_승점 = 아스날_승점 + 1
            elif (Arsenal_fieldown > Newcastle_fieldown and Arsenal_attack < Newcastle_attack and Arsenal_defence < Newcastle_defence) or (Arsenal_fieldown == Newcastle_fieldown and Arsenal_attack < Newcastle_attack and Arsenal_defence < Newcastle_defence) or (Arsenal_fieldown < Newcastle_fieldown and Arsenal_attack < Newcastle_attack and Arsenal_defence >= Newcastle_defence) or (Arsenal_fieldown < Newcastle_fieldown and Arsenal_attack >= Newcastle_attack and Arsenal_defence < Newcastle_defence) or  (Arsenal_fieldown < Newcastle_fieldown and Arsenal_attack < Newcastle_attack and Arsenal_defence < Newcastle_defence):
                print("--------------------------------------------\n{} - {}, 뉴캐슬 승\n--------------------------------------------".format(random.randint(2, 4), random.randint(0, 1)))
                아스날_승점 = 아스날_승점 + 0
        n = n + 1
        print("[첫] 번째 경기를 무사히 끝냈습니다. 당신의 승점은 {}점 입니다".format(아스날_승점))
        print("{}주차 프리미어리그 순위".format(n))
        아스날_승점 = 아스날_승점
        맨시티_승점 = random.randint(0,3)
        리버풀_승점 = random.randint(0,3)
        맨유_승점 = random.randint(0,3)
        토트넘_승점 = random.randint(0,3)
        첼시_승점 = random.randint(0,3)
        울버햄튼_승점 = random.randint(0,3)
        웨스트햄_승점 = random.randint(0,3)
        뉴캐슬_승점 = random.randint(0,3)
        팀_승점 = {
        "아스날 FC": 아스날_승점,
        "맨체스터 시티 FC": 맨시티_승점,
        "맨체스터 유나이티드 FC" : 맨유_승점,
        "리버풀 FC" : 리버풀_승점,
        "토트넘 홋스퍼 FC" : 토트넘_승점,
        "첼시 FC" : 첼시_승점,
        "울버햄튼 원더러스 FC" : 울버햄튼_승점,
        "웨스트햄 유나이티드 FC" : 웨스트햄_승점,
        "뉴캐슬 FC" : 뉴캐슬_승점          
        }
        sorted_scoreboard = sorted(팀_승점.items(), key=lambda x: x[1], reverse=True)
        print("\nEngland Premier League\n")
        for 순위, (팀, 승점) in enumerate((sorted_scoreboard), start=1):
            print(f"{순위}위 : {팀} - {승점}점")
    a = str(input("다음 단계로 넘어가려면 Y를 입력해주세요.\n"))
    if a == "Y":
        print("Pre-Matchweek\n투자할 부분을 선택하세요 : 트레이닝, 시설확충, 구단홍보")
        c_arsenal = input("선택 : ")
        if c_arsenal == "트레이닝":
            print("트레이닝을 선택하셨습니다. 중원 지배 능력치 +1")
            Arsenal_fieldown = Arsenal_fieldown + 1
            print("다른 팀 1개의 투자를 랜덤으로 살펴보겠습니다.")
            random_choice()
        elif c_arsenal == "시설확충":
            print("시설확충을 선택하셨습니다. 공격력 +1")
            Arsenal_attack = Arsenal_fieldown + 1
            print("다른 팀 1개의 투자를 랜덤으로 살펴보겠습니다.")
            random_choice()
        else:
            print("구단홍보를 선택하셨습니다. 수비력 +1")
            Arsenal_defence = Arsenal_defence + 1
            print("다른 팀 1개의 투자를 랜덤으로 살펴보겠습니다.")
            random_choice()
        print("2주가 흘렀습니다.\n--------------------------------------------\nMatchweek 2 - Home (Emirates Stadium)\n--------------------------------------------\nArsenal F.C.(HOME) vs West Ham United F.C.(AWAY)\n")
        print("아스날 vs 웨스트햄 전력 분석\n웨스트햄의 vs 아스날의\n공격력은 {} vs {}입니다.\n수비력은 {} vs {}입니다.\n중원 지배력은 {} vs {}입니다.\n".format(West_Ham_attack, Arsenal_attack, West_Ham_defence, Arsenal_defence, West_Ham_fieldown, Arsenal_fieldown))
        b = input(("포메이션을 선택하세요 : 3-4-3, 4-3-3, 4-2-3-1\n공격 우선 : 3-4-3, 수비 우선 : 4-3-3, 둘 다 : 4-2-3-1\n"))
        if b == "3-4-3":
            if (Arsenal_attack > West_Ham_attack and Arsenal_defence >= West_Ham_defence and Arsenal_fieldown >= West_Ham_fieldown) or (Arsenal_attack > West_Ham_attack and Arsenal_defence >= West_Ham_defence and Arsenal_fieldown < West_Ham_fieldown) or (Arsenal_attack == West_Ham_attack and Arsenal_defence >= West_Ham_defence and Arsenal_fieldown >= West_Ham_fieldown):
                print("--------------------------------------------\n{} - {}, 아스날 승\n--------------------------------------------".format(random.randint(0, 1), random.randint(2, 4)))
                아스날_승점 = 아스날_승점 + 3
            elif (Arsenal_attack > West_Ham_attack and Arsenal_defence < West_Ham_defence and Arsenal_fieldown >= West_Ham_fieldown) or (Arsenal_attack == West_Ham_attack and Arsenal_defence < West_Ham_defence and Arsenal_fieldown >= West_Ham_fieldown) or (Arsenal_attack == West_Ham_attack and Arsenal_defence >= Newcastle_defence and Arsenal_fieldown < Newcastle_fieldown) or  (Arsenal_attack < West_Ham_attack and Arsenal_defence >= West_Ham_defence and Arsenal_fieldown >= West_Ham_fieldown):
                print("--------------------------------------------\n{} - {}, 무승부\n--------------------------------------------".format(random.randint(2, 2), random.randint(2, 2)))
                아스날_승점 = 아스날_승점 + 1
            elif (Arsenal_attack > West_Ham_attack and Arsenal_defence < West_Ham_defence and Arsenal_fieldown < West_Ham_fieldown) or (Arsenal_attack == West_Ham_attack and Arsenal_defence < West_Ham_defence and Arsenal_fieldown < West_Ham_fieldown) or (Arsenal_attack < West_Ham_attack and Arsenal_defence < West_Ham_defence and Arsenal_fieldown >= West_Ham_fieldown) or (Arsenal_attack < West_Ham_attack and Arsenal_defence >= West_Ham_defence and Arsenal_fieldown < West_Ham_fieldown) or  (Arsenal_attack < West_Ham_attack and Arsenal_defence < West_Ham_defence and Arsenal_fieldown < West_Ham_fieldown):
                print("--------------------------------------------\n{} - {}, 뉴캐슬 승\n--------------------------------------------".format(random.randint(2, 3), random.randint(0, 1)))
                아스날_승점 = 아스날_승점 + 0
        elif b == "4-3-3":
            if (Arsenal_defence > West_Ham_defence and Arsenal_attack >= West_Ham_attack and Arsenal_fieldown >= West_Ham_fieldown) or (Arsenal_defence > West_Ham_defence and Arsenal_attack >= West_Ham_attack and Arsenal_fieldown < West_Ham_fieldown) or (Arsenal_defence == West_Ham_defence and Arsenal_attack >= West_Ham_attack and Arsenal_fieldown >= West_Ham_fieldown):
                print("--------------------------------------------\n{} - {}, 아스날 승\n--------------------------------------------".format(random.randint(0, 1), random.randint(2, 3)))
                아스날_승점 = 아스날_승점 + 3
            elif (Arsenal_defence > West_Ham_defence and Arsenal_attack < West_Ham_attack and Arsenal_fieldown >= West_Ham_fieldown) or (Arsenal_defence == West_Ham_defence and Arsenal_attack < West_Ham_attack and Arsenal_fieldown >= West_Ham_fieldown) or (Arsenal_defence == West_Ham_defence and Arsenal_attack >= West_Ham_attack and Arsenal_fieldown < West_Ham_fieldown) or  (Arsenal_defence < West_Ham_defence and Arsenal_attack >= West_Ham_attack and Arsenal_fieldown >= West_Ham_fieldown):
                print("--------------------------------------------\n{} - {}, 무승부\n--------------------------------------------".format(random.randint(2, 2), random.randint(2, 2)))
                아스날_승점 = 아스날_승점 + 1
            elif (Arsenal_defence > West_Ham_defence and Arsenal_attack < West_Ham_attack and Arsenal_fieldown < West_Ham_fieldown) or (Arsenal_defence == West_Ham_defence and Arsenal_attack < West_Ham_attack and Arsenal_fieldown < West_Ham_fieldown) or (Arsenal_defence < West_Ham_defence and Arsenal_attack < West_Ham_attack and Arsenal_fieldown >= West_Ham_fieldown) or (Arsenal_defence < West_Ham_defence and Arsenal_attack >= West_Ham_attack and Arsenal_fieldown < West_Ham_fieldown) or  (Arsenal_defence < West_Ham_defence and Arsenal_attack < West_Ham_attack and Arsenal_fieldown < West_Ham_fieldown):
                print("--------------------------------------------\n{} - {}, 뉴캐슬 승\n--------------------------------------------".format(random.randint(2, 4), random.randint(0, 1)))
                아스날_승점 = 아스날_승점 + 0
        elif b == "4-2-3-1":
            if (Arsenal_fieldown > West_Ham_fieldown and Arsenal_attack >= West_Ham_attack and Arsenal_defence >= West_Ham_defence) or (Arsenal_fieldown > West_Ham_fieldown and Arsenal_attack >= West_Ham_attack and Arsenal_defence < West_Ham_defence) or (Arsenal_fieldown == West_Ham_fieldown and Arsenal_attack >= West_Ham_attack and Arsenal_defence >= West_Ham_defence):
                print("--------------------------------------------\n{} - {}, 아스날 승\n--------------------------------------------".format(random.randint(0, 1), random.randint(2, 3)))
                아스날_승점 = 아스날_승점 + 3
            elif (Arsenal_fieldown > West_Ham_fieldown and Arsenal_attack < West_Ham_attack and Arsenal_defence >= West_Ham_defence) or (Arsenal_fieldown == West_Ham_fieldown and Arsenal_attack < West_Ham_attack and Arsenal_defence >= West_Ham_defence) or (Arsenal_fieldown == West_Ham_fieldown and Arsenal_attack >= West_Ham_attack and Arsenal_defence < West_Ham_defence) or  (Arsenal_fieldown < West_Ham_fieldown and Arsenal_attack >= West_Ham_attack and Arsenal_defence >= West_Ham_defence):
                print("--------------------------------------------\n{} - {}, 무승부\n--------------------------------------------".format(random.randint(2, 2), random.randint(2, 2)))
                아스날_승점 = 아스날_승점 + 1
            elif (Arsenal_fieldown > West_Ham_fieldown and Arsenal_attack < West_Ham_attack and Arsenal_defence < West_Ham_defence) or (Arsenal_fieldown == West_Ham_fieldown and Arsenal_attack < West_Ham_attack and Arsenal_defence < West_Ham_defence) or (Arsenal_fieldown < West_Ham_fieldown and Arsenal_attack < West_Ham_attack and Arsenal_defence >= West_Ham_defence) or (Arsenal_fieldown < West_Ham_fieldown and Arsenal_attack >= West_Ham_attack and Arsenal_defence < West_Ham_defence) or  (Arsenal_fieldown < West_Ham_fieldown and Arsenal_attack < West_Ham_attack and Arsenal_defence < West_Ham_defence):
                print("--------------------------------------------\n{} - {}, 뉴캐슬 승\n--------------------------------------------".format(random.randint(2, 4), random.randint(0, 1)))
                아스날_승점 = 아스날_승점 + 0
        n = n + 1
        print("[두] 번째 경기를 무사히 끝냈습니다. 당신의 승점은 {}점 입니다".format(아스날_승점))
        print("{}주차 프리미어리그 순위".format(n))
        아스날_승점 = 아스날_승점
        맨시티_승점 = random.randint(0,3) + 맨시티_승점
        리버풀_승점 = random.randint(0,3) + 리버풀_승점
        맨유_승점 = random.randint(0,3) + 맨유_승점
        토트넘_승점 = random.randint(0,3) + 토트넘_승점
        첼시_승점 = random.randint(0,3) + 첼시_승점
        울버햄튼_승점 = random.randint(0,3) + 울버햄튼_승점
        웨스트햄_승점 = random.randint(0,3) + 웨스트햄_승점
        뉴캐슬_승점 = random.randint(0,3) + 뉴캐슬_승점
        팀_승점 = {
        "아스날 FC": 아스날_승점,
        "맨체스터 시티 FC": 맨시티_승점,
        "맨체스터 유나이티드 FC" : 맨유_승점,
        "리버풀 FC" : 리버풀_승점,
        "토트넘 홋스퍼 FC" : 토트넘_승점,
        "첼시 FC" : 첼시_승점,
        "울버햄튼 원더러스 FC" : 울버햄튼_승점,
        "웨스트햄 유나이티드 FC" : 웨스트햄_승점,
        "뉴캐슬 FC" : 뉴캐슬_승점          
        }
        sorted_scoreboard = sorted(팀_승점.items(), key=lambda x: x[1], reverse=True)
        print("\nEngland Premier League\n")
        for 순위, (팀, 승점) in enumerate((sorted_scoreboard), start=1):
            print(f"{순위}위 : {팀} - {승점}점")
        a = str(input("다음 단계로 넘어가려면 Y를 입력해주세요.\n"))
    if a == "Y":
        print("Pre-Matchweek\n투자할 부분을 선택하세요 : 트레이닝, 시설확충, 구단홍보")
        c_arsenal = input("선택 : ")
        if c_arsenal == "트레이닝":
            print("트레이닝을 선택하셨습니다. 중원 지배 능력치 +1")
            Arsenal_fieldown = Arsenal_fieldown + 1
            print("다른 팀 1개의 투자를 랜덤으로 살펴보겠습니다.")
            random_choice()
        elif c_arsenal == "시설확충":
            print("시설확충을 선택하셨습니다. 공격력 +1")
            Arsenal_attack = Arsenal_fieldown + 1
            print("다른 팀 1개의 투자를 랜덤으로 살펴보겠습니다.")
            random_choice()
        else:
            print("구단홍보를 선택하셨습니다. 수비력 +1")
            Arsenal_defence = Arsenal_defence + 1
            print("다른 팀 1개의 투자를 랜덤으로 살펴보겠습니다.")
            random_choice()
    if a == "Y":
        print("2주가 흘렀습니다.\n--------------------------------------------\nMatchweek 3 - Away (Molineux Stadium)\n--------------------------------------------\nNewcastle F.C.(HOME) vs Arsenal F.C.(AWAY)\n")
        print("울버햄튼 vs 아스날 전력 분석\n뉴캐슬의 vs 아스날의\n공격력은 {} vs {}입니다.\n수비력은 {} vs {}입니다.\n중원 지배력은 {} vs {}입니다.\n".format(Newcastle_attack, Arsenal_attack, Newcastle_defence, Arsenal_defence, Newcastle_fieldown, Arsenal_fieldown))
        b = input(("포메이션을 선택하세요 : 3-4-3, 4-3-3, 4-2-3-1\n공격 우선 : 3-4-3, 수비 우선 : 4-3-3, 둘 다 : 4-2-3-1\n"))
        if b == "3-4-3":
            if (Arsenal_attack > Wolverhampton_attack and Arsenal_defence >= Wolverhampton_defence and Arsenal_fieldown >= Wolverhampton_fieldown) or (Arsenal_attack > Wolverhampton_attack and Arsenal_defence >= Newcastle_defence and Arsenal_fieldown < Newcastle_fieldown) or (Arsenal_attack == Newcastle_attack and Arsenal_defence >= Newcastle_defence and Arsenal_fieldown >= Newcastle_fieldown):
                print("--------------------------------------------\n{} - {}, 아스날 승\n--------------------------------------------".format(random.randint(0, 1), random.randint(2, 4)))
                아스날_승점 = 아스날_승점 + 3
            elif (Arsenal_attack > Wolverhampton_attack and Arsenal_defence < Wolverhampton_defence and Arsenal_fieldown >= Wolverhampton_fieldown) or (Arsenal_attack == Wolverhampton_attack and Arsenal_defence < Wolverhampton_defence and Arsenal_fieldown >= Wolverhampton_fieldown) or (Arsenal_attack == Wolverhampton_attack and Arsenal_defence >= Wolverhampton_defence and Arsenal_fieldown < Wolverhampton_fieldown) or (Arsenal_attack < Wolverhampton_attack and Arsenal_defence >= Wolverhampton_defence and Arsenal_fieldown >= Wolverhampton_fieldown):
                print("--------------------------------------------\n{} - {}, 무승부\n--------------------------------------------".format(random.randint(2, 2), random.randint(2, 2)))
                아스날_승점 = 아스날_승점 + 1
            elif (Arsenal_attack > Wolverhampton_attack and Arsenal_defence < Wolverhampton_defence and Arsenal_fieldown < Wolverhampton_fieldown) or (Arsenal_attack == Wolverhampton_attack and Arsenal_defence < Wolverhampton_defence and Arsenal_fieldown < Wolverhampton_fieldown) or (Arsenal_attack < Wolverhampton_attack and Arsenal_defence < Wolverhampton_defence and Arsenal_fieldown >= Wolverhampton_fieldown) or (Arsenal_attack < Wolverhampton_attack and Arsenal_defence >= Wolverhampton_defence and Arsenal_fieldown < Wolverhampton_fieldown) or (Arsenal_attack < Wolverhampton_attack and Arsenal_defence < Wolverhampton_defence and Arsenal_fieldown < Wolverhampton_fieldown):
                print("--------------------------------------------\n{} - {}, 뉴캐슬 승\n--------------------------------------------".format(random.randint(2, 3), random.randint(0, 1)))
                아스날_승점 = 아스날_승점 + 0
        elif b == "4-3-3":
            if (Arsenal_defence > Wolverhampton_defence and Arsenal_attack >= Wolverhampton_attack and Arsenal_fieldown >= Wolverhampton_fieldown) or (Arsenal_defence > Wolverhampton_defence and Arsenal_attack >= Wolverhampton_attack and Arsenal_fieldown < Wolverhampton_fieldown) or (Arsenal_defence == Wolverhampton_defence and Arsenal_attack >= Wolverhampton_attack and Arsenal_fieldown >= Wolverhampton_fieldown):
                print("--------------------------------------------\n{} - {}, 아스날 승\n--------------------------------------------".format(random.randint(0, 1), random.randint(2, 3)))
                아스날_승점 = 아스날_승점 + 3
            elif (Arsenal_defence > Wolverhampton_defence and Arsenal_attack < Wolverhampton_attack and Arsenal_fieldown >= Wolverhampton_fieldown) or (Arsenal_defence == Wolverhampton_defence and Arsenal_attack < Wolverhampton_attack and Arsenal_fieldown >= Wolverhampton_fieldown) or (Arsenal_defence == Wolverhampton_defence and Arsenal_attack >= Wolverhampton_attack and Arsenal_fieldown < Wolverhampton_fieldown) or  (Arsenal_defence < Wolverhampton_defence and Arsenal_attack >= Wolverhampton_attack and Arsenal_fieldown >= Wolverhampton_fieldown):
                print("--------------------------------------------\n{} - {}, 무승부\n--------------------------------------------".format(random.randint(2, 2), random.randint(2, 2)))
                아스날_승점 = 아스날_승점 + 1
            elif (Arsenal_defence > Wolverhampton_defence and Arsenal_attack < Wolverhampton_attack and Arsenal_fieldown < Wolverhampton_fieldown) or (Arsenal_defence == Wolverhampton_defence and Arsenal_attack < Wolverhampton_attack and Arsenal_fieldown < Wolverhampton_fieldown) or (Arsenal_defence < Wolverhampton_defence and Arsenal_attack < Wolverhampton_attack and Arsenal_fieldown >= Wolverhampton_fieldown) or (Arsenal_defence < Wolverhampton_defence and Arsenal_attack >= Wolverhampton_attack and Arsenal_fieldown < Wolverhampton_fieldown) or (Arsenal_defence < Wolverhampton_defence and Arsenal_attack < Wolverhampton_attack and Arsenal_fieldown < Wolverhampton_fieldown):
                print("--------------------------------------------\n{} - {}, 울버햄튼 승\n--------------------------------------------".format(random.randint(2, 4), random.randint(0, 1)))
                아스날_승점 = 아스날_승점 + 0
        elif b == "4-2-3-1":
            if (Arsenal_fieldown > Wolverhampton_fieldown and Arsenal_attack >= Wolverhampton_attack and Arsenal_defence >= Wolverhampton_defence) or (Arsenal_fieldown > Wolverhampton_fieldown and Arsenal_attack >= Wolverhampton_attack and Arsenal_defence < Wolverhampton_defence) or (Arsenal_fieldown == Wolverhampton_fieldown and Arsenal_attack >= Wolverhampton_attack and Arsenal_defence >= Wolverhampton_defence):
                print("--------------------------------------------\n{} - {}, 아스날 승\n--------------------------------------------".format(random.randint(0, 1), random.randint(2, 3)))
                아스날_승점 = 아스날_승점 + 3
            elif (Arsenal_fieldown > Wolverhampton_fieldown and Arsenal_attack < Wolverhampton_attack and Arsenal_defence >= Wolverhampton_defence) or (Arsenal_fieldown == Wolverhampton_fieldown and Arsenal_attack < Wolverhampton_attack and Arsenal_defence >= Wolverhampton_defence) or (Arsenal_fieldown == Wolverhampton_fieldown and Arsenal_attack >= Wolverhampton_attack and Arsenal_defence < Wolverhampton_defence) or  (Arsenal_fieldown < Wolverhampton_fieldown and Arsenal_attack >= Wolverhampton_attack and Arsenal_defence >= Wolverhampton_defence):
                print("--------------------------------------------\n{} - {}, 무승부\n--------------------------------------------".format(random.randint(2, 2), random.randint(2, 2)))
                아스날_승점 = 아스날_승점 + 1
            elif (Arsenal_fieldown > Wolverhampton_fieldown and Arsenal_attack < Wolverhampton_attack and Arsenal_defence < Wolverhampton_defence) or (Arsenal_fieldown == Wolverhampton_fieldown and Arsenal_attack < Wolverhampton_attack and Arsenal_defence < Wolverhampton_defence) or (Arsenal_fieldown < Wolverhampton_fieldown and Arsenal_attack < Wolverhampton_attack and Arsenal_defence >= Wolverhampton_defence) or (Arsenal_fieldown < Wolverhampton_fieldown and Arsenal_attack >= Wolverhampton_attack and Arsenal_defence < Wolverhampton_defence) or  (Arsenal_fieldown < Wolverhampton_fieldown and Arsenal_attack < Wolverhampton_attack and Arsenal_defence < Wolverhampton_defence):
                print("--------------------------------------------\n{} - {}, 울버햄튼 승\n--------------------------------------------".format(random.randint(2, 4), random.randint(0, 1)))
                아스날_승점 = 아스날_승점 + 0
        n = n + 1
        print("[세] 번째 경기를 무사히 끝냈습니다. 당신의 승점은 {}점 입니다".format(아스날_승점))
        print("{}주차 프리미어리그 순위".format(n))
        아스날_승점 = 아스날_승점
        맨시티_승점 = random.randint(0,3) + 맨시티_승점
        리버풀_승점 = random.randint(0,3) + 리버풀_승점
        맨유_승점 = random.randint(0,3) + 맨유_승점
        토트넘_승점 = random.randint(0,3) + 토트넘_승점
        첼시_승점 = random.randint(0,3) + 첼시_승점
        울버햄튼_승점 = random.randint(0,3) + 울버햄튼_승점
        웨스트햄_승점 = random.randint(0,3) + 웨스트햄_승점
        뉴캐슬_승점 = random.randint(0,3) + 뉴캐슬_승점
        팀_승점 = {
        "아스날 FC": 아스날_승점,
        "맨체스터 시티 FC": 맨시티_승점,
        "맨체스터 유나이티드 FC" : 맨유_승점,
        "리버풀 FC" : 리버풀_승점,
        "토트넘 홋스퍼 FC" : 토트넘_승점,
        "첼시 FC" : 첼시_승점,
        "울버햄튼 원더러스 FC" : 울버햄튼_승점,
        "웨스트햄 유나이티드 FC" : 웨스트햄_승점,
        "뉴캐슬 FC" : 뉴캐슬_승점          
        }
        sorted_scoreboard = sorted(팀_승점.items(), key=lambda x: x[1], reverse=True)
        print("\nEngland Premier League\n")
        for 순위, (팀, 승점) in enumerate((sorted_scoreboard), start=1):
            print(f"{순위}위 : {팀} - {승점}점")
    a = str(input("다음 단계로 넘어가려면 Y를 입력해주세요.\n"))
    if a == "Y":
        print("Pre-Matchweek\n투자할 부분을 선택하세요 : 트레이닝, 시설확충, 구단홍보")
        c_arsenal = input("선택 : ")
        if c_arsenal == "트레이닝":
            print("트레이닝을 선택하셨습니다. 중원 지배 능력치 +1")
            Arsenal_fieldown = Arsenal_fieldown + 1
            print("다른 팀 1개의 투자를 랜덤으로 살펴보겠습니다.")
            random_choice()
        elif c_arsenal == "시설확충":
            print("시설확충을 선택하셨습니다. 공격력 +1")
            Arsenal_attack = Arsenal_fieldown + 1
            print("다른 팀 1개의 투자를 랜덤으로 살펴보겠습니다.")
            random_choice()
        else:
            print("구단홍보를 선택하셨습니다. 수비력 +1")
            Arsenal_defence = Arsenal_defence + 1
            print("다른 팀 1개의 투자를 랜덤으로 살펴보겠습니다.")
            random_choice()
    if a == "Y":
        print("2주가 흘렀습니다.\n--------------------------------------------\nMatchweek 4 - Home (Emirates Stadium)\n--------------------------------------------\nArsenal F.C.(HOME) vs Chelsea F.C.(AWAY)\n")
        print("아스날 vs 첼시 전력 분석\n아스날의 vs 첼시의\n공격력은 {} vs {}입니다.\n수비력은 {} vs {}입니다.\n중원 지배력은 {} vs {}입니다.\n".format(Arsenal_attack, Chelsea_attack, Arsenal_defence, Chelsea_defence, Arsenal_fieldown, Chelsea_fieldown))
        b = input(("포메이션을 선택하세요 : 3-4-3, 4-3-3, 4-2-3-1\n공격 우선 : 3-4-3, 수비 우선 : 4-3-3, 둘 다 : 4-2-3-1\n"))
        if b == "3-4-3":
            if (Arsenal_attack > Chelsea_attack and Arsenal_defence >= Chelsea_defence and Arsenal_fieldown >= Chelsea_fieldown) or (Arsenal_attack > Chelsea_attack and Arsenal_defence >= Newcastle_defence and Arsenal_fieldown < Newcastle_fieldown) or (Arsenal_attack == Newcastle_attack and Arsenal_defence >= Newcastle_defence and Arsenal_fieldown >= Newcastle_fieldown):
                print("--------------------------------------------\n{} - {}, 아스날 승\n--------------------------------------------".format(random.randint(0, 1), random.randint(2, 4)))
                아스날_승점 = 아스날_승점 + 3
            elif (Arsenal_attack > Chelsea_attack and Arsenal_defence < Chelsea_defence and Arsenal_fieldown >= Chelsea_fieldown) or (Arsenal_attack == Chelsea_attack and Arsenal_defence < Chelsea_defence and Arsenal_fieldown >= Chelsea_fieldown) or (Arsenal_attack == Chelsea_attack and Arsenal_defence >= Chelsea_defence and Arsenal_fieldown < Chelsea_fieldown) or (Arsenal_attack < Chelsea_attack and Arsenal_defence >= Chelsea_defence and Arsenal_fieldown >= Chelsea_fieldown):
                print("--------------------------------------------\n{} - {}, 무승부\n--------------------------------------------".format(random.randint(2, 2), random.randint(2, 2)))
                아스날_승점 = 아스날_승점 + 1
            elif (Arsenal_attack > Chelsea_attack and Arsenal_defence < Chelsea_defence and Arsenal_fieldown < Chelsea_fieldown) or (Arsenal_attack == Chelsea_attack and Arsenal_defence < Chelsea_defence and Arsenal_fieldown < Chelsea_fieldown) or (Arsenal_attack < Chelsea_attack and Arsenal_defence < Chelsea_defence and Arsenal_fieldown >= Chelsea_fieldown) or (Arsenal_attack < Chelsea_attack and Arsenal_defence >= Chelsea_defence and Arsenal_fieldown < Chelsea_fieldown) or (Arsenal_attack < Chelsea_attack and Arsenal_defence < Chelsea_defence and Arsenal_fieldown < Chelsea_fieldown):
                print("--------------------------------------------\n{} - {}, 첼시 승\n--------------------------------------------".format(random.randint(2, 3), random.randint(0, 1)))
                아스날_승점 = 아스날_승점 + 0
        elif b == "4-3-3":
            if (Arsenal_defence > Chelsea_defence and Arsenal_attack >= Chelsea_attack and Arsenal_fieldown >= Chelsea_fieldown) or (Arsenal_defence > Chelsea_defence and Arsenal_attack >= Chelsea_attack and Arsenal_fieldown < Chelsea_fieldown) or (Arsenal_defence == Chelsea_defence and Arsenal_attack >= Chelsea_attack and Arsenal_fieldown >= Chelsea_fieldown):
                print("--------------------------------------------\n{} - {}, 아스날 승\n--------------------------------------------".format(random.randint(0, 1), random.randint(2, 3)))
                아스날_승점 = 아스날_승점 + 3
            elif (Arsenal_defence > Chelsea_defence and Arsenal_attack < Chelsea_attack and Arsenal_fieldown >= Chelsea_fieldown) or (Arsenal_defence == Chelsea_defence and Arsenal_attack < Chelsea_attack and Arsenal_fieldown >= Chelsea_fieldown) or (Arsenal_defence == Chelsea_defence and Arsenal_attack >= Chelsea_attack and Arsenal_fieldown < Chelsea_fieldown) or  (Arsenal_defence < Chelsea_defence and Arsenal_attack >= Chelsea_attack and Arsenal_fieldown >= Chelsea_fieldown):
                print("--------------------------------------------\n{} - {}, 무승부\n--------------------------------------------".format(random.randint(2, 2), random.randint(2, 2)))
                아스날_승점 = 아스날_승점 + 1
            elif (Arsenal_defence > Chelsea_defence and Arsenal_attack < Chelsea_attack and Arsenal_fieldown < Chelsea_fieldown) or (Arsenal_defence == Chelsea_defence and Arsenal_attack < Chelsea_attack and Arsenal_fieldown < Chelsea_fieldown) or (Arsenal_defence < Chelsea_defence and Arsenal_attack < Chelsea_attack and Arsenal_fieldown >= Chelsea_fieldown) or (Arsenal_defence < Chelsea_defence and Arsenal_attack >= Chelsea_attack and Arsenal_fieldown < Chelsea_fieldown) or (Arsenal_defence < Chelsea_defence and Arsenal_attack < Chelsea_attack and Arsenal_fieldown < Chelsea_fieldown):
                print("--------------------------------------------\n{} - {}, 첼시 승\n--------------------------------------------".format(random.randint(2, 4), random.randint(0, 1)))
                아스날_승점 = 아스날_승점 + 0
        elif b == "4-2-3-1":
            if (Arsenal_fieldown > Chelsea_fieldown and Arsenal_attack >= Chelsea_attack and Arsenal_defence >= Chelsea_defence) or (Arsenal_fieldown > Chelsea_fieldown and Arsenal_attack >= Chelsea_attack and Arsenal_defence < Chelsea_defence) or (Arsenal_fieldown == Chelsea_fieldown and Arsenal_attack >= Chelsea_attack and Arsenal_defence >= Chelsea_defence):
                print("--------------------------------------------\n{} - {}, 아스날 승\n--------------------------------------------".format(random.randint(0, 1), random.randint(2, 3)))
                아스날_승점 = 아스날_승점 + 3
            elif (Arsenal_fieldown > Chelsea_fieldown and Arsenal_attack < Chelsea_attack and Arsenal_defence >= Chelsea_defence) or (Arsenal_fieldown == Chelsea_fieldown and Arsenal_attack < Chelsea_attack and Arsenal_defence >= Chelsea_defence) or (Arsenal_fieldown == Chelsea_fieldown and Arsenal_attack >= Chelsea_attack and Arsenal_defence < Chelsea_defence) or  (Arsenal_fieldown < Chelsea_fieldown and Arsenal_attack >= Chelsea_attack and Arsenal_defence >= Chelsea_defence):
                print("--------------------------------------------\n{} - {}, 무승부\n--------------------------------------------".format(random.randint(2, 2), random.randint(2, 2)))
                아스날_승점 = 아스날_승점 + 1
            elif (Arsenal_fieldown > Chelsea_fieldown and Arsenal_attack < Chelsea_attack and Arsenal_defence < Chelsea_defence) or (Arsenal_fieldown == Chelsea_fieldown and Arsenal_attack < Chelsea_attack and Arsenal_defence < Chelsea_defence) or (Arsenal_fieldown < Chelsea_fieldown and Arsenal_attack < Chelsea_attack and Arsenal_defence >= Chelsea_defence) or (Arsenal_fieldown < Chelsea_fieldown and Arsenal_attack >= Chelsea_attack and Arsenal_defence < Chelsea_defence) or  (Arsenal_fieldown < Chelsea_fieldown and Arsenal_attack < Chelsea_attack and Arsenal_defence < Chelsea_defence):
                print("--------------------------------------------\n{} - {}, 첼시 승\n--------------------------------------------".format(random.randint(2, 4), random.randint(0, 1)))
                아스날_승점 = 아스날_승점 + 0
        n = n + 1
        print("[네] 번째 경기를 무사히 끝냈습니다. 당신의 승점은 {}점 입니다".format(아스날_승점))
        print("{}주차 프리미어리그 순위".format(n))
        아스날_승점 = 아스날_승점
        맨시티_승점 = random.randint(0,3) + 맨시티_승점
        리버풀_승점 = random.randint(0,3) + 리버풀_승점
        맨유_승점 = random.randint(0,3) + 맨유_승점
        토트넘_승점 = random.randint(0,3) + 토트넘_승점
        첼시_승점 = random.randint(0,3) + 첼시_승점
        울버햄튼_승점 = random.randint(0,3) + 울버햄튼_승점
        웨스트햄_승점 = random.randint(0,3) + 웨스트햄_승점
        뉴캐슬_승점 = random.randint(0,3) + 뉴캐슬_승점
        팀_승점 = {
        "아스날 FC": 아스날_승점,
        "맨체스터 시티 FC": 맨시티_승점,
        "맨체스터 유나이티드 FC" : 맨유_승점,
        "리버풀 FC" : 리버풀_승점,
        "토트넘 홋스퍼 FC" : 토트넘_승점,
        "첼시 FC" : 첼시_승점,
        "울버햄튼 원더러스 FC" : 울버햄튼_승점,
        "웨스트햄 유나이티드 FC" : 웨스트햄_승점,
        "뉴캐슬 FC" : 뉴캐슬_승점          
        }
        sorted_scoreboard = sorted(팀_승점.items(), key=lambda x: x[1], reverse=True)
        print("\nEngland Premier League\n")
        for 순위, (팀, 승점) in enumerate((sorted_scoreboard), start=1):
            print(f"{순위}위 : {팀} - {승점}점")
    a = str(input("다음 단계로 넘어가려면 Y를 입력해주세요.\n"))
    if a == "Y":
        print("Pre-Matchweek\n투자할 부분을 선택하세요 : 트레이닝, 시설확충, 구단홍보")
        c_arsenal = input("선택 : ")
        if c_arsenal == "트레이닝":
            print("트레이닝을 선택하셨습니다. 중원 지배 능력치 +1")
            Arsenal_fieldown = Arsenal_fieldown + 1
            print("다른 팀 1개의 투자를 랜덤으로 살펴보겠습니다.")
            random_choice()
        elif c_arsenal == "시설확충":
            print("시설확충을 선택하셨습니다. 공격력 +1")
            Arsenal_attack = Arsenal_fieldown + 1
            print("다른 팀 1개의 투자를 랜덤으로 살펴보겠습니다.")
            random_choice()
        else:
            print("구단홍보를 선택하셨습니다. 수비력 +1")
            Arsenal_defence = Arsenal_defence + 1
            print("다른 팀 1개의 투자를 랜덤으로 살펴보겠습니다.")
            random_choice()
    if a == "Y":
        print("2주가 흘렀습니다.\n---북런던 더비---\n--------------------------------------------\nSUPER Matchweek - Away (Tottenham Hotspur Stadium)\n--------------------------------------------\nArsenal F.C.(HOME) vs Chelsea F.C.(AWAY)\n")
        print("토트넘 vs 아스날 전력 분석\n토트넘의 vs 아스날의\n공격력은 {} vs {}입니다.\n수비력은 {} vs {}입니다.\n중원 지배력은 {} vs {}입니다.\n".format(Tottenham_attack, Arsenal_attack, Tottenham_defence, Arsenal_defence, Tottenham_fieldown, Arsenal_fieldown))
        b = input(("포메이션을 선택하세요 : 3-4-3, 4-3-3, 4-2-3-1\n공격 우선 : 3-4-3, 수비 우선 : 4-3-3, 둘 다 : 4-2-3-1\n"))
        if b == "3-4-3":
            if (Arsenal_attack > Tottenham_attack and Arsenal_defence >= Tottenham_defence and Arsenal_fieldown >= Tottenham_fieldown) or (Arsenal_attack > Tottenham_attack and Arsenal_defence >= Tottenham_defence and Arsenal_fieldown < Tottenham_fieldown) or (Arsenal_attack == Newcastle_attack and Arsenal_defence >= Newcastle_defence and Arsenal_fieldown >= Newcastle_fieldown):
                print("--------------------------------------------\n{} - {}, [북런던 더비 우승] 아스날 승\n--------------------------------------------".format(random.randint(0, 1), random.randint(2, 4)))
                아스날_승점 = 아스날_승점 + 3
            elif (Arsenal_attack > Tottenham_attack and Arsenal_defence < Tottenham_defence and Arsenal_fieldown >= Tottenham_fieldown) or (Arsenal_attack == Tottenham_attack and Arsenal_defence < Tottenham_defence and Arsenal_fieldown >= Tottenham_fieldown) or (Arsenal_attack == Tottenham_attack and Arsenal_defence >= Tottenham_defence and Arsenal_fieldown < Tottenham_fieldown) or (Arsenal_attack < Tottenham_attack and Arsenal_defence >= Tottenham_defence and Arsenal_fieldown >= Tottenham_fieldown):
                print("--------------------------------------------\n{} - {}, 무승부\n--------------------------------------------".format(random.randint(2, 2), random.randint(2, 2)))
                아스날_승점 = 아스날_승점 + 1
            elif (Arsenal_attack > Tottenham_attack and Arsenal_defence < Tottenham_defence and Arsenal_fieldown < Tottenham_fieldown) or (Arsenal_attack == Tottenham_attack and Arsenal_defence < Tottenham_defence and Arsenal_fieldown < Tottenham_fieldown) or (Arsenal_attack < Tottenham_attack and Arsenal_defence < Tottenham_defence and Arsenal_fieldown >= Tottenham_fieldown) or (Arsenal_attack < Tottenham_attack and Arsenal_defence >= Tottenham_defence and Arsenal_fieldown < Tottenham_fieldown) or (Arsenal_attack < Tottenham_attack and Arsenal_defence < Tottenham_defence and Arsenal_fieldown < Tottenham_fieldown):
                print("--------------------------------------------\n{} - {}, 토트넘 승\n--------------------------------------------".format(random.randint(2, 3), random.randint(0, 1)))
                아스날_승점 = 아스날_승점 + 0
        elif b == "4-3-3":
            if (Arsenal_defence > Tottenham_defence and Arsenal_attack >= Tottenham_attack and Arsenal_fieldown >= Tottenham_fieldown) or (Arsenal_defence > Tottenham_defence and Arsenal_attack >= Tottenham_attack and Arsenal_fieldown < Tottenham_fieldown) or (Arsenal_defence == Tottenham_defence and Arsenal_attack >= Tottenham_attack and Arsenal_fieldown >= Tottenham_fieldown):
                print("--------------------------------------------\n{} - {}, [북런던 더비 우승] 아스날 승\n--------------------------------------------".format(random.randint(0, 1), random.randint(2, 3)))
                아스날_승점 = 아스날_승점 + 3
            elif (Arsenal_defence > Tottenham_defence and Arsenal_attack < Tottenham_attack and Arsenal_fieldown >= Tottenham_fieldown) or (Arsenal_defence == Tottenham_defence and Arsenal_attack < Tottenham_attack and Arsenal_fieldown >= Tottenham_fieldown) or (Arsenal_defence == Tottenham_defence and Arsenal_attack >= Tottenham_attack and Arsenal_fieldown < Tottenham_fieldown) or  (Arsenal_defence < Tottenham_defence and Arsenal_attack >= Tottenham_attack and Arsenal_fieldown >= Tottenham_fieldown):
                print("--------------------------------------------\n{} - {}, 무승부\n--------------------------------------------".format(random.randint(2, 2), random.randint(2, 2)))
                아스날_승점 = 아스날_승점 + 1
            elif (Arsenal_defence > Tottenham_defence and Arsenal_attack < Tottenham_attack and Arsenal_fieldown < Tottenham_fieldown) or (Arsenal_defence == Tottenham_defence and Arsenal_attack < Tottenham_attack and Arsenal_fieldown < Tottenham_fieldown) or (Arsenal_defence < Tottenham_defence and Arsenal_attack < Tottenham_attack and Arsenal_fieldown >= Tottenham_fieldown) or (Arsenal_defence < Tottenham_defence and Arsenal_attack >= Tottenham_attack and Arsenal_fieldown < Tottenham_fieldown) or (Arsenal_defence < Tottenham_defence and Arsenal_attack < Tottenham_attack and Arsenal_fieldown < Tottenham_fieldown):
                print("--------------------------------------------\n{} - {}, 첼시 승\n--------------------------------------------".format(random.randint(2, 4), random.randint(0, 1)))
                아스날_승점 = 아스날_승점 + 0
        elif b == "4-2-3-1":
            if (Arsenal_fieldown > Tottenham_fieldown and Arsenal_attack >= Tottenham_attack and Arsenal_defence >= Tottenham_defence) or (Arsenal_fieldown > Tottenham_fieldown and Arsenal_attack >= Tottenham_attack and Arsenal_defence < Tottenham_defence) or (Arsenal_fieldown == Tottenham_fieldown and Arsenal_attack >= Tottenham_attack and Arsenal_defence >= Tottenham_defence):
                print("--------------------------------------------\n{} - {}, 아스날 승\n--------------------------------------------".format(random.randint(0, 1), random.randint(2, 3)))
                아스날_승점 = 아스날_승점 + 3
            elif (Arsenal_fieldown > Tottenham_fieldown and Arsenal_attack < Tottenham_attack and Arsenal_defence >= Tottenham_defence) or (Arsenal_fieldown == Tottenham_fieldown and Arsenal_attack < Tottenham_attack and Arsenal_defence >= Tottenham_defence) or (Arsenal_fieldown == Tottenham_fieldown and Arsenal_attack >= Tottenham_attack and Arsenal_defence < Tottenham_defence) or  (Arsenal_fieldown < Tottenham_fieldown and Arsenal_attack >= Tottenham_attack and Arsenal_defence >= Tottenham_defence):
                print("--------------------------------------------\n{} - {}, 무승부\n--------------------------------------------".format(random.randint(2, 2), random.randint(2, 2)))
                아스날_승점 = 아스날_승점 + 1
            elif (Arsenal_fieldown > Tottenham_fieldown and Arsenal_attack < Tottenham_attack and Arsenal_defence < Tottenham_defence) or (Arsenal_fieldown == Tottenham_fieldown and Arsenal_attack < Tottenham_attack and Arsenal_defence < Tottenham_defence) or (Arsenal_fieldown < Tottenham_fieldown and Arsenal_attack < Tottenham_attack and Arsenal_defence >= Tottenham_defence) or (Arsenal_fieldown < Tottenham_fieldown and Arsenal_attack >= Tottenham_attack and Arsenal_defence < Tottenham_defence) or  (Arsenal_fieldown < Tottenham_fieldown and Arsenal_attack < Tottenham_attack and Arsenal_defence < Tottenham_defence):
                print("--------------------------------------------\n{} - {}, 토트넘 승\n--------------------------------------------".format(random.randint(2, 4), random.randint(0, 1)))
                아스날_승점 = 아스날_승점 + 0
        n = n + 1
        print("[다섯] 번째 경기를 무사히 끝냈습니다. 당신의 승점은 {}점 입니다".format(아스날_승점))
        print("{}주차 프리미어리그 순위".format(n))
        아스날_승점 = 아스날_승점
        맨시티_승점 = random.randint(0,3) + 맨시티_승점
        리버풀_승점 = random.randint(0,3) + 리버풀_승점
        맨유_승점 = random.randint(0,3) + 맨유_승점
        토트넘_승점 = random.randint(0,3) + 토트넘_승점
        첼시_승점 = random.randint(0,3) + 첼시_승점
        울버햄튼_승점 = random.randint(0,3) + 울버햄튼_승점
        웨스트햄_승점 = random.randint(0,3) + 웨스트햄_승점
        뉴캐슬_승점 = random.randint(0,3) + 뉴캐슬_승점
        팀_승점 = {
        "아스날 FC": 아스날_승점,
        "맨체스터 시티 FC": 맨시티_승점,
        "맨체스터 유나이티드 FC" : 맨유_승점,
        "리버풀 FC" : 리버풀_승점,
        "토트넘 홋스퍼 FC" : 토트넘_승점,
        "첼시 FC" : 첼시_승점,
        "울버햄튼 원더러스 FC" : 울버햄튼_승점,
        "웨스트햄 유나이티드 FC" : 웨스트햄_승점,
        "뉴캐슬 FC" : 뉴캐슬_승점          
        }
        sorted_scoreboard = sorted(팀_승점.items(), key=lambda x: x[1], reverse=True)
        print("\nEngland Premier League\n")
        for 순위, (팀, 승점) in enumerate((sorted_scoreboard), start=1):
            print(f"{순위}위 : {팀} - {승점}점")
    a = str(input("다음 단계로 넘어가려면 Y를 입력해주세요.\n"))
    if a == "Y":
        print("Pre-Matchweek\n투자할 부분을 선택하세요 : 트레이닝, 시설확충, 구단홍보")
        c_arsenal = input("선택 : ")
        if c_arsenal == "트레이닝":
            print("트레이닝을 선택하셨습니다. 중원 지배 능력치 +1")
            Arsenal_fieldown = Arsenal_fieldown + 1
            print("다른 팀 1개의 투자를 랜덤으로 살펴보겠습니다.")
            random_choice()
        elif c_arsenal == "시설확충":
            print("시설확충을 선택하셨습니다. 공격력 +1")
            Arsenal_attack = Arsenal_fieldown + 1
            print("다른 팀 1개의 투자를 랜덤으로 살펴보겠습니다.")
            random_choice()
        else:
            print("구단홍보를 선택하셨습니다. 수비력 +1")
            Arsenal_defence = Arsenal_defence + 1
            print("다른 팀 1개의 투자를 랜덤으로 살펴보겠습니다.")
            random_choice()
    if a == "Y":
        print("\n=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n경고! HELL-WEEK 지옥의 릴레이가 시작되었습니다. 이제부터 당신은 PL 최강의 팀이라고 일컬어지는 맨유, 리버풀, 맨시티와 연속 경기를 치르게 됩니다.\n=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n")
        print("2주가 흘렀습니다.\n--------------------------------------------\nHELLweek 1 - Away (Old Trafford)\n--------------------------------------------\nArsenal F.C.(HOME) vs Chelsea F.C.(AWAY)\n")
        print("아스날 vs 맨 유 전력 분석\n아스날의 vs 맨유의\n공격력은 {} vs {}입니다.\n수비력은 {} vs {}입니다.\n중원 지배력은 {} vs {}입니다.\n".format(Arsenal_attack, Man_Utd_attack, Arsenal_defence, Man_Utd_defence, Arsenal_fieldown, Man_Utd_fieldown))
        b = input(("포메이션을 선택하세요 : 3-4-3, 4-3-3, 4-2-3-1\n공격 우선 : 3-4-3, 수비 우선 : 4-3-3, 둘 다 : 4-2-3-1\n"))
        if b == "3-4-3":
            if (Arsenal_attack > Man_Utd_attack and Arsenal_defence >= Man_Utd_defence and Arsenal_fieldown >= Man_Utd_fieldown) or (Arsenal_attack > Man_Utd_attack and Arsenal_defence >= Man_Utd_defence and Arsenal_fieldown < Man_Utd_fieldown) or (Arsenal_attack == Newcastle_attack and Arsenal_defence >= Newcastle_defence and Arsenal_fieldown >= Newcastle_fieldown):
                print("--------------------------------------------\n{} - {}, 아스날 승\n--------------------------------------------".format(random.randint(0, 1), random.randint(2, 4)))
                아스날_승점 = 아스날_승점 + 3
            elif (Arsenal_attack > Man_Utd_attack and Arsenal_defence < Man_Utd_defence and Arsenal_fieldown >= Man_Utd_fieldown) or (Arsenal_attack == Man_Utd_attack and Arsenal_defence < Man_Utd_defence and Arsenal_fieldown >= Man_Utd_fieldown) or (Arsenal_attack == Man_Utd_attack and Arsenal_defence >= Man_Utd_defence and Arsenal_fieldown < Man_Utd_fieldown) or (Arsenal_attack < Man_Utd_attack and Arsenal_defence >= Man_Utd_defence and Arsenal_fieldown >= Man_Utd_fieldown):
                print("--------------------------------------------\n{} - {}, 무승부\n--------------------------------------------".format(random.randint(2, 2), random.randint(2, 2)))
                아스날_승점 = 아스날_승점 + 1
            elif (Arsenal_attack > Man_Utd_attack and Arsenal_defence < Man_Utd_defence and Arsenal_fieldown < Man_Utd_fieldown) or (Arsenal_attack == Man_Utd_attack and Arsenal_defence < Man_Utd_defence and Arsenal_fieldown < Man_Utd_fieldown) or (Arsenal_attack < Man_Utd_attack and Arsenal_defence < Man_Utd_defence and Arsenal_fieldown >= Man_Utd_fieldown) or (Arsenal_attack < Man_Utd_attack and Arsenal_defence >= Man_Utd_defence and Arsenal_fieldown < Man_Utd_fieldown) or (Arsenal_attack < Man_Utd_attack and Arsenal_defence < Man_Utd_defence and Arsenal_fieldown < Man_Utd_fieldown):
                print("--------------------------------------------\n{} - {}, 맨체스터 유나이티드 승\n--------------------------------------------".format(random.randint(2, 3), random.randint(0, 1)))
                아스날_승점 = 아스날_승점 + 0
        elif b == "4-3-3":
            if (Arsenal_defence > Man_Utd_defence and Arsenal_attack >= Man_Utd_attack and Arsenal_fieldown >= Man_Utd_fieldown) or (Arsenal_defence > Man_Utd_defence and Arsenal_attack >= Man_Utd_attack and Arsenal_fieldown < Man_Utd_fieldown) or (Arsenal_defence == Man_Utd_defence and Arsenal_attack >= Man_Utd_attack and Arsenal_fieldown >= Man_Utd_fieldown):
                print("--------------------------------------------\n{} - {}, 아스날 승\n--------------------------------------------".format(random.randint(0, 1), random.randint(2, 3)))
                아스날_승점 = 아스날_승점 + 3
            elif (Arsenal_defence > Man_Utd_defence and Arsenal_attack < Man_Utd_attack and Arsenal_fieldown >= Man_Utd_fieldown) or (Arsenal_defence == Man_Utd_defence and Arsenal_attack < Man_Utd_attack and Arsenal_fieldown >= Man_Utd_fieldown) or (Arsenal_defence == Man_Utd_defence and Arsenal_attack >= Man_Utd_attack and Arsenal_fieldown < Man_Utd_fieldown) or  (Arsenal_defence < Man_Utd_defence and Arsenal_attack >= Man_Utd_attack and Arsenal_fieldown >= Man_Utd_fieldown):
                print("--------------------------------------------\n{} - {}, 무승부\n--------------------------------------------".format(random.randint(2, 2), random.randint(2, 2)))
                아스날_승점 = 아스날_승점 + 1
            elif (Arsenal_defence > Man_Utd_defence and Arsenal_attack < Man_Utd_attack and Arsenal_fieldown < Man_Utd_fieldown) or (Arsenal_defence == Man_Utd_defence and Arsenal_attack < Man_Utd_attack and Arsenal_fieldown < Man_Utd_fieldown) or (Arsenal_defence < Man_Utd_defence and Arsenal_attack < Man_Utd_attack and Arsenal_fieldown >= Man_Utd_fieldown) or (Arsenal_defence < Man_Utd_defence and Arsenal_attack >= Man_Utd_attack and Arsenal_fieldown < Man_Utd_fieldown) or (Arsenal_defence < Man_Utd_defence and Arsenal_attack < Man_Utd_attack and Arsenal_fieldown < Man_Utd_fieldown):
                print("--------------------------------------------\n{} - {}, 맨체스터 유나이티드 승\n--------------------------------------------".format(random.randint(2, 4), random.randint(0, 1)))
                아스날_승점 = 아스날_승점 + 0
        elif b == "4-2-3-1":
            if (Arsenal_fieldown > Man_Utd_fieldown and Arsenal_attack >= Man_Utd_attack and Arsenal_defence >= Man_Utd_defence) or (Arsenal_fieldown > Man_Utd_fieldown and Arsenal_attack >= Man_Utd_attack and Arsenal_defence < Man_Utd_defence) or (Arsenal_fieldown == Man_Utd_fieldown and Arsenal_attack >= Man_Utd_attack and Arsenal_defence >= Man_Utd_defence):
                print("--------------------------------------------\n{} - {}, 아스날 승\n--------------------------------------------".format(random.randint(0, 1), random.randint(2, 3)))
                아스날_승점 = 아스날_승점 + 3
            elif (Arsenal_fieldown > Man_Utd_fieldown and Arsenal_attack < Man_Utd_attack and Arsenal_defence >= Man_Utd_defence) or (Arsenal_fieldown == Man_Utd_fieldown and Arsenal_attack < Man_Utd_attack and Arsenal_defence >= Man_Utd_defence) or (Arsenal_fieldown == Man_Utd_fieldown and Arsenal_attack >= Man_Utd_attack and Arsenal_defence < Man_Utd_defence) or  (Arsenal_fieldown < Man_Utd_fieldown and Arsenal_attack >= Man_Utd_attack and Arsenal_defence >= Man_Utd_defence):
                print("--------------------------------------------\n{} - {}, 무승부\n--------------------------------------------".format(random.randint(2, 2), random.randint(2, 2)))
                아스날_승점 = 아스날_승점 + 1
            elif (Arsenal_fieldown > Man_Utd_fieldown and Arsenal_attack < Man_Utd_attack and Arsenal_defence < Man_Utd_defence) or (Arsenal_fieldown == Man_Utd_fieldown and Arsenal_attack < Man_Utd_attack and Arsenal_defence < Man_Utd_defence) or (Arsenal_fieldown < Man_Utd_fieldown and Arsenal_attack < Man_Utd_attack and Arsenal_defence >= Man_Utd_defence) or (Arsenal_fieldown < Man_Utd_fieldown and Arsenal_attack >= Man_Utd_attack and Arsenal_defence < Man_Utd_defence) or  (Arsenal_fieldown < Man_Utd_fieldown and Arsenal_attack < Man_Utd_attack and Arsenal_defence < Man_Utd_defence):
                print("--------------------------------------------\n{} - {}, 토트넘 승\n--------------------------------------------".format(random.randint(2, 4), random.randint(0, 1)))
                아스날_승점 = 아스날_승점 + 0
        n = n + 1
        print("[여섯] 번째 경기를 무사히 끝냈습니다. 당신의 승점은 {}점 입니다".format(아스날_승점))
        print("{}주차 프리미어리그 순위".format(n))
        아스날_승점 = 아스날_승점
        맨시티_승점 = random.randint(0,3) + 맨시티_승점
        리버풀_승점 = random.randint(0,3) + 리버풀_승점
        맨유_승점 = random.randint(0,3) + 맨유_승점
        토트넘_승점 = random.randint(0,3) + 토트넘_승점
        첼시_승점 = random.randint(0,3) + 첼시_승점
        울버햄튼_승점 = random.randint(0,3) + 울버햄튼_승점
        웨스트햄_승점 = random.randint(0,3) + 웨스트햄_승점
        뉴캐슬_승점 = random.randint(0,3) + 뉴캐슬_승점
        팀_승점 = {
        "아스날 FC": 아스날_승점,
        "맨체스터 시티 FC": 맨시티_승점,
        "맨체스터 유나이티드 FC" : 맨유_승점,
        "리버풀 FC" : 리버풀_승점,
        "토트넘 홋스퍼 FC" : 토트넘_승점,
        "첼시 FC" : 첼시_승점,
        "울버햄튼 원더러스 FC" : 울버햄튼_승점,
        "웨스트햄 유나이티드 FC" : 웨스트햄_승점,
        "뉴캐슬 FC" : 뉴캐슬_승점          
        }
        sorted_scoreboard = sorted(팀_승점.items(), key=lambda x: x[1], reverse=True)
        print("\nEngland Premier League\n")
        for 순위, (팀, 승점) in enumerate((sorted_scoreboard), start=1):
            print(f"{순위}위 : {팀} - {승점}점")
    a = str(input("다음 단계로 넘어가려면 Y를 입력해주세요.\n"))
    if a == "Y":
        print("Pre-Matchweek\n투자할 부분을 선택하세요 : 트레이닝, 시설확충, 구단홍보")
        c_arsenal = input("선택 : ")
        if c_arsenal == "트레이닝":
            print("트레이닝을 선택하셨습니다. 중원 지배 능력치 +1")
            Arsenal_fieldown = Arsenal_fieldown + 1
            print("다른 팀 1개의 투자를 랜덤으로 살펴보겠습니다.")
            random_choice()
        elif c_arsenal == "시설확충":
            print("시설확충을 선택하셨습니다. BONUS + 공격력 +2")
            Arsenal_attack = Arsenal_fieldown + 1
            print("다른 팀 1개의 투자를 랜덤으로 살펴보겠습니다.")
            random_choice()
        else:
            print("구단홍보를 선택하셨습니다. 수비력 +1")
            Arsenal_defence = Arsenal_defence + 1
            print("다른 팀 1개의 투자를 랜덤으로 살펴보겠습니다.")
            random_choice()
    if a == "Y":
        print("\n=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n경고! HELL-WEEK 지옥의 릴레이가 [실행 중]입니다. 이제부터 당신은 PL 최강의 팀이라고 일컬어지는 리버풀, 맨시티와 연속 경기를 치르게 됩니다.\n=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n")
        print("2주가 흘렀습니다.\n--------------------------------------------\nHELLweek 1 - Home (Emirates Stadium)\n--------------------------------------------\nArsenal F.C.(HOME) vs Liverpool F.C.(AWAY)\n")
        print("아스날 vs 리버풀 전력 분석\n아스날의 vs 맨유의\n공격력은 {} vs {}입니다.\n수비력은 {} vs {}입니다.\n중원 지배력은 {} vs {}입니다.\n".format(Arsenal_attack, Liverpool_attack, Arsenal_defence, Liverpool_defence, Arsenal_fieldown, Liverpool_fieldown))
        b = input(("포메이션을 선택하세요 : 3-4-3, 4-3-3, 4-2-3-1\n공격 우선 : 3-4-3, 수비 우선 : 4-3-3, 둘 다 : 4-2-3-1\n"))
        if b == "3-4-3":
            if (Arsenal_attack > Liverpool_attack and Arsenal_defence >= Liverpool_defence and Arsenal_fieldown >= Liverpool_fieldown) or (Arsenal_attack > Liverpool_attack and Arsenal_defence >= Liverpool_defence and Arsenal_fieldown < Liverpool_fieldown) or (Arsenal_attack == Liverpool_attack and Arsenal_defence >= Liverpool_defence and Arsenal_fieldown >= Liverpool_fieldown):
                print("--------------------------------------------\n{} - {}, 아스날 승\n--------------------------------------------".format(random.randint(0, 1), random.randint(2, 4)))
                아스날_승점 = 아스날_승점 + 3
            elif (Arsenal_attack > Liverpool_attack and Arsenal_defence < Liverpool_defence and Arsenal_fieldown >= Liverpool_fieldown) or (Arsenal_attack == Liverpool_attack and Arsenal_defence < Liverpool_defence and Arsenal_fieldown >= Liverpool_fieldown) or (Arsenal_attack == Liverpool_attack and Arsenal_defence >= Liverpool_defence and Arsenal_fieldown < Liverpool_fieldown) or (Arsenal_attack < Liverpool_attack and Arsenal_defence >= Liverpool_defence and Arsenal_fieldown >= Liverpool_fieldown):
                print("--------------------------------------------\n{} - {}, 무승부\n--------------------------------------------".format(random.randint(2, 2), random.randint(2, 2)))
                아스날_승점 = 아스날_승점 + 1
            elif (Arsenal_attack > Liverpool_attack and Arsenal_defence < Liverpool_defence and Arsenal_fieldown < Liverpool_fieldown) or (Arsenal_attack == Liverpool_attack and Arsenal_defence < Liverpool_defence and Arsenal_fieldown < Liverpool_fieldown) or (Arsenal_attack < Liverpool_attack and Arsenal_defence < Liverpool_defence and Arsenal_fieldown >= Liverpool_fieldown) or (Arsenal_attack < Liverpool_attack and Arsenal_defence >= Liverpool_defence and Arsenal_fieldown < Liverpool_fieldown) or (Arsenal_attack < Liverpool_attack and Arsenal_defence < Liverpool_defence and Arsenal_fieldown < Liverpool_fieldown):
                print("--------------------------------------------\n{} - {}, 리버풀 승\n--------------------------------------------".format(random.randint(2, 3), random.randint(0, 1)))
                아스날_승점 = 아스날_승점 + 0
        elif b == "4-3-3":
            if (Arsenal_defence > Liverpool_defence and Arsenal_attack >= Liverpool_attack and Arsenal_fieldown >= Liverpool_fieldown) or (Arsenal_defence > Liverpool_defence and Arsenal_attack >= Liverpool_attack and Arsenal_fieldown < Liverpool_fieldown) or (Arsenal_defence == Liverpool_defence and Arsenal_attack >= Liverpool_attack and Arsenal_fieldown >= Liverpool_fieldown):
                print("--------------------------------------------\n{} - {}, 아스날 승\n--------------------------------------------".format(random.randint(0, 1), random.randint(2, 3)))
                아스날_승점 = 아스날_승점 + 3
            elif (Arsenal_defence > Liverpool_defence and Arsenal_attack < Liverpool_attack and Arsenal_fieldown >= Liverpool_fieldown) or (Arsenal_defence == Liverpool_defence and Arsenal_attack < Liverpool_attack and Arsenal_fieldown >= Liverpool_fieldown) or (Arsenal_defence == Liverpool_defence and Arsenal_attack >= Liverpool_attack and Arsenal_fieldown < Liverpool_fieldown) or  (Arsenal_defence < Liverpool_defence and Arsenal_attack >= Liverpool_attack and Arsenal_fieldown >= Liverpool_fieldown):
                print("--------------------------------------------\n{} - {}, 무승부\n--------------------------------------------".format(random.randint(2, 2), random.randint(2, 2)))
                아스날_승점 = 아스날_승점 + 1
            elif (Arsenal_defence > Liverpool_defence and Arsenal_attack < Liverpool_attack and Arsenal_fieldown < Liverpool_fieldown) or (Arsenal_defence == Liverpool_defence and Arsenal_attack < Liverpool_attack and Arsenal_fieldown < Liverpool_fieldown) or (Arsenal_defence < Liverpool_defence and Arsenal_attack < Liverpool_attack and Arsenal_fieldown >= Liverpool_fieldown) or (Arsenal_defence < Liverpool_defence and Arsenal_attack >= Liverpool_attack and Arsenal_fieldown < Liverpool_fieldown) or (Arsenal_defence < Liverpool_defence and Arsenal_attack < Liverpool_attack and Arsenal_fieldown < Liverpool_fieldown):
                print("--------------------------------------------\n{} - {}, 리버풀 승\n--------------------------------------------".format(random.randint(2, 4), random.randint(0, 1)))
                아스날_승점 = 아스날_승점 + 0
        elif b == "4-2-3-1":
            if (Arsenal_fieldown > Liverpool_fieldown and Arsenal_attack >= Liverpool_attack and Arsenal_defence >= Liverpool_defence) or (Arsenal_fieldown > Liverpool_fieldown and Arsenal_attack >= Liverpool_attack and Arsenal_defence < Liverpool_defence) or (Arsenal_fieldown == Liverpool_fieldown and Arsenal_attack >= Liverpool_attack and Arsenal_defence >= Liverpool_defence):
                print("--------------------------------------------\n{} - {}, 아스날 승\n--------------------------------------------".format(random.randint(0, 1), random.randint(2, 3)))
                아스날_승점 = 아스날_승점 + 3
            elif (Arsenal_fieldown > Liverpool_fieldown and Arsenal_attack < Liverpool_attack and Arsenal_defence >= Liverpool_defence) or (Arsenal_fieldown == Liverpool_fieldown and Arsenal_attack < Liverpool_attack and Arsenal_defence >= Liverpool_defence) or (Arsenal_fieldown == Liverpool_fieldown and Arsenal_attack >= Liverpool_attack and Arsenal_defence < Liverpool_defence) or  (Arsenal_fieldown < Liverpool_fieldown and Arsenal_attack >= Liverpool_attack and Arsenal_defence >= Liverpool_defence):
                print("--------------------------------------------\n{} - {}, 무승부\n--------------------------------------------".format(random.randint(2, 2), random.randint(2, 2)))
                아스날_승점 = 아스날_승점 + 1
            elif (Arsenal_fieldown > Liverpool_fieldown and Arsenal_attack < Liverpool_attack and Arsenal_defence < Liverpool_defence) or (Arsenal_fieldown == Liverpool_fieldown and Arsenal_attack < Liverpool_attack and Arsenal_defence < Liverpool_defence) or (Arsenal_fieldown < Liverpool_fieldown and Arsenal_attack < Liverpool_attack and Arsenal_defence >= Liverpool_defence) or (Arsenal_fieldown < Liverpool_fieldown and Arsenal_attack >= Liverpool_attack and Arsenal_defence < Liverpool_defence) or  (Arsenal_fieldown < Liverpool_fieldown and Arsenal_attack < Liverpool_attack and Arsenal_defence < Liverpool_defence):
                print("--------------------------------------------\n{} - {}, 리버풀 승\n--------------------------------------------".format(random.randint(2, 4), random.randint(0, 1)))
                아스날_승점 = 아스날_승점 + 0
        n = n + 1
        print("[일곱] 번째 경기를 무사히 끝냈습니다. 당신의 승점은 {}점 입니다".format(아스날_승점))
        print("{}주차 프리미어리그 순위".format(n))
        아스날_승점 = 아스날_승점
        맨시티_승점 = random.randint(0,3) + 맨시티_승점
        리버풀_승점 = random.randint(0,3) + 리버풀_승점
        맨유_승점 = random.randint(0,3) + 맨유_승점
        토트넘_승점 = random.randint(0,3) + 토트넘_승점
        첼시_승점 = random.randint(0,3) + 첼시_승점
        울버햄튼_승점 = random.randint(0,3) + 울버햄튼_승점
        웨스트햄_승점 = random.randint(0,3) + 웨스트햄_승점
        뉴캐슬_승점 = random.randint(0,3) + 뉴캐슬_승점
        팀_승점 = {
        "아스날 FC": 아스날_승점,
        "맨체스터 시티 FC": 맨시티_승점,
        "맨체스터 유나이티드 FC" : 맨유_승점,
        "리버풀 FC" : 리버풀_승점,
        "토트넘 홋스퍼 FC" : 토트넘_승점,
        "첼시 FC" : 첼시_승점,
        "울버햄튼 원더러스 FC" : 울버햄튼_승점,
        "웨스트햄 유나이티드 FC" : 웨스트햄_승점,
        "뉴캐슬 FC" : 뉴캐슬_승점          
        }
        sorted_scoreboard = sorted(팀_승점.items(), key=lambda x: x[1], reverse=True)
        print("\nEngland Premier League\n")
        for 순위, (팀, 승점) in enumerate((sorted_scoreboard), start=1):
            print(f"{순위}위 : {팀} - {승점}점")
    a = str(input("다음 단계로 넘어가려면 Y를 입력해주세요.\n"))
    if a == "Y":
        print("Pre-Matchweek\n투자할 부분을 선택하세요 : 트레이닝, 시설확충, 구단홍보")
        c_arsenal = input("선택 : ")
        if c_arsenal == "트레이닝":
            print("트레이닝을 선택하셨습니다. 중원 지배 능력치 +1")
            Arsenal_fieldown = Arsenal_fieldown + 1
            print("다른 팀 1개의 투자를 랜덤으로 살펴보겠습니다.")
            random_choice()
        elif c_arsenal == "시설확충":
            print("시설확충을 선택하셨습니다. BONUS + 공격력 +2")
            Arsenal_attack = Arsenal_fieldown + 1
            print("다른 팀 1개의 투자를 랜덤으로 살펴보겠습니다.")
            random_choice()
        else:
            print("구단홍보를 선택하셨습니다. 수비력 +1")
            Arsenal_defence = Arsenal_defence + 1
            print("다른 팀 1개의 투자를 랜덤으로 살펴보겠습니다.")
            random_choice()
    if a == "Y":
        print("\n=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\nLast-Week 지옥의 릴레이가 [마지막]입니다. 이제부터 당신은 PL 최다 우승 팀, 최강의 공격진을 자랑하는 맨시티와 경기를 치르게 됩니다.\n=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n")
        print("2주가 흘렀습니다.\n--------------------------------------------\nLast week - Away (Etihad Stadium)\n--------------------------------------------\nManchester City F.C.(HOME) vs Arsenal F.C.(AWAY)\n")
        print("맨시티 vs 아스날 전력 분석\n맨시티의 vs 아스날의\n공격력은 {} vs {}입니다.\n수비력은 {} vs {}입니다.\n중원 지배력은 {} vs {}입니다.\n".format(Man_City_attack, Arsenal_attack, Man_City_defence, Arsenal_defence, Man_City_fieldown, Arsenal_fieldown))
        b = input(("포메이션을 선택하세요 : 3-4-3, 4-3-3, 4-2-3-1\n공격 우선 : 3-4-3, 수비 우선 : 4-3-3, 둘 다 : 4-2-3-1\n"))
        if b == "3-4-3":
            if (Arsenal_attack > Man_City_attack and Arsenal_defence >= Man_City_defence and Arsenal_fieldown >= Man_City_fieldown) or (Arsenal_attack > Man_City_attack and Arsenal_defence >= Man_City_defence and Arsenal_fieldown < Man_City_fieldown) or (Arsenal_attack == Man_City_attack and Arsenal_defence >= Man_City_defence and Arsenal_fieldown >= Man_City_fieldown):
                print("--------------------------------------------\n{} - {}, 아스날 승\n--------------------------------------------".format(random.randint(0, 1), random.randint(2, 4)))
                아스날_승점 = 아스날_승점 + 3
            elif (Arsenal_attack > Man_City_attack and Arsenal_defence < Man_City_defence and Arsenal_fieldown >= Man_City_fieldown) or (Arsenal_attack == Man_City_attack and Arsenal_defence < Man_City_defence and Arsenal_fieldown >= Man_City_fieldown) or (Arsenal_attack == Man_City_attack and Arsenal_defence >= Man_City_defence and Arsenal_fieldown < Man_City_fieldown) or (Arsenal_attack < Man_City_attack and Arsenal_defence >= Man_City_defence and Arsenal_fieldown >= Man_City_fieldown):
                print("--------------------------------------------\n{} - {}, 무승부\n--------------------------------------------".format(random.randint(2, 2), random.randint(2, 2)))
                아스날_승점 = 아스날_승점 + 1
            elif (Arsenal_attack > Man_City_attack and Arsenal_defence < Man_City_defence and Arsenal_fieldown < Man_City_fieldown) or (Arsenal_attack == Man_City_attack and Arsenal_defence < Man_City_defence and Arsenal_fieldown < Man_City_fieldown) or (Arsenal_attack < Man_City_attack and Arsenal_defence < Man_City_defence and Arsenal_fieldown >= Man_City_fieldown) or (Arsenal_attack < Man_City_attack and Arsenal_defence >= Man_City_defence and Arsenal_fieldown < Man_City_fieldown) or (Arsenal_attack < Man_City_attack and Arsenal_defence < Man_City_defence and Arsenal_fieldown < Man_City_fieldown):
                print("--------------------------------------------\n{} - {}, 맨체스터 시티 승\n--------------------------------------------".format(random.randint(2, 3), random.randint(0, 1)))
                아스날_승점 = 아스날_승점 + 0
        elif b == "4-3-3":
            if (Arsenal_defence > Man_City_defence and Arsenal_attack >= Man_City_attack and Arsenal_fieldown >= Man_City_fieldown) or (Arsenal_defence > Man_City_defence and Arsenal_attack >= Man_City_attack and Arsenal_fieldown < Man_City_fieldown) or (Arsenal_defence == Man_City_defence and Arsenal_attack >= Man_City_attack and Arsenal_fieldown >= Man_City_fieldown):
                print("--------------------------------------------\n{} - {}, 아스날 승\n--------------------------------------------".format(random.randint(0, 1), random.randint(2, 3)))
                아스날_승점 = 아스날_승점 + 3
            elif (Arsenal_defence > Man_City_defence and Arsenal_attack < Man_City_attack and Arsenal_fieldown >= Man_City_fieldown) or (Arsenal_defence == Man_City_defence and Arsenal_attack < Man_City_attack and Arsenal_fieldown >= Man_City_fieldown) or (Arsenal_defence == Man_City_defence and Arsenal_attack >= Man_City_attack and Arsenal_fieldown < Man_City_fieldown) or  (Arsenal_defence < Man_City_defence and Arsenal_attack >= Man_City_attack and Arsenal_fieldown >= Man_City_fieldown):
                print("--------------------------------------------\n{} - {}, 무승부\n--------------------------------------------".format(random.randint(2, 2), random.randint(2, 2)))
                아스날_승점 = 아스날_승점 + 1
            elif (Arsenal_defence > Man_City_defence and Arsenal_attack < Man_City_attack and Arsenal_fieldown < Man_City_fieldown) or (Arsenal_defence == Man_City_defence and Arsenal_attack < Man_City_attack and Arsenal_fieldown < Man_City_fieldown) or (Arsenal_defence < Man_City_defence and Arsenal_attack < Man_City_attack and Arsenal_fieldown >= Man_City_fieldown) or (Arsenal_defence < Man_City_defence and Arsenal_attack >= Man_City_attack and Arsenal_fieldown < Man_City_fieldown) or (Arsenal_defence < Man_City_defence and Arsenal_attack < Man_City_attack and Arsenal_fieldown < Man_City_fieldown):
                print("--------------------------------------------\n{} - {}, 맨체스터 시티 승\n--------------------------------------------".format(random.randint(2, 4), random.randint(0, 1)))
                아스날_승점 = 아스날_승점 + 0
        elif b == "4-2-3-1":
            if (Arsenal_fieldown > Man_City_fieldown and Arsenal_attack >= Man_City_attack and Arsenal_defence >= Man_City_defence) or (Arsenal_fieldown > Man_City_fieldown and Arsenal_attack >= Man_City_attack and Arsenal_defence < Man_City_defence) or (Arsenal_fieldown == Man_City_fieldown and Arsenal_attack >= Man_City_attack and Arsenal_defence >= Man_City_defence):
                print("--------------------------------------------\n{} - {}, 아스날 승\n--------------------------------------------".format(random.randint(0, 1), random.randint(2, 3)))
                아스날_승점 = 아스날_승점 + 3
            elif (Arsenal_fieldown > Man_City_fieldown and Arsenal_attack < Man_City_attack and Arsenal_defence >= Man_City_defence) or (Arsenal_fieldown == Man_City_fieldown and Arsenal_attack < Man_City_attack and Arsenal_defence >= Man_City_defence) or (Arsenal_fieldown == Man_City_fieldown and Arsenal_attack >= Man_City_attack and Arsenal_defence < Man_City_defence) or  (Arsenal_fieldown < Man_City_fieldown and Arsenal_attack >= Man_City_attack and Arsenal_defence >= Man_City_defence):
                print("--------------------------------------------\n{} - {}, 무승부\n--------------------------------------------".format(random.randint(2, 2), random.randint(2, 2)))
                아스날_승점 = 아스날_승점 + 1
            elif (Arsenal_fieldown > Man_City_fieldown and Arsenal_attack < Man_City_attack and Arsenal_defence < Man_City_defence) or (Arsenal_fieldown == Man_City_fieldown and Arsenal_attack < Man_City_attack and Arsenal_defence < Man_City_defence) or (Arsenal_fieldown < Man_City_fieldown and Arsenal_attack < Man_City_attack and Arsenal_defence >= Man_City_defence) or (Arsenal_fieldown < Man_City_fieldown and Arsenal_attack >= Man_City_attack and Arsenal_defence < Man_City_defence) or  (Arsenal_fieldown < Man_City_fieldown and Arsenal_attack < Man_City_attack and Arsenal_defence < Man_City_defence):
                print("--------------------------------------------\n{} - {}, 리버풀 승\n--------------------------------------------".format(random.randint(2, 4), random.randint(0, 1)))
                아스날_승점 = 아스날_승점 + 0
        n = n + 1
        print("[여덟] 번째 경기를 무사히 끝냈습니다. 당신의 승점은 {}점 입니다".format(아스날_승점))
        print("{}주차 프리미어리그 순위".format(n))
        아스날_승점 = 아스날_승점
        맨시티_승점 = random.randint(0,3) + 맨시티_승점
        리버풀_승점 = random.randint(0,3) + 리버풀_승점
        맨유_승점 = random.randint(0,3) + 맨유_승점
        토트넘_승점 = random.randint(0,3) + 토트넘_승점
        첼시_승점 = random.randint(0,3) + 첼시_승점
        울버햄튼_승점 = random.randint(0,3) + 울버햄튼_승점
        웨스트햄_승점 = random.randint(0,3) + 웨스트햄_승점
        뉴캐슬_승점 = random.randint(0,3) + 뉴캐슬_승점
        팀_승점 = {
        "아스날 FC": 아스날_승점,
        "맨체스터 시티 FC": 맨시티_승점,
        "맨체스터 유나이티드 FC" : 맨유_승점,
        "리버풀 FC" : 리버풀_승점,
        "토트넘 홋스퍼 FC" : 토트넘_승점,
        "첼시 FC" : 첼시_승점,
        "울버햄튼 원더러스 FC" : 울버햄튼_승점,
        "웨스트햄 유나이티드 FC" : 웨스트햄_승점,
        "뉴캐슬 FC" : 뉴캐슬_승점          
        }
        sorted_scoreboard = sorted(팀_승점.items(), key=lambda x: x[1], reverse=True)
        print("\nEngland Premier League\n")
        for 순위, (팀, 승점) in enumerate((sorted_scoreboard), start=1):
            print(f"{순위}위 : {팀} - {승점}점")
    a = str(input("다음 단계로 넘어가려면 Y를 입력해주세요.\n"))
    if 아스날_승점 > 12:
        print("------------------------------------------------------------------")
        print("축하합니다. 당신의 팀은 2024-25 시즌 UEFA 챔피언스 리그에 진출했습니다.")
        print("Congrats. Ur team finally get the tickets to Champs.")
        print("...........      ...........               .................................               ...................................                        .\n...........      ...........               .................................               ...................................                       ....\n...........      ...........               ...........                            ..........                                    ..   ..\n...........      ...........               .................................               ...................................                    ................\n...........      ...........               .................................               ....................................                  .....................\n...........      ...........               ...........                            ..........                               ....            ....\n.................................               .................................               ..........                             ....                 ....\n.................................               ................................               ..........                           ....                     ....\n")
    else:
        print("------------------------------------------------------------------")
        print("수고했습니다. 당신의 팀은 비록 UEFA 챔피언스 리그에 진출하지 못했더라도 프리미어리그의 전설로 남을 것입니다.")

print("PL에서 챔스가기!\n---------------------------------------------\n이제부터 당신은 Arsenal 팀의 감독입니다. PL 팀 중 하나를 선택하세요. 팀 변경의 기회는 없으니 신중히 고르세요!\n(용량 문제로 모든 팀들을 넣지 못한 점 죄송합니다!!)\n--------------------------------------------")
print("계속 진행하시려면 Y를 눌러주세요.")
jersey = input("입력 : ")
if jersey == "Y":
    Arsenal_Run()

def introduce_powerbalance(a, b, c, d):
    print("{}의\n공격력은 {}입니다.\n수비력은 {}입니다.\n중원 지배력은 {}입니다.".format(a, b, c, d))

if commandteam == Arsenal:
    introduce_powerbalance(Arsenal, Arsenal_attack, Arsenal_defence, Arsenal_fieldown)
    print("\n아스날은 프리미어리그 전통의 강팀으로, 공격, 수비, 중원 모두 우수한 활약을 보입니다.")
    Arsenal_Run()
elif commandteam == Man_City:
    introduce_powerbalance(Man_City, Man_City_attack, Man_City_defence, Man_City_fieldown)
    print("\n맨체스터 시티는 세계 최강의 공격진을 필두로 한 강팀으로, 매 경기마다 화끈한 득점력을 선보입니다.")
elif commandteam == Man_Utd:
    introduce_powerbalance(Man_Utd, Man_Utd_attack, Man_Utd_defence, Man_Utd_fieldown)
    print("\n호날두, 루니, 박지성, 베컴 등의 세계적인 스타 선수들이 거쳐간 맨체스터 유나이티드는 전 세계적인 팬덤을 보유한 클럽입니다.")
elif commandteam == Liverpool:
    introduce_powerbalance(Liverpool, Liverpool_attack, Liverpool_defence, Liverpool_fieldown)
    print("\n오랜 침체기를 끝내고 리그 상위권으로 도약한 리버풀은 공격과 수비에서 특히 우수한 클럽입니다.")
elif commandteam == Tottenham:
    introduce_powerbalance(Tottenham, Tottenham_attack, Tottenham_defence, Tottenham_fieldown)
    print("\n북런던의 전통과 역사를 자랑하는 토트넘은 세계적인 한국인 선수 손흥민이 주장을 맡고 있는 상위권 클럽입니다.")
elif commandteam == Chelsea:
    introduce_powerbalance(Chelsea, Chelsea_attack, Chelsea_defence, Chelsea_fieldown)
    print("\n예로부터 철벽 수비로 유명했던 첼시는 최근 젊은 공격수들의 영입으로 예전 PL에서의의 영광을 되찾고 있습니다.")
elif commandteam == Wolverhampton:
    introduce_powerbalance(Wolverhampton, Wolverhampton_attack, Wolverhampton_defence, Wolverhampton_fieldown)
    print("\n한국 국적인 황희찬 선수가 뛰고 있는 울버햄튼 또한 중원 점유율에서 높은 점수를 가져가는 클럽입니다.")
elif commandteam == West_Ham:
    introduce_powerbalance(West_Ham, West_Ham_attack, West_Ham_defence, West_Ham_fieldown)
    print("\n런던의 최고 인기 클럽인 웨스트햄은 최근 보웬과 쿠두스의 활약으로 좋은 폼을 이어나가고 있습니다.")
elif commandteam == Newcastle:
    introduce_powerbalance(Newcastle, Newcastle_attack, Newcastle_defence, Newcastle_fieldown)
    print("\n최근 빈 살만이 뉴캐슬을 인수하면서 최고의 자본력을 등에 업고 급격한 성장을 거듭하며 공격력을 큰 폭으로 향상한 PL의 돌풍입니다.")

def random_choice_예비용():
    PL = [Arsenal, Man_City, Man_Utd, Liverpool, Tottenham, Chelsea, Wolverhampton, West_Ham, Newcastle]
    PL_attack = [Arsenal_attack, Man_City_attack, Man_Utd_attack, Liverpool_attack, Tottenham_attack, Chelsea_attack, Wolverhampton_attack, West_Ham_attack, Newcastle_attack]
    PL_defence = [Arsenal_defence, Man_City_defence, Man_Utd_defence, Liverpool_defence, Tottenham_defence, Chelsea_defence, Wolverhampton_defence, West_Ham_defence, Newcastle_defence]
    PL_fieldown = [Arsenal_fieldown, Man_City_fieldown, Man_Utd_fieldown, Liverpool_fieldown, Tottenham_fieldown, Chelsea_fieldown, Wolverhampton_fieldown, West_Ham_fieldown, Newcastle_fieldown]
    PL_Random = random.choice(PL)
    PL_attack_Random = random.choice(PL_attack)
    PL_defence_Random = random.choice(PL_defence)
    PL_fieldown_Random = random.choice(PL_fieldown)
    print(PL_Random, "은 투자한 결과 다음과 같이 전력이 보강되었습니다:")
    print("공격진 : ", PL_attack_Random)
    print("수비진 : ", PL_defence_Random)
    print("중원 지배력", PL_fieldown_Random)

# def Arsenal_Run():
#     print("Pre-Matchweek\n투자할 부분을 선택하세요 : 트레이닝, 시설확충, 구단홍보")
#     c_arsenal = input("선택 : ")
#     if c_arsenal == "트레이닝":
#         print("트레이닝을 선택하셨습니다. 모든 능력치 +1")
#         Arsenal_attack + 1
#         Arsenal_defence + 1
#         Arsenal_fieldown + 1
#         print("다른 팀의 전략을 참고하시겠습니까?")
#         a_arsenal = input("Y/N")
#         if a_arsenal == "Y":
#             random_choice()


--------------------------------------------------------------------

# #2024-06-11 4차 수정본(준최종)

# import random
# import math
# import signal

# money = 100
# commandteam = 0
# Arsenal = "아스날"
# Arsenal_attack = 5
# Arsenal_defence = 5
# Arsenal_fieldown = 6
# Man_City = "맨시티"
# Man_City_attack = 11
# Man_City_defence = 7
# Man_City_fieldown = 7
# Man_Utd = "맨유"
# Man_Utd_attack = 5
# Man_Utd_defence = 7
# Man_Utd_fieldown = 8
# Liverpool = "리버풀"
# Liverpool_attack = 8
# Liverpool_defence = 9
# Liverpool_fieldown = 6
# Tottenham = "토트넘"
# Tottenham_attack = 7
# Tottenham_defence = 5
# Tottenham_fieldown = 9
# Chelsea = "첼시"
# Chelsea_attack = 6
# Chelsea_defence = 9
# Chelsea_fieldown = 8
# Wolverhampton = "울버햄튼"
# Wolverhampton_attack = 6
# Wolverhampton_defence = 6
# Wolverhampton_fieldown = 8
# West_Ham = "웨스트햄"
# West_Ham_attack = 5
# West_Ham_defence = 7
# West_Ham_fieldown = 6
# Newcastle = "뉴캐슬"
# Newcastle_attack = 8
# Newcastle_defence = 5
# Newcastle_fieldown = 5
# Arsenallist = [Arsenal_attack, Arsenal_defence, Arsenal_fieldown]
# Man_Citylist = [Man_City_attack, Man_City_defence, Man_City_fieldown]
# Man_Utdlist = [Man_Utd_attack, Man_Utd_defence, Man_Utd_fieldown]
# Liverpoollist = [Liverpool_attack, Liverpool_defence, Liverpool_fieldown]
# Tottenhamlist = [Tottenham_attack, Tottenham_defence, Tottenham_fieldown]
# Chelsealist = [Chelsea_attack, Chelsea_defence, Chelsea_fieldown]
# Wolverhamptonlist = [Wolverhampton_attack, Wolverhampton_defence, Wolverhampton_fieldown]
# West_Hamlist = [West_Ham_attack, West_Ham_defence, West_Ham_fieldown]
# Newcastlelist = [Newcastle_attack, Newcastle_defence, Newcastle_fieldown]
# PL = [Arsenal, Man_City, Man_Utd, Liverpool, Tottenham, Chelsea, Wolverhampton, West_Ham, Newcastle]

# print("PL에서 챔스가기!\n---------------------------------------------\n이제부터 당신은 Arsenal 팀의 감독입니다. PL 팀 중 하나를 선택하세요. 팀 변경의 기회는 없으니 신중히 고르세요!\n(용량 문제로 모든 팀들을 넣지 못한 점 죄송합니다!!)\n--------------------------------------------")
# print("[아스날, 맨시티, 맨유, 리버풀, 토트넘, 첼시, 울버햄튼, 웨스트햄, 뉴캐슬]")
# team = input("선택한 팀 : ")
# if team == "아스날":
#     commandteam = Arsenal
# elif team == "맨시티":
#     commandteam = Man_City
# elif team == "맨유":
#     commandteam = Man_Utd
# elif team == "리버풀":
#     commandteam = Liverpool
# elif team == "토트넘":
#     commandteam = Tottenham
# elif team == "첼시":
#     commandteam = Chelsea
# elif team == "울버햄튼":
#     commandteam = Wolverhampton
# elif team == "웨스트햄":
#     commandteam = West_Ham
# elif team == "뉴캐슬":
#     commandteam = Newcastle
# else:
#     print("양식에 맞춰 다시 작성해주세요!!")
#     exit()
# print("--------------------------------------------")
# print(team, "을 선택하셨습니다.\n")

# def introduce_powerbalance(a, b, c, d):
#     print("{}의\n공격력은 {}입니다.\n수비력은 {}입니다.\n중원 지배력은 {}입니다.".format(a, b, c, d))

# # 랜덤 초이스 (최종)

# def random_choice():
#     PL = [Man_City, Man_Utd, Liverpool, Tottenham, Chelsea, Wolverhampton, West_Ham, Newcastle]
#     PL_attack = [Arsenal_attack, Man_City_attack, Man_Utd_attack, Liverpool_attack, Tottenham_attack, Chelsea_attack, Wolverhampton_attack, West_Ham_attack, Newcastle_attack]
#     PL_defence = [Arsenal_defence, Man_City_defence, Man_Utd_defence, Liverpool_defence, Tottenham_defence, Chelsea_defence, Wolverhampton_defence, West_Ham_defence, Newcastle_defence]
#     PL_fieldown = [Arsenal_fieldown, Man_City_fieldown, Man_Utd_fieldown, Liverpool_fieldown, Tottenham_fieldown, Chelsea_fieldown, Wolverhampton_fieldown, West_Ham_fieldown, Newcastle_fieldown]
#     PL_Random = random.choice(PL)
#     PL_attack_Random = random.choice(PL_attack)
#     if PL_Random == Arsenal:
#         a = random.randint(-3, 3)
#         b = random.randint(-3, 3)
#         c = random.randint(-3, 3)
#         Arsenal_attack + a
#         Arsenal_defence + b
#         Arsenal_fieldown + c
#         print("아스날은 투자한 결과 다음과 같이 전력이 보강되었습니다:")
#         print("공격진 : ", Arsenal_attack)
#         print("수비진 : ", Arsenal_defence)
#         print("중원 지배력", Arsenal_fieldown)
#     elif PL_Random == Man_City:
#         a = random.randint(-3, 3)
#         b = random.randint(-3, 3)
#         c = random.randint(-3, 3)
#         Man_City_attack + a
#         Man_City_defence + b
#         Man_City_fieldown + c
#         print("맨시티는 투자한 결과 다음과 같이 전력이 보강되었습니다:")
#         print("공격진 : ", Man_City_attack)
#         print("수비진 : ", Man_City_defence)
#         print("중원 지배력", Man_City_fieldown)
#     elif PL_Random == Liverpool:
#         a = random.randint(-3, 3)
#         b = random.randint(-3, 3)
#         c = random.randint(-3, 3)
#         Liverpool_attack + a
#         Liverpool_defence + b
#         Liverpool_fieldown + c
#         print("리버풀은 투자한 결과 다음과 같이 전력이 보강되었습니다:")
#         print("공격진 : ", Liverpool_attack)
#         print("수비진 : ", Liverpool_defence)
#         print("중원 지배력", Liverpool_fieldown)
#     elif PL_Random == Tottenham:
#         a = random.randint(-3, 3)
#         b = random.randint(-3, 3)
#         c = random.randint(-3, 3)
#         Tottenham_attack + a
#         Tottenham_defence + b
#         Tottenham_fieldown + c
#         print("토트넘은 투자한 결과 다음과 같이 전력이 보강되었습니다:")
#         print("공격진 : ", Tottenham_attack)
#         print("수비진 : ", Tottenham_defence)
#         print("중원 지배력", Tottenham_fieldown)
#     elif PL_Random == Chelsea:
#         a = random.randint(-3, 3)
#         b = random.randint(-3, 3)
#         c = random.randint(-3, 3)
#         Chelsea_attack + a
#         Chelsea_defence + b
#         Chelsea_fieldown + c
#         print("첼시는 투자한 결과 다음과 같이 전력이 보강되었습니다:")
#         print("공격진 : ", Chelsea_attack)
#         print("수비진 : ", Chelsea_defence)
#         print("중원 지배력", Chelsea_fieldown)
#     elif PL_Random == Wolverhampton:
#         a = random.randint(-3, 3)
#         b = random.randint(-3, 3)
#         c = random.randint(-3, 3)
#         Wolverhampton_attack + a
#         Wolverhampton_defence + b
#         Wolverhampton_fieldown + c
#         print("첼시는 투자한 결과 다음과 같이 전력이 보강되었습니다:")
#         print("공격진 : ", Wolverhampton_attack)
#         print("수비진 : ", Wolverhampton_defence)
#         print("중원 지배력", Wolverhampton_fieldown)
#     elif PL_Random == West_Ham:
#         a = random.randint(-3, 3)
#         b = random.randint(-3, 3)
#         c = random.randint(-3, 3)
#         West_Ham_attack + a
#         West_Ham_defence + b
#         West_Ham_fieldown + c
#         print("웨스트햄은 투자한 결과 다음과 같이 전력이 보강되었습니다:")
#         print("공격진 : ", West_Ham_attack)
#         print("수비진 : ", West_Ham_defence)
#         print("중원 지배력", West_Ham_fieldown)
#     elif PL_Random == Newcastle:
#         a = random.randint(-3, 3)
#         b = random.randint(-3, 3)
#         c = random.randint(-3, 3)
#         Newcastle_attack + a
#         Newcastle_defence + b
#         Newcastle_fieldown + c
#         print("뉴캐슬은 투자한 결과 다음과 같이 전력이 보강되었습니다:")
#         print("공격진 : ", Newcastle_attack)
#         print("수비진 : ", Newcastle_defence)
#         print("중원 지배력", Newcastle_fieldown)

# 아스날_승점 = 0
# 맨시티_승점 = 0
# 맨유_승점 = 0
# 리버풀_승점 = 0
# 토트넘_승점 = 0
# 첼시_승점 = 0
# 울버햄튼_승점 = 0
# 웨스트햄_승점 = 0
# 뉴캐슬_승점 = 0

# # def Pre_MW():
# #     print("Pre-Matchweek\n투자할 부분을 선택하세요 : 트레이닝, 시설확충, 구단홍보")
# #     c_arsenal = input("선택 : ")
# #     if c_arsenal == "트레이닝":
# #         print("트레이닝을 선택하셨습니다. 중원 지배 능력치 +1")
# #         Arsenal_fieldown = Arsenal_fieldown + 1
# #         print("다른 팀 1개의 투자를 랜덤으로 살펴보겠습니다.")
# #         random_choice()
# #     elif c_arsenal == "시설확충":
# #         print("시설확충을 선택하셨습니다. 공격력 +1")
# #         Arsenal_attack = Arsenal_attack + 1
# #         print("다른 팀 1개의 투자를 랜덤으로 살펴보겠습니다.")
# #         random_choice()
# #     else:
# #         print("구단홍보를 선택하셨습니다. 수비력 +1")
# #         Arsenal_defence = Arsenal_defence + 1
# #         print("다른 팀 1개의 투자를 랜덤으로 살펴보겠습니다.")
# #         random_choice()
    

# n = 0
# def Arsenal_Run():
#     # UnboundLocalError: cannot access local variable '승점' where it is not associated with a value 이거 안뜨게 하려면 함수 안에서 변수를 초기화 시켜줘야 한다.
#     n = 0
#     Arsenal_attack = 5
#     Arsenal_defence = 5
#     Arsenal_fieldown = 6
#     print("Pre-Matchweek\n투자할 부분을 선택하세요 : 트레이닝, 시설확충, 구단홍보")
#     c_arsenal = input("선택 : ")
#     if c_arsenal == "트레이닝":
#         print("트레이닝을 선택하셨습니다. 중원 지배 능력치 +1")
#         Arsenal_fieldown = Arsenal_fieldown + 1
#         print("다른 팀 1개의 투자를 랜덤으로 살펴보겠습니다.")
#         random_choice()
#     elif c_arsenal == "시설확충":
#         print("시설확충을 선택하셨습니다. 공격력 +1")
#         Arsenal_attack = Arsenal_fieldown + 1
#         print("다른 팀 1개의 투자를 랜덤으로 살펴보겠습니다.")
#         random_choice()
#     else:
#         print("구단홍보를 선택하셨습니다. 수비력 +1")
#         Arsenal_defence = Arsenal_defence + 1
#         print("다른 팀 1개의 투자를 랜덤으로 살펴보겠습니다.")
#         random_choice()
#     아스날_승점 = 0
#     맨시티_승점 = 0
#     맨유_승점 = 0
#     리버풀_승점 = 0
#     토트넘_승점 = 0
#     첼시_승점 = 0
#     울버햄튼_승점 = 0
#     웨스트햄_승점 = 0
#     뉴캐슬_승점 = 0
#     아스날_승점 = 아스날_승점 + 0
#     맨시티_승점 = 맨시티_승점 + 0
#     맨유_승점 = 맨유_승점 + 0
#     리버풀_승점 = 리버풀_승점 + 0
#     토트넘_승점 = 토트넘_승점 + 0
#     첼시_승점 = 첼시_승점 + 0
#     울버햄튼_승점 = 울버햄튼_승점 + 0
#     웨스트햄_승점 = 웨스트햄_승점 + 0
#     뉴캐슬_승점 = 뉴캐슬_승점 + 0
#     a = str(input("다음 단계로 넘어가려면 Y를 입력해주세요.\n"))
#     if a == "Y":
#         print("2주가 흘렀습니다.\n--------------------------------------------\nMatchweek 1 - Away (St. James Park)\n--------------------------------------------\nNewcastle F.C.(HOME) vs Arsenal F.C.(AWAY)\n")
#         print("뉴캐슬 vs 아스날 전력 분석\n뉴캐슬의 vs 아스날의\n공격력은 {} vs {}입니다.\n수비력은 {} vs {}입니다.\n중원 지배력은 {} vs {}입니다.\n".format(Newcastle_attack, Arsenal_attack, Newcastle_defence, Arsenal_defence, Newcastle_fieldown, Arsenal_fieldown))
#         b = input(("포메이션을 선택하세요 : 3-4-3, 4-3-3, 4-2-3-1\n공격 우선 : 3-4-3, 수비 우선 : 4-3-3, 둘 다 : 4-2-3-1\n"))
#         if b == "3-4-3":
#             if (Arsenal_attack > Newcastle_attack and Arsenal_defence >= Newcastle_defence and Arsenal_fieldown >= Newcastle_fieldown) or (Arsenal_attack > Newcastle_attack and Arsenal_defence >= Newcastle_defence and Arsenal_fieldown < Newcastle_fieldown) or (Arsenal_attack == Newcastle_attack and Arsenal_defence >= Newcastle_defence and Arsenal_fieldown >= Newcastle_fieldown):
#                 print("--------------------------------------------\n{} - {}, 아스날 승\n--------------------------------------------".format(random.randint(0, 1), random.randint(2, 4)))
#                 아스날_승점 = 아스날_승점 + 3
#             elif (Arsenal_attack > Newcastle_attack and Arsenal_defence < Newcastle_defence and Arsenal_fieldown >= Newcastle_fieldown) or (Arsenal_attack == Newcastle_attack and Arsenal_defence < Newcastle_defence and Arsenal_fieldown >= Newcastle_fieldown) or (Arsenal_attack == Newcastle_attack and Arsenal_defence >= Newcastle_defence and Arsenal_fieldown < Newcastle_fieldown) or  (Arsenal_attack < Newcastle_attack and Arsenal_defence >= Newcastle_defence and Arsenal_fieldown >= Newcastle_fieldown):
#                 print("--------------------------------------------\n{} - {}, 무승부\n--------------------------------------------".format(random.randint(2, 2), random.randint(2, 2)))
#                 아스날_승점 = 아스날_승점 + 1
#             elif (Arsenal_attack > Newcastle_attack and Arsenal_defence < Newcastle_defence and Arsenal_fieldown < Newcastle_fieldown) or (Arsenal_attack == Newcastle_attack and Arsenal_defence < Newcastle_defence and Arsenal_fieldown < Newcastle_fieldown) or (Arsenal_attack < Newcastle_attack and Arsenal_defence < Newcastle_defence and Arsenal_fieldown >= Newcastle_fieldown) or (Arsenal_attack < Newcastle_attack and Arsenal_defence >= Newcastle_defence and Arsenal_fieldown < Newcastle_fieldown) or  (Arsenal_attack < Newcastle_attack and Arsenal_defence < Newcastle_defence and Arsenal_fieldown < Newcastle_fieldown):
#                 print("--------------------------------------------\n{} - {}, 뉴캐슬 승\n--------------------------------------------".format(random.randint(2, 3), random.randint(0, 1)))
#                 아스날_승점 = 아스날_승점 + 0
#         elif b == "4-3-3":
#             if (Arsenal_defence > Newcastle_defence and Arsenal_attack >= Newcastle_attack and Arsenal_fieldown >= Newcastle_fieldown) or (Arsenal_defence > Newcastle_defence and Arsenal_attack >= Newcastle_attack and Arsenal_fieldown < Newcastle_fieldown) or (Arsenal_defence == Newcastle_defence and Arsenal_attack >= Newcastle_attack and Arsenal_fieldown >= Newcastle_fieldown):
#                 print("--------------------------------------------\n{} - {}, 아스날 승\n--------------------------------------------".format(random.randint(0, 1), random.randint(2, 3)))
#                 아스날_승점 = 아스날_승점 + 3
#             elif (Arsenal_defence > Newcastle_defence and Arsenal_attack < Newcastle_attack and Arsenal_fieldown >= Newcastle_fieldown) or (Arsenal_defence == Newcastle_defence and Arsenal_attack < Newcastle_attack and Arsenal_fieldown >= Newcastle_fieldown) or (Arsenal_defence == Newcastle_defence and Arsenal_attack >= Newcastle_attack and Arsenal_fieldown < Newcastle_fieldown) or  (Arsenal_defence < Newcastle_defence and Arsenal_attack >= Newcastle_attack and Arsenal_fieldown >= Newcastle_fieldown):
#                 print("--------------------------------------------\n{} - {}, 무승부\n--------------------------------------------".format(random.randint(2, 2), random.randint(2, 2)))
#                 아스날_승점 = 아스날_승점 + 1
#             elif (Arsenal_defence > Newcastle_defence and Arsenal_attack < Newcastle_attack and Arsenal_fieldown < Newcastle_fieldown) or (Arsenal_defence == Newcastle_defence and Arsenal_attack < Newcastle_attack and Arsenal_fieldown < Newcastle_fieldown) or (Arsenal_defence < Newcastle_defence and Arsenal_attack < Newcastle_attack and Arsenal_fieldown >= Newcastle_fieldown) or (Arsenal_defence < Newcastle_defence and Arsenal_attack >= Newcastle_attack and Arsenal_fieldown < Newcastle_fieldown) or  (Arsenal_defence < Newcastle_defence and Arsenal_attack < Newcastle_attack and Arsenal_fieldown < Newcastle_fieldown):
#                 print("--------------------------------------------\n{} - {}, 뉴캐슬 승\n--------------------------------------------".format(random.randint(2, 4), random.randint(0, 1)))
#                 아스날_승점 = 아스날_승점 + 0
#         elif b == "4-2-3-1":
#             if (Arsenal_fieldown > Newcastle_fieldown and Arsenal_attack >= Newcastle_attack and Arsenal_defence >= Newcastle_defence) or (Arsenal_fieldown > Newcastle_fieldown and Arsenal_attack >= Newcastle_attack and Arsenal_defence < Newcastle_defence) or (Arsenal_fieldown == Newcastle_fieldown and Arsenal_attack >= Newcastle_attack and Arsenal_defence >= Newcastle_defence):
#                 print("--------------------------------------------\n{} - {}, 아스날 승\n--------------------------------------------".format(random.randint(0, 1), random.randint(2, 3)))
#                 아스날_승점 = 아스날_승점 + 3
#             elif (Arsenal_fieldown > Newcastle_fieldown and Arsenal_attack < Newcastle_attack and Arsenal_defence >= Newcastle_defence) or (Arsenal_fieldown == Newcastle_fieldown and Arsenal_attack < Newcastle_attack and Arsenal_defence >= Newcastle_defence) or (Arsenal_fieldown == Newcastle_fieldown and Arsenal_attack >= Newcastle_attack and Arsenal_defence < Newcastle_defence) or  (Arsenal_fieldown < Newcastle_fieldown and Arsenal_attack >= Newcastle_attack and Arsenal_defence >= Newcastle_defence):
#                 print("--------------------------------------------\n{} - {}, 무승부\n--------------------------------------------".format(random.randint(2, 2), random.randint(2, 2)))
#                 아스날_승점 = 아스날_승점 + 1
#             elif (Arsenal_fieldown > Newcastle_fieldown and Arsenal_attack < Newcastle_attack and Arsenal_defence < Newcastle_defence) or (Arsenal_fieldown == Newcastle_fieldown and Arsenal_attack < Newcastle_attack and Arsenal_defence < Newcastle_defence) or (Arsenal_fieldown < Newcastle_fieldown and Arsenal_attack < Newcastle_attack and Arsenal_defence >= Newcastle_defence) or (Arsenal_fieldown < Newcastle_fieldown and Arsenal_attack >= Newcastle_attack and Arsenal_defence < Newcastle_defence) or  (Arsenal_fieldown < Newcastle_fieldown and Arsenal_attack < Newcastle_attack and Arsenal_defence < Newcastle_defence):
#                 print("--------------------------------------------\n{} - {}, 뉴캐슬 승\n--------------------------------------------".format(random.randint(2, 4), random.randint(0, 1)))
#                 아스날_승점 = 아스날_승점 + 0
#         n = n + 1
#         print("[첫] 번째 경기를 무사히 끝냈습니다. 당신의 승점은 {}점 입니다".format(아스날_승점))
#         print("{}주차 프리미어리그 순위".format(n))
#         아스날_승점 = 아스날_승점
#         맨시티_승점 = random.randint(0,3)
#         리버풀_승점 = random.randint(0,3)
#         맨유_승점 = random.randint(0,3)
#         토트넘_승점 = random.randint(0,3)
#         첼시_승점 = random.randint(0,3)
#         울버햄튼_승점 = random.randint(0,3)
#         웨스트햄_승점 = random.randint(0,3)
#         뉴캐슬_승점 = random.randint(0,3)
#         팀_승점 = {
#         "아스날 FC": 아스날_승점,
#         "맨체스터 시티 FC": 맨시티_승점,
#         "맨체스터 유나이티드 FC" : 맨유_승점,
#         "리버풀 FC" : 리버풀_승점,
#         "토트넘 홋스퍼 FC" : 토트넘_승점,
#         "첼시 FC" : 첼시_승점,
#         "울버햄튼 원더러스 FC" : 울버햄튼_승점,
#         "웨스트햄 유나이티드 FC" : 웨스트햄_승점,
#         "뉴캐슬 FC" : 뉴캐슬_승점          
#         }
#         sorted_scoreboard = sorted(팀_승점.items(), key=lambda x: x[1], reverse=True)
#         print("\nEngland Premier League\n")
#         for 순위, (팀, 승점) in enumerate((sorted_scoreboard), start=1):
#             print(f"{순위}위 : {팀} - {승점}점")
#     a = str(input("다음 단계로 넘어가려면 Y를 입력해주세요.\n"))
#     if a == "Y":
#         print("Pre-Matchweek\n투자할 부분을 선택하세요 : 트레이닝, 시설확충, 구단홍보")
#         c_arsenal = input("선택 : ")
#         if c_arsenal == "트레이닝":
#             print("트레이닝을 선택하셨습니다. 중원 지배 능력치 +1")
#             Arsenal_fieldown = Arsenal_fieldown + 1
#             print("다른 팀 1개의 투자를 랜덤으로 살펴보겠습니다.")
#             random_choice()
#         elif c_arsenal == "시설확충":
#             print("시설확충을 선택하셨습니다. 공격력 +1")
#             Arsenal_attack = Arsenal_fieldown + 1
#             print("다른 팀 1개의 투자를 랜덤으로 살펴보겠습니다.")
#             random_choice()
#         else:
#             print("구단홍보를 선택하셨습니다. 수비력 +1")
#             Arsenal_defence = Arsenal_defence + 1
#             print("다른 팀 1개의 투자를 랜덤으로 살펴보겠습니다.")
#             random_choice()
#         print("2주가 흘렀습니다.\n--------------------------------------------\nMatchweek 2 - Home (Emirates Stadium)\n--------------------------------------------\nArsenal F.C.(HOME) vs West Ham United F.C.(AWAY)\n")
#         print("아스날 vs 웨스트햄 전력 분석\n웨스트햄의 vs 아스날의\n공격력은 {} vs {}입니다.\n수비력은 {} vs {}입니다.\n중원 지배력은 {} vs {}입니다.\n".format(West_Ham_attack, Arsenal_attack, West_Ham_defence, Arsenal_defence, West_Ham_fieldown, Arsenal_fieldown))
#         b = input(("포메이션을 선택하세요 : 3-4-3, 4-3-3, 4-2-3-1\n공격 우선 : 3-4-3, 수비 우선 : 4-3-3, 둘 다 : 4-2-3-1\n"))
#         if b == "3-4-3":
#             if (Arsenal_attack > West_Ham_attack and Arsenal_defence >= West_Ham_defence and Arsenal_fieldown >= West_Ham_fieldown) or (Arsenal_attack > West_Ham_attack and Arsenal_defence >= West_Ham_defence and Arsenal_fieldown < West_Ham_fieldown) or (Arsenal_attack == West_Ham_attack and Arsenal_defence >= West_Ham_defence and Arsenal_fieldown >= West_Ham_fieldown):
#                 print("--------------------------------------------\n{} - {}, 아스날 승\n--------------------------------------------".format(random.randint(0, 1), random.randint(2, 4)))
#                 아스날_승점 = 아스날_승점 + 3
#             elif (Arsenal_attack > West_Ham_attack and Arsenal_defence < West_Ham_defence and Arsenal_fieldown >= West_Ham_fieldown) or (Arsenal_attack == West_Ham_attack and Arsenal_defence < West_Ham_defence and Arsenal_fieldown >= West_Ham_fieldown) or (Arsenal_attack == West_Ham_attack and Arsenal_defence >= Newcastle_defence and Arsenal_fieldown < Newcastle_fieldown) or  (Arsenal_attack < West_Ham_attack and Arsenal_defence >= West_Ham_defence and Arsenal_fieldown >= West_Ham_fieldown):
#                 print("--------------------------------------------\n{} - {}, 무승부\n--------------------------------------------".format(random.randint(2, 2), random.randint(2, 2)))
#                 아스날_승점 = 아스날_승점 + 1
#             elif (Arsenal_attack > West_Ham_attack and Arsenal_defence < West_Ham_defence and Arsenal_fieldown < West_Ham_fieldown) or (Arsenal_attack == West_Ham_attack and Arsenal_defence < West_Ham_defence and Arsenal_fieldown < West_Ham_fieldown) or (Arsenal_attack < West_Ham_attack and Arsenal_defence < West_Ham_defence and Arsenal_fieldown >= West_Ham_fieldown) or (Arsenal_attack < West_Ham_attack and Arsenal_defence >= West_Ham_defence and Arsenal_fieldown < West_Ham_fieldown) or  (Arsenal_attack < West_Ham_attack and Arsenal_defence < West_Ham_defence and Arsenal_fieldown < West_Ham_fieldown):
#                 print("--------------------------------------------\n{} - {}, 뉴캐슬 승\n--------------------------------------------".format(random.randint(2, 3), random.randint(0, 1)))
#                 아스날_승점 = 아스날_승점 + 0
#         elif b == "4-3-3":
#             if (Arsenal_defence > West_Ham_defence and Arsenal_attack >= West_Ham_attack and Arsenal_fieldown >= West_Ham_fieldown) or (Arsenal_defence > West_Ham_defence and Arsenal_attack >= West_Ham_attack and Arsenal_fieldown < West_Ham_fieldown) or (Arsenal_defence == West_Ham_defence and Arsenal_attack >= West_Ham_attack and Arsenal_fieldown >= West_Ham_fieldown):
#                 print("--------------------------------------------\n{} - {}, 아스날 승\n--------------------------------------------".format(random.randint(0, 1), random.randint(2, 3)))
#                 아스날_승점 = 아스날_승점 + 3
#             elif (Arsenal_defence > West_Ham_defence and Arsenal_attack < West_Ham_attack and Arsenal_fieldown >= West_Ham_fieldown) or (Arsenal_defence == West_Ham_defence and Arsenal_attack < West_Ham_attack and Arsenal_fieldown >= West_Ham_fieldown) or (Arsenal_defence == West_Ham_defence and Arsenal_attack >= West_Ham_attack and Arsenal_fieldown < West_Ham_fieldown) or  (Arsenal_defence < West_Ham_defence and Arsenal_attack >= West_Ham_attack and Arsenal_fieldown >= West_Ham_fieldown):
#                 print("--------------------------------------------\n{} - {}, 무승부\n--------------------------------------------".format(random.randint(2, 2), random.randint(2, 2)))
#                 아스날_승점 = 아스날_승점 + 1
#             elif (Arsenal_defence > West_Ham_defence and Arsenal_attack < West_Ham_attack and Arsenal_fieldown < West_Ham_fieldown) or (Arsenal_defence == West_Ham_defence and Arsenal_attack < West_Ham_attack and Arsenal_fieldown < West_Ham_fieldown) or (Arsenal_defence < West_Ham_defence and Arsenal_attack < West_Ham_attack and Arsenal_fieldown >= West_Ham_fieldown) or (Arsenal_defence < West_Ham_defence and Arsenal_attack >= West_Ham_attack and Arsenal_fieldown < West_Ham_fieldown) or  (Arsenal_defence < West_Ham_defence and Arsenal_attack < West_Ham_attack and Arsenal_fieldown < West_Ham_fieldown):
#                 print("--------------------------------------------\n{} - {}, 뉴캐슬 승\n--------------------------------------------".format(random.randint(2, 4), random.randint(0, 1)))
#                 아스날_승점 = 아스날_승점 + 0
#         elif b == "4-2-3-1":
#             if (Arsenal_fieldown > West_Ham_fieldown and Arsenal_attack >= West_Ham_attack and Arsenal_defence >= West_Ham_defence) or (Arsenal_fieldown > West_Ham_fieldown and Arsenal_attack >= West_Ham_attack and Arsenal_defence < West_Ham_defence) or (Arsenal_fieldown == West_Ham_fieldown and Arsenal_attack >= West_Ham_attack and Arsenal_defence >= West_Ham_defence):
#                 print("--------------------------------------------\n{} - {}, 아스날 승\n--------------------------------------------".format(random.randint(0, 1), random.randint(2, 3)))
#                 아스날_승점 = 아스날_승점 + 3
#             elif (Arsenal_fieldown > West_Ham_fieldown and Arsenal_attack < West_Ham_attack and Arsenal_defence >= West_Ham_defence) or (Arsenal_fieldown == West_Ham_fieldown and Arsenal_attack < West_Ham_attack and Arsenal_defence >= West_Ham_defence) or (Arsenal_fieldown == West_Ham_fieldown and Arsenal_attack >= West_Ham_attack and Arsenal_defence < West_Ham_defence) or  (Arsenal_fieldown < West_Ham_fieldown and Arsenal_attack >= West_Ham_attack and Arsenal_defence >= West_Ham_defence):
#                 print("--------------------------------------------\n{} - {}, 무승부\n--------------------------------------------".format(random.randint(2, 2), random.randint(2, 2)))
#                 아스날_승점 = 아스날_승점 + 1
#             elif (Arsenal_fieldown > West_Ham_fieldown and Arsenal_attack < West_Ham_attack and Arsenal_defence < West_Ham_defence) or (Arsenal_fieldown == West_Ham_fieldown and Arsenal_attack < West_Ham_attack and Arsenal_defence < West_Ham_defence) or (Arsenal_fieldown < West_Ham_fieldown and Arsenal_attack < West_Ham_attack and Arsenal_defence >= West_Ham_defence) or (Arsenal_fieldown < West_Ham_fieldown and Arsenal_attack >= West_Ham_attack and Arsenal_defence < West_Ham_defence) or  (Arsenal_fieldown < West_Ham_fieldown and Arsenal_attack < West_Ham_attack and Arsenal_defence < West_Ham_defence):
#                 print("--------------------------------------------\n{} - {}, 뉴캐슬 승\n--------------------------------------------".format(random.randint(2, 4), random.randint(0, 1)))
#                 아스날_승점 = 아스날_승점 + 0
#         n = n + 1
#         print("[두] 번째 경기를 무사히 끝냈습니다. 당신의 승점은 {}점 입니다".format(아스날_승점))
#         print("{}주차 프리미어리그 순위".format(n))
#         아스날_승점 = 아스날_승점
#         맨시티_승점 = random.randint(0,3) + 맨시티_승점
#         리버풀_승점 = random.randint(0,3) + 리버풀_승점
#         맨유_승점 = random.randint(0,3) + 맨유_승점
#         토트넘_승점 = random.randint(0,3) + 토트넘_승점
#         첼시_승점 = random.randint(0,3) + 첼시_승점
#         울버햄튼_승점 = random.randint(0,3) + 울버햄튼_승점
#         웨스트햄_승점 = random.randint(0,3) + 웨스트햄_승점
#         뉴캐슬_승점 = random.randint(0,3) + 뉴캐슬_승점
#         팀_승점 = {
#         "아스날 FC": 아스날_승점,
#         "맨체스터 시티 FC": 맨시티_승점,
#         "맨체스터 유나이티드 FC" : 맨유_승점,
#         "리버풀 FC" : 리버풀_승점,
#         "토트넘 홋스퍼 FC" : 토트넘_승점,
#         "첼시 FC" : 첼시_승점,
#         "울버햄튼 원더러스 FC" : 울버햄튼_승점,
#         "웨스트햄 유나이티드 FC" : 웨스트햄_승점,
#         "뉴캐슬 FC" : 뉴캐슬_승점          
#         }
#         sorted_scoreboard = sorted(팀_승점.items(), key=lambda x: x[1], reverse=True)
#         print("\nEngland Premier League\n")
#         for 순위, (팀, 승점) in enumerate((sorted_scoreboard), start=1):
#             print(f"{순위}위 : {팀} - {승점}점")
#         a = str(input("다음 단계로 넘어가려면 Y를 입력해주세요.\n"))
#     if a == "Y":
#         print("Pre-Matchweek\n투자할 부분을 선택하세요 : 트레이닝, 시설확충, 구단홍보")
#         c_arsenal = input("선택 : ")
#         if c_arsenal == "트레이닝":
#             print("트레이닝을 선택하셨습니다. 중원 지배 능력치 +1")
#             Arsenal_fieldown = Arsenal_fieldown + 1
#             print("다른 팀 1개의 투자를 랜덤으로 살펴보겠습니다.")
#             random_choice()
#         elif c_arsenal == "시설확충":
#             print("시설확충을 선택하셨습니다. 공격력 +1")
#             Arsenal_attack = Arsenal_fieldown + 1
#             print("다른 팀 1개의 투자를 랜덤으로 살펴보겠습니다.")
#             random_choice()
#         else:
#             print("구단홍보를 선택하셨습니다. 수비력 +1")
#             Arsenal_defence = Arsenal_defence + 1
#             print("다른 팀 1개의 투자를 랜덤으로 살펴보겠습니다.")
#             random_choice()
#     if a == "Y":
#         print("2주가 흘렀습니다.\n--------------------------------------------\nMatchweek 3 - Away (Molineux Stadium)\n--------------------------------------------\nNewcastle F.C.(HOME) vs Arsenal F.C.(AWAY)\n")
#         print("울버햄튼 vs 아스날 전력 분석\n뉴캐슬의 vs 아스날의\n공격력은 {} vs {}입니다.\n수비력은 {} vs {}입니다.\n중원 지배력은 {} vs {}입니다.\n".format(Newcastle_attack, Arsenal_attack, Newcastle_defence, Arsenal_defence, Newcastle_fieldown, Arsenal_fieldown))
#         b = input(("포메이션을 선택하세요 : 3-4-3, 4-3-3, 4-2-3-1\n공격 우선 : 3-4-3, 수비 우선 : 4-3-3, 둘 다 : 4-2-3-1\n"))
#         if b == "3-4-3":
#             if (Arsenal_attack > Wolverhampton_attack and Arsenal_defence >= Wolverhampton_defence and Arsenal_fieldown >= Wolverhampton_fieldown) or (Arsenal_attack > Wolverhampton_attack and Arsenal_defence >= Newcastle_defence and Arsenal_fieldown < Newcastle_fieldown) or (Arsenal_attack == Newcastle_attack and Arsenal_defence >= Newcastle_defence and Arsenal_fieldown >= Newcastle_fieldown):
#                 print("--------------------------------------------\n{} - {}, 아스날 승\n--------------------------------------------".format(random.randint(0, 1), random.randint(2, 4)))
#                 아스날_승점 = 아스날_승점 + 3
#             elif (Arsenal_attack > Wolverhampton_attack and Arsenal_defence < Wolverhampton_defence and Arsenal_fieldown >= Wolverhampton_fieldown) or (Arsenal_attack == Wolverhampton_attack and Arsenal_defence < Wolverhampton_defence and Arsenal_fieldown >= Wolverhampton_fieldown) or (Arsenal_attack == Wolverhampton_attack and Arsenal_defence >= Wolverhampton_defence and Arsenal_fieldown < Wolverhampton_fieldown) or (Arsenal_attack < Wolverhampton_attack and Arsenal_defence >= Wolverhampton_defence and Arsenal_fieldown >= Wolverhampton_fieldown):
#                 print("--------------------------------------------\n{} - {}, 무승부\n--------------------------------------------".format(random.randint(2, 2), random.randint(2, 2)))
#                 아스날_승점 = 아스날_승점 + 1
#             elif (Arsenal_attack > Wolverhampton_attack and Arsenal_defence < Wolverhampton_defence and Arsenal_fieldown < Wolverhampton_fieldown) or (Arsenal_attack == Wolverhampton_attack and Arsenal_defence < Wolverhampton_defence and Arsenal_fieldown < Wolverhampton_fieldown) or (Arsenal_attack < Wolverhampton_attack and Arsenal_defence < Wolverhampton_defence and Arsenal_fieldown >= Wolverhampton_fieldown) or (Arsenal_attack < Wolverhampton_attack and Arsenal_defence >= Wolverhampton_defence and Arsenal_fieldown < Wolverhampton_fieldown) or (Arsenal_attack < Wolverhampton_attack and Arsenal_defence < Wolverhampton_defence and Arsenal_fieldown < Wolverhampton_fieldown):
#                 print("--------------------------------------------\n{} - {}, 뉴캐슬 승\n--------------------------------------------".format(random.randint(2, 3), random.randint(0, 1)))
#                 아스날_승점 = 아스날_승점 + 0
#         elif b == "4-3-3":
#             if (Arsenal_defence > Wolverhampton_defence and Arsenal_attack >= Wolverhampton_attack and Arsenal_fieldown >= Wolverhampton_fieldown) or (Arsenal_defence > Wolverhampton_defence and Arsenal_attack >= Wolverhampton_attack and Arsenal_fieldown < Wolverhampton_fieldown) or (Arsenal_defence == Wolverhampton_defence and Arsenal_attack >= Wolverhampton_attack and Arsenal_fieldown >= Wolverhampton_fieldown):
#                 print("--------------------------------------------\n{} - {}, 아스날 승\n--------------------------------------------".format(random.randint(0, 1), random.randint(2, 3)))
#                 아스날_승점 = 아스날_승점 + 3
#             elif (Arsenal_defence > Wolverhampton_defence and Arsenal_attack < Wolverhampton_attack and Arsenal_fieldown >= Wolverhampton_fieldown) or (Arsenal_defence == Wolverhampton_defence and Arsenal_attack < Wolverhampton_attack and Arsenal_fieldown >= Wolverhampton_fieldown) or (Arsenal_defence == Wolverhampton_defence and Arsenal_attack >= Wolverhampton_attack and Arsenal_fieldown < Wolverhampton_fieldown) or  (Arsenal_defence < Wolverhampton_defence and Arsenal_attack >= Wolverhampton_attack and Arsenal_fieldown >= Wolverhampton_fieldown):
#                 print("--------------------------------------------\n{} - {}, 무승부\n--------------------------------------------".format(random.randint(2, 2), random.randint(2, 2)))
#                 아스날_승점 = 아스날_승점 + 1
#             elif (Arsenal_defence > Wolverhampton_defence and Arsenal_attack < Wolverhampton_attack and Arsenal_fieldown < Wolverhampton_fieldown) or (Arsenal_defence == Wolverhampton_defence and Arsenal_attack < Wolverhampton_attack and Arsenal_fieldown < Wolverhampton_fieldown) or (Arsenal_defence < Wolverhampton_defence and Arsenal_attack < Wolverhampton_attack and Arsenal_fieldown >= Wolverhampton_fieldown) or (Arsenal_defence < Wolverhampton_defence and Arsenal_attack >= Wolverhampton_attack and Arsenal_fieldown < Wolverhampton_fieldown) or (Arsenal_defence < Wolverhampton_defence and Arsenal_attack < Wolverhampton_attack and Arsenal_fieldown < Wolverhampton_fieldown):
#                 print("--------------------------------------------\n{} - {}, 울버햄튼 승\n--------------------------------------------".format(random.randint(2, 4), random.randint(0, 1)))
#                 아스날_승점 = 아스날_승점 + 0
#         elif b == "4-2-3-1":
#             if (Arsenal_fieldown > Wolverhampton_fieldown and Arsenal_attack >= Wolverhampton_attack and Arsenal_defence >= Wolverhampton_defence) or (Arsenal_fieldown > Wolverhampton_fieldown and Arsenal_attack >= Wolverhampton_attack and Arsenal_defence < Wolverhampton_defence) or (Arsenal_fieldown == Wolverhampton_fieldown and Arsenal_attack >= Wolverhampton_attack and Arsenal_defence >= Wolverhampton_defence):
#                 print("--------------------------------------------\n{} - {}, 아스날 승\n--------------------------------------------".format(random.randint(0, 1), random.randint(2, 3)))
#                 아스날_승점 = 아스날_승점 + 3
#             elif (Arsenal_fieldown > Wolverhampton_fieldown and Arsenal_attack < Wolverhampton_attack and Arsenal_defence >= Wolverhampton_defence) or (Arsenal_fieldown == Wolverhampton_fieldown and Arsenal_attack < Wolverhampton_attack and Arsenal_defence >= Wolverhampton_defence) or (Arsenal_fieldown == Wolverhampton_fieldown and Arsenal_attack >= Wolverhampton_attack and Arsenal_defence < Wolverhampton_defence) or  (Arsenal_fieldown < Wolverhampton_fieldown and Arsenal_attack >= Wolverhampton_attack and Arsenal_defence >= Wolverhampton_defence):
#                 print("--------------------------------------------\n{} - {}, 무승부\n--------------------------------------------".format(random.randint(2, 2), random.randint(2, 2)))
#                 아스날_승점 = 아스날_승점 + 1
#             elif (Arsenal_fieldown > Wolverhampton_fieldown and Arsenal_attack < Wolverhampton_attack and Arsenal_defence < Wolverhampton_defence) or (Arsenal_fieldown == Wolverhampton_fieldown and Arsenal_attack < Wolverhampton_attack and Arsenal_defence < Wolverhampton_defence) or (Arsenal_fieldown < Wolverhampton_fieldown and Arsenal_attack < Wolverhampton_attack and Arsenal_defence >= Wolverhampton_defence) or (Arsenal_fieldown < Wolverhampton_fieldown and Arsenal_attack >= Wolverhampton_attack and Arsenal_defence < Wolverhampton_defence) or  (Arsenal_fieldown < Wolverhampton_fieldown and Arsenal_attack < Wolverhampton_attack and Arsenal_defence < Wolverhampton_defence):
#                 print("--------------------------------------------\n{} - {}, 울버햄튼 승\n--------------------------------------------".format(random.randint(2, 4), random.randint(0, 1)))
#                 아스날_승점 = 아스날_승점 + 0
#         n = n + 1
#         print("[세] 번째 경기를 무사히 끝냈습니다. 당신의 승점은 {}점 입니다".format(아스날_승점))
#         print("{}주차 프리미어리그 순위".format(n))
#         아스날_승점 = 아스날_승점
#         맨시티_승점 = random.randint(0,3) + 맨시티_승점
#         리버풀_승점 = random.randint(0,3) + 리버풀_승점
#         맨유_승점 = random.randint(0,3) + 맨유_승점
#         토트넘_승점 = random.randint(0,3) + 토트넘_승점
#         첼시_승점 = random.randint(0,3) + 첼시_승점
#         울버햄튼_승점 = random.randint(0,3) + 울버햄튼_승점
#         웨스트햄_승점 = random.randint(0,3) + 웨스트햄_승점
#         뉴캐슬_승점 = random.randint(0,3) + 뉴캐슬_승점
#         팀_승점 = {
#         "아스날 FC": 아스날_승점,
#         "맨체스터 시티 FC": 맨시티_승점,
#         "맨체스터 유나이티드 FC" : 맨유_승점,
#         "리버풀 FC" : 리버풀_승점,
#         "토트넘 홋스퍼 FC" : 토트넘_승점,
#         "첼시 FC" : 첼시_승점,
#         "울버햄튼 원더러스 FC" : 울버햄튼_승점,
#         "웨스트햄 유나이티드 FC" : 웨스트햄_승점,
#         "뉴캐슬 FC" : 뉴캐슬_승점          
#         }
#         sorted_scoreboard = sorted(팀_승점.items(), key=lambda x: x[1], reverse=True)
#         print("\nEngland Premier League\n")
#         for 순위, (팀, 승점) in enumerate((sorted_scoreboard), start=1):
#             print(f"{순위}위 : {팀} - {승점}점")
#     a = str(input("다음 단계로 넘어가려면 Y를 입력해주세요.\n"))
#     if a == "Y":
#         print("Pre-Matchweek\n투자할 부분을 선택하세요 : 트레이닝, 시설확충, 구단홍보")
#         c_arsenal = input("선택 : ")
#         if c_arsenal == "트레이닝":
#             print("트레이닝을 선택하셨습니다. 중원 지배 능력치 +1")
#             Arsenal_fieldown = Arsenal_fieldown + 1
#             print("다른 팀 1개의 투자를 랜덤으로 살펴보겠습니다.")
#             random_choice()
#         elif c_arsenal == "시설확충":
#             print("시설확충을 선택하셨습니다. 공격력 +1")
#             Arsenal_attack = Arsenal_fieldown + 1
#             print("다른 팀 1개의 투자를 랜덤으로 살펴보겠습니다.")
#             random_choice()
#         else:
#             print("구단홍보를 선택하셨습니다. 수비력 +1")
#             Arsenal_defence = Arsenal_defence + 1
#             print("다른 팀 1개의 투자를 랜덤으로 살펴보겠습니다.")
#             random_choice()
#     if a == "Y":
#         print("2주가 흘렀습니다.\n--------------------------------------------\nMatchweek 4 - Home (Emirates Stadium)\n--------------------------------------------\nArsenal F.C.(HOME) vs Chelsea F.C.(AWAY)\n")
#         print("아스날 vs 첼시 전력 분석\n아스날의 vs 첼시의\n공격력은 {} vs {}입니다.\n수비력은 {} vs {}입니다.\n중원 지배력은 {} vs {}입니다.\n".format(Arsenal_attack, Chelsea_attack, Arsenal_defence, Chelsea_defence, Arsenal_fieldown, Chelsea_fieldown))
#         b = input(("포메이션을 선택하세요 : 3-4-3, 4-3-3, 4-2-3-1\n공격 우선 : 3-4-3, 수비 우선 : 4-3-3, 둘 다 : 4-2-3-1\n"))
#         if b == "3-4-3":
#             if (Arsenal_attack > Chelsea_attack and Arsenal_defence >= Chelsea_defence and Arsenal_fieldown >= Chelsea_fieldown) or (Arsenal_attack > Chelsea_attack and Arsenal_defence >= Newcastle_defence and Arsenal_fieldown < Newcastle_fieldown) or (Arsenal_attack == Newcastle_attack and Arsenal_defence >= Newcastle_defence and Arsenal_fieldown >= Newcastle_fieldown):
#                 print("--------------------------------------------\n{} - {}, 아스날 승\n--------------------------------------------".format(random.randint(0, 1), random.randint(2, 4)))
#                 아스날_승점 = 아스날_승점 + 3
#             elif (Arsenal_attack > Chelsea_attack and Arsenal_defence < Chelsea_defence and Arsenal_fieldown >= Chelsea_fieldown) or (Arsenal_attack == Chelsea_attack and Arsenal_defence < Chelsea_defence and Arsenal_fieldown >= Chelsea_fieldown) or (Arsenal_attack == Chelsea_attack and Arsenal_defence >= Chelsea_defence and Arsenal_fieldown < Chelsea_fieldown) or (Arsenal_attack < Chelsea_attack and Arsenal_defence >= Chelsea_defence and Arsenal_fieldown >= Chelsea_fieldown):
#                 print("--------------------------------------------\n{} - {}, 무승부\n--------------------------------------------".format(random.randint(2, 2), random.randint(2, 2)))
#                 아스날_승점 = 아스날_승점 + 1
#             elif (Arsenal_attack > Chelsea_attack and Arsenal_defence < Chelsea_defence and Arsenal_fieldown < Chelsea_fieldown) or (Arsenal_attack == Chelsea_attack and Arsenal_defence < Chelsea_defence and Arsenal_fieldown < Chelsea_fieldown) or (Arsenal_attack < Chelsea_attack and Arsenal_defence < Chelsea_defence and Arsenal_fieldown >= Chelsea_fieldown) or (Arsenal_attack < Chelsea_attack and Arsenal_defence >= Chelsea_defence and Arsenal_fieldown < Chelsea_fieldown) or (Arsenal_attack < Chelsea_attack and Arsenal_defence < Chelsea_defence and Arsenal_fieldown < Chelsea_fieldown):
#                 print("--------------------------------------------\n{} - {}, 첼시 승\n--------------------------------------------".format(random.randint(2, 3), random.randint(0, 1)))
#                 아스날_승점 = 아스날_승점 + 0
#         elif b == "4-3-3":
#             if (Arsenal_defence > Chelsea_defence and Arsenal_attack >= Chelsea_attack and Arsenal_fieldown >= Chelsea_fieldown) or (Arsenal_defence > Chelsea_defence and Arsenal_attack >= Chelsea_attack and Arsenal_fieldown < Chelsea_fieldown) or (Arsenal_defence == Chelsea_defence and Arsenal_attack >= Chelsea_attack and Arsenal_fieldown >= Chelsea_fieldown):
#                 print("--------------------------------------------\n{} - {}, 아스날 승\n--------------------------------------------".format(random.randint(0, 1), random.randint(2, 3)))
#                 아스날_승점 = 아스날_승점 + 3
#             elif (Arsenal_defence > Chelsea_defence and Arsenal_attack < Chelsea_attack and Arsenal_fieldown >= Chelsea_fieldown) or (Arsenal_defence == Chelsea_defence and Arsenal_attack < Chelsea_attack and Arsenal_fieldown >= Chelsea_fieldown) or (Arsenal_defence == Chelsea_defence and Arsenal_attack >= Chelsea_attack and Arsenal_fieldown < Chelsea_fieldown) or  (Arsenal_defence < Chelsea_defence and Arsenal_attack >= Chelsea_attack and Arsenal_fieldown >= Chelsea_fieldown):
#                 print("--------------------------------------------\n{} - {}, 무승부\n--------------------------------------------".format(random.randint(2, 2), random.randint(2, 2)))
#                 아스날_승점 = 아스날_승점 + 1
#             elif (Arsenal_defence > Chelsea_defence and Arsenal_attack < Chelsea_attack and Arsenal_fieldown < Chelsea_fieldown) or (Arsenal_defence == Chelsea_defence and Arsenal_attack < Chelsea_attack and Arsenal_fieldown < Chelsea_fieldown) or (Arsenal_defence < Chelsea_defence and Arsenal_attack < Chelsea_attack and Arsenal_fieldown >= Chelsea_fieldown) or (Arsenal_defence < Chelsea_defence and Arsenal_attack >= Chelsea_attack and Arsenal_fieldown < Chelsea_fieldown) or (Arsenal_defence < Chelsea_defence and Arsenal_attack < Chelsea_attack and Arsenal_fieldown < Chelsea_fieldown):
#                 print("--------------------------------------------\n{} - {}, 첼시 승\n--------------------------------------------".format(random.randint(2, 4), random.randint(0, 1)))
#                 아스날_승점 = 아스날_승점 + 0
#         elif b == "4-2-3-1":
#             if (Arsenal_fieldown > Chelsea_fieldown and Arsenal_attack >= Chelsea_attack and Arsenal_defence >= Chelsea_defence) or (Arsenal_fieldown > Chelsea_fieldown and Arsenal_attack >= Chelsea_attack and Arsenal_defence < Chelsea_defence) or (Arsenal_fieldown == Chelsea_fieldown and Arsenal_attack >= Chelsea_attack and Arsenal_defence >= Chelsea_defence):
#                 print("--------------------------------------------\n{} - {}, 아스날 승\n--------------------------------------------".format(random.randint(0, 1), random.randint(2, 3)))
#                 아스날_승점 = 아스날_승점 + 3
#             elif (Arsenal_fieldown > Chelsea_fieldown and Arsenal_attack < Chelsea_attack and Arsenal_defence >= Chelsea_defence) or (Arsenal_fieldown == Chelsea_fieldown and Arsenal_attack < Chelsea_attack and Arsenal_defence >= Chelsea_defence) or (Arsenal_fieldown == Chelsea_fieldown and Arsenal_attack >= Chelsea_attack and Arsenal_defence < Chelsea_defence) or  (Arsenal_fieldown < Chelsea_fieldown and Arsenal_attack >= Chelsea_attack and Arsenal_defence >= Chelsea_defence):
#                 print("--------------------------------------------\n{} - {}, 무승부\n--------------------------------------------".format(random.randint(2, 2), random.randint(2, 2)))
#                 아스날_승점 = 아스날_승점 + 1
#             elif (Arsenal_fieldown > Chelsea_fieldown and Arsenal_attack < Chelsea_attack and Arsenal_defence < Chelsea_defence) or (Arsenal_fieldown == Chelsea_fieldown and Arsenal_attack < Chelsea_attack and Arsenal_defence < Chelsea_defence) or (Arsenal_fieldown < Chelsea_fieldown and Arsenal_attack < Chelsea_attack and Arsenal_defence >= Chelsea_defence) or (Arsenal_fieldown < Chelsea_fieldown and Arsenal_attack >= Chelsea_attack and Arsenal_defence < Chelsea_defence) or  (Arsenal_fieldown < Chelsea_fieldown and Arsenal_attack < Chelsea_attack and Arsenal_defence < Chelsea_defence):
#                 print("--------------------------------------------\n{} - {}, 첼시 승\n--------------------------------------------".format(random.randint(2, 4), random.randint(0, 1)))
#                 아스날_승점 = 아스날_승점 + 0
#         n = n + 1
#         print("[세] 번째 경기를 무사히 끝냈습니다. 당신의 승점은 {}점 입니다".format(아스날_승점))
#         print("{}주차 프리미어리그 순위".format(n))
#         아스날_승점 = 아스날_승점
#         맨시티_승점 = random.randint(0,3) + 맨시티_승점
#         리버풀_승점 = random.randint(0,3) + 리버풀_승점
#         맨유_승점 = random.randint(0,3) + 맨유_승점
#         토트넘_승점 = random.randint(0,3) + 토트넘_승점
#         첼시_승점 = random.randint(0,3) + 첼시_승점
#         울버햄튼_승점 = random.randint(0,3) + 울버햄튼_승점
#         웨스트햄_승점 = random.randint(0,3) + 웨스트햄_승점
#         뉴캐슬_승점 = random.randint(0,3) + 뉴캐슬_승점
#         팀_승점 = {
#         "아스날 FC": 아스날_승점,
#         "맨체스터 시티 FC": 맨시티_승점,
#         "맨체스터 유나이티드 FC" : 맨유_승점,
#         "리버풀 FC" : 리버풀_승점,
#         "토트넘 홋스퍼 FC" : 토트넘_승점,
#         "첼시 FC" : 첼시_승점,
#         "울버햄튼 원더러스 FC" : 울버햄튼_승점,
#         "웨스트햄 유나이티드 FC" : 웨스트햄_승점,
#         "뉴캐슬 FC" : 뉴캐슬_승점          
#         }
#         sorted_scoreboard = sorted(팀_승점.items(), key=lambda x: x[1], reverse=True)
#         print("\nEngland Premier League\n")
#         for 순위, (팀, 승점) in enumerate((sorted_scoreboard), start=1):
#             print(f"{순위}위 : {팀} - {승점}점")
#     a = str(input("다음 단계로 넘어가려면 Y를 입력해주세요.\n"))
#     if a == "Y":
#         print("Pre-Matchweek\n투자할 부분을 선택하세요 : 트레이닝, 시설확충, 구단홍보")
#         c_arsenal = input("선택 : ")
#         if c_arsenal == "트레이닝":
#             print("트레이닝을 선택하셨습니다. 중원 지배 능력치 +1")
#             Arsenal_fieldown = Arsenal_fieldown + 1
#             print("다른 팀 1개의 투자를 랜덤으로 살펴보겠습니다.")
#             random_choice()
#         elif c_arsenal == "시설확충":
#             print("시설확충을 선택하셨습니다. 공격력 +1")
#             Arsenal_attack = Arsenal_fieldown + 1
#             print("다른 팀 1개의 투자를 랜덤으로 살펴보겠습니다.")
#             random_choice()
#         else:
#             print("구단홍보를 선택하셨습니다. 수비력 +1")
#             Arsenal_defence = Arsenal_defence + 1
#             print("다른 팀 1개의 투자를 랜덤으로 살펴보겠습니다.")
#             random_choice()
#     if a == "Y":
#         print("2주가 흘렀습니다.\n---북런던 더비---\n--------------------------------------------\nSUPER Matchweek - Away (Tottenham Hotspur Stadium)\n--------------------------------------------\nArsenal F.C.(HOME) vs Chelsea F.C.(AWAY)\n")
#         print("토트넘 vs 아스날 전력 분석\n토트넘의 vs 아스날의\n공격력은 {} vs {}입니다.\n수비력은 {} vs {}입니다.\n중원 지배력은 {} vs {}입니다.\n".format(Tottenham_attack, Arsenal_attack, Tottenham_defence, Arsenal_defence, Tottenham_fieldown, Arsenal_fieldown))
#         b = input(("포메이션을 선택하세요 : 3-4-3, 4-3-3, 4-2-3-1\n공격 우선 : 3-4-3, 수비 우선 : 4-3-3, 둘 다 : 4-2-3-1\n"))
#         if b == "3-4-3":
#             if (Arsenal_attack > Tottenham_attack and Arsenal_defence >= Tottenham_defence and Arsenal_fieldown >= Tottenham_fieldown) or (Arsenal_attack > Tottenham_attack and Arsenal_defence >= Tottenham_defence and Arsenal_fieldown < Tottenham_fieldown) or (Arsenal_attack == Newcastle_attack and Arsenal_defence >= Newcastle_defence and Arsenal_fieldown >= Newcastle_fieldown):
#                 print("--------------------------------------------\n{} - {}, [북런던 더비 우승] 아스날 승\n--------------------------------------------".format(random.randint(0, 1), random.randint(2, 4)))
#                 아스날_승점 = 아스날_승점 + 3
#             elif (Arsenal_attack > Tottenham_attack and Arsenal_defence < Tottenham_defence and Arsenal_fieldown >= Tottenham_fieldown) or (Arsenal_attack == Tottenham_attack and Arsenal_defence < Tottenham_defence and Arsenal_fieldown >= Tottenham_fieldown) or (Arsenal_attack == Tottenham_attack and Arsenal_defence >= Tottenham_defence and Arsenal_fieldown < Tottenham_fieldown) or (Arsenal_attack < Tottenham_attack and Arsenal_defence >= Tottenham_defence and Arsenal_fieldown >= Tottenham_fieldown):
#                 print("--------------------------------------------\n{} - {}, 무승부\n--------------------------------------------".format(random.randint(2, 2), random.randint(2, 2)))
#                 아스날_승점 = 아스날_승점 + 1
#             elif (Arsenal_attack > Tottenham_attack and Arsenal_defence < Tottenham_defence and Arsenal_fieldown < Tottenham_fieldown) or (Arsenal_attack == Tottenham_attack and Arsenal_defence < Tottenham_defence and Arsenal_fieldown < Tottenham_fieldown) or (Arsenal_attack < Tottenham_attack and Arsenal_defence < Tottenham_defence and Arsenal_fieldown >= Tottenham_fieldown) or (Arsenal_attack < Tottenham_attack and Arsenal_defence >= Tottenham_defence and Arsenal_fieldown < Tottenham_fieldown) or (Arsenal_attack < Tottenham_attack and Arsenal_defence < Tottenham_defence and Arsenal_fieldown < Tottenham_fieldown):
#                 print("--------------------------------------------\n{} - {}, 토트넘 승\n--------------------------------------------".format(random.randint(2, 3), random.randint(0, 1)))
#                 아스날_승점 = 아스날_승점 + 0
#         elif b == "4-3-3":
#             if (Arsenal_defence > Tottenham_defence and Arsenal_attack >= Tottenham_attack and Arsenal_fieldown >= Tottenham_fieldown) or (Arsenal_defence > Tottenham_defence and Arsenal_attack >= Tottenham_attack and Arsenal_fieldown < Tottenham_fieldown) or (Arsenal_defence == Tottenham_defence and Arsenal_attack >= Tottenham_attack and Arsenal_fieldown >= Tottenham_fieldown):
#                 print("--------------------------------------------\n{} - {}, [북런던 더비 우승] 아스날 승\n--------------------------------------------".format(random.randint(0, 1), random.randint(2, 3)))
#                 아스날_승점 = 아스날_승점 + 3
#             elif (Arsenal_defence > Tottenham_defence and Arsenal_attack < Tottenham_attack and Arsenal_fieldown >= Tottenham_fieldown) or (Arsenal_defence == Tottenham_defence and Arsenal_attack < Tottenham_attack and Arsenal_fieldown >= Tottenham_fieldown) or (Arsenal_defence == Tottenham_defence and Arsenal_attack >= Tottenham_attack and Arsenal_fieldown < Tottenham_fieldown) or  (Arsenal_defence < Tottenham_defence and Arsenal_attack >= Tottenham_attack and Arsenal_fieldown >= Tottenham_fieldown):
#                 print("--------------------------------------------\n{} - {}, 무승부\n--------------------------------------------".format(random.randint(2, 2), random.randint(2, 2)))
#                 아스날_승점 = 아스날_승점 + 1
#             elif (Arsenal_defence > Tottenham_defence and Arsenal_attack < Tottenham_attack and Arsenal_fieldown < Tottenham_fieldown) or (Arsenal_defence == Tottenham_defence and Arsenal_attack < Tottenham_attack and Arsenal_fieldown < Tottenham_fieldown) or (Arsenal_defence < Tottenham_defence and Arsenal_attack < Tottenham_attack and Arsenal_fieldown >= Tottenham_fieldown) or (Arsenal_defence < Tottenham_defence and Arsenal_attack >= Tottenham_attack and Arsenal_fieldown < Tottenham_fieldown) or (Arsenal_defence < Tottenham_defence and Arsenal_attack < Tottenham_attack and Arsenal_fieldown < Tottenham_fieldown):
#                 print("--------------------------------------------\n{} - {}, 첼시 승\n--------------------------------------------".format(random.randint(2, 4), random.randint(0, 1)))
#                 아스날_승점 = 아스날_승점 + 0
#         elif b == "4-2-3-1":
#             if (Arsenal_fieldown > Tottenham_fieldown and Arsenal_attack >= Tottenham_attack and Arsenal_defence >= Tottenham_defence) or (Arsenal_fieldown > Tottenham_fieldown and Arsenal_attack >= Tottenham_attack and Arsenal_defence < Tottenham_defence) or (Arsenal_fieldown == Tottenham_fieldown and Arsenal_attack >= Tottenham_attack and Arsenal_defence >= Tottenham_defence):
#                 print("--------------------------------------------\n{} - {}, 아스날 승\n--------------------------------------------".format(random.randint(0, 1), random.randint(2, 3)))
#                 아스날_승점 = 아스날_승점 + 3
#             elif (Arsenal_fieldown > Tottenham_fieldown and Arsenal_attack < Tottenham_attack and Arsenal_defence >= Tottenham_defence) or (Arsenal_fieldown == Tottenham_fieldown and Arsenal_attack < Tottenham_attack and Arsenal_defence >= Tottenham_defence) or (Arsenal_fieldown == Tottenham_fieldown and Arsenal_attack >= Tottenham_attack and Arsenal_defence < Tottenham_defence) or  (Arsenal_fieldown < Tottenham_fieldown and Arsenal_attack >= Tottenham_attack and Arsenal_defence >= Tottenham_defence):
#                 print("--------------------------------------------\n{} - {}, 무승부\n--------------------------------------------".format(random.randint(2, 2), random.randint(2, 2)))
#                 아스날_승점 = 아스날_승점 + 1
#             elif (Arsenal_fieldown > Tottenham_fieldown and Arsenal_attack < Tottenham_attack and Arsenal_defence < Tottenham_defence) or (Arsenal_fieldown == Tottenham_fieldown and Arsenal_attack < Tottenham_attack and Arsenal_defence < Tottenham_defence) or (Arsenal_fieldown < Tottenham_fieldown and Arsenal_attack < Tottenham_attack and Arsenal_defence >= Tottenham_defence) or (Arsenal_fieldown < Tottenham_fieldown and Arsenal_attack >= Tottenham_attack and Arsenal_defence < Tottenham_defence) or  (Arsenal_fieldown < Tottenham_fieldown and Arsenal_attack < Tottenham_attack and Arsenal_defence < Tottenham_defence):
#                 print("--------------------------------------------\n{} - {}, 토트넘 승\n--------------------------------------------".format(random.randint(2, 4), random.randint(0, 1)))
#                 아스날_승점 = 아스날_승점 + 0
#         n = n + 1
#         print("[다섯] 번째 경기를 무사히 끝냈습니다. 당신의 승점은 {}점 입니다".format(아스날_승점))
#         print("{}주차 프리미어리그 순위".format(n))
#         아스날_승점 = 아스날_승점
#         맨시티_승점 = random.randint(0,3) + 맨시티_승점
#         리버풀_승점 = random.randint(0,3) + 리버풀_승점
#         맨유_승점 = random.randint(0,3) + 맨유_승점
#         토트넘_승점 = random.randint(0,3) + 토트넘_승점
#         첼시_승점 = random.randint(0,3) + 첼시_승점
#         울버햄튼_승점 = random.randint(0,3) + 울버햄튼_승점
#         웨스트햄_승점 = random.randint(0,3) + 웨스트햄_승점
#         뉴캐슬_승점 = random.randint(0,3) + 뉴캐슬_승점
#         팀_승점 = {
#         "아스날 FC": 아스날_승점,
#         "맨체스터 시티 FC": 맨시티_승점,
#         "맨체스터 유나이티드 FC" : 맨유_승점,
#         "리버풀 FC" : 리버풀_승점,
#         "토트넘 홋스퍼 FC" : 토트넘_승점,
#         "첼시 FC" : 첼시_승점,
#         "울버햄튼 원더러스 FC" : 울버햄튼_승점,
#         "웨스트햄 유나이티드 FC" : 웨스트햄_승점,
#         "뉴캐슬 FC" : 뉴캐슬_승점          
#         }
#         sorted_scoreboard = sorted(팀_승점.items(), key=lambda x: x[1], reverse=True)
#         print("\nEngland Premier League\n")
#         for 순위, (팀, 승점) in enumerate((sorted_scoreboard), start=1):
#             print(f"{순위}위 : {팀} - {승점}점")
#     a = str(input("다음 단계로 넘어가려면 Y를 입력해주세요.\n"))
#     if a == "Y":
#         print("Pre-Matchweek\n투자할 부분을 선택하세요 : 트레이닝, 시설확충, 구단홍보")
#         c_arsenal = input("선택 : ")
#         if c_arsenal == "트레이닝":
#             print("트레이닝을 선택하셨습니다. 중원 지배 능력치 +1")
#             Arsenal_fieldown = Arsenal_fieldown + 1
#             print("다른 팀 1개의 투자를 랜덤으로 살펴보겠습니다.")
#             random_choice()
#         elif c_arsenal == "시설확충":
#             print("시설확충을 선택하셨습니다. 공격력 +1")
#             Arsenal_attack = Arsenal_fieldown + 1
#             print("다른 팀 1개의 투자를 랜덤으로 살펴보겠습니다.")
#             random_choice()
#         else:
#             print("구단홍보를 선택하셨습니다. 수비력 +1")
#             Arsenal_defence = Arsenal_defence + 1
#             print("다른 팀 1개의 투자를 랜덤으로 살펴보겠습니다.")
#             random_choice()
#     if a == "Y":
#         print("\n=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n경고! HELL-WEEK 지옥의 릴레이가 시작되었습니다. 이제부터 당신은 PL 최강의 팀이라고 일컬어지는 맨유, 리버풀, 맨시티와 연속 경기를 치르게 됩니다.\n=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n")
#         print("2주가 흘렀습니다.\n--------------------------------------------\nHELLweek 1 - Away (Old Trafford)\n--------------------------------------------\nArsenal F.C.(HOME) vs Chelsea F.C.(AWAY)\n")
#         print("아스날 vs 맨 유 전력 분석\n아스날의 vs 맨유의\n공격력은 {} vs {}입니다.\n수비력은 {} vs {}입니다.\n중원 지배력은 {} vs {}입니다.\n".format(Arsenal_attack, Man_Utd_attack, Arsenal_defence, Man_Utd_defence, Arsenal_fieldown, Man_Utd_fieldown))
#         b = input(("포메이션을 선택하세요 : 3-4-3, 4-3-3, 4-2-3-1\n공격 우선 : 3-4-3, 수비 우선 : 4-3-3, 둘 다 : 4-2-3-1\n"))
#         if b == "3-4-3":
#             if (Arsenal_attack > Man_Utd_attack and Arsenal_defence >= Man_Utd_defence and Arsenal_fieldown >= Man_Utd_fieldown) or (Arsenal_attack > Man_Utd_attack and Arsenal_defence >= Man_Utd_defence and Arsenal_fieldown < Man_Utd_fieldown) or (Arsenal_attack == Newcastle_attack and Arsenal_defence >= Newcastle_defence and Arsenal_fieldown >= Newcastle_fieldown):
#                 print("--------------------------------------------\n{} - {}, 아스날 승\n--------------------------------------------".format(random.randint(0, 1), random.randint(2, 4)))
#                 아스날_승점 = 아스날_승점 + 3
#             elif (Arsenal_attack > Man_Utd_attack and Arsenal_defence < Man_Utd_defence and Arsenal_fieldown >= Man_Utd_fieldown) or (Arsenal_attack == Man_Utd_attack and Arsenal_defence < Man_Utd_defence and Arsenal_fieldown >= Man_Utd_fieldown) or (Arsenal_attack == Man_Utd_attack and Arsenal_defence >= Man_Utd_defence and Arsenal_fieldown < Man_Utd_fieldown) or (Arsenal_attack < Man_Utd_attack and Arsenal_defence >= Man_Utd_defence and Arsenal_fieldown >= Man_Utd_fieldown):
#                 print("--------------------------------------------\n{} - {}, 무승부\n--------------------------------------------".format(random.randint(2, 2), random.randint(2, 2)))
#                 아스날_승점 = 아스날_승점 + 1
#             elif (Arsenal_attack > Man_Utd_attack and Arsenal_defence < Man_Utd_defence and Arsenal_fieldown < Man_Utd_fieldown) or (Arsenal_attack == Man_Utd_attack and Arsenal_defence < Man_Utd_defence and Arsenal_fieldown < Man_Utd_fieldown) or (Arsenal_attack < Man_Utd_attack and Arsenal_defence < Man_Utd_defence and Arsenal_fieldown >= Man_Utd_fieldown) or (Arsenal_attack < Man_Utd_attack and Arsenal_defence >= Man_Utd_defence and Arsenal_fieldown < Man_Utd_fieldown) or (Arsenal_attack < Man_Utd_attack and Arsenal_defence < Man_Utd_defence and Arsenal_fieldown < Man_Utd_fieldown):
#                 print("--------------------------------------------\n{} - {}, 맨체스터 유나이티드 승\n--------------------------------------------".format(random.randint(2, 3), random.randint(0, 1)))
#                 아스날_승점 = 아스날_승점 + 0
#         elif b == "4-3-3":
#             if (Arsenal_defence > Man_Utd_defence and Arsenal_attack >= Man_Utd_attack and Arsenal_fieldown >= Man_Utd_fieldown) or (Arsenal_defence > Man_Utd_defence and Arsenal_attack >= Man_Utd_attack and Arsenal_fieldown < Man_Utd_fieldown) or (Arsenal_defence == Man_Utd_defence and Arsenal_attack >= Man_Utd_attack and Arsenal_fieldown >= Man_Utd_fieldown):
#                 print("--------------------------------------------\n{} - {}, 아스날 승\n--------------------------------------------".format(random.randint(0, 1), random.randint(2, 3)))
#                 아스날_승점 = 아스날_승점 + 3
#             elif (Arsenal_defence > Man_Utd_defence and Arsenal_attack < Man_Utd_attack and Arsenal_fieldown >= Man_Utd_fieldown) or (Arsenal_defence == Man_Utd_defence and Arsenal_attack < Man_Utd_attack and Arsenal_fieldown >= Man_Utd_fieldown) or (Arsenal_defence == Man_Utd_defence and Arsenal_attack >= Man_Utd_attack and Arsenal_fieldown < Man_Utd_fieldown) or  (Arsenal_defence < Man_Utd_defence and Arsenal_attack >= Man_Utd_attack and Arsenal_fieldown >= Man_Utd_fieldown):
#                 print("--------------------------------------------\n{} - {}, 무승부\n--------------------------------------------".format(random.randint(2, 2), random.randint(2, 2)))
#                 아스날_승점 = 아스날_승점 + 1
#             elif (Arsenal_defence > Man_Utd_defence and Arsenal_attack < Man_Utd_attack and Arsenal_fieldown < Man_Utd_fieldown) or (Arsenal_defence == Man_Utd_defence and Arsenal_attack < Man_Utd_attack and Arsenal_fieldown < Man_Utd_fieldown) or (Arsenal_defence < Man_Utd_defence and Arsenal_attack < Man_Utd_attack and Arsenal_fieldown >= Man_Utd_fieldown) or (Arsenal_defence < Man_Utd_defence and Arsenal_attack >= Man_Utd_attack and Arsenal_fieldown < Man_Utd_fieldown) or (Arsenal_defence < Man_Utd_defence and Arsenal_attack < Man_Utd_attack and Arsenal_fieldown < Man_Utd_fieldown):
#                 print("--------------------------------------------\n{} - {}, 맨체스터 유나이티드 승\n--------------------------------------------".format(random.randint(2, 4), random.randint(0, 1)))
#                 아스날_승점 = 아스날_승점 + 0
#         elif b == "4-2-3-1":
#             if (Arsenal_fieldown > Man_Utd_fieldown and Arsenal_attack >= Man_Utd_attack and Arsenal_defence >= Man_Utd_defence) or (Arsenal_fieldown > Man_Utd_fieldown and Arsenal_attack >= Man_Utd_attack and Arsenal_defence < Man_Utd_defence) or (Arsenal_fieldown == Man_Utd_fieldown and Arsenal_attack >= Man_Utd_attack and Arsenal_defence >= Man_Utd_defence):
#                 print("--------------------------------------------\n{} - {}, 아스날 승\n--------------------------------------------".format(random.randint(0, 1), random.randint(2, 3)))
#                 아스날_승점 = 아스날_승점 + 3
#             elif (Arsenal_fieldown > Man_Utd_fieldown and Arsenal_attack < Man_Utd_attack and Arsenal_defence >= Man_Utd_defence) or (Arsenal_fieldown == Man_Utd_fieldown and Arsenal_attack < Man_Utd_attack and Arsenal_defence >= Man_Utd_defence) or (Arsenal_fieldown == Man_Utd_fieldown and Arsenal_attack >= Man_Utd_attack and Arsenal_defence < Man_Utd_defence) or  (Arsenal_fieldown < Man_Utd_fieldown and Arsenal_attack >= Man_Utd_attack and Arsenal_defence >= Man_Utd_defence):
#                 print("--------------------------------------------\n{} - {}, 무승부\n--------------------------------------------".format(random.randint(2, 2), random.randint(2, 2)))
#                 아스날_승점 = 아스날_승점 + 1
#             elif (Arsenal_fieldown > Man_Utd_fieldown and Arsenal_attack < Man_Utd_attack and Arsenal_defence < Man_Utd_defence) or (Arsenal_fieldown == Man_Utd_fieldown and Arsenal_attack < Man_Utd_attack and Arsenal_defence < Man_Utd_defence) or (Arsenal_fieldown < Man_Utd_fieldown and Arsenal_attack < Man_Utd_attack and Arsenal_defence >= Man_Utd_defence) or (Arsenal_fieldown < Man_Utd_fieldown and Arsenal_attack >= Man_Utd_attack and Arsenal_defence < Man_Utd_defence) or  (Arsenal_fieldown < Man_Utd_fieldown and Arsenal_attack < Man_Utd_attack and Arsenal_defence < Man_Utd_defence):
#                 print("--------------------------------------------\n{} - {}, 토트넘 승\n--------------------------------------------".format(random.randint(2, 4), random.randint(0, 1)))
#                 아스날_승점 = 아스날_승점 + 0
#         n = n + 1
#         print("[다섯] 번째 경기를 무사히 끝냈습니다. 당신의 승점은 {}점 입니다".format(아스날_승점))
#         print("{}주차 프리미어리그 순위".format(n))
#         아스날_승점 = 아스날_승점
#         맨시티_승점 = random.randint(0,3) + 맨시티_승점
#         리버풀_승점 = random.randint(0,3) + 리버풀_승점
#         맨유_승점 = random.randint(0,3) + 맨유_승점
#         토트넘_승점 = random.randint(0,3) + 토트넘_승점
#         첼시_승점 = random.randint(0,3) + 첼시_승점
#         울버햄튼_승점 = random.randint(0,3) + 울버햄튼_승점
#         웨스트햄_승점 = random.randint(0,3) + 웨스트햄_승점
#         뉴캐슬_승점 = random.randint(0,3) + 뉴캐슬_승점
#         팀_승점 = {
#         "아스날 FC": 아스날_승점,
#         "맨체스터 시티 FC": 맨시티_승점,
#         "맨체스터 유나이티드 FC" : 맨유_승점,
#         "리버풀 FC" : 리버풀_승점,
#         "토트넘 홋스퍼 FC" : 토트넘_승점,
#         "첼시 FC" : 첼시_승점,
#         "울버햄튼 원더러스 FC" : 울버햄튼_승점,
#         "웨스트햄 유나이티드 FC" : 웨스트햄_승점,
#         "뉴캐슬 FC" : 뉴캐슬_승점          
#         }
#         sorted_scoreboard = sorted(팀_승점.items(), key=lambda x: x[1], reverse=True)
#         print("\nEngland Premier League\n")
#         for 순위, (팀, 승점) in enumerate((sorted_scoreboard), start=1):
#             print(f"{순위}위 : {팀} - {승점}점")
#     a = str(input("다음 단계로 넘어가려면 Y를 입력해주세요.\n"))
#     if a == "Y":
#         print("Pre-Matchweek\n투자할 부분을 선택하세요 : 트레이닝, 시설확충, 구단홍보")
#         c_arsenal = input("선택 : ")
#         if c_arsenal == "트레이닝":
#             print("트레이닝을 선택하셨습니다. 중원 지배 능력치 +1")
#             Arsenal_fieldown = Arsenal_fieldown + 1
#             print("다른 팀 1개의 투자를 랜덤으로 살펴보겠습니다.")
#             random_choice()
#         elif c_arsenal == "시설확충":
#             print("시설확충을 선택하셨습니다. BONUS + 공격력 +2")
#             Arsenal_attack = Arsenal_fieldown + 1
#             print("다른 팀 1개의 투자를 랜덤으로 살펴보겠습니다.")
#             random_choice()
#         else:
#             print("구단홍보를 선택하셨습니다. 수비력 +1")
#             Arsenal_defence = Arsenal_defence + 1
#             print("다른 팀 1개의 투자를 랜덤으로 살펴보겠습니다.")
#             random_choice()
#     if a == "Y":
#         print("\n=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n경고! HELL-WEEK 지옥의 릴레이가 [실행 중]입니다. 이제부터 당신은 PL 최강의 팀이라고 일컬어지는 리버풀, 맨시티와 연속 경기를 치르게 됩니다.\n=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n")
#         print("2주가 흘렀습니다.\n--------------------------------------------\nHELLweek 1 - Home (Emirates Stadium)\n--------------------------------------------\nArsenal F.C.(HOME) vs Liverpool F.C.(AWAY)\n")
#         print("아스날 vs 리버풀 전력 분석\n아스날의 vs 맨유의\n공격력은 {} vs {}입니다.\n수비력은 {} vs {}입니다.\n중원 지배력은 {} vs {}입니다.\n".format(Arsenal_attack, Liverpool_attack, Arsenal_defence, Liverpool_defence, Arsenal_fieldown, Liverpool_fieldown))
#         b = input(("포메이션을 선택하세요 : 3-4-3, 4-3-3, 4-2-3-1\n공격 우선 : 3-4-3, 수비 우선 : 4-3-3, 둘 다 : 4-2-3-1\n"))
#         if b == "3-4-3":
#             if (Arsenal_attack > Liverpool_attack and Arsenal_defence >= Liverpool_defence and Arsenal_fieldown >= Liverpool_fieldown) or (Arsenal_attack > Liverpool_attack and Arsenal_defence >= Liverpool_defence and Arsenal_fieldown < Liverpool_fieldown) or (Arsenal_attack == Liverpool_attack and Arsenal_defence >= Liverpool_defence and Arsenal_fieldown >= Liverpool_fieldown):
#                 print("--------------------------------------------\n{} - {}, 아스날 승\n--------------------------------------------".format(random.randint(0, 1), random.randint(2, 4)))
#                 아스날_승점 = 아스날_승점 + 3
#             elif (Arsenal_attack > Liverpool_attack and Arsenal_defence < Liverpool_defence and Arsenal_fieldown >= Liverpool_fieldown) or (Arsenal_attack == Liverpool_attack and Arsenal_defence < Liverpool_defence and Arsenal_fieldown >= Liverpool_fieldown) or (Arsenal_attack == Liverpool_attack and Arsenal_defence >= Liverpool_defence and Arsenal_fieldown < Liverpool_fieldown) or (Arsenal_attack < Liverpool_attack and Arsenal_defence >= Liverpool_defence and Arsenal_fieldown >= Liverpool_fieldown):
#                 print("--------------------------------------------\n{} - {}, 무승부\n--------------------------------------------".format(random.randint(2, 2), random.randint(2, 2)))
#                 아스날_승점 = 아스날_승점 + 1
#             elif (Arsenal_attack > Liverpool_attack and Arsenal_defence < Liverpool_defence and Arsenal_fieldown < Liverpool_fieldown) or (Arsenal_attack == Liverpool_attack and Arsenal_defence < Liverpool_defence and Arsenal_fieldown < Liverpool_fieldown) or (Arsenal_attack < Liverpool_attack and Arsenal_defence < Liverpool_defence and Arsenal_fieldown >= Liverpool_fieldown) or (Arsenal_attack < Liverpool_attack and Arsenal_defence >= Liverpool_defence and Arsenal_fieldown < Liverpool_fieldown) or (Arsenal_attack < Liverpool_attack and Arsenal_defence < Liverpool_defence and Arsenal_fieldown < Liverpool_fieldown):
#                 print("--------------------------------------------\n{} - {}, 리버풀 승\n--------------------------------------------".format(random.randint(2, 3), random.randint(0, 1)))
#                 아스날_승점 = 아스날_승점 + 0
#         elif b == "4-3-3":
#             if (Arsenal_defence > Liverpool_defence and Arsenal_attack >= Liverpool_attack and Arsenal_fieldown >= Liverpool_fieldown) or (Arsenal_defence > Liverpool_defence and Arsenal_attack >= Liverpool_attack and Arsenal_fieldown < Liverpool_fieldown) or (Arsenal_defence == Liverpool_defence and Arsenal_attack >= Liverpool_attack and Arsenal_fieldown >= Liverpool_fieldown):
#                 print("--------------------------------------------\n{} - {}, 아스날 승\n--------------------------------------------".format(random.randint(0, 1), random.randint(2, 3)))
#                 아스날_승점 = 아스날_승점 + 3
#             elif (Arsenal_defence > Liverpool_defence and Arsenal_attack < Liverpool_attack and Arsenal_fieldown >= Liverpool_fieldown) or (Arsenal_defence == Liverpool_defence and Arsenal_attack < Liverpool_attack and Arsenal_fieldown >= Liverpool_fieldown) or (Arsenal_defence == Liverpool_defence and Arsenal_attack >= Liverpool_attack and Arsenal_fieldown < Liverpool_fieldown) or  (Arsenal_defence < Liverpool_defence and Arsenal_attack >= Liverpool_attack and Arsenal_fieldown >= Liverpool_fieldown):
#                 print("--------------------------------------------\n{} - {}, 무승부\n--------------------------------------------".format(random.randint(2, 2), random.randint(2, 2)))
#                 아스날_승점 = 아스날_승점 + 1
#             elif (Arsenal_defence > Liverpool_defence and Arsenal_attack < Liverpool_attack and Arsenal_fieldown < Liverpool_fieldown) or (Arsenal_defence == Liverpool_defence and Arsenal_attack < Liverpool_attack and Arsenal_fieldown < Liverpool_fieldown) or (Arsenal_defence < Liverpool_defence and Arsenal_attack < Liverpool_attack and Arsenal_fieldown >= Liverpool_fieldown) or (Arsenal_defence < Liverpool_defence and Arsenal_attack >= Liverpool_attack and Arsenal_fieldown < Liverpool_fieldown) or (Arsenal_defence < Liverpool_defence and Arsenal_attack < Liverpool_attack and Arsenal_fieldown < Liverpool_fieldown):
#                 print("--------------------------------------------\n{} - {}, 리버풀 승\n--------------------------------------------".format(random.randint(2, 4), random.randint(0, 1)))
#                 아스날_승점 = 아스날_승점 + 0
#         elif b == "4-2-3-1":
#             if (Arsenal_fieldown > Liverpool_fieldown and Arsenal_attack >= Liverpool_attack and Arsenal_defence >= Liverpool_defence) or (Arsenal_fieldown > Liverpool_fieldown and Arsenal_attack >= Liverpool_attack and Arsenal_defence < Liverpool_defence) or (Arsenal_fieldown == Liverpool_fieldown and Arsenal_attack >= Liverpool_attack and Arsenal_defence >= Liverpool_defence):
#                 print("--------------------------------------------\n{} - {}, 아스날 승\n--------------------------------------------".format(random.randint(0, 1), random.randint(2, 3)))
#                 아스날_승점 = 아스날_승점 + 3
#             elif (Arsenal_fieldown > Liverpool_fieldown and Arsenal_attack < Liverpool_attack and Arsenal_defence >= Liverpool_defence) or (Arsenal_fieldown == Liverpool_fieldown and Arsenal_attack < Liverpool_attack and Arsenal_defence >= Liverpool_defence) or (Arsenal_fieldown == Liverpool_fieldown and Arsenal_attack >= Liverpool_attack and Arsenal_defence < Liverpool_defence) or  (Arsenal_fieldown < Liverpool_fieldown and Arsenal_attack >= Liverpool_attack and Arsenal_defence >= Liverpool_defence):
#                 print("--------------------------------------------\n{} - {}, 무승부\n--------------------------------------------".format(random.randint(2, 2), random.randint(2, 2)))
#                 아스날_승점 = 아스날_승점 + 1
#             elif (Arsenal_fieldown > Liverpool_fieldown and Arsenal_attack < Liverpool_attack and Arsenal_defence < Liverpool_defence) or (Arsenal_fieldown == Liverpool_fieldown and Arsenal_attack < Liverpool_attack and Arsenal_defence < Liverpool_defence) or (Arsenal_fieldown < Liverpool_fieldown and Arsenal_attack < Liverpool_attack and Arsenal_defence >= Liverpool_defence) or (Arsenal_fieldown < Liverpool_fieldown and Arsenal_attack >= Liverpool_attack and Arsenal_defence < Liverpool_defence) or  (Arsenal_fieldown < Liverpool_fieldown and Arsenal_attack < Liverpool_attack and Arsenal_defence < Liverpool_defence):
#                 print("--------------------------------------------\n{} - {}, 리버풀 승\n--------------------------------------------".format(random.randint(2, 4), random.randint(0, 1)))
#                 아스날_승점 = 아스날_승점 + 0
#         n = n + 1
#         print("[다섯] 번째 경기를 무사히 끝냈습니다. 당신의 승점은 {}점 입니다".format(아스날_승점))
#         print("{}주차 프리미어리그 순위".format(n))
#         아스날_승점 = 아스날_승점
#         맨시티_승점 = random.randint(0,3) + 맨시티_승점
#         리버풀_승점 = random.randint(0,3) + 리버풀_승점
#         맨유_승점 = random.randint(0,3) + 맨유_승점
#         토트넘_승점 = random.randint(0,3) + 토트넘_승점
#         첼시_승점 = random.randint(0,3) + 첼시_승점
#         울버햄튼_승점 = random.randint(0,3) + 울버햄튼_승점
#         웨스트햄_승점 = random.randint(0,3) + 웨스트햄_승점
#         뉴캐슬_승점 = random.randint(0,3) + 뉴캐슬_승점
#         팀_승점 = {
#         "아스날 FC": 아스날_승점,
#         "맨체스터 시티 FC": 맨시티_승점,
#         "맨체스터 유나이티드 FC" : 맨유_승점,
#         "리버풀 FC" : 리버풀_승점,
#         "토트넘 홋스퍼 FC" : 토트넘_승점,
#         "첼시 FC" : 첼시_승점,
#         "울버햄튼 원더러스 FC" : 울버햄튼_승점,
#         "웨스트햄 유나이티드 FC" : 웨스트햄_승점,
#         "뉴캐슬 FC" : 뉴캐슬_승점          
#         }
#         sorted_scoreboard = sorted(팀_승점.items(), key=lambda x: x[1], reverse=True)
#         print("\nEngland Premier League\n")
#         for 순위, (팀, 승점) in enumerate((sorted_scoreboard), start=1):
#             print(f"{순위}위 : {팀} - {승점}점")
#     a = str(input("다음 단계로 넘어가려면 Y를 입력해주세요.\n"))
#     if a == "Y":
#         print("Pre-Matchweek\n투자할 부분을 선택하세요 : 트레이닝, 시설확충, 구단홍보")
#         c_arsenal = input("선택 : ")
#         if c_arsenal == "트레이닝":
#             print("트레이닝을 선택하셨습니다. 중원 지배 능력치 +1")
#             Arsenal_fieldown = Arsenal_fieldown + 1
#             print("다른 팀 1개의 투자를 랜덤으로 살펴보겠습니다.")
#             random_choice()
#         elif c_arsenal == "시설확충":
#             print("시설확충을 선택하셨습니다. BONUS + 공격력 +2")
#             Arsenal_attack = Arsenal_fieldown + 1
#             print("다른 팀 1개의 투자를 랜덤으로 살펴보겠습니다.")
#             random_choice()
#         else:
#             print("구단홍보를 선택하셨습니다. 수비력 +1")
#             Arsenal_defence = Arsenal_defence + 1
#             print("다른 팀 1개의 투자를 랜덤으로 살펴보겠습니다.")
#             random_choice()
#     if a == "Y":
#         print("\n=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\nLast-Week 지옥의 릴레이가 [마지막]입니다. 이제부터 당신은 PL 최다 우승 팀, 최강의 공격진을 자랑하는 맨시티와 경기를 치르게 됩니다.\n=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+\n")
#         print("2주가 흘렀습니다.\n--------------------------------------------\nLast week - Away (Etihad Stadium)\n--------------------------------------------\nManchester City F.C.(HOME) vs Arsenal F.C.(AWAY)\n")
#         print("맨시티 vs 아스날 전력 분석\n맨시티의 vs 아스날의\n공격력은 {} vs {}입니다.\n수비력은 {} vs {}입니다.\n중원 지배력은 {} vs {}입니다.\n".format(Man_City_attack, Arsenal_attack, Man_City_defence, Arsenal_defence, Man_City_fieldown, Arsenal_fieldown))
#         b = input(("포메이션을 선택하세요 : 3-4-3, 4-3-3, 4-2-3-1\n공격 우선 : 3-4-3, 수비 우선 : 4-3-3, 둘 다 : 4-2-3-1\n"))
#         if b == "3-4-3":
#             if (Arsenal_attack > Man_City_attack and Arsenal_defence >= Man_City_defence and Arsenal_fieldown >= Man_City_fieldown) or (Arsenal_attack > Man_City_attack and Arsenal_defence >= Man_City_defence and Arsenal_fieldown < Man_City_fieldown) or (Arsenal_attack == Man_City_attack and Arsenal_defence >= Man_City_defence and Arsenal_fieldown >= Man_City_fieldown):
#                 print("--------------------------------------------\n{} - {}, 아스날 승\n--------------------------------------------".format(random.randint(0, 1), random.randint(2, 4)))
#                 아스날_승점 = 아스날_승점 + 3
#             elif (Arsenal_attack > Man_City_attack and Arsenal_defence < Man_City_defence and Arsenal_fieldown >= Man_City_fieldown) or (Arsenal_attack == Man_City_attack and Arsenal_defence < Man_City_defence and Arsenal_fieldown >= Man_City_fieldown) or (Arsenal_attack == Man_City_attack and Arsenal_defence >= Man_City_defence and Arsenal_fieldown < Man_City_fieldown) or (Arsenal_attack < Man_City_attack and Arsenal_defence >= Man_City_defence and Arsenal_fieldown >= Man_City_fieldown):
#                 print("--------------------------------------------\n{} - {}, 무승부\n--------------------------------------------".format(random.randint(2, 2), random.randint(2, 2)))
#                 아스날_승점 = 아스날_승점 + 1
#             elif (Arsenal_attack > Man_City_attack and Arsenal_defence < Man_City_defence and Arsenal_fieldown < Man_City_fieldown) or (Arsenal_attack == Man_City_attack and Arsenal_defence < Man_City_defence and Arsenal_fieldown < Man_City_fieldown) or (Arsenal_attack < Man_City_attack and Arsenal_defence < Man_City_defence and Arsenal_fieldown >= Man_City_fieldown) or (Arsenal_attack < Man_City_attack and Arsenal_defence >= Man_City_defence and Arsenal_fieldown < Man_City_fieldown) or (Arsenal_attack < Man_City_attack and Arsenal_defence < Man_City_defence and Arsenal_fieldown < Man_City_fieldown):
#                 print("--------------------------------------------\n{} - {}, 맨체스터 시티 승\n--------------------------------------------".format(random.randint(2, 3), random.randint(0, 1)))
#                 아스날_승점 = 아스날_승점 + 0
#         elif b == "4-3-3":
#             if (Arsenal_defence > Man_City_defence and Arsenal_attack >= Man_City_attack and Arsenal_fieldown >= Man_City_fieldown) or (Arsenal_defence > Man_City_defence and Arsenal_attack >= Man_City_attack and Arsenal_fieldown < Man_City_fieldown) or (Arsenal_defence == Man_City_defence and Arsenal_attack >= Man_City_attack and Arsenal_fieldown >= Man_City_fieldown):
#                 print("--------------------------------------------\n{} - {}, 아스날 승\n--------------------------------------------".format(random.randint(0, 1), random.randint(2, 3)))
#                 아스날_승점 = 아스날_승점 + 3
#             elif (Arsenal_defence > Man_City_defence and Arsenal_attack < Man_City_attack and Arsenal_fieldown >= Man_City_fieldown) or (Arsenal_defence == Man_City_defence and Arsenal_attack < Man_City_attack and Arsenal_fieldown >= Man_City_fieldown) or (Arsenal_defence == Man_City_defence and Arsenal_attack >= Man_City_attack and Arsenal_fieldown < Man_City_fieldown) or  (Arsenal_defence < Man_City_defence and Arsenal_attack >= Man_City_attack and Arsenal_fieldown >= Man_City_fieldown):
#                 print("--------------------------------------------\n{} - {}, 무승부\n--------------------------------------------".format(random.randint(2, 2), random.randint(2, 2)))
#                 아스날_승점 = 아스날_승점 + 1
#             elif (Arsenal_defence > Man_City_defence and Arsenal_attack < Man_City_attack and Arsenal_fieldown < Man_City_fieldown) or (Arsenal_defence == Man_City_defence and Arsenal_attack < Man_City_attack and Arsenal_fieldown < Man_City_fieldown) or (Arsenal_defence < Man_City_defence and Arsenal_attack < Man_City_attack and Arsenal_fieldown >= Man_City_fieldown) or (Arsenal_defence < Man_City_defence and Arsenal_attack >= Man_City_attack and Arsenal_fieldown < Man_City_fieldown) or (Arsenal_defence < Man_City_defence and Arsenal_attack < Man_City_attack and Arsenal_fieldown < Man_City_fieldown):
#                 print("--------------------------------------------\n{} - {}, 맨체스터 시티 승\n--------------------------------------------".format(random.randint(2, 4), random.randint(0, 1)))
#                 아스날_승점 = 아스날_승점 + 0
#         elif b == "4-2-3-1":
#             if (Arsenal_fieldown > Man_City_fieldown and Arsenal_attack >= Man_City_attack and Arsenal_defence >= Man_City_defence) or (Arsenal_fieldown > Man_City_fieldown and Arsenal_attack >= Man_City_attack and Arsenal_defence < Man_City_defence) or (Arsenal_fieldown == Man_City_fieldown and Arsenal_attack >= Man_City_attack and Arsenal_defence >= Man_City_defence):
#                 print("--------------------------------------------\n{} - {}, 아스날 승\n--------------------------------------------".format(random.randint(0, 1), random.randint(2, 3)))
#                 아스날_승점 = 아스날_승점 + 3
#             elif (Arsenal_fieldown > Man_City_fieldown and Arsenal_attack < Man_City_attack and Arsenal_defence >= Man_City_defence) or (Arsenal_fieldown == Man_City_fieldown and Arsenal_attack < Man_City_attack and Arsenal_defence >= Man_City_defence) or (Arsenal_fieldown == Man_City_fieldown and Arsenal_attack >= Man_City_attack and Arsenal_defence < Man_City_defence) or  (Arsenal_fieldown < Man_City_fieldown and Arsenal_attack >= Man_City_attack and Arsenal_defence >= Man_City_defence):
#                 print("--------------------------------------------\n{} - {}, 무승부\n--------------------------------------------".format(random.randint(2, 2), random.randint(2, 2)))
#                 아스날_승점 = 아스날_승점 + 1
#             elif (Arsenal_fieldown > Man_City_fieldown and Arsenal_attack < Man_City_attack and Arsenal_defence < Man_City_defence) or (Arsenal_fieldown == Man_City_fieldown and Arsenal_attack < Man_City_attack and Arsenal_defence < Man_City_defence) or (Arsenal_fieldown < Man_City_fieldown and Arsenal_attack < Man_City_attack and Arsenal_defence >= Man_City_defence) or (Arsenal_fieldown < Man_City_fieldown and Arsenal_attack >= Man_City_attack and Arsenal_defence < Man_City_defence) or  (Arsenal_fieldown < Man_City_fieldown and Arsenal_attack < Man_City_attack and Arsenal_defence < Man_City_defence):
#                 print("--------------------------------------------\n{} - {}, 리버풀 승\n--------------------------------------------".format(random.randint(2, 4), random.randint(0, 1)))
#                 아스날_승점 = 아스날_승점 + 0
#         n = n + 1
#         print("[다섯] 번째 경기를 무사히 끝냈습니다. 당신의 승점은 {}점 입니다".format(아스날_승점))
#         print("{}주차 프리미어리그 순위".format(n))
#         아스날_승점 = 아스날_승점
#         맨시티_승점 = random.randint(0,3) + 맨시티_승점
#         리버풀_승점 = random.randint(0,3) + 리버풀_승점
#         맨유_승점 = random.randint(0,3) + 맨유_승점
#         토트넘_승점 = random.randint(0,3) + 토트넘_승점
#         첼시_승점 = random.randint(0,3) + 첼시_승점
#         울버햄튼_승점 = random.randint(0,3) + 울버햄튼_승점
#         웨스트햄_승점 = random.randint(0,3) + 웨스트햄_승점
#         뉴캐슬_승점 = random.randint(0,3) + 뉴캐슬_승점
#         팀_승점 = {
#         "아스날 FC": 아스날_승점,
#         "맨체스터 시티 FC": 맨시티_승점,
#         "맨체스터 유나이티드 FC" : 맨유_승점,
#         "리버풀 FC" : 리버풀_승점,
#         "토트넘 홋스퍼 FC" : 토트넘_승점,
#         "첼시 FC" : 첼시_승점,
#         "울버햄튼 원더러스 FC" : 울버햄튼_승점,
#         "웨스트햄 유나이티드 FC" : 웨스트햄_승점,
#         "뉴캐슬 FC" : 뉴캐슬_승점          
#         }
#         sorted_scoreboard = sorted(팀_승점.items(), key=lambda x: x[1], reverse=True)
#         print("\nEngland Premier League\n")
#         for 순위, (팀, 승점) in enumerate((sorted_scoreboard), start=1):
#             print(f"{순위}위 : {팀} - {승점}점")
#     a = str(input("다음 단계로 넘어가려면 Y를 입력해주세요.\n"))
#     if 아스날_승점 > 12:
#         print("------------------------------------------------------------------")
#         print("축하합니다. 당신의 팀은 2024-25 시즌 UEFA 챔피언스 리그에 진출했습니다.")
#         print("Congrats. Ur team finally get the tickets to Champs.")
#         print("...........      ...........               .................................               ...................................                        .\n...........      ...........               .................................               ...................................                       ....\n...........      ...........               ...........                            ..........                                    ..   ..\n...........      ...........               .................................               ...................................                    ................\n...........      ...........               .................................               ....................................                  .....................\n...........      ...........               ...........                            ..........                               ....            ....\n.................................               .................................               ..........                             ....                 ....\n.................................               ................................               ..........                           ....                     ....\n")
#     else:
#         print("------------------------------------------------------------------")
#         print("수고했습니다. 당신의 팀은 비록 UEFA 챔피언스 리그에 진출하지 못했더라도 프리미어리그의 전설로 남을 것입니다.")


# if commandteam == Arsenal:
#     introduce_powerbalance(Arsenal, Arsenal_attack, Arsenal_defence, Arsenal_fieldown)
#     print("\n아스날은 프리미어리그 전통의 강팀으로, 공격, 수비, 중원 모두 우수한 활약을 보입니다.")
#     Arsenal_Run()
# elif commandteam == Man_City:
#     introduce_powerbalance(Man_City, Man_City_attack, Man_City_defence, Man_City_fieldown)
#     print("\n맨체스터 시티는 세계 최강의 공격진을 필두로 한 강팀으로, 매 경기마다 화끈한 득점력을 선보입니다.")
# elif commandteam == Man_Utd:
#     introduce_powerbalance(Man_Utd, Man_Utd_attack, Man_Utd_defence, Man_Utd_fieldown)
#     print("\n호날두, 루니, 박지성, 베컴 등의 세계적인 스타 선수들이 거쳐간 맨체스터 유나이티드는 전 세계적인 팬덤을 보유한 클럽입니다.")
# elif commandteam == Liverpool:
#     introduce_powerbalance(Liverpool, Liverpool_attack, Liverpool_defence, Liverpool_fieldown)
#     print("\n오랜 침체기를 끝내고 리그 상위권으로 도약한 리버풀은 공격과 수비에서 특히 우수한 클럽입니다.")
# elif commandteam == Tottenham:
#     introduce_powerbalance(Tottenham, Tottenham_attack, Tottenham_defence, Tottenham_fieldown)
#     print("\n북런던의 전통과 역사를 자랑하는 토트넘은 세계적인 한국인 선수 손흥민이 주장을 맡고 있는 상위권 클럽입니다.")
# elif commandteam == Chelsea:
#     introduce_powerbalance(Chelsea, Chelsea_attack, Chelsea_defence, Chelsea_fieldown)
#     print("\n예로부터 철벽 수비로 유명했던 첼시는 최근 젊은 공격수들의 영입으로 예전 PL에서의의 영광을 되찾고 있습니다.")
# elif commandteam == Wolverhampton:
#     introduce_powerbalance(Wolverhampton, Wolverhampton_attack, Wolverhampton_defence, Wolverhampton_fieldown)
#     print("\n한국 국적인 황희찬 선수가 뛰고 있는 울버햄튼 또한 중원 점유율에서 높은 점수를 가져가는 클럽입니다.")
# elif commandteam == West_Ham:
#     introduce_powerbalance(West_Ham, West_Ham_attack, West_Ham_defence, West_Ham_fieldown)
#     print("\n런던의 최고 인기 클럽인 웨스트햄은 최근 보웬과 쿠두스의 활약으로 좋은 폼을 이어나가고 있습니다.")
# elif commandteam == Newcastle:
#     introduce_powerbalance(Newcastle, Newcastle_attack, Newcastle_defence, Newcastle_fieldown)
#     print("\n최근 빈 살만이 뉴캐슬을 인수하면서 최고의 자본력을 등에 업고 급격한 성장을 거듭하며 공격력을 큰 폭으로 향상한 PL의 돌풍입니다.")

# def random_choice():
#     PL = [Arsenal, Man_City, Man_Utd, Liverpool, Tottenham, Chelsea, Wolverhampton, West_Ham, Newcastle]
#     PL_attack = [Arsenal_attack, Man_City_attack, Man_Utd_attack, Liverpool_attack, Tottenham_attack, Chelsea_attack, Wolverhampton_attack, West_Ham_attack, Newcastle_attack]
#     PL_defence = [Arsenal_defence, Man_City_defence, Man_Utd_defence, Liverpool_defence, Tottenham_defence, Chelsea_defence, Wolverhampton_defence, West_Ham_defence, Newcastle_defence]
#     PL_fieldown = [Arsenal_fieldown, Man_City_fieldown, Man_Utd_fieldown, Liverpool_fieldown, Tottenham_fieldown, Chelsea_fieldown, Wolverhampton_fieldown, West_Ham_fieldown, Newcastle_fieldown]
#     PL_Random = random.choice(PL)
#     PL_attack_Random = random.choice(PL_attack)
#     PL_defence_Random = random.choice(PL_defence)
#     PL_fieldown_Random = random.choice(PL_fieldown)
#     print(PL_Random, "은 투자한 결과 다음과 같이 전력이 보강되었습니다:")
#     print("공격진 : ", PL_attack_Random)
#     print("수비진 : ", PL_defence_Random)
#     print("중원 지배력", PL_fieldown_Random)

# # def Arsenal_Run():
# #     print("Pre-Matchweek\n투자할 부분을 선택하세요 : 트레이닝, 시설확충, 구단홍보")
# #     c_arsenal = input("선택 : ")
# #     if c_arsenal == "트레이닝":
# #         print("트레이닝을 선택하셨습니다. 모든 능력치 +1")
# #         Arsenal_attack + 1
# #         Arsenal_defence + 1
# #         Arsenal_fieldown + 1
# #         print("다른 팀의 전략을 참고하시겠습니까?")
# #         a_arsenal = input("Y/N")
# #         if a_arsenal == "Y":
# #             random_choice()


----------------------------------------------------------------------

# # 2024-05-29 3차 수정본(미완)
# import random
# import math
# import signal

# money = 100
# commandteam = 0
# Arsenal = "아스날"
# Arsenal_attack = 8
# Arsenal_defence = 8
# Arsenal_fieldown = 9
# Man_City = "맨시티"
# Man_City_attack = 10
# Man_City_defence = 7
# Man_City_fieldown = 7
# Man_Utd = "맨유"
# Man_Utd_attack = 5
# Man_Utd_defence = 7
# Man_Utd_fieldown = 8
# Liverpool = "리버풀"
# Liverpool_attack = 8
# Liverpool_defence = 9
# Liverpool_fieldown = 6
# Tottenham = "토트넘"
# Tottenham_attack = 7
# Tottenham_defence = 5
# Tottenham_fieldown = 9
# Chelsea = "첼시"
# Chelsea_attack = 6
# Chelsea_defence = 9
# Chelsea_fieldown = 8
# Wolverhampton = "울버햄튼"
# Wolverhampton_attack = 6
# Wolverhampton_defence = 6
# Wolverhampton_fieldown = 8
# West_Ham = "웨스트햄"
# West_Ham_attack = 5
# West_Ham_defence = 7
# West_Ham_fieldown = 6
# Newcastle = "뉴캐슬"
# Newcastle_attack = 8
# Newcastle_defence = 5
# Newcastle_fieldown = 5
# Arsenallist = [Arsenal_attack, Arsenal_defence, Arsenal_fieldown]
# Man_Citylist = [Man_City_attack, Man_City_defence, Man_City_fieldown]
# Man_Utdlist = [Man_Utd_attack, Man_Utd_defence, Man_Utd_fieldown]
# Liverpoollist = [Liverpool_attack, Liverpool_defence, Liverpool_fieldown]
# Tottenhamlist = [Tottenham_attack, Tottenham_defence, Tottenham_fieldown]
# Chelsealist = [Chelsea_attack, Chelsea_defence, Chelsea_fieldown]
# Wolverhamptonlist = [Wolverhampton_attack, Wolverhampton_defence, Wolverhampton_fieldown]
# West_Hamlist = [West_Ham_attack, West_Ham_defence, West_Ham_fieldown]
# Newcastlelist = [Newcastle_attack, Newcastle_defence, Newcastle_fieldown]
# PL = [Arsenal, Man_City, Man_Utd, Liverpool, Tottenham, Chelsea, Wolverhampton, West_Ham, Newcastle]

# print("PL에서 챔스가기!\n---------------------------------------------\n이제부터 당신은 한 팀의 감독입니다. PL 팀 중 하나를 선택하세요. 팀 변경의 기회는 없으니 신중히 고르세요!\n(용량 문제로 모든 팀들을 넣지 못한 점 죄송합니다!!)\n--------------------------------------------")
# print("[아스날, 맨시티, 맨유, 리버풀, 토트넘, 첼시, 울버햄튼, 웨스트햄, 뉴캐슬]")
# team = input("선택한 팀 : ")
# if team == "아스날":
#     commandteam = Arsenal
# elif team == "맨시티":
#     commandteam = Man_City
# elif team == "맨유":
#     commandteam = Man_Utd
# elif team == "리버풀":
#     commandteam = Liverpool
# elif team == "토트넘":
#     commandteam = Tottenham
# elif team == "첼시":
#     commandteam = Chelsea
# elif team == "울버햄튼":
#     commandteam = Wolverhampton
# elif team == "웨스트햄":
#     commandteam = West_Ham
# elif team == "뉴캐슬":
#     commandteam = Newcastle
# else:
#     print("양식에 맞춰 다시 작성해주세요!!")
#     exit()
# print("--------------------------------------------")
# print(team, "을 선택하셨습니다.\n")

# def introduce_powerbalance(a, b, c, d):
#     print("{}의\n공격력은 {}입니다.\n수비력은 {}입니다.\n중원 지배력은 {}입니다.".format(a, b, c, d))

# # 랜덤 초이스 (최종)

# def random_choice():
#     PL = [Arsenal, Man_City, Man_Utd, Liverpool, Tottenham, Chelsea, Wolverhampton, West_Ham, Newcastle]
#     PL_attack = [Arsenal_attack, Man_City_attack, Man_Utd_attack, Liverpool_attack, Tottenham_attack, Chelsea_attack, Wolverhampton_attack, West_Ham_attack, Newcastle_attack]
#     PL_defence = [Arsenal_defence, Man_City_defence, Man_Utd_defence, Liverpool_defence, Tottenham_defence, Chelsea_defence, Wolverhampton_defence, West_Ham_defence, Newcastle_defence]
#     PL_fieldown = [Arsenal_fieldown, Man_City_fieldown, Man_Utd_fieldown, Liverpool_fieldown, Tottenham_fieldown, Chelsea_fieldown, Wolverhampton_fieldown, West_Ham_fieldown, Newcastle_fieldown]
#     PL_Random = random.choice(PL)
#     PL_attack_Random = random.choice(PL_attack)
#     if PL_Random == Arsenal:
#         a = random.randint(-3, 3)
#         b = random.randint(-3, 3)
#         c = random.randint(-3, 3)
#         Arsenal_attack + a
#         Arsenal_defence + b
#         Arsenal_fieldown + c
#         print("아스날은 투자한 결과 다음과 같이 전력이 보강되었습니다:")
#         print("공격진 : ", Arsenal_attack)
#         print("수비진 : ", Arsenal_defence)
#         print("중원 지배력", Arsenal_fieldown)
#     elif PL_Random == Man_City:
#         a = random.randint(-3, 3)
#         b = random.randint(-3, 3)
#         c = random.randint(-3, 3)
#         Man_City_attack + a
#         Man_City_defence + b
#         Man_City_fieldown + c
#         print("맨시티는 투자한 결과 다음과 같이 전력이 보강되었습니다:")
#         print("공격진 : ", Man_City_attack)
#         print("수비진 : ", Man_City_defence)
#         print("중원 지배력", Man_City_fieldown)
#     elif PL_Random == Liverpool:
#         a = random.randint(-3, 3)
#         b = random.randint(-3, 3)
#         c = random.randint(-3, 3)
#         Liverpool_attack + a
#         Liverpool_defence + b
#         Liverpool_fieldown + c
#         print("리버풀은 투자한 결과 다음과 같이 전력이 보강되었습니다:")
#         print("공격진 : ", Liverpool_attack)
#         print("수비진 : ", Liverpool_defence)
#         print("중원 지배력", Liverpool_fieldown)
#     elif PL_Random == Tottenham:
#         a = random.randint(-3, 3)
#         b = random.randint(-3, 3)
#         c = random.randint(-3, 3)
#         Tottenham_attack + a
#         Tottenham_defence + b
#         Tottenham_fieldown + c
#         print("토트넘은 투자한 결과 다음과 같이 전력이 보강되었습니다:")
#         print("공격진 : ", Tottenham_attack)
#         print("수비진 : ", Tottenham_defence)
#         print("중원 지배력", Tottenham_fieldown)
#     elif PL_Random == Chelsea:
#         a = random.randint(-3, 3)
#         b = random.randint(-3, 3)
#         c = random.randint(-3, 3)
#         Chelsea_attack + a
#         Chelsea_defence + b
#         Chelsea_fieldown + c
#         print("첼시는 투자한 결과 다음과 같이 전력이 보강되었습니다:")
#         print("공격진 : ", Chelsea_attack)
#         print("수비진 : ", Chelsea_defence)
#         print("중원 지배력", Chelsea_fieldown)
#     elif PL_Random == Wolverhampton:
#         a = random.randint(-3, 3)
#         b = random.randint(-3, 3)
#         c = random.randint(-3, 3)
#         Wolverhampton_attack + a
#         Wolverhampton_defence + b
#         Wolverhampton_fieldown + c
#         print("첼시는 투자한 결과 다음과 같이 전력이 보강되었습니다:")
#         print("공격진 : ", Wolverhampton_attack)
#         print("수비진 : ", Wolverhampton_defence)
#         print("중원 지배력", Wolverhampton_fieldown)
#     elif PL_Random == West_Ham:
#         a = random.randint(-3, 3)
#         b = random.randint(-3, 3)
#         c = random.randint(-3, 3)
#         West_Ham_attack + a
#         West_Ham_defence + b
#         West_Ham_fieldown + c
#         print("웨스트햄은 투자한 결과 다음과 같이 전력이 보강되었습니다:")
#         print("공격진 : ", West_Ham_attack)
#         print("수비진 : ", West_Ham_defence)
#         print("중원 지배력", West_Ham_fieldown)
#     elif PL_Random == Newcastle:
#         a = random.randint(-3, 3)
#         b = random.randint(-3, 3)
#         c = random.randint(-3, 3)
#         Newcastle_attack + a
#         Newcastle_defence + b
#         Newcastle_fieldown + c
#         print("뉴캐슬은 투자한 결과 다음과 같이 전력이 보강되었습니다:")
#         print("공격진 : ", Newcastle_attack)
#         print("수비진 : ", Newcastle_defence)
#         print("중원 지배력", Newcastle_fieldown)

# 아스날_승점 = 0
# 맨시티_승점 = 0
# 맨유_승점 = 0
# 리버풀_승점 = 0
# 토트넘_승점 = 0
# 첼시_승점 = 0
# 울버햄튼_승점 = 0
# 웨스트햄_승점 = 0
# 뉴캐슬_승점 = 0



# n = 0
# def Arsenal_Run():
#     # UnboundLocalError: cannot access local variable '승점' where it is not associated with a value 이거 안뜨게 하려면 함수 안에서 변수를 초기화 시켜줘야 한다.
#     n = 0
#     print("Pre-Matchweek\n투자할 부분을 선택하세요 : 트레이닝, 시설확충, 구단홍보")
#     c_arsenal = input("선택 : ")
#     if c_arsenal == "트레이닝":
#         print("트레이닝을 선택하셨습니다. 모든 능력치 +1")
#         Arsenal_attack + 1
#         Arsenal_defence + 1
#         Arsenal_fieldown + 1
#         print("다른 팀 1개의 투자를 랜덤으로 살펴보겠습니다.")
#         random_choice()
#         아스날_승점 = 0
#         맨시티_승점 = 0
#         맨유_승점 = 0
#         리버풀_승점 = 0
#         토트넘_승점 = 0
#         첼시_승점 = 0
#         울버햄튼_승점 = 0
#         웨스트햄_승점 = 0
#         뉴캐슬_승점 = 0
#         아스날_승점 = 아스날_승점 + 0
#         맨시티_승점 = 맨시티_승점 + 0
#         맨유_승점 = 맨유_승점 + 0
#         리버풀_승점 = 리버풀_승점 + 0
#         토트넘_승점 = 토트넘_승점 + 0
#         첼시_승점 = 첼시_승점 + 0
#         울버햄튼_승점 = 울버햄튼_승점 + 0
#         웨스트햄_승점 = 웨스트햄_승점 + 0
#         뉴캐슬_승점 = 뉴캐슬_승점 + 0
#         a = str(input("다음 단계로 넘어가려면 Y를 입력해주세요.\n"))
#         if a == "Y":
#             print("2주가 흘렀습니다.\n--------------------------------------------\nMatchweek 1 - Away (St. James Park)\n--------------------------------------------\nNewcastle F.C.(HOME) vs Arsenal F.C.(AWAY)\n")
#             print("뉴캐슬 vs 아스날 전력 분석\n뉴캐슬의 vs 아스날의\n공격력은 {} vs {}입니다.\n수비력은 {} vs {}입니다.\n중원 지배력은 {} vs {}입니다.\n".format(Newcastle_attack, Arsenal_attack, Newcastle_defence, Arsenal_defence, Newcastle_fieldown, Arsenal_fieldown))
#             b = input(("포메이션을 선택하세요 : 3-4-3, 4-3-3, 4-2-3-1\n공격 우선 : 3-4-3, 수비 우선 : 4-3-3, 둘 다 : 4-2-3-1\n"))
#             if b == "3-4-3":
#                 if (Arsenal_attack > Newcastle_attack and Arsenal_defence >= Newcastle_defence and Arsenal_fieldown >= Newcastle_fieldown) or (Arsenal_attack > Newcastle_attack and Arsenal_defence >= Newcastle_defence and Arsenal_fieldown < Newcastle_fieldown) or (Arsenal_attack == Newcastle_attack and Arsenal_defence >= Newcastle_defence and Arsenal_fieldown >= Newcastle_fieldown):
#                     print("--------------------------------------------\n{} - {}, 아스날 승\n--------------------------------------------".format(random.randint(0, 1), random.randint(2, 4)))
#                     아스날_승점 = 아스날_승점 + 3
#                 elif (Arsenal_attack > Newcastle_attack and Arsenal_defence < Newcastle_defence and Arsenal_fieldown >= Newcastle_fieldown) or (Arsenal_attack == Newcastle_attack and Arsenal_defence < Newcastle_defence and Arsenal_fieldown >= Newcastle_fieldown) or (Arsenal_attack == Newcastle_attack and Arsenal_defence >= Newcastle_defence and Arsenal_fieldown < Newcastle_fieldown) or  (Arsenal_attack < Newcastle_attack and Arsenal_defence >= Newcastle_defence and Arsenal_fieldown >= Newcastle_fieldown):
#                     print("--------------------------------------------\n{} - {}, 무승부\n--------------------------------------------".format(random.randint(2, 2), random.randint(2, 2)))
#                     아스날_승점 = 아스날_승점 + 1
#                 elif (Arsenal_attack > Newcastle_attack and Arsenal_defence < Newcastle_defence and Arsenal_fieldown < Newcastle_fieldown) or (Arsenal_attack == Newcastle_attack and Arsenal_defence < Newcastle_defence and Arsenal_fieldown < Newcastle_fieldown) or (Arsenal_attack < Newcastle_attack and Arsenal_defence < Newcastle_defence and Arsenal_fieldown >= Newcastle_fieldown) or (Arsenal_attack < Newcastle_attack and Arsenal_defence >= Newcastle_defence and Arsenal_fieldown < Newcastle_fieldown) or  (Arsenal_attack < Newcastle_attack and Arsenal_defence < Newcastle_defence and Arsenal_fieldown < Newcastle_fieldown):
#                     print("--------------------------------------------\n{} - {}, 뉴캐슬 승\n--------------------------------------------".format(random.randint(2, 3), random.randint(0, 1)))
#                     아스날_승점 = 아스날_승점 + 0
#             elif b == "4-3-3":
#                 if (Arsenal_defence > Newcastle_defence and Arsenal_attack >= Newcastle_attack and Arsenal_fieldown >= Newcastle_fieldown) or (Arsenal_defence > Newcastle_defence and Arsenal_attack >= Newcastle_attack and Arsenal_fieldown < Newcastle_fieldown) or (Arsenal_defence == Newcastle_defence and Arsenal_attack >= Newcastle_attack and Arsenal_fieldown >= Newcastle_fieldown):
#                     print("--------------------------------------------\n{} - {}, 아스날 승\n--------------------------------------------".format(random.randint(0, 1), random.randint(2, 3)))
#                     아스날_승점 = 아스날_승점 + 3
#                 elif (Arsenal_defence > Newcastle_defence and Arsenal_attack < Newcastle_attack and Arsenal_fieldown >= Newcastle_fieldown) or (Arsenal_defence == Newcastle_defence and Arsenal_attack < Newcastle_attack and Arsenal_fieldown >= Newcastle_fieldown) or (Arsenal_defence == Newcastle_defence and Arsenal_attack >= Newcastle_attack and Arsenal_fieldown < Newcastle_fieldown) or  (Arsenal_defence < Newcastle_defence and Arsenal_attack >= Newcastle_attack and Arsenal_fieldown >= Newcastle_fieldown):
#                     print("--------------------------------------------\n{} - {}, 무승부\n--------------------------------------------".format(random.randint(2, 2), random.randint(2, 2)))
#                     아스날_승점 = 아스날_승점 + 1
#                 elif (Arsenal_defence > Newcastle_defence and Arsenal_attack < Newcastle_attack and Arsenal_fieldown < Newcastle_fieldown) or (Arsenal_defence == Newcastle_defence and Arsenal_attack < Newcastle_attack and Arsenal_fieldown < Newcastle_fieldown) or (Arsenal_defence < Newcastle_defence and Arsenal_attack < Newcastle_attack and Arsenal_fieldown >= Newcastle_fieldown) or (Arsenal_defence < Newcastle_defence and Arsenal_attack >= Newcastle_attack and Arsenal_fieldown < Newcastle_fieldown) or  (Arsenal_defence < Newcastle_defence and Arsenal_attack < Newcastle_attack and Arsenal_fieldown < Newcastle_fieldown):
#                     print("--------------------------------------------\n{} - {}, 뉴캐슬 승\n--------------------------------------------".format(random.randint(2, 4), random.randint(0, 1)))
#                     아스날_승점 = 아스날_승점 + 0
#             elif b == "4-2-3-1":
#                 if (Arsenal_fieldown > Newcastle_fieldown and Arsenal_attack >= Newcastle_attack and Arsenal_defence >= Newcastle_defence) or (Arsenal_fieldown > Newcastle_fieldown and Arsenal_attack >= Newcastle_attack and Arsenal_defence < Newcastle_defence) or (Arsenal_fieldown == Newcastle_fieldown and Arsenal_attack >= Newcastle_attack and Arsenal_defence >= Newcastle_defence):
#                     print("--------------------------------------------\n{} - {}, 아스날 승\n--------------------------------------------".format(random.randint(0, 1), random.randint(2, 3)))
#                     아스날_승점 = 아스날_승점 + 3
#                 elif (Arsenal_fieldown > Newcastle_fieldown and Arsenal_attack < Newcastle_attack and Arsenal_defence >= Newcastle_defence) or (Arsenal_fieldown == Newcastle_fieldown and Arsenal_attack < Newcastle_attack and Arsenal_defence >= Newcastle_defence) or (Arsenal_fieldown == Newcastle_fieldown and Arsenal_attack >= Newcastle_attack and Arsenal_defence < Newcastle_defence) or  (Arsenal_fieldown < Newcastle_fieldown and Arsenal_attack >= Newcastle_attack and Arsenal_defence >= Newcastle_defence):
#                     print("--------------------------------------------\n{} - {}, 무승부\n--------------------------------------------".format(random.randint(2, 2), random.randint(2, 2)))
#                     아스날_승점 = 아스날_승점 + 1
#                 elif (Arsenal_fieldown > Newcastle_fieldown and Arsenal_attack < Newcastle_attack and Arsenal_defence < Newcastle_defence) or (Arsenal_fieldown == Newcastle_fieldown and Arsenal_attack < Newcastle_attack and Arsenal_defence < Newcastle_defence) or (Arsenal_fieldown < Newcastle_fieldown and Arsenal_attack < Newcastle_attack and Arsenal_defence >= Newcastle_defence) or (Arsenal_fieldown < Newcastle_fieldown and Arsenal_attack >= Newcastle_attack and Arsenal_defence < Newcastle_defence) or  (Arsenal_fieldown < Newcastle_fieldown and Arsenal_attack < Newcastle_attack and Arsenal_defence < Newcastle_defence):
#                     print("--------------------------------------------\n{} - {}, 뉴캐슬 승\n--------------------------------------------".format(random.randint(2, 4), random.randint(0, 1)))
#                     아스날_승점 = 아스날_승점 + 0
#             n = n + 1
#             print("[첫] 번째 경기를 무사히 끝냈습니다. 당신의 승점은 {}점 입니다".format(아스날_승점))
#             print("{}주차 프리미어리그 순위".format(n))
#             아스날_승점 = 아스날_승점
#             맨시티_승점 = random.randint(0,3)
#             리버풀_승점 = random.randint(0,3)
#             맨유_승점 = random.randint(0,3)
#             토트넘_승점 = random.randint(0,3)
#             첼시_승점 = random.randint(0,3)
#             울버햄튼_승점 = random.randint(0,3)
#             웨스트햄_승점 = random.randint(0,3)
#             뉴캐슬_승점 = random.randint(0,3)
#             팀_승점 = {
#             "아스날 FC": 아스날_승점,
#             "맨체스터 시티 FC": 맨시티_승점,
#             "맨체스터 유나이티드 FC" : 맨유_승점,
#             "리버풀 FC" : 리버풀_승점,
#             "토트넘 홋스퍼 FC" : 토트넘_승점,
#             "첼시 FC" : 첼시_승점,
#             "울버햄튼 원더러스 FC" : 울버햄튼_승점,
#             "웨스트햄 유나이티드 FC" : 웨스트햄_승점,
#             "뉴캐슬 FC" : 뉴캐슬_승점          
#             }
#             sorted_scoreboard = sorted(팀_승점.items(), key=lambda x: x[1], reverse=True)
#             print("\nEngland Premier League\n")
#             for 순위, (팀, 승점) in enumerate((sorted_scoreboard), start=1):
#                 print(f"{순위}위 : {팀} - {승점}점")
#         a = str(input("다음 단계로 넘어가려면 Y를 입력해주세요.\n"))
#         if a == "Y":
#             print("2주가 흘렀습니다.\n--------------------------------------------\nMatchweek 2 - Home (Emirates Stadium)\n--------------------------------------------\nNewcastle F.C.(HOME) vs Arsenal F.C.(AWAY)\n")
#             print("뉴캐슬 vs 아스날 전력 분석\n뉴캐슬의 vs 아스날의\n공격력은 {} vs {}입니다.\n수비력은 {} vs {}입니다.\n중원 지배력은 {} vs {}입니다.\n".format(Newcastle_attack, Arsenal_attack, Newcastle_defence, Arsenal_defence, Newcastle_fieldown, Arsenal_fieldown))
#             b = input(("포메이션을 선택하세요 : 3-4-3, 4-3-3, 4-2-3-1\n공격 우선 : 3-4-3, 수비 우선 : 4-3-3, 둘 다 : 4-2-3-1\n"))
#             if b == "3-4-3":
#                 if (Arsenal_attack > Newcastle_attack and Arsenal_defence >= Newcastle_defence and Arsenal_fieldown >= Newcastle_fieldown) or (Arsenal_attack > Newcastle_attack and Arsenal_defence >= Newcastle_defence and Arsenal_fieldown < Newcastle_fieldown) or (Arsenal_attack == Newcastle_attack and Arsenal_defence >= Newcastle_defence and Arsenal_fieldown >= Newcastle_fieldown):
#                     print("--------------------------------------------\n{} - {}, 아스날 승\n--------------------------------------------".format(random.randint(0, 1), random.randint(2, 4)))
#                     아스날_승점 = 아스날_승점 + 3
#                 elif (Arsenal_attack > Newcastle_attack and Arsenal_defence < Newcastle_defence and Arsenal_fieldown >= Newcastle_fieldown) or (Arsenal_attack == Newcastle_attack and Arsenal_defence < Newcastle_defence and Arsenal_fieldown >= Newcastle_fieldown) or (Arsenal_attack == Newcastle_attack and Arsenal_defence >= Newcastle_defence and Arsenal_fieldown < Newcastle_fieldown) or  (Arsenal_attack < Newcastle_attack and Arsenal_defence >= Newcastle_defence and Arsenal_fieldown >= Newcastle_fieldown):
#                     print("--------------------------------------------\n{} - {}, 무승부\n--------------------------------------------".format(random.randint(2, 2), random.randint(2, 2)))
#                     아스날_승점 = 아스날_승점 + 1
#                 elif (Arsenal_attack > Newcastle_attack and Arsenal_defence < Newcastle_defence and Arsenal_fieldown < Newcastle_fieldown) or (Arsenal_attack == Newcastle_attack and Arsenal_defence < Newcastle_defence and Arsenal_fieldown < Newcastle_fieldown) or (Arsenal_attack < Newcastle_attack and Arsenal_defence < Newcastle_defence and Arsenal_fieldown >= Newcastle_fieldown) or (Arsenal_attack < Newcastle_attack and Arsenal_defence >= Newcastle_defence and Arsenal_fieldown < Newcastle_fieldown) or  (Arsenal_attack < Newcastle_attack and Arsenal_defence < Newcastle_defence and Arsenal_fieldown < Newcastle_fieldown):
#                     print("--------------------------------------------\n{} - {}, 뉴캐슬 승\n--------------------------------------------".format(random.randint(2, 3), random.randint(0, 1)))
#                     아스날_승점 = 아스날_승점 + 0
#             elif b == "4-3-3":
#                 if (Arsenal_defence > Newcastle_defence and Arsenal_attack >= Newcastle_attack and Arsenal_fieldown >= Newcastle_fieldown) or (Arsenal_defence > Newcastle_defence and Arsenal_attack >= Newcastle_attack and Arsenal_fieldown < Newcastle_fieldown) or (Arsenal_defence == Newcastle_defence and Arsenal_attack >= Newcastle_attack and Arsenal_fieldown >= Newcastle_fieldown):
#                     print("--------------------------------------------\n{} - {}, 아스날 승\n--------------------------------------------".format(random.randint(0, 1), random.randint(2, 3)))
#                     아스날_승점 = 아스날_승점 + 3
#                 elif (Arsenal_defence > Newcastle_defence and Arsenal_attack < Newcastle_attack and Arsenal_fieldown >= Newcastle_fieldown) or (Arsenal_defence == Newcastle_defence and Arsenal_attack < Newcastle_attack and Arsenal_fieldown >= Newcastle_fieldown) or (Arsenal_defence == Newcastle_defence and Arsenal_attack >= Newcastle_attack and Arsenal_fieldown < Newcastle_fieldown) or  (Arsenal_defence < Newcastle_defence and Arsenal_attack >= Newcastle_attack and Arsenal_fieldown >= Newcastle_fieldown):
#                     print("--------------------------------------------\n{} - {}, 무승부\n--------------------------------------------".format(random.randint(2, 2), random.randint(2, 2)))
#                     아스날_승점 = 아스날_승점 + 1
#                 elif (Arsenal_defence > Newcastle_defence and Arsenal_attack < Newcastle_attack and Arsenal_fieldown < Newcastle_fieldown) or (Arsenal_defence == Newcastle_defence and Arsenal_attack < Newcastle_attack and Arsenal_fieldown < Newcastle_fieldown) or (Arsenal_defence < Newcastle_defence and Arsenal_attack < Newcastle_attack and Arsenal_fieldown >= Newcastle_fieldown) or (Arsenal_defence < Newcastle_defence and Arsenal_attack >= Newcastle_attack and Arsenal_fieldown < Newcastle_fieldown) or  (Arsenal_defence < Newcastle_defence and Arsenal_attack < Newcastle_attack and Arsenal_fieldown < Newcastle_fieldown):
#                     print("--------------------------------------------\n{} - {}, 뉴캐슬 승\n--------------------------------------------".format(random.randint(2, 4), random.randint(0, 1)))
#                     아스날_승점 = 아스날_승점 + 0
#             elif b == "4-2-3-1":
#                 if (Arsenal_fieldown > Newcastle_fieldown and Arsenal_attack >= Newcastle_attack and Arsenal_defence >= Newcastle_defence) or (Arsenal_fieldown > Newcastle_fieldown and Arsenal_attack >= Newcastle_attack and Arsenal_defence < Newcastle_defence) or (Arsenal_fieldown == Newcastle_fieldown and Arsenal_attack >= Newcastle_attack and Arsenal_defence >= Newcastle_defence):
#                     print("--------------------------------------------\n{} - {}, 아스날 승\n--------------------------------------------".format(random.randint(0, 1), random.randint(2, 3)))
#                     아스날_승점 = 아스날_승점 + 3
#                 elif (Arsenal_fieldown > Newcastle_fieldown and Arsenal_attack < Newcastle_attack and Arsenal_defence >= Newcastle_defence) or (Arsenal_fieldown == Newcastle_fieldown and Arsenal_attack < Newcastle_attack and Arsenal_defence >= Newcastle_defence) or (Arsenal_fieldown == Newcastle_fieldown and Arsenal_attack >= Newcastle_attack and Arsenal_defence < Newcastle_defence) or  (Arsenal_fieldown < Newcastle_fieldown and Arsenal_attack >= Newcastle_attack and Arsenal_defence >= Newcastle_defence):
#                     print("--------------------------------------------\n{} - {}, 무승부\n--------------------------------------------".format(random.randint(2, 2), random.randint(2, 2)))
#                     아스날_승점 = 아스날_승점 + 1
#                 elif (Arsenal_fieldown > Newcastle_fieldown and Arsenal_attack < Newcastle_attack and Arsenal_defence < Newcastle_defence) or (Arsenal_fieldown == Newcastle_fieldown and Arsenal_attack < Newcastle_attack and Arsenal_defence < Newcastle_defence) or (Arsenal_fieldown < Newcastle_fieldown and Arsenal_attack < Newcastle_attack and Arsenal_defence >= Newcastle_defence) or (Arsenal_fieldown < Newcastle_fieldown and Arsenal_attack >= Newcastle_attack and Arsenal_defence < Newcastle_defence) or  (Arsenal_fieldown < Newcastle_fieldown and Arsenal_attack < Newcastle_attack and Arsenal_defence < Newcastle_defence):
#                     print("--------------------------------------------\n{} - {}, 뉴캐슬 승\n--------------------------------------------".format(random.randint(2, 4), random.randint(0, 1)))
#                     아스날_승점 = 아스날_승점 + 0
#             n = n + 1
#             print("[첫] 번째 경기를 무사히 끝냈습니다. 당신의 승점은 {}점 입니다".format(아스날_승점))
#             print("{}주차 프리미어리그 순위".format(n))
#             아스날_승점 = 아스날_승점
#             맨시티_승점 = random.randint(0,3) + 맨시티_승점
#             리버풀_승점 = random.randint(0,3) + 리버풀_승점
#             맨유_승점 = random.randint(0,3) + 맨유_승점
#             토트넘_승점 = random.randint(0,3) + 토트넘_승점
#             첼시_승점 = random.randint(0,3) + 첼시_승점
#             울버햄튼_승점 = random.randint(0,3) + 울버햄튼_승점
#             웨스트햄_승점 = random.randint(0,3) + 웨스트햄_승점
#             뉴캐슬_승점 = random.randint(0,3) + 뉴캐슬_승점
#             팀_승점 = {
#             "아스날 FC": 아스날_승점,
#             "맨체스터 시티 FC": 맨시티_승점,
#             "맨체스터 유나이티드 FC" : 맨유_승점,
#             "리버풀 FC" : 리버풀_승점,
#             "토트넘 홋스퍼 FC" : 토트넘_승점,
#             "첼시 FC" : 첼시_승점,
#             "울버햄튼 원더러스 FC" : 울버햄튼_승점,
#             "웨스트햄 유나이티드 FC" : 웨스트햄_승점,
#             "뉴캐슬 FC" : 뉴캐슬_승점          
#             }
#             sorted_scoreboard = sorted(팀_승점.items(), key=lambda x: x[1], reverse=True)
#             print("\nEngland Premier League\n")
#             for 순위, (팀, 승점) in enumerate((sorted_scoreboard), start=1):
#                 print(f"{순위}위 : {팀} - {승점}점")   
# if commandteam == Arsenal:
#     introduce_powerbalance(Arsenal, Arsenal_attack, Arsenal_defence, Arsenal_fieldown)
#     print("\n아스날은 프리미어리그 전통의 강팀으로, 공격, 수비, 중원 모두 우수한 활약을 보입니다.")
#     Arsenal_Run()
# elif commandteam == Man_City:
#     introduce_powerbalance(Man_City, Man_City_attack, Man_City_defence, Man_City_fieldown)
#     print("\n맨체스터 시티는 세계 최강의 공격진을 필두로 한 강팀으로, 매 경기마다 화끈한 득점력을 선보입니다.")
# elif commandteam == Man_Utd:
#     introduce_powerbalance(Man_Utd, Man_Utd_attack, Man_Utd_defence, Man_Utd_fieldown)
#     print("\n호날두, 루니, 박지성, 베컴 등의 세계적인 스타 선수들이 거쳐간 맨체스터 유나이티드는 전 세계적인 팬덤을 보유한 클럽입니다.")
# elif commandteam == Liverpool:
#     introduce_powerbalance(Liverpool, Liverpool_attack, Liverpool_defence, Liverpool_fieldown)
#     print("\n오랜 침체기를 끝내고 리그 상위권으로 도약한 리버풀은 공격과 수비에서 특히 우수한 클럽입니다.")
# elif commandteam == Tottenham:
#     introduce_powerbalance(Tottenham, Tottenham_attack, Tottenham_defence, Tottenham_fieldown)
#     print("\n북런던의 전통과 역사를 자랑하는 토트넘은 세계적인 한국인 선수 손흥민이 주장을 맡고 있는 상위권 클럽입니다.")
# elif commandteam == Chelsea:
#     introduce_powerbalance(Chelsea, Chelsea_attack, Chelsea_defence, Chelsea_fieldown)
#     print("\n예로부터 철벽 수비로 유명했던 첼시는 최근 젊은 공격수들의 영입으로 예전 PL에서의의 영광을 되찾고 있습니다.")
# elif commandteam == Wolverhampton:
#     introduce_powerbalance(Wolverhampton, Wolverhampton_attack, Wolverhampton_defence, Wolverhampton_fieldown)
#     print("\n한국 국적인 황희찬 선수가 뛰고 있는 울버햄튼 또한 중원 점유율에서 높은 점수를 가져가는 클럽입니다.")
# elif commandteam == West_Ham:
#     introduce_powerbalance(West_Ham, West_Ham_attack, West_Ham_defence, West_Ham_fieldown)
#     print("\n런던의 최고 인기 클럽인 웨스트햄은 최근 보웬과 쿠두스의 활약으로 좋은 폼을 이어나가고 있습니다.")
# elif commandteam == Newcastle:
#     introduce_powerbalance(Newcastle, Newcastle_attack, Newcastle_defence, Newcastle_fieldown)
#     print("\n최근 빈 살만이 뉴캐슬을 인수하면서 최고의 자본력을 등에 업고 급격한 성장을 거듭하며 공격력을 큰 폭으로 향상한 PL의 돌풍입니다.")

# def random_choice():
#     PL = [Arsenal, Man_City, Man_Utd, Liverpool, Tottenham, Chelsea, Wolverhampton, West_Ham, Newcastle]
#     PL_attack = [Arsenal_attack, Man_City_attack, Man_Utd_attack, Liverpool_attack, Tottenham_attack, Chelsea_attack, Wolverhampton_attack, West_Ham_attack, Newcastle_attack]
#     PL_defence = [Arsenal_defence, Man_City_defence, Man_Utd_defence, Liverpool_defence, Tottenham_defence, Chelsea_defence, Wolverhampton_defence, West_Ham_defence, Newcastle_defence]
#     PL_fieldown = [Arsenal_fieldown, Man_City_fieldown, Man_Utd_fieldown, Liverpool_fieldown, Tottenham_fieldown, Chelsea_fieldown, Wolverhampton_fieldown, West_Ham_fieldown, Newcastle_fieldown]
#     PL_Random = random.choice(PL)
#     PL_attack_Random = random.choice(PL_attack)
#     PL_defence_Random = random.choice(PL_defence)
#     PL_fieldown_Random = random.choice(PL_fieldown)
#     print(PL_Random, "은 투자한 결과 다음과 같이 전력이 보강되었습니다:")
#     print("공격진 : ", PL_attack_Random)
#     print("수비진 : ", PL_defence_Random)
#     print("중원 지배력", PL_fieldown_Random)

# # def Arsenal_Run():
# #     print("Pre-Matchweek\n투자할 부분을 선택하세요 : 트레이닝, 시설확충, 구단홍보")
# #     c_arsenal = input("선택 : ")
# #     if c_arsenal == "트레이닝":
# #         print("트레이닝을 선택하셨습니다. 모든 능력치 +1")
# #         Arsenal_attack + 1
# #         Arsenal_defence + 1
# #         Arsenal_fieldown + 1
# #         print("다른 팀의 전략을 참고하시겠습니까?")
# #         a_arsenal = input("Y/N")
# #         if a_arsenal == "Y":
# #             random_choice()

# # # 2024-05-24 2차 수정본
# # import random
# # import math
# # import signal

# # 승점 = 0
# # money = 100
# # commandteam = 0
# # Arsenal = "아스날"
# # Arsenal_attack = 8
# # Arsenal_defence = 8
# # Arsenal_fieldown = 9
# # Man_City = "맨시티"
# # Man_City_attack = 10
# # Man_City_defence = 7
# # Man_City_fieldown = 7
# # Man_Utd = "맨유"
# # Man_Utd_attack = 5
# # Man_Utd_defence = 7
# # Man_Utd_fieldown = 8
# # Liverpool = "리버풀"
# # Liverpool_attack = 8
# # Liverpool_defence = 9
# # Liverpool_fieldown = 6
# # Tottenham = "토트넘"
# # Tottenham_attack = 7
# # Tottenham_defence = 5
# # Tottenham_fieldown = 9
# # Chelsea = "첼시"
# # Chelsea_attack = 6
# # Chelsea_defence = 9
# # Chelsea_fieldown = 8
# # Wolverhampton = "울버햄튼"
# # Wolverhampton_attack = 6
# # Wolverhampton_defence = 6
# # Wolverhampton_fieldown = 8
# # West_Ham = "웨스트햄"
# # West_Ham_attack = 5
# # West_Ham_defence = 7
# # West_Ham_fieldown = 6
# # Newcastle = "뉴캐슬"
# # Newcastle_attack = 8
# # Newcastle_defence = 5
# # Newcastle_fieldown = 5
# # Arsenallist = [Arsenal_attack, Arsenal_defence, Arsenal_fieldown]
# # Man_Citylist = [Man_City_attack, Man_City_defence, Man_City_fieldown]
# # Man_Utdlist = [Man_Utd_attack, Man_Utd_defence, Man_Utd_fieldown]
# # Liverpoollist = [Liverpool_attack, Liverpool_defence, Liverpool_fieldown]
# # Tottenhamlist = [Tottenham_attack, Tottenham_defence, Tottenham_fieldown]
# # Chelsealist = [Chelsea_attack, Chelsea_defence, Chelsea_fieldown]
# # Wolverhamptonlist = [Wolverhampton_attack, Wolverhampton_defence, Wolverhampton_fieldown]
# # West_Hamlist = [West_Ham_attack, West_Ham_defence, West_Ham_fieldown]
# # Newcastlelist = [Newcastle_attack, Newcastle_defence, Newcastle_fieldown]

# # print("PL에서 챔스가기!\n---------------------------------------------\n이제부터 당신은 한 팀의 감독입니다. PL 팀 중 하나를 선택하세요. 팀 변경의 기회는 없으니 신중히 고르세요!\n(용량 문제로 모든 팀들을 넣지 못한 점 죄송합니다!!)\n--------------------------------------------")
# # print("[아스날, 맨시티, 맨유, 리버풀, 토트넘, 첼시, 울버햄튼, 웨스트햄, 뉴캐슬]")
# # team = input("선택한 팀 : ")
# # if team == "아스날":
# #     commandteam = Arsenal
# # elif team == "맨시티":
# #     commandteam = Man_City
# # elif team == "맨유":
# #     commandteam = Man_Utd
# # elif team == "리버풀":
# #     commandteam = Liverpool
# # elif team == "토트넘":
# #     commandteam = Tottenham
# # elif team == "첼시":
# #     commandteam = Chelsea
# # elif team == "울버햄튼":
# #     commandteam = Wolverhampton
# # elif team == "웨스트햄":
# #     commandteam = West_Ham
# # elif team == "뉴캐슬":
# #     commandteam = Newcastle
# # else:
# #     print("양식에 맞춰 다시 작성해주세요!!")
# #     exit()
# # print("--------------------------------------------")
# # print(team, "을 선택하셨습니다.\n")

# # def introduce_powerbalance(a, b, c, d):
# #     print("{}의\n공격력은 {}입니다.\n수비력은 {}입니다.\n중원 지배력은 {}입니다.".format(a, b, c, d))

# # # 랜덤 초이스 (최종)

# # def random_choice():
# #     PL = [Arsenal, Man_City, Man_Utd, Liverpool, Tottenham, Chelsea, Wolverhampton, West_Ham, Newcastle]
# #     PL_attack = [Arsenal_attack, Man_City_attack, Man_Utd_attack, Liverpool_attack, Tottenham_attack, Chelsea_attack, Wolverhampton_attack, West_Ham_attack, Newcastle_attack]
# #     PL_defence = [Arsenal_defence, Man_City_defence, Man_Utd_defence, Liverpool_defence, Tottenham_defence, Chelsea_defence, Wolverhampton_defence, West_Ham_defence, Newcastle_defence]
# #     PL_fieldown = [Arsenal_fieldown, Man_City_fieldown, Man_Utd_fieldown, Liverpool_fieldown, Tottenham_fieldown, Chelsea_fieldown, Wolverhampton_fieldown, West_Ham_fieldown, Newcastle_fieldown]
# #     PL_Random = random.choice(PL)
# #     PL_attack_Random = random.choice(PL_attack)
# #     if PL_Random == Arsenal:
# #         a = random.randint(-3, 3)
# #         b = random.randint(-3, 3)
# #         c = random.randint(-3, 3)
# #         Arsenal_attack + a
# #         Arsenal_defence + b
# #         Arsenal_fieldown + c
# #         print("아스날은 투자한 결과 다음과 같이 전력이 보강되었습니다:")
# #         print("공격진 : ", Arsenal_attack)
# #         print("수비진 : ", Arsenal_defence)
# #         print("중원 지배력", Arsenal_fieldown)
# #     elif PL_Random == Man_City:
# #         a = random.randint(-3, 3)
# #         b = random.randint(-3, 3)
# #         c = random.randint(-3, 3)
# #         Man_City_attack + a
# #         Man_City_defence + b
# #         Man_City_fieldown + c
# #         print("맨시티는 투자한 결과 다음과 같이 전력이 보강되었습니다:")
# #         print("공격진 : ", Man_City_attack)
# #         print("수비진 : ", Man_City_defence)
# #         print("중원 지배력", Man_City_fieldown)
# #     elif PL_Random == Liverpool:
# #         a = random.randint(-3, 3)
# #         b = random.randint(-3, 3)
# #         c = random.randint(-3, 3)
# #         Liverpool_attack + a
# #         Liverpool_defence + b
# #         Liverpool_fieldown + c
# #         print("리버풀은 투자한 결과 다음과 같이 전력이 보강되었습니다:")
# #         print("공격진 : ", Liverpool_attack)
# #         print("수비진 : ", Liverpool_defence)
# #         print("중원 지배력", Liverpool_fieldown)
# #     elif PL_Random == Tottenham:
# #         a = random.randint(-3, 3)
# #         b = random.randint(-3, 3)
# #         c = random.randint(-3, 3)
# #         Tottenham_attack + a
# #         Tottenham_defence + b
# #         Tottenham_fieldown + c
# #         print("토트넘은 투자한 결과 다음과 같이 전력이 보강되었습니다:")
# #         print("공격진 : ", Tottenham_attack)
# #         print("수비진 : ", Tottenham_defence)
# #         print("중원 지배력", Tottenham_fieldown)
# #     elif PL_Random == Chelsea:
# #         a = random.randint(-3, 3)
# #         b = random.randint(-3, 3)
# #         c = random.randint(-3, 3)
# #         Chelsea_attack + a
# #         Chelsea_defence + b
# #         Chelsea_fieldown + c
# #         print("첼시는 투자한 결과 다음과 같이 전력이 보강되었습니다:")
# #         print("공격진 : ", Chelsea_attack)
# #         print("수비진 : ", Chelsea_defence)
# #         print("중원 지배력", Chelsea_fieldown)
# #     elif PL_Random == Wolverhampton:
# #         a = random.randint(-3, 3)
# #         b = random.randint(-3, 3)
# #         c = random.randint(-3, 3)
# #         Wolverhampton_attack + a
# #         Wolverhampton_defence + b
# #         Wolverhampton_fieldown + c
# #         print("첼시는 투자한 결과 다음과 같이 전력이 보강되었습니다:")
# #         print("공격진 : ", Wolverhampton_attack)
# #         print("수비진 : ", Wolverhampton_defence)
# #         print("중원 지배력", Wolverhampton_fieldown)
# #     elif PL_Random == West_Ham:
# #         a = random.randint(-3, 3)
# #         b = random.randint(-3, 3)
# #         c = random.randint(-3, 3)
# #         West_Ham_attack + a
# #         West_Ham_defence + b
# #         West_Ham_fieldown + c
# #         print("웨스트햄은 투자한 결과 다음과 같이 전력이 보강되었습니다:")
# #         print("공격진 : ", West_Ham_attack)
# #         print("수비진 : ", West_Ham_defence)
# #         print("중원 지배력", West_Ham_fieldown)
# #     elif PL_Random == Newcastle:
# #         a = random.randint(-3, 3)
# #         b = random.randint(-3, 3)
# #         c = random.randint(-3, 3)
# #         Newcastle_attack + a
# #         Newcastle_defence + b
# #         Newcastle_fieldown + c
# #         print("뉴캐슬은 투자한 결과 다음과 같이 전력이 보강되었습니다:")
# #         print("공격진 : ", Newcastle_attack)
# #         print("수비진 : ", Newcastle_defence)
# #         print("중원 지배력", Newcastle_fieldown)


# # def Arsenal_Run():
# #     # UnboundLocalError: cannot access local variable '승점' where it is not associated with a value 이거 안뜨게 하려면 함수 안에서 변수를 초기화 시켜줘야 한다.
# #     승점 = 0
# #     print("Pre-Matchweek\n투자할 부분을 선택하세요 : 트레이닝, 시설확충, 구단홍보")
# #     c_arsenal = input("선택 : ")
# #     if c_arsenal == "트레이닝":
# #         print("트레이닝을 선택하셨습니다. 모든 능력치 +1")
# #         Arsenal_attack + 1
# #         Arsenal_defence + 1
# #         Arsenal_fieldown + 1
# #         print("다른 팀 1개의 투자를 랜덤으로 살펴보겠습니다.")
# #         random_choice()
# #         a = str(input("다음 단계로 넘어가려면 Y를 입력해주세요.\n"))
# #         if a == "Y":
# #             print("2주가 흘렀습니다.\n--------------------------------------------\nMatchweek 1 - Away (St. James Park)\n--------------------------------------------\nNewcastle F.C.(HOME) vs Arsenal F.C.(AWAY)\n")
# #             print("뉴캐슬 vs 아스날 전력 분석\n뉴캐슬의 vs 아스날의\n공격력은 {} vs {}입니다.\n수비력은 {} vs {}입니다.\n중원 지배력은 {} vs {}입니다.\n".format(Newcastle_attack, Arsenal_attack, Newcastle_defence, Arsenal_defence, Newcastle_fieldown, Arsenal_fieldown))
# #             b = input(("포메이션을 선택하세요 : 3-4-3, 4-3-3, 4-2-3-1\n공격 우선 : 3-4-3, 수비 우선 : 4-3-3, 둘 다 : 4-2-3-1\n"))
# #             if b == "3-4-3":
# #                 if (Arsenal_attack > Newcastle_attack and Arsenal_defence >= Newcastle_defence and Arsenal_fieldown >= Newcastle_fieldown) or (Arsenal_attack > Newcastle_attack and Arsenal_defence >= Newcastle_defence and Arsenal_fieldown < Newcastle_fieldown) or (Arsenal_attack == Newcastle_attack and Arsenal_defence >= Newcastle_defence and Arsenal_fieldown >= Newcastle_fieldown):
# #                     print("--------------------------------------------\n{} - {}, 아스날 승\n--------------------------------------------".format(random.randint(0, 1), random.randint(2, 4)))
# #                     승점 = 승점 + 3
# #                 elif (Arsenal_attack > Newcastle_attack and Arsenal_defence < Newcastle_defence and Arsenal_fieldown >= Newcastle_fieldown) or (Arsenal_attack == Newcastle_attack and Arsenal_defence < Newcastle_defence and Arsenal_fieldown >= Newcastle_fieldown) or (Arsenal_attack == Newcastle_attack and Arsenal_defence >= Newcastle_defence and Arsenal_fieldown < Newcastle_fieldown) or  (Arsenal_attack < Newcastle_attack and Arsenal_defence >= Newcastle_defence and Arsenal_fieldown >= Newcastle_fieldown):
# #                     print("--------------------------------------------\n{} - {}, 무승부\n--------------------------------------------".format(random.randint(2, 2), random.randint(2, 2)))
# #                     승점 = 승점 + 1
# #                 elif (Arsenal_attack > Newcastle_attack and Arsenal_defence < Newcastle_defence and Arsenal_fieldown < Newcastle_fieldown) or (Arsenal_attack == Newcastle_attack and Arsenal_defence < Newcastle_defence and Arsenal_fieldown < Newcastle_fieldown) or (Arsenal_attack < Newcastle_attack and Arsenal_defence < Newcastle_defence and Arsenal_fieldown >= Newcastle_fieldown) or (Arsenal_attack < Newcastle_attack and Arsenal_defence >= Newcastle_defence and Arsenal_fieldown < Newcastle_fieldown) or  (Arsenal_attack < Newcastle_attack and Arsenal_defence < Newcastle_defence and Arsenal_fieldown < Newcastle_fieldown):
# #                     print("--------------------------------------------\n{} - {}, 뉴캐슬 승\n--------------------------------------------".format(random.randint(2, 3), random.randint(0, 1)))
# #                     승점 = 승점 + 0
# #             elif b == "4-3-3":
# #                 if (Arsenal_defence > Newcastle_defence and Arsenal_attack >= Newcastle_attack and Arsenal_fieldown >= Newcastle_fieldown) or (Arsenal_defence > Newcastle_defence and Arsenal_attack >= Newcastle_attack and Arsenal_fieldown < Newcastle_fieldown) or (Arsenal_defence == Newcastle_defence and Arsenal_attack >= Newcastle_attack and Arsenal_fieldown >= Newcastle_fieldown):
# #                     print("--------------------------------------------\n{} - {}, 아스날 승\n--------------------------------------------".format(random.randint(0, 1), random.randint(2, 3)))
# #                     승점 = 승점 + 3
# #                 elif (Arsenal_defence > Newcastle_defence and Arsenal_attack < Newcastle_attack and Arsenal_fieldown >= Newcastle_fieldown) or (Arsenal_defence == Newcastle_defence and Arsenal_attack < Newcastle_attack and Arsenal_fieldown >= Newcastle_fieldown) or (Arsenal_defence == Newcastle_defence and Arsenal_attack >= Newcastle_attack and Arsenal_fieldown < Newcastle_fieldown) or  (Arsenal_defence < Newcastle_defence and Arsenal_attack >= Newcastle_attack and Arsenal_fieldown >= Newcastle_fieldown):
# #                     print("--------------------------------------------\n{} - {}, 무승부\n--------------------------------------------".format(random.randint(2, 2), random.randint(2, 2)))
# #                     승점 = 승점 + 1
# #                 elif (Arsenal_defence > Newcastle_defence and Arsenal_attack < Newcastle_attack and Arsenal_fieldown < Newcastle_fieldown) or (Arsenal_defence == Newcastle_defence and Arsenal_attack < Newcastle_attack and Arsenal_fieldown < Newcastle_fieldown) or (Arsenal_defence < Newcastle_defence and Arsenal_attack < Newcastle_attack and Arsenal_fieldown >= Newcastle_fieldown) or (Arsenal_defence < Newcastle_defence and Arsenal_attack >= Newcastle_attack and Arsenal_fieldown < Newcastle_fieldown) or  (Arsenal_defence < Newcastle_defence and Arsenal_attack < Newcastle_attack and Arsenal_fieldown < Newcastle_fieldown):
# #                     print("--------------------------------------------\n{} - {}, 뉴캐슬 승\n--------------------------------------------".format(random.randint(2, 4), random.randint(0, 1)))
# #                     승점 = 승점 + 0
# #             elif b == "4-2-3-1":
# #                 if (Arsenal_fieldown > Newcastle_fieldown and Arsenal_attack >= Newcastle_attack and Arsenal_defence >= Newcastle_defence) or (Arsenal_fieldown > Newcastle_fieldown and Arsenal_attack >= Newcastle_attack and Arsenal_defence < Newcastle_defence) or (Arsenal_fieldown == Newcastle_fieldown and Arsenal_attack >= Newcastle_attack and Arsenal_defence >= Newcastle_defence):
# #                     print("--------------------------------------------\n{} - {}, 아스날 승\n--------------------------------------------".format(random.randint(0, 1), random.randint(2, 3)))
# #                     승점 = 승점 + 3
# #                 elif (Arsenal_fieldown > Newcastle_fieldown and Arsenal_attack < Newcastle_attack and Arsenal_defence >= Newcastle_defence) or (Arsenal_fieldown == Newcastle_fieldown and Arsenal_attack < Newcastle_attack and Arsenal_defence >= Newcastle_defence) or (Arsenal_fieldown == Newcastle_fieldown and Arsenal_attack >= Newcastle_attack and Arsenal_defence < Newcastle_defence) or  (Arsenal_fieldown < Newcastle_fieldown and Arsenal_attack >= Newcastle_attack and Arsenal_defence >= Newcastle_defence):
# #                     print("--------------------------------------------\n{} - {}, 무승부\n--------------------------------------------".format(random.randint(2, 2), random.randint(2, 2)))
# #                     승점 = 승점 + 1
# #                 elif (Arsenal_fieldown > Newcastle_fieldown and Arsenal_attack < Newcastle_attack and Arsenal_defence < Newcastle_defence) or (Arsenal_fieldown == Newcastle_fieldown and Arsenal_attack < Newcastle_attack and Arsenal_defence < Newcastle_defence) or (Arsenal_fieldown < Newcastle_fieldown and Arsenal_attack < Newcastle_attack and Arsenal_defence >= Newcastle_defence) or (Arsenal_fieldown < Newcastle_fieldown and Arsenal_attack >= Newcastle_attack and Arsenal_defence < Newcastle_defence) or  (Arsenal_fieldown < Newcastle_fieldown and Arsenal_attack < Newcastle_attack and Arsenal_defence < Newcastle_defence):
# #                     print("--------------------------------------------\n{} - {}, 뉴캐슬 승\n--------------------------------------------".format(random.randint(2, 4), random.randint(0, 1)))
# #                     승점 = 승점 + 0
# #             print("[첫] 번째 경기를 무사히 끝냈습니다. 당신의 승점은 {}점 입니다".format(승점))




# # if commandteam == Arsenal:
# #     introduce_powerbalance(Arsenal, Arsenal_attack, Arsenal_defence, Arsenal_fieldown)
# #     print("\n날은 프리미어리그 전통의 강팀으로, 공격, 수비, 중원 모두 우수한 활약을 보입니다.")
# #     Arsenal_Run()
# # elif commandteam == Man_City:
# #     introduce_powerbalance(Man_City, Man_City_attack, Man_City_defence, Man_City_fieldown)
# #     print("\n맨체스터 시티는 세계 최강의 공격진을 필두로 한 강팀으로, 매 경기마다 화끈한 득점력을 선보입니다.")
# # elif commandteam == Man_Utd:
# #     introduce_powerbalance(Man_Utd, Man_Utd_attack, Man_Utd_defence, Man_Utd_fieldown)
# #     print("\n호날두, 루니, 박지성, 베컴 등의 세계적인 스타 선수들이 거쳐간 맨체스터 유나이티드는 전 세계적인 팬덤을 보유한 클럽입니다.")
# # elif commandteam == Liverpool:
# #     introduce_powerbalance(Liverpool, Liverpool_attack, Liverpool_defence, Liverpool_fieldown)
# #     print("\n오랜 침체기를 끝내고 리그 상위권으로 도약한 리버풀은 공격과 수비에서 특히 우수한 클럽입니다.")
# # elif commandteam == Tottenham:
# #     introduce_powerbalance(Tottenham, Tottenham_attack, Tottenham_defence, Tottenham_fieldown)
# #     print("\n북런던의 전통과 역사를 자랑하는 토트넘은 세계적인 한국인 선수 손흥민이 주장을 맡고 있는 상위권 클럽입니다.")
# # elif commandteam == Chelsea:
# #     introduce_powerbalance(Chelsea, Chelsea_attack, Chelsea_defence, Chelsea_fieldown)
# #     print("\n예로부터 철벽 수비로 유명했던 첼시는 최근 젊은 공격수들의 영입으로 예전 PL에서의의 영광을 되찾고 있습니다.")
# # elif commandteam == Wolverhampton:
# #     introduce_powerbalance(Wolverhampton, Wolverhampton_attack, Wolverhampton_defence, Wolverhampton_fieldown)
# #     print("\n한국 국적인 황희찬 선수가 뛰고 있는 울버햄튼 또한 중원 점유율에서 높은 점수를 가져가는 클럽입니다.")
# # elif commandteam == West_Ham:
# #     introduce_powerbalance(West_Ham, West_Ham_attack, West_Ham_defence, West_Ham_fieldown)
# #     print("\n런던의 최고 인기 클럽인 웨스트햄은 최근 보웬과 쿠두스의 활약으로 좋은 폼을 이어나가고 있습니다.")
# # elif commandteam == Newcastle:
# #     introduce_powerbalance(Newcastle, Newcastle_attack, Newcastle_defence, Newcastle_fieldown)
# #     print("\n최근 빈 살만이 뉴캐슬을 인수하면서 최고의 자본력을 등에 업고 급격한 성장을 거듭하며 공격력을 큰 폭으로 향상한 PL의 돌풍입니다.")

# # def random_choice():
# #     PL = [Arsenal, Man_City, Man_Utd, Liverpool, Tottenham, Chelsea, Wolverhampton, West_Ham, Newcastle]
# #     PL_attack = [Arsenal_attack, Man_City_attack, Man_Utd_attack, Liverpool_attack, Tottenham_attack, Chelsea_attack, Wolverhampton_attack, West_Ham_attack, Newcastle_attack]
# #     PL_defence = [Arsenal_defence, Man_City_defence, Man_Utd_defence, Liverpool_defence, Tottenham_defence, Chelsea_defence, Wolverhampton_defence, West_Ham_defence, Newcastle_defence]
# #     PL_fieldown = [Arsenal_fieldown, Man_City_fieldown, Man_Utd_fieldown, Liverpool_fieldown, Tottenham_fieldown, Chelsea_fieldown, Wolverhampton_fieldown, West_Ham_fieldown, Newcastle_fieldown]
# #     PL_Random = random.choice(PL)
# #     PL_attack_Random = random.choice(PL_attack)
# #     PL_defence_Random = random.choice(PL_defence)
# #     PL_fieldown_Random = random.choice(PL_fieldown)
# #     print(PL_Random, "은 투자한 결과 다음과 같이 전력이 보강되었습니다:")
# #     print("공격진 : ", PL_attack_Random)
# #     print("수비진 : ", PL_defence_Random)
# #     print("중원 지배력", PL_fieldown_Random)

# # # def Arsenal_Run():
# # #     print("Pre-Matchweek\n투자할 부분을 선택하세요 : 트레이닝, 시설확충, 구단홍보")
# # #     c_arsenal = input("선택 : ")
# # #     if c_arsenal == "트레이닝":
# # #         print("트레이닝을 선택하셨습니다. 모든 능력치 +1")
# # #         Arsenal_attack + 1
# # #         Arsenal_defence + 1
# # #         Arsenal_fieldown + 1
# # #         print("다른 팀의 전략을 참고하시겠습니까?")
# # #         a_arsenal = input("Y/N")
# # #         if a_arsenal == "Y":
# # #             random_choice()

# # # -----------------------------------------------------------------------------------------------------------------------------------------------------

# # # 2024-05-14 1차 수정
# # # import random
# # # import math
# # # import signal

# # # money = 100
# # # commandteam = 0
# # # Arsenal = "아스날"
# # # Arsenal_attack = 8
# # # Arsenal_defence = 8
# # # Arsenal_fieldown = 9
# # # Man_City = "맨시티"
# # # Man_City_attack = 10
# # # Man_City_defence = 7
# # # Man_City_fieldown = 7
# # # Man_Utd = "맨유"
# # # Man_Utd_attack = 5
# # # Man_Utd_defence = 7
# # # Man_Utd_fieldown = 8
# # # Liverpool = "리버풀"
# # # Liverpool_attack = 8
# # # Liverpool_defence = 9
# # # Liverpool_fieldown = 6
# # # Tottenham = "토트넘"
# # # Tottenham_attack = 7
# # # Tottenham_defence = 5
# # # Tottenham_fieldown = 9
# # # Chelsea = "첼시"
# # # Chelsea_attack = 6
# # # Chelsea_defence = 9
# # # Chelsea_fieldown = 8
# # # Wolverhampton = "울버햄튼"
# # # Wolverhampton_attack = 6
# # # Wolverhampton_defence = 6
# # # Wolverhampton_fieldown = 8
# # # West_Ham = "웨스트햄"
# # # West_Ham_attack = 5
# # # West_Ham_defence = 7
# # # West_Ham_fieldown = 6
# # # Newcastle = "뉴캐슬"
# # # Newcastle_attack = 8
# # # Newcastle_defence = 5
# # # Newcastle_fieldown = 5
# # # Arsenallist = [Arsenal_attack, Arsenal_defence, Arsenal_fieldown]
# # # Man_Citylist = [Man_City_attack, Man_City_defence, Man_City_fieldown]
# # # Man_Utdlist = [Man_Utd_attack, Man_Utd_defence, Man_Utd_fieldown]
# # # Liverpoollist = [Liverpool_attack, Liverpool_defence, Liverpool_fieldown]
# # # Tottenhamlist = [Tottenham_attack, Tottenham_defence, Tottenham_fieldown]
# # # Chelsealist = [Chelsea_attack, Chelsea_defence, Chelsea_fieldown]
# # # Wolverhamptonlist = [Wolverhampton_attack, Wolverhampton_defence, Wolverhampton_fieldown]
# # # West_Hamlist = [West_Ham_attack, West_Ham_defence, West_Ham_fieldown]
# # # Newcastlelist = [Newcastle_attack, Newcastle_defence, Newcastle_fieldown]

# # # print("PL에서 챔스가기!\n---------------------------------------------\n이제부터 당신은 한 팀의 감독입니다. PL 팀 중 하나를 선택하세요. 팀 변경의 기회는 없으니 신중히 고르세요!\n(용량 문제로 모든 팀들을 넣지 못한 점 죄송합니다!!)\n--------------------------------------------")
# # # print("[아스날, 맨시티, 맨유, 리버풀, 토트넘, 첼시, 울버햄튼, 웨스트햄, 뉴캐슬]")
# # # team = input("선택한 팀 : ")
# # # if team == "아스날":
# # #     commandteam = Arsenal
# # # elif team == "맨시티":
# # #     commandteam = Man_City
# # # elif team == "맨유":
# # #     commandteam = Man_Utd
# # # elif team == "리버풀":
# # #     commandteam = Liverpool
# # # elif team == "토트넘":
# # #     commandteam = Tottenham
# # # elif team == "첼시":
# # #     commandteam = Chelsea
# # # elif team == "울버햄튼":
# # #     commandteam = Wolverhampton
# # # elif team == "웨스트햄":
# # #     commandteam = West_Ham
# # # elif team == "뉴캐슬":
# # #     commandteam = Newcastle
# # # else:
# # #     print("양식에 맞춰 다시 작성해주세요!!")
# # #     exit()
# # # print("--------------------------------------------")
# # # print(team, "을 선택하셨습니다.\n")

# # # def introduce_powerbalance(a, b, c, d):
# # #     print("{}의\n공격력은 {}입니다.\n수비력은 {}입니다.\n중원 지배력은 {}입니다.".format(a, b, c, d))

# # # def random_choice():
# # #     PL = [Arsenal, Man_City, Man_Utd, Liverpool, Tottenham, Chelsea, Wolverhampton, West_Ham, Newcastle]
# # #     PL_attack = [Arsenal_attack, Man_City_attack, Man_Utd_attack, Liverpool_attack, Tottenham_attack, Chelsea_attack, Wolverhampton_attack, West_Ham_attack, Newcastle_attack]
# # #     PL_defence = [Arsenal_defence, Man_City_defence, Man_Utd_defence, Liverpool_defence, Tottenham_defence, Chelsea_defence, Wolverhampton_defence, West_Ham_defence, Newcastle_defence]
# # #     PL_fieldown = [Arsenal_fieldown, Man_City_fieldown, Man_Utd_fieldown, Liverpool_fieldown, Tottenham_fieldown, Chelsea_fieldown, Wolverhampton_fieldown, West_Ham_fieldown, Newcastle_fieldown]
# # #     PL_Random = random.choice(PL)
# # #     PL_attack_Random = random.choice(PL_attack)
# # #     if PL_Random == Arsenal:
# # #         a = random.randint(-3, 3)
# # #         b = random.randint(-3, 3)
# # #         c = random.randint(-3, 3)
# # #         Arsenal_attack + a
# # #         Arsenal_defence + b
# # #         Arsenal_fieldown + c
# # #         print("아스날은 투자한 결과 다음과 같이 전력이 보강되었습니다:")
# # #         print("공격진 : ", Arsenal_attack)
# # #         print("수비진 : ", Arsenal_defence)
# # #         print("중원 지배력", Arsenal_fieldown)
# # #     elif PL_Random == Man_City:
# # #         a = random.randint(-3, 3)
# # #         b = random.randint(-3, 3)
# # #         c = random.randint(-3, 3)
# # #         Man_City_attack + a
# # #         Man_City_defence + b
# # #         Man_City_fieldown + c
# # #         print("맨시티는 투자한 결과 다음과 같이 전력이 보강되었습니다:")
# # #         print("공격진 : ", Man_City_attack)
# # #         print("수비진 : ", Man_City_defence)
# # #         print("중원 지배력", Man_City_fieldown)
# # #     elif PL_Random == Liverpool:
# # #         a = random.randint(-3, 3)
# # #         b = random.randint(-3, 3)
# # #         c = random.randint(-3, 3)
# # #         Liverpool_attack + a
# # #         Liverpool_defence + b
# # #         Liverpool_fieldown + c
# # #         print("리버풀은 투자한 결과 다음과 같이 전력이 보강되었습니다:")
# # #         print("공격진 : ", Liverpool_attack)
# # #         print("수비진 : ", Liverpool_defence)
# # #         print("중원 지배력", Liverpool_fieldown)
# # #     elif PL_Random == Tottenham:
# # #         a = random.randint(-3, 3)
# # #         b = random.randint(-3, 3)
# # #         c = random.randint(-3, 3)
# # #         Tottenham_attack + a
# # #         Tottenham_defence + b
# # #         Tottenham_fieldown + c
# # #         print("토트넘은 투자한 결과 다음과 같이 전력이 보강되었습니다:")
# # #         print("공격진 : ", Tottenham_attack)
# # #         print("수비진 : ", Tottenham_defence)
# # #         print("중원 지배력", Tottenham_fieldown)
# # #     elif PL_Random == Chelsea:
# # #         a = random.randint(-3, 3)
# # #         b = random.randint(-3, 3)
# # #         c = random.randint(-3, 3)
# # #         Chelsea_attack + a
# # #         Chelsea_defence + b
# # #         Chelsea_fieldown + c
# # #         print("첼시는 투자한 결과 다음과 같이 전력이 보강되었습니다:")
# # #         print("공격진 : ", Chelsea_attack)
# # #         print("수비진 : ", Chelsea_defence)
# # #         print("중원 지배력", Chelsea_fieldown)
# # #     elif PL_Random == Wolverhampton:
# # #         a = random.randint(-3, 3)
# # #         b = random.randint(-3, 3)
# # #         c = random.randint(-3, 3)
# # #         Wolverhampton_attack + a
# # #         Wolverhampton_defence + b
# # #         Wolverhampton_fieldown + c
# # #         print("첼시는 투자한 결과 다음과 같이 전력이 보강되었습니다:")
# # #         print("공격진 : ", Wolverhampton_attack)
# # #         print("수비진 : ", Wolverhampton_defence)
# # #         print("중원 지배력", Wolverhampton_fieldown)
# # #     elif PL_Random == West_Ham:
# # #         a = random.randint(-3, 3)
# # #         b = random.randint(-3, 3)
# # #         c = random.randint(-3, 3)
# # #         West_Ham_attack + a
# # #         West_Ham_defence + b
# # #         West_Ham_fieldown + c
# # #         print("웨스트햄은 투자한 결과 다음과 같이 전력이 보강되었습니다:")
# # #         print("공격진 : ", West_Ham_attack)
# # #         print("수비진 : ", West_Ham_defence)
# # #         print("중원 지배력", West_Ham_fieldown)
# # #     elif PL_Random == Newcastle:
# # #         a = random.randint(-3, 3)
# # #         b = random.randint(-3, 3)
# # #         c = random.randint(-3, 3)
# # #         Newcastle_attack + a
# # #         Newcastle_defence + b
# # #         Newcastle_fieldown + c
# # #         print("뉴캐슬은 투자한 결과 다음과 같이 전력이 보강되었습니다:")
# # #         print("공격진 : ", Newcastle_attack)
# # #         print("수비진 : ", Newcastle_defence)
# # #         print("중원 지배력", Newcastle_fieldown)


# # # def Arsenal_Run():
# # #     print("Pre-Matchweek\n투자할 부분을 선택하세요 : 트레이닝, 시설확충, 구단홍보")
# # #     c_arsenal = input("선택 : ")
# # #     if c_arsenal == "트레이닝":
# # #         print("트레이닝을 선택하셨습니다. 모든 능력치 +1")
# # #         Arsenal_attack + 1
# # #         Arsenal_defence + 1
# # #         Arsenal_fieldown + 1
# # #         print("다른 팀의 전략을 참고하시겠습니까?")
# # #         a_arsenal = input("Y/N : ")
# # #         if a_arsenal == "Y":
# # #             random_choice()



# # # if commandteam == Arsenal:
# # #     introduce_powerbalance(Arsenal, Arsenal_attack, Arsenal_defence, Arsenal_fieldown)
# # #     print("\n날은 프리미어리그 전통의 강팀으로, 공격, 수비, 중원 모두 우수한 활약을 보입니다.")
# # #     Arsenal_Run()
# # # elif commandteam == Man_City:
# # #     introduce_powerbalance(Man_City, Man_City_attack, Man_City_defence, Man_City_fieldown)
# # #     print("\n맨체스터 시티는 세계 최강의 공격진을 필두로 한 강팀으로, 매 경기마다 화끈한 득점력을 선보입니다.")
# # # elif commandteam == Man_Utd:
# # #     introduce_powerbalance(Man_Utd, Man_Utd_attack, Man_Utd_defence, Man_Utd_fieldown)
# # #     print("\n호날두, 루니, 박지성, 베컴 등의 세계적인 스타 선수들이 거쳐간 맨체스터 유나이티드는 전 세계적인 팬덤을 보유한 클럽입니다.")
# # # elif commandteam == Liverpool:
# # #     introduce_powerbalance(Liverpool, Liverpool_attack, Liverpool_defence, Liverpool_fieldown)
# # #     print("\n오랜 침체기를 끝내고 리그 상위권으로 도약한 리버풀은 공격과 수비에서 특히 우수한 클럽입니다.")
# # # elif commandteam == Tottenham:
# # #     introduce_powerbalance(Tottenham, Tottenham_attack, Tottenham_defence, Tottenham_fieldown)
# # #     print("\n북런던의 전통과 역사를 자랑하는 토트넘은 세계적인 한국인 선수 손흥민이 주장을 맡고 있는 상위권 클럽입니다.")
# # # elif commandteam == Chelsea:
# # #     introduce_powerbalance(Chelsea, Chelsea_attack, Chelsea_defence, Chelsea_fieldown)
# # #     print("\n예로부터 철벽 수비로 유명했던 첼시는 최근 젊은 공격수들의 영입으로 예전 PL에서의의 영광을 되찾고 있습니다.")
# # # elif commandteam == Wolverhampton:
# # #     introduce_powerbalance(Wolverhampton, Wolverhampton_attack, Wolverhampton_defence, Wolverhampton_fieldown)
# # #     print("\n한국 국적인 황희찬 선수가 뛰고 있는 울버햄튼 또한 중원 점유율에서 높은 점수를 가져가는 클럽입니다.")
# # # elif commandteam == West_Ham:
# # #     introduce_powerbalance(West_Ham, West_Ham_attack, West_Ham_defence, West_Ham_fieldown)
# # #     print("\n런던의 최고 인기 클럽인 웨스트햄은 최근 보웬과 쿠두스의 활약으로 좋은 폼을 이어나가고 있습니다.")
# # # elif commandteam == Newcastle:
# # #     introduce_powerbalance(Newcastle, Newcastle_attack, Newcastle_defence, Newcastle_fieldown)
# # #     print("\n최근 빈 살만이 뉴캐슬을 인수하면서 최고의 자본력을 등에 업고 급격한 성장을 거듭하며 공격력을 큰 폭으로 향상한 PL의 돌풍입니다.")

# # # def random_choice():
# # #     PL = [Arsenal, Man_City, Man_Utd, Liverpool, Tottenham, Chelsea, Wolverhampton, West_Ham, Newcastle]
# # #     PL_attack = [Arsenal_attack, Man_City_attack, Man_Utd_attack, Liverpool_attack, Tottenham_attack, Chelsea_attack, Wolverhampton_attack, West_Ham_attack, Newcastle_attack]
# # #     PL_defence = [Arsenal_defence, Man_City_defence, Man_Utd_defence, Liverpool_defence, Tottenham_defence, Chelsea_defence, Wolverhampton_defence, West_Ham_defence, Newcastle_defence]
# # #     PL_fieldown = [Arsenal_fieldown, Man_City_fieldown, Man_Utd_fieldown, Liverpool_fieldown, Tottenham_fieldown, Chelsea_fieldown, Wolverhampton_fieldown, West_Ham_fieldown, Newcastle_fieldown]
# # #     PL_Random = random.choice(PL)
# # #     PL_attack_Random = random.choice(PL_attack)
# # #     PL_defence_Random = random.choice(PL_defence)
# # #     PL_fieldown_Random = random.choice(PL_fieldown)
# # #     print(PL_Random, "은 투자한 결과 다음과 같이 전력이 보강되었습니다:")
# # #     print("공격진 : ", PL_attack_Random)
# # #     print("수비진 : ", PL_defence_Random)
# # #     print("중원 지배력", PL_fieldown_Random)

# # # def Arsenal_Run():
# # #     print("Pre-Matchweek\n투자할 부분을 선택하세요 : 트레이닝, 시설확충, 구단홍보")
# # #     c_arsenal = input("선택 : ")
# # #     if c_arsenal == "트레이닝":
# # #         print("트레이닝을 선택하셨습니다. 모든 능력치 +1")
# # #         Arsenal_attack + 1
# # #         Arsenal_defence + 1
# # #         Arsenal_fieldown + 1
# # #         print("다른 팀의 전략을 참고하시겠습니까?")
# # #         a_arsenal = input("Y/N")
# # #         if a_arsenal == "Y":
# # #             random_choice()
