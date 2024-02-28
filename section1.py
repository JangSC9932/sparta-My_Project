from random import randint

# 점수 기록 목록
play_score_list = []


# 기록 한 점수 표출 데코레이터
def score_list(func):
    def wrapper():
        # 기록한 점수가 있을시에만 표출
        if play_score_list:
            print("이전 게임 플레이어 최고 시도 횟수 :" + str(max(play_score_list)))
            print("이전 게임 플레이어 최저 시도 횟수 :" + str(min(play_score_list)))
        # 함수 호출
        func()
    return wrapper


@score_list
def up_and_down():
    # 랜덤 숫자 설정
    random_number = randint(1, 100)  # randint(1, 100) - 1 이상 100 이하
    # 시도 횟수
    play_count = 0

    while True:
        try:
            # 사용자 입력 값 받기
            input_number = int(input("숫자를 입력하세요:"))
            # 시도 추가
            play_count += 1
            # 1 ~ 100의 범위 체크
            if input_number in range(1, 101):  # range(1, 101) - 1 이상 101 미만
                # 랜덤 숫자 체크
                if input_number != random_number:
                    if input_number > random_number:
                        print("DOWN!")  # 랜덤숫자가 작을때
                    if input_number < random_number:
                        print("UP!")  # 랜덤숫자가 클때
                else:
                    print(f"맞았습니다 정답:{random_number}")
                    print(f"시도횟수 :{play_count}")
                    while True:
                        input_replay = input("다시 하시겠습니까? (y/n):")
                        # 대소문자 상관없이 비교
                        if input_replay.casefold() == "y":
                            # y 이면 재시작
                            play_score_list.append(play_count)
                            up_and_down()
                            # point. break 안하면 중첩이됨
                            break
                        elif input_replay.casefold() == "n":
                            # n 이면 종료 및 break
                            print("게임을 종료합니다.")
                            break
                        else:
                            print("제대로 입력해주세요. (y/n)")
                    break
            else:
                print("유효한 범위 내의 숫자를 입력하세요.( 1 ~ 100 )")
        except ValueError:
            print("정수만 입력해주세요!")
        except TypeError:
            print("숫자만 입력해주세요!")


up_and_down()
