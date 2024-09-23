def xac_dinh_quy(thang):
    if thang < 1 or thang > 12:
        return "Tháng {} không hợp lệ".format(thang)
    if thang <= 3:
        return "Tháng {} thuộc Quý 1".format(thang)
    elif thang <= 6:
        return "Tháng {} thuộc Quý 2".format(thang)
    elif thang <= 9:
        return "Tháng {} thuộc Quý 3".format(thang)
    else:
        return "Tháng {} thuộc Quý 4".format(thang)

thang=int(input("Nhập một tháng (1-12): "))
print(xac_dinh_quy(thang))
