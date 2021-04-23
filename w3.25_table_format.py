dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
for index in dict:
    i=0
    while i<len(dict[index]):
        j=0
        while j<len(dict[index]):
            a=(dict[index][i])
            j+=1
        print(a)
        i+=1
    print( )

        

    # print(dict[i])
    # for j in range(0,len(dict[i])):
    #     pass
    # print(dict[i])
    # # print(a)


# C1 C2 C3                                                                                                      
# 1 5 9                                                                                                         
# 2 6 10                                                                                                        
# 3 7 11