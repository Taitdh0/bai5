print ("Tran Tuan Tai")
print("235752021610014")
# main.py
import sort_utils

# Nhập số lượng phần tử của danh sách
n = int(input("Nhập số lượng phần tử của danh sách: "))

# Nhập các giá trị của danh sách
nlist = []
for _ in range(n):
    value = int(input("Nhập giá trị: "))
    nlist.append(value)

# Sử dụng hàm bubbleSort từ module sort_utils
sorted_list = sort_utils.bubbleSort(nlist)

# In kết quả
print("Danh sách sau khi sắp xếp: ", sorted_list)
