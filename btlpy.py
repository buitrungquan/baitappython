# Khai báo danh sách lưu trữ xe và khách hàng
ds_xe = []
ds_khach_hang = []
ds_hoa_don = []

# Tên tệp dữ liệu
ten_tap_tin = "/Users/macbook/Documents/tuan4/thư mục k/baitaplon1/du_lieu_xe.txt"

# Thêm xe mới
def them_xe():
    ma_xe = input("Nhập mã xe: ")
    hang_xe = input("Nhập hãng xe: ")
    mau_xe = input("Nhập mẫu xe: ")
    nam_sx = int(input("Nhập năm sản xuất: "))
    gia_ban = float(input("Nhập giá bán: "))
    so_luong = int(input("Nhập số lượng tồn kho: "))
    xe_moi = {
        "ma_xe": ma_xe,
        "hang_xe": hang_xe,
        "mau_xe": mau_xe,
        "nam_sx": nam_sx,
        "gia_ban": gia_ban,
        "so_luong": so_luong
    }
    ds_xe.append(xe_moi)
    print("Đã thêm xe mới thành công!")

# Xóa xe
def xoa_xe():
    ma_xe = input("Nhập mã xe cần xóa: ")
    for xe in ds_xe:
        if xe["ma_xe"] == ma_xe:
            ds_xe.remove(xe)
            print("Đã xóa xe thành công!")
            return
    print("Không tìm thấy mã xe!")

# Sắp xếp xe
def sap_xep_theo_gia():
    ds_xe.sort(key=lambda x: x["gia_ban"])
    print("Danh sách xe đã được sắp xếp theo giá bán.")

def sap_xep_theo_nam():
    ds_xe.sort(key=lambda x: x["nam_sx"])
    print("Danh sách xe đã được sắp xếp theo năm sản xuất.")

# Tìm kiếm xe
def tim_kiem_xe():
    ten_xe = input("Nhập tên mẫu xe cần tìm: ")
    for xe in ds_xe:
        if xe["mau_xe"].lower() == ten_xe.lower():
            print("Thông tin xe:", xe)
            return
    print("Không tìm thấy xe!")

# Cập nhật thông tin xe
def cap_nhat_thong_tin():
    ma_xe = input("Nhập mã xe cần cập nhật: ")
    for xe in ds_xe:
        if xe["ma_xe"] == ma_xe:
            gia_moi = float(input("Nhập giá bán mới: "))
            so_luong_moi = int(input("Nhập số lượng tồn kho mới: "))
            xe["gia_ban"] = gia_moi
            xe["so_luong"] = so_luong_moi
            print("Đã cập nhật thông tin xe.")
            return
    print("Không tìm thấy mã xe!")

# Quản lý khách hàng
def them_khach_hang():
    ma_kh = input("Nhập mã khách hàng: ")
    ten_kh = input("Nhập tên khách hàng: ")
    so_dien_thoai = input("Nhập số điện thoại: ")
    dia_chi = input("Nhập địa chỉ: ")
    khach_moi = {
        "ma_kh": ma_kh,
        "ten_kh": ten_kh,
        "so_dien_thoai": so_dien_thoai,
        "dia_chi": dia_chi
    }
    ds_khach_hang.append(khach_moi)
    print("Đã thêm khách hàng mới thành công!")

def tim_kiem_khach_hang():
    ten_kh = input("Nhập tên khách hàng cần tìm: ")
    for kh in ds_khach_hang:
        if kh["ten_kh"].lower() == ten_kh.lower():
            print("Thông tin khách hàng:", kh)
            return
    print("Không tìm thấy khách hàng!")

# Quản lý hóa đơn
def lap_hoa_don():
    ma_kh = input("Nhập mã khách hàng: ")
    for kh in ds_khach_hang:
        if kh["ma_kh"] == ma_kh:
            ma_xe = input("Nhập mã xe cần mua: ")
            for xe in ds_xe:
                if xe["ma_xe"] == ma_xe and xe["so_luong"] > 0:
                    so_luong_mua = int(input("Nhập số lượng xe cần mua: "))
                    if so_luong_mua <= xe["so_luong"]:
                        tong_tien = xe["gia_ban"] * so_luong_mua
                        hoa_don = {
                            "ma_kh": ma_kh,
                            "ma_xe": ma_xe,
                            "so_luong_mua": so_luong_mua,
                            "tong_tien": tong_tien
                        }
                        ds_hoa_don.append(hoa_don)
                        xe["so_luong"] -= so_luong_mua
                        print(f"Đã lập hóa đơn. Tổng tiền: {tong_tien}")
                        return
                    else:
                        print("Số lượng xe không đủ!")
                        return
            print("Không tìm thấy mã xe hoặc xe đã hết hàng!")
            return
    print("Không tìm thấy mã khách hàng!")

# Thống kê doanh số
def thong_ke_doanh_so():
    doanh_so = sum(hd["tong_tien"] for hd in ds_hoa_don)
    so_xe_ban_ra = sum(hd["so_luong_mua"] for hd in ds_hoa_don)
    print(f"Tổng doanh số: {doanh_so}")
    print(f"Tổng số xe bán ra: {so_xe_ban_ra}")

# Ghi và đọc dữ liệu từ tệp txt
def ghi_tap_tin():
    with open(ten_tap_tin, 'w') as f:
        for xe in ds_xe:
            f.write(f'{xe["ma_xe"]}|{xe["hang_xe"]}|{xe["mau_xe"]}|{xe["nam_sx"]}|{xe["gia_ban"]}|{xe["so_luong"]}\n')
        f.write("===KH===\n")
        for kh in ds_khach_hang:
            f.write(f'{kh["ma_kh"]}|{kh["ten_kh"]}|{kh["so_dien_thoai"]}|{kh["dia_chi"]}\n')
        f.write("===HD===\n")
        for hd in ds_hoa_don:
            f.write(f'{hd["ma_kh"]}|{hd["ma_xe"]}|{hd["so_luong_mua"]}|{hd["tong_tien"]}\n')
    print("Đã ghi dữ liệu vào tệp.")

def doc_tap_tin():
    global ds_xe, ds_khach_hang, ds_hoa_don
    try:
        with open(ten_tap_tin, 'r') as f:
            ds_xe = []
            ds_khach_hang = []
            ds_hoa_don = []
            lines = f.readlines()
            idx = 0
            # Đọc dữ liệu xe
            while idx < len(lines) and lines[idx].strip() != "===KH===":
                line_data = lines[idx].strip().split('|')
                if len(line_data) == 6:  # Kiểm tra nếu có đủ 6 giá trị
                    ma_xe, hang_xe, mau_xe, nam_sx, gia_ban, so_luong = line_data
                    ds_xe.append({
                        "ma_xe": ma_xe,
                        "hang_xe": hang_xe,
                        "mau_xe": mau_xe,
                        "nam_sx": int(nam_sx),
                        "gia_ban": float(gia_ban),
                        "so_luong": int(so_luong)
                    })
                idx += 1
            idx += 1  
            # Đọc dữ liệu khách hàng
            while idx < len(lines) and lines[idx].strip() != "===HD===":
                line_data = lines[idx].strip().split('|')
                if len(line_data) == 4:  # Kiểm tra nếu có đủ 4 giá trị
                    ma_kh, ten_kh, so_dien_thoai, dia_chi = line_data
                    ds_khach_hang.append({
                        "ma_kh": ma_kh,
                        "ten_kh": ten_kh,
                        "so_dien_thoai": so_dien_thoai,
                        "dia_chi": dia_chi
                    })
                idx += 1

            idx += 1  

            # Đọc dữ liệu hóa đơn
            while idx < len(lines):
                line_data = lines[idx].strip().split('|')
                if len(line_data) == 4:  # Kiểm tra nếu có đủ 4 giá trị
                    ma_kh, ma_xe, so_luong_mua, tong_tien = line_data
                    ds_hoa_don.append({
                        "ma_kh": ma_kh,
                        "ma_xe": ma_xe,
                        "so_luong_mua": int(so_luong_mua),
                        "tong_tien": float(tong_tien)
                    })
                idx += 1

        print("Đã đọc dữ liệu từ tệp.")
    except FileNotFoundError:
        print("Tệp dữ liệu không tồn tại!")

# Menu chính
def menu():
    while True:
        print("\n---- QUẢN LÝ GARA OTO ----")
        print("1. Thêm xe")
        print("2. Xóa xe")
        print("3. Sắp xếp xe theo giá")
        print("4. Sắp xếp xe theo năm sản xuất")
        print("5. Tìm kiếm xe")
        print("6. Cập nhật thông tin xe")
        print("7. Thêm khách hàng")
        print("8. Tìm kiếm khách hàng")
        print("9. Lập hóa đơn")
        print("10. Thống kê doanh số")
        print("11. Ghi dữ liệu vào tệp")
        print("12. Đọc dữ liệu từ tệp")
        print("13. In danh sách xe")
        print("14. In danh sách khách hàng")
        print("15. In danh sách hóa đơn")
        print("0. Thoát")

        lua_chon = input("Chọn chức năng: ")

        if lua_chon == '1':
            them_xe()
        elif lua_chon == '2':
            xoa_xe()
        elif lua_chon == '3':
            sap_xep_theo_gia()
        elif lua_chon == '4':
            sap_xep_theo_nam()
        elif lua_chon == '5':
            tim_kiem_xe()
        elif lua_chon == '6':
            cap_nhat_thong_tin()
        elif lua_chon == '7':
            them_khach_hang()
        elif lua_chon == '8':
            tim_kiem_khach_hang()
        elif lua_chon == '9':
            lap_hoa_don()
        elif lua_chon == '10':
            thong_ke_doanh_so()
        elif lua_chon == '11':
            ghi_tap_tin()
        elif lua_chon == '12':
            doc_tap_tin()
        elif lua_chon == '13':
            print("Danh sách xe:")
            for xe in ds_xe:
                print(xe)
        elif lua_chon == '14':
            print("Danh sách khách hàng:")
            for kh in ds_khach_hang:
                print(kh)
        elif lua_chon == '15':
            print("Danh sách hóa đơn:")
            for hd in ds_hoa_don:
                print(hd)
        elif lua_chon == '0':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ!")

# Chạy chương trình
doc_tap_tin()  
menu()
