def ConsecutiveOnes(N):
  #this is default OUTPUT. You can change it.

  result = 0
  number = N
  binary = ""
  num = N-1
  #write your Logic here:

  while num >= 0:
#    print("number = %d" % (number))
#    print("num = %d" % (num))
    if 2**num <= number:
#      print("2^%d = %d" % (num, 2**num))
      binary += "1"
      number -= 2**num
    elif binary != "":
      binary += "0"
    num -= 1
    thisCount = 0
#    print(binary)

  for letter in binary:
#    print(letter)
    if letter == "1":
      thisCount += 1
      if thisCount > result:
        result = thisCount
    else:
      if thisCount > result:
        result = thisCount
      thisCount = 0

  return result

#INPUT [uncomment & modify if required]

# N = int(input())

#OUTPUT [uncomment & modify if required]

# print(ConsecutiveOnes(N))

def MaxSubmatrix(N,M,A):
  #this is default OUTPUT. You can change it.
  result = 1

  start_row = 0
  start_col = 0
  end_row = 0
  end_col = 0

  while(True):
    
    B = [[A[i][j] for j in range(start_row, end_row+1)] for i in range(start_col, end_col+1)]
        
    subArray_len = len(B) * len(B[0])
    break2 = False
    allSameNumber = True

    for i in range(0, len(B)):
      for j in range(0, len(B[0])):
        if i == 0 and j == 0:
          check_num = B[i][j]
        elif B[i][j] == check_num:
          continue
        else:
          allSameNumber = False
          break2 = True
          break
      if break2 == True:
        break2 = False
        break
        
    if allSameNumber == True and subArray_len > result:
      result = subArray_len

    if start_row == N-1 and start_col == M-1:
      break
    elif end_row == N-1 and end_col == M-1:
      if start_row < N-1:
        start_row += 1
      elif start_col < M-1:
        start_row = 0
        start_col += 1
      end_row = start_row
      end_col = start_col
    elif end_row < N-1:
      end_row += 1
    elif end_col < M-1:
      end_row = 0
      end_col += 1

    for i in range(0, len(B)):
      print(B[i])

    print()

  #write your Logic here:

  # [1 0 0]
  # [0 0 0]
  # [1 1 1]

  # for i in range(N):
  #   for j in range(M):
  #     while(True):
  #       subset = i*j

  return result

#INPUT [uncomment & modify if required]
# N=int(input())
# M=int(input())

# A=[[0 for j in range(M)] for i in range(N)]

# temp=[]

# for i in range(N):
#   temp=input().split()
#   for j in range(M):
#     A[i][j]=temp[j]

N = 3
M = 3
A = [["1","0","0"],["0","0","0"],["1","1","1"]]

print(MaxSubmatrix(N,M,A))