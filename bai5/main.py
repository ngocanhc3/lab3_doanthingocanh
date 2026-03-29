# ===== BÀI 5 =====

ds = []

with open("sinhvien.txt", "r") as f:
    for line in f:
        parts = line.strip().split(",")
        masv = parts[0]
        ten = parts[1]
        diem = float(parts[2])

        ds.append((masv, ten, diem))

# Thống kê
tong = len(ds)
dtb = sum(sv[2] for sv in ds) / tong

dat = 0
for sv in ds:
    if sv[2] >= 5:
        dat += 1

rot = tong - dat

print("\n===== KẾT QUẢ FILE TXT =====")
print("Tổng:", tong)
print("Điểm TB:", dtb)
print("Đạt:", dat)
print("Rớt:", rot)
with open("baocao.txt", "w", encoding="utf-8") as f:
    f.write(f"Tổng: {tong}\n")
    f.write(f"Điểm TB: {dtb}\n")
    f.write(f"Đạt: {dat}\n")
    f.write(f"Rớt: {rot}\n")