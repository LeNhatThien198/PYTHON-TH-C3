x=int(input("Nhập vào x: "))
n=int(input("Nhập vào N: "))
s=0
for i in range(1,n + 1):
    tu=x**i
    mau=1
    for j in range(1,i + 1): #lấy kết quả lần lặp cuối của i này xong mới chạy tiếp i trên
        mau=mau*j
    s=s+(tu/mau)
print("s({},{})={}".format(x,n,s))
