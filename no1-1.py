
N, M = map(int, input().split())
A = [int(a) for a in input().split()]

index = 0
tmp, max_sum, cnt = 0, 0, 0
diff_list = []
#差のリストを作る
for i in range(N):
    
    if(i == 0):
        for j in range(M):
            max_sum += A[j]
        present_sum = max_sum
        index = i+1
       
    elif(i < N-M+1):
        diff = - A[i-1] + A[i+M-1]
        present_sum += diff

        if(max_sum < present_sum):
          index = i+1
          max_sum = present_sum
        
      


print(str(max_sum) + ' ' + str(index))




        

    

            
        



    

    

