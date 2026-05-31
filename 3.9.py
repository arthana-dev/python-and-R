A=[1,2,3]
B=[4,5,6]

C=A.copy()
C.append(B)
print(C)

D=A.copy()
D.extend(B)
print(D)

E=A+B
print(E)
