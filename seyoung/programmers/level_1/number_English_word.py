def solution(s):
    number = [["zero","0"],["one","1"],["two","2"],["three","3"],
             ["four","4"],["five","5"],["six","6"],["seven","7"],
             ["eight","8"],["nine","9"]]
    for x in number:
        s = s.replace(x[0],x[1])
    return int(s)