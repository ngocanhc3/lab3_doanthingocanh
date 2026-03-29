ds_diem = [7.5, 8.0, 4.5, 9.0, 6.0, 5.5, 8.5, 3.0]

# Điểm đạt
dat = [d for d in ds_diem if d >= 5]

# Bình phương
binh_phuong = [d**2 for d in dat]

# Xếp loại
xep_loai = {
    i+1: ("A" if d >= 8 else "B" if d >= 6.5 else "C" if d >= 5 else "F")
    for i, d in enumerate(ds_diem)
}

print("Điểm đạt:", dat)
print("Bình phương:", binh_phuong)
print("Xếp loại:", xep_loai)