print("Chương trình đọc số ra dạng chữ")
def doc_so(n):
    hangdv = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    hangchuc = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi", "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]

    if n < 10:
        return hangdv[n]
    else:
        chuc = n // 10
        dv = n % 10
        if dv == 0:
            return hangchuc[chuc]
        else:
            return hangchuc[chuc] + " " + hangdv[dv]

n = int(input("Nhập một số có tối đa 2 chữ số: "))

if n <= 0 or n > 99:
    print("Vui lòng nhập một số có tối đa 2 chữ số.")
else:
    print("Cách đọc:", doc_so(n))
