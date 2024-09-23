while True:
    try:
        n=(input("Nhập vào n nguyên dương: "))
        n=int(n)
        if n <= 0:
            print(n, "không phải là số nguyên dương! Vui lòng nhập lại.")
            continue
    except:
        print(n,"không hợp lệ! Vui lòng nhập một số nguyên hợp lệ.")
        continue
   
    dem = 0
    for i in range(1, n + 1):
        if n % i == 0:
            dem += 1
    if dem==2:
        print(n,"là số nguyên tố")
    else:
        print(n,"không phải số nguyên tố")
    while True:
        hoi=input("Bạn có muốn kiểm tra tiếp số nguyên tố không?(c/k): ").lower()
        if hoi == "k":
            break
        elif hoi == "c":
            break
        else:
            print(hoi, "là kí tự không hợp lệ! Vui lòng nhập lại.")
        
    if hoi == "k":
        print("Tạm biệt người anh em!")
        break



    

