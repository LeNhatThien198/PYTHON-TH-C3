def xac_dinh_quy(thang):
    if thang < 1 or thang > 12:
        return "Tháng {} không hợp lệ".format(thang)
    quy = {
        1: "Quý 1", 2: "Quý 1", 3: "Quý 1",
        4: "Quý 2", 5: "Quý 2", 6: "Quý 2",
        7: "Quý 3", 8: "Quý 3", 9: "Quý 3",
        10: "Quý 4", 11: "Quý 4", 12: "Quý 4"
    }
    return "Tháng {} thuộc {}".format(thang, quy[thang])

def main():
    thang = int(input("Nhập một tháng (1-12): "))
    print(xac_dinh_quy(thang))
    
    
main()
