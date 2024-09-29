(a) range(5): Tạo ra dãy số từ 0 đến 4
Kết quả: [0, 1, 2, 3, 4]

(b) range(5, 10): Tạo ra dãy số từ 5 đến 9
Kết quả: [5, 6, 7, 8, 9]

(c) range(5, 20, 3): Tạo ra dãy số từ 5 đến 20 với bước nhảy là 3
Kết quả: [5, 8, 11, 14, 17]

(d) range(20, 5, -1): Tạo ra dãy số từ 20 đến 6 với bước nhảy là -1
Kết quả: [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6]

(e) range(20, 5, -3): Tạo ra dãy số từ 20 đến 8 với bước nhảy là -3
Kết quả: [20, 17, 14, 11, 8]

(f) range(10, 5): Không tạo ra dãy số nào vì điểm bắt đầu lớn hơn điểm kết thúc và không có bước nhảy âm

(g) range(0): Không tạo ra dãy số nào vì điểm bắt đầu và kết thúc đều là 0

(h) range(10, 101, 10): Tạo ra dãy số từ 10 đến 100 với bước nhảy là 10
Kết quả: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

(i) range(10, -1, -1): Tạo ra dãy số từ 10 đến 0 với bước nhảy là -1
Kết quả: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

(j) range(-3, 4): Tạo ra dãy số từ -3 đến 3
Kết quả: [-3, -2, -1, 0, 1, 2, 3]

(k) range(0, 10, 1): Tạo ra dãy số từ 0 đến 9 với bước nhảy là 1
Kết quả: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
ví dụ:
for i in range(0, 10, 1):
    print(i)


