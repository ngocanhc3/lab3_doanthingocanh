data = ["Python", "CSDL", "Python", "Java", "CSDL", "AI", "Python"]

# Loại trùng
unique = set(data)
print("Không trùng:", unique)

# Đếm
count = {}
for mon in data:
    count[mon] = count.get(mon, 0) + 1

print("Số lần xuất hiện:", count)

# Môn nhiều nhất
max_mon = max(count, key=count.get)
print("Môn nhiều nhất:", max_mon)

# Sắp xếp giảm dần
sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)
print("Sắp xếp:", sorted_count)