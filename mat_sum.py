mat1=[]
mat2=[]
mat=[]
for i in range(3):
    ele=[]
    for j in range(3):
        ele.append(int(input("enter element:")))
    mat1.append(ele)

for i in range(3):
    ele=[]
    for j in range(3):
        ele.append(int(input("enter element:")))
    mat2.append(ele)
#res=[0 for j in range(3) for i in range(3)]
for i in range(3):
    ele=[]
    for j in range(3):
        ele.append(mat1[i][j]+mat2[i][j])
    mat.append(ele)      
print(mat)
        
