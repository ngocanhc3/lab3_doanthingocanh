# ===== BÀI 4 =====

def nhap_danh_sach():
    ds = []
    n = int(input("Nhập số sinh viên: "))

    for i in range(n):
        print(f"\nSinh viên {i+1}")
        masv = input("Mã SV: ")
        ten = input("Tên: ")
        diem = float(input("Điểm: "))

        ds.append((masv, ten, diem))

    return ds


def tinh_diem_trung_binh(ds):
    tong = 0
    for sv in ds:
        tong += sv[2]
    return tong / len(ds)


def tim_sv_max(ds):
    sv_max = ds[0]
    for sv in ds:
        if sv[2] > sv_max[2]:
            sv_max = sv
    return sv_max


def xep_loai(diem):
    if diem >= 8:
        return "A"
    elif diem >= 6.5:
        return "B"
    elif diem >= 5:
        return "C"
    else:
        return "F"


def in_bao_cao(ds):
    print("\n===== BÁO CÁO =====")
    for sv in ds:
        print(sv, "- Xếp loại:", xep_loai(sv[2]))

    print("Điểm trung bình:", tinh_diem_trung_binh(ds))
    print("Sinh viên giỏi nhất:", tim_sv_max(ds))


# CHẠY
ds = nhap_danh_sach()
in_bao_cao(ds)