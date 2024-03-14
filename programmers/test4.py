def solution(answers):
    a = [1, 2, 3, 4, 5]  # 수포자 1
    b = [2, 1, 2, 3, 2, 4, 2, 5]  # 수포자 2
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  # 수포자 3

    score = [0, 0, 0]  # 점수 저장

    result = []
    for i, ans in enumerate(answers):
        # cf. 리스트를 반복해서 추출 할때 유용한 연산식 중요
        # 수포자 리스트를 answers 수만큼 무한 반복함
        if a[i % len(a)] == ans:
            score[0] += 1
        if b[i % len(b)] == ans:
            score[1] += 1
        if c[i % len(c)] == ans:
            score[2] += 1
    print(score)
    print(max(score))

    # 저장한 스코어 최개값이 어느 수포자의 것인지 확인
    for i, rank in enumerate(score):
        if max(score) == rank:
            result.append(i + 1)
    print(result)


solution([1,3,2,4,2])
