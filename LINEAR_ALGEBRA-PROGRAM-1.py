import numpy as ak
r=input("no.of Rows=")
c=input("no.of columns=")
m=[]
for i in range(r):
	m.append([0]*c)
for j in range(r):
	for k in range(c):
		print("enter the elements in matrix=",[j+1,k+1])
		m[j][k]=int(input())
print("The Matrix is=")
print(ak.matrix(m))
print("	choose the operation which you want to perform"
	"\n\t\t\t0.EXIT(){no operation perform}"
	"\n\t\t\t1.Determinant"
	"\n\t\t\t2.TRANSPOSE"
	"\n\t\t\t3.INVERSE"
	"\n\t\t\t4.EIGEN VALUES"
	"\n\t\t\t5.TRACE"
	"\n\t\t\t6.MATRIX RAISED TO POWER"
	"\n\t\t\t7.NORM"
	"\n\t\t\t8.RANK OF MATRIX"
	"\n\t\t\t9.PSEUDO INVERSE"
	"\n\t\t\t10.MAXIMUM AND MINIMIM OF MATRIX")
while True:
	d=input("\nENTER THE OPERATION=")
	if d==1:
		if r==c:
			print("\nDETERMINANT OF MATRIX IS="),
			print(ak.linalg.det(m))
		else:
			print("\nPLEASE ENTER SQUARE MATRIX")
	elif d==2:
		print("\nTRANSPOSE OF MATRIX IS=")
		print(ak.transpose(m))
	elif d==3:
		if r==c:
			print("\nINVERSE MATRIX IS=")
			print(ak.linalg.inv(m))
		else:
			print("\nPLEASE ENTER SQUARE MATRIX")
	elif d==4:
		if r==c:
			print("\nEIGEN VALUES=")
			print(ak.linalg.eigvals(m))
		else:
			print("\nPLEASE ENTER SQUARE MATRIX")
	elif d==5:
		if r==c:
			print("\nTRACE OF MATRIX IS="),
			print(ak.trace(m))
		else:
			print("\nPLEASE ENTER SQUARE MATRIX")
	elif d==6:
		if r==c:
			p=input("ENTER POWER=")
			print("\nTHE RESULT MATRIX IS=")
			print(ak.linalg.matrix_power(m,p))
		else:
			print("\nPLEASE ENTER SQUARE MATRIX")
	elif d==7:
		print("\nNORM OF MATRIX IS=")
		print(ak.linalg.norm(m))
	elif d==8:
		 print("\nRANK OF THE GIVEN MATRIX IS=")
		 print(ak.linalg.matrix_rank(m))
	elif d==9:
		print("\nPSEUDO INVERSE OF MATRIX IS=")
		print(ak.linalg.pinv(m))
	elif d==10:
			print("MAXIMUM IN MATRIX=")
			print(ak.max(m))
			print("MINIMUM IN MATRIX=")
			print(ak.min(m))
	elif(d==0):
		print("\nPROGRAM ENDED")
		break

	else:
		print("ENTER VALID OPTION")

	
 
