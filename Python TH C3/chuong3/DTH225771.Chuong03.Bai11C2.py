def kiem_tra_so_nguyen_to(n):
    if n <= 1:
        return False
    dem = 0
    for i in range(1, n + 1):
        if n % i == 0:
            dem += 1
    return dem == 2

def nhap_so_nguyen_duong():
    while True:
        try:
            n = int(input("Nhập vào n nguyên dương: "))
            if n > 0:
                return n
            else:
                print(n, "không phải là số nguyên dương! Vui lòng nhập lại.")
        except:
            print("Không hợp lệ! Vui lòng nhập một số nguyên hợp lệ.")

def hoi_tiep_tuc():
    while True:
        hoi = input("Bạn có muốn kiểm tra tiếp số nguyên tố không?(c/k): ").lower()
        if hoi in ['c', 'k']:
            return hoi
        else:
            print(hoi, "là kí tự không hợp lệ! Vui lòng nhập lại.")

def main():
    while True:
        n = nhap_so_nguyen_duong()
        if kiem_tra_so_nguyen_to(n):
            print(n, "là số nguyên tố")
        else:
            print(n, "không phải số nguyên tố")
        
        hoi = hoi_tiep_tuc()
        if hoi == 'k':
            print("Tạm biệt người anh em!")
            break

if __name__ == "__main__":
    main()
