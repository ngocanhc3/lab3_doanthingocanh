# ===== BÀI 6 =====

import csv

hop_le = []
loi = []

with open("diemlop.csv", newline="") as f:
    reader = csv.DictReader(f)

    for row in reader:
        try:
            diem = float(row["Diem"])

            if 0 <= diem <= 10:
                hop_le.append((row["MaSV"], row["HoTen"], diem))
            else:
                loi.append(row)

        except:
            print("Lỗi:", row)
            loi.append(row)

# Tính TB
if hop_le:
    dtb = sum(sv[2] for sv in hop_le) / len(hop_le)
    print("\nĐiểm trung bình hợp lệ:", dtb)

# Ghi lỗi
with open("loi.txt", "w") as f:
    for row in loi:
        f.write(str(row) + "\n")