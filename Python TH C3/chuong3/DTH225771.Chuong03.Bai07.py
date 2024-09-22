import datetime

def ngay_ke_tiep(ngay, thang, nam):
    ngay_hien_tai = datetime.date(nam, thang, ngay)
    ngay_ke_tiep = ngay_hien_tai + datetime.timedelta(days=1)
    return ngay_ke_tiep

ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

ngay_sau = ngay_ke_tiep(ngay, thang, nam)
print("Ngày kế tiếp là:", ngay_sau.strftime("%d/%m/%Y"))
