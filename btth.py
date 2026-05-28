branch_names = ["Highlands Nhà Thờ", "Highlands Bà Triệu", "Highlands Nguyễn Du", "Highlands Landmark 81", "Highlands Trần Hưng Đạo"]
daily_revenues = [15500000, 28000000, 9200000, 45000000, 11000000] 
target_achieved = [True, True, False, True, False] 

while True:

    print("\n===== HỆ THỐNG QUẢN LÝ DOANH THU HIGHLANDS =====")
    print("1. Hiển thị báo cáo doanh thu tổng hợp")
    print("2. Thống kê chi nhánh Cao nhất / Thấp nhất")
    print("3. Lọc danh sách cơ sở kém (Không đạt chỉ tiêu)")
    print("4. Thoát chương trình")
    print("================================================")
    try:
        choice = int(input("Nhập lựa chọn của bạn (1-4): "))
        if choice == 1:
            print("\n========= BÁO CÁO DOANH THU =========")
            print(f"{'STT'}{'Tên Chi Nhánh'}{'Doanh Thu'}{'Trạng Thái'}")
            for i in range(len(branch_names)):
                status = "Đạt" if target_achieved[i] else "Không Đạt"
                print(
                    f"{i+1:<5}"
                    f"{branch_names[i]:<35}"
                    f"{daily_revenues[i]:,} VNĐ".ljust(20)
                    + f"{status}"
                )
                total_revenue = sum(daily_revenues)
            print(f"Tổng doanh thu toàn hệ thống: {total_revenue:,} VNĐ")    
        elif choice ==2: 
            max_revenue = max(daily_revenues)
            min_revenue = min(daily_revenues)

            max_index = daily_revenues.index(max_revenue)
            min_index = daily_revenues.index(min_revenue)

            print("\n===== THỐNG KÊ DOANH THU =====")

            print(f"Chi nhánh doanh thu cao nhất:")
            print(f"- {branch_names[max_index]}: {max_revenue:,} VNĐ")

            print(f"\nChi nhánh doanh thu thấp nhất:")
            print(f"- {branch_names[min_index]}: {min_revenue:,} VNĐ")
        elif choice == 3: 
            failed_branches = []
            for i in range(len(branch_names)):
                if(target_achieved[i]==False): 
                    failed_branches.append(branch_names[i])
            print(failed_branches)      
        elif choice == 4:
            print("Bạn đã thoát chương trình")
            break

    except ValueError:
        print("\n[Lỗi] Bạn phải nhập số từ 1 đến 4!")