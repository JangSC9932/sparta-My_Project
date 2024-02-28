import hashlib


# member 클래스
class Member:

    def __init__(self, name, user_name, passwd):
        self.name = name
        self.user_name = user_name
        self.passwd = passwd

    def display(self):
        print(f" name : {self.name} | user_name : {self.user_name}")


# post 클래스
class Post:

    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def display_post(self):
        print(f" 제목 : {self.title} | 내용 : {self.content} | 작성자 : {self.author}")


members = []
posts = []

# 기본 member 인스턴스 생성
member1 = Member(name="장석천", user_name="user1", passwd=hashlib.sha256("1234".encode("utf-8")).hexdigest())
members.append(member1)
member2 = Member(name="장석만", user_name="user2", passwd=hashlib.sha256("2345".encode("utf-8")).hexdigest())
members.append(member2)
member3 = Member(name="장석억", user_name="user3", passwd=hashlib.sha256("6789".encode("utf-8")).hexdigest())
members.append(member3)


# member 등록 함수
def join_member():
    input_name = input("[메인으로 : *] \n이름을 입력하세요 :")
    if input_name == "*":       # "*"입력시 main 으로가는 함수 호출
        main()
        return
    input_user_name = input("[메인으로 : *] \nUSER_NAME을 입력하세요 :")
    if input_name == "*":       # "*"입력시 main 으로가는 함수 호출
        main()
        return
    input_passwd = input("[메인으로 : *] \nPASSWORD를 입력하세요 :")
    if input_passwd == "*":     # "*"입력시 main 으로가는 함수 호출
        main()
        return

    while True:
        # 등록계정 정보 확인
        input_check = input(
            f"[메인으로 : *] \n입력하신 내용이 이름:{input_name} / USER_NAME:{input_user_name} / PASSWD:{input_passwd}가 맞으면 1번 틀리면 "
            f"2번을 눌러주세요 :")
        # 확인 결과 조건
        if input_check == "1":
            # 확인시 비밀번호 암호화하고 members에 추가 후 main 호출
            members.append(Member(name=input_name, user_name=input_user_name,
                                  passwd=hashlib.sha256(input_passwd.encode("UTF-8")).hexdigest()))
            print("정상적으로 추가되었습니다.")
            main()
            return
        elif input_check == "2":
            # 틀렸을시 다시 join_member 호출 ( 재귀 )
            join_member()
            return
        elif input_check == "*":
            # main 호출
            main()
            return
        else:
            print("다시 입력해주세요.")
            continue


# member 목록 화면 함수
def member_display(user_name=""):           # 기본값 공백으로 호출
    # members 목록 추출
    for member in members:
        if user_name in member.user_name:
            # user_name에 해당하는 인스턴스의 정보를 보여주는 클래스 함수 호출
            member.display()
    input_search = input("[메인으로 : *] \n찾으시는 USER_NAME을 입력해주세요 :")
    if input_search == "*":
        main()
        return
    else:
        # 목록 화면 함수 호출 ( user_name 입력시 해당하는 목록만 나옴 )
        member_display(input_search)
        return


# post 등록 함수
def post_insert():
    input_title = input("[메인으로 : *] \n제목을 입력하세요 :")
    if input_title == "*":
        main()
        return
    input_content = input("[메인으로 : *] \n내용을 입력하세요 :")
    if input_content == "*":
        main()
        return
    input_user_name = input("[메인으로 : *] \nUSER_NAME을 입력하세요 :")
    if input_user_name == "*":
        main()
        return
    input_passwd = input("[메인으로 : *] \nUSER_NAME의 PASSWORD를 입력하세요 :")
    if input_passwd == "*":
        main()
        return
    
    # 비밀번호 체크
    member_check = False
    for member in members:
        # 암호화된 비밀번호를 비교하기 위해서 입력한 값도 암호화
        if (member.user_name == input_user_name
                and member.passwd == hashlib.sha256(input_passwd.encode("UTF-8")).hexdigest()):
            member_check = True

    if member_check:
        posts.append(Post(title=input_title, content=input_content, author=input_user_name))
        print("정상적으로 등록되었습니다.")
        main()
        return
    else:
        print("등록된 계정이 없습니다.")
        post_insert()
        return


# post 목록 화면 함수
def post_display(user_name=""):
    for post in posts:
        if user_name in post.author:
            post.display_post()
    input_search = input("[메인으로 : *] \n찾으시는 USER_NAME을 입력해주세요 :")
    if input_search == "*":
        main()
        return
    else:
        post_display(input_search)
        return


# main 함수
def main():
    while True:
        input_text = input("[MEMBER 등록 : JOIN][MEMBER 목록 : MEMBER][POST 등록 : INSERT][POST 목록 : POST][종료 : EXIT]\n"
                           "명령어를 입력해주세요 :")
        if input_text.casefold() == "join":
            join_member()
            break
        elif input_text.casefold() == "member":
            member_display()
            break
        elif input_text.casefold() == "insert":
            post_insert()
            break
        elif input_text.casefold() == "post":
            post_display()
            break
        elif input_text.casefold() == "exit":
            print("프로그램을 종료합니다.")
            break
        else:
            print("다시 입력해주세요.")
            continue


main()
