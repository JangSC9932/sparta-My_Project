import random


def rock_paper_scissors():

    player_piece_list = ['가위', '바위', '보']       # 사용자
    computer_piece_list = ['가위', '바위', '보']     # 컴퓨터
    player_score_list = [0, 0, 0]                 # 승/무/패 점수
    is_replay = True                              # 재시작 여부

    while True:
        player_piece = input(f"{player_piece_list} 중 하나를 선택하세요:")
        if player_piece in player_piece_list:
            # 컴퓨터가 리스트에서 랜덤 선택
            computer_piece = random.choice(computer_piece_list)
            if player_piece == computer_piece:
                # 비겼을시, 무조건 재시작
                print(f"비겼습니다. 컴퓨터 : {computer_piece}")
                player_score_list[1] += 1
            else:
                # 경우에 따라 승패 결정
                if player_piece == '가위':
                    if computer_piece == '보':
                        print(f"이겼습니다. 컴퓨터 : {computer_piece}")
                        player_score_list[0] += 1
                    else:
                        print(f"졌습니다. 컴퓨터 : {computer_piece}")
                        player_score_list[2] += 1
                elif player_piece == '바위':
                    if computer_piece == '가위':
                        print(f"이겼습니다. 컴퓨터 : {computer_piece}")
                        player_score_list[0] += 1
                    else:
                        print(f"졌습니다. 컴퓨터 : {computer_piece}")
                        player_score_list[2] += 1
                else:
                    if computer_piece == '바위':
                        print(f"이겼습니다. 컴퓨터 : {computer_piece}")
                        player_score_list[0] += 1
                    else:
                        print(f"졌습니다. 컴퓨터 : {computer_piece}")
                        player_score_list[2] += 1
                # 다시시작 질문 반복문
                while True:
                    input_replay = input("다시 하시겠습니까? (y/n):")
                    # 대소문자 상관없이 비교
                    if input_replay.casefold() == "y":
                        is_replay = True
                        break
                    elif input_replay.casefold() == "n":
                        is_replay = False
                        print("게임을 종료합니다.")
                        print(f"승: {player_score_list[0]} 패: {player_score_list[2]} 무: {player_score_list[1]}")
                        break
                    else:
                        print("다시 입력해주세요. (y/n)")

                if is_replay:
                    continue    # 재시작일시 다시 반복
                else:
                    break       # 아니면 break

        else:
            print("유효한 입력이 아닙니다.")


rock_paper_scissors()