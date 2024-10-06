x=int(input("Nhập vào x: "))
n=int(input("Nhập vào N: "))
s=0
for i in range(n+1):
        luythua=2*i + 1
        tu=x**luythua
        mau=1
        for j in range(1, luythua + 1): #lấy kết quả lần lặp cuối của luythua xong mới chạy tiếp i
            mau *= j
        s += tu/mau
print("s({},{})={}".format(x,n,s))
    
            
        
        
