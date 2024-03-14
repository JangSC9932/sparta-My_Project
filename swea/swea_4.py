# t = int(input())

# for i in range(1,t+1):
text = "SAMSUNGSAMSUNGSAMSUNGSAMSUNGSA"


def find_pattern(string):
    for i in range(len(string)):
        string = string[:len(string) - 1]
        print(f'start {string}')
        replace = ""
        for char in text:
            replace += char
            print(replace)
            if replace == string:
                continue
            elif len(string.replace(replace, "")) == 0:
                return print(f'# {len(replace)}')


find_pattern(text)
# 10
# KOREAKOREAKOREAKOREAKOREAKOREA
# SAMSUNGSAMSUNGSAMSUNGSAMSUNGSA
# GALAXYGALAXYGALAXYGALAXYGALAXY
# EXOEXOEXOEXOEXOEXOEXOEXOEXOEXO
# B1A4B1A4B1A4B1A4B1A4B1A4B1A4B1
# APINKAPINKAPINKAPINKAPINKAPINK
# BLACKPINKBLACKPINKBLACKPINKBLA
# TWICETWICETWICETWICETWICETWICE
# REDVELVETREDVELVETREDVELVETRED
# ABCABCABCABCABCABCABCABCABCABC

# 1 5
# 2 7
# 3 6
# 4 3
# 5 4
# 6 5
# 7 9
# 8 5
# 9 9
# 10 3
