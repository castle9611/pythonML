### 1. 递归过程

# def f(n):
#     print(n,'------递------')
#     if n>0:
#         f(n-1)    ## 它以下的代码暂时不会执行，被暂停阻塞，会向下开辟新的内存积压（栈）这些指令，等到阻塞放开，指令逐个执行（自上而下）
#     print(n,'------归------')
# f(2)



### 2. 汉诺塔问题

# i = []
# def hanoi(n,x,y,z):
#     if n==1:
#         print(x,'-->',z)         ####直接从x移动到z
#         i.append(1)
#     elif n>1:
#         hanoi(n-1,x,z,y)         ####借助z将x移动到y   
#         print(x,'-->',z)
#         i.append(1)
#         hanoi(n-1,y,x,z)         ####借助x将y移动到z
# while True:
#     n=input('请输入汉诺塔的层数：')
#     if n.isdigit():
#         if int(n) > 0:
#             hanoi(int(n),'X','Y','Z')
#             print(len(i))
#             break
#     else:
#         print('请重新输入')



# ### 3. 阶乘
# def factorial(num):
#     if num == 1 :
#         return 1
#     else :
#         return num*factorial(num-1) 
# while True:
#     n=input('请输入想要完成几的阶乘：')
#     if n.isdigit():
#         if int(n) > 0:
#             print(factorial(int(n)))
#             break
#     else:
#         print('请重新输入')



# ### 4. 斐波那挈
# def fibo(n):
#     if n == 1 :
#         return 1
#     if n == 2 :
#         return 1
#     else :
#         element = fibo(n-2) + fibo(n-1)
#         return element
# while True:
#     n=input('请输入想得到的斐波那挈数列长度：')
#     if n.isdigit():
#         if int(n) > 0:
#             print(fibo(int(n)))
#             j=[]
#             for i in range(1,int(n)+1):
#                 j.append(fibo(i))
#             print(j)
#             break
#     else:
#         print('请重新输入')



### 