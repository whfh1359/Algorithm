# def ans():
#     strS = input()
#     strP = input()
#     l = len(strP)
#     i =0 

#     while i <= len(strS)-l:
#         if strS[i] == strP[0]:    
#             for j in range(l) :
#                 if strS[i] == strP[j]:                   
#                     i= i+1
#                     if j == l-1:
#                         return 1                     
#                 else:
#                     break;
#         else :
#             i +=1
#     return 0

# print(ans())

def getPi(str):
    pi = [0 for i in range(len(str))]
    for i in range(len(str)):
        j = 0
        # print(str[-j])
        while str[j] == str[-j-1] and j < i/2 :
            j+=1
        pi[i]=j
    return pi

def KMPmatch(str1,str2):
    pi = getPi(str2)
    j = 0
    i = 0
    print(str)
    print(pi)

    while i <= (len(str1)-len(str2)):
        if str[i] == str2[j] :
            i+=1
            j+=1
        elif j==0:
            i +=1
        else :
            j =pi[j]
        if j == len(str2) :
            print(1)
            break
    print(0)
str1 = input()
str2 = input()
KMPmatch(str1,str2)
        


    # for i in range(len(str1)) :
    #     if str[i] == str2[j] :
    #         j+=1
    #     else : 
            
         





