import random

def generate_generic_question(description, start_year, end_year, initial_value, final_value, unit):
    initial_question = """
    {description}

    Từ năm {start_year} đến năm {end_year}, {variable} (gọi là y) được tính theo công thức y = at + b, trong đó y là {variable}, t là số năm tính từ năm {start_year}. Biết rằng vào năm {start_year}, {variable} là {initial_value}{unit}, và vào năm {end_year}, {variable} là {final_value}{unit}.

    a) Hãy lập công thức liên hệ giữa {variable} và số năm. Dựa vào công thức, tính {variable} cho năm {year}.

    b) Nếu vào năm {new_year}, {variable} là {new_value}{unit}. Hãy tính số năm cần để đạt được {variable} là {target_value}{unit}.
    """

    new_question = initial_question.format(description=description, start_year=start_year, end_year=end_year,
                                           variable=description.lower(), initial_value=initial_value,
                                           final_value=final_value, year=start_year + (end_year - start_year) // 2,
                                           new_year=end_year + 1, new_value=final_value + (final_value - initial_value),
                                           target_value=final_value + (final_value - initial_value) + 1, unit=unit)

    print("Đề bài mới:")
    print(new_question)

    a = (final_value - initial_value) / (end_year - start_year)
    b = initial_value - a * start_year
    print("a =", a)
    print("b =", b)

    mid_year_value = a * (start_year + (end_year - start_year) // 2) + b
    print("{variable} cho năm {year}:".format(variable=description.lower(), year=start_year + (end_year - start_year) // 2),
          mid_year_value)

    target_value = final_value + (final_value - initial_value) + 1
    years_to_reach_target = (target_value - b) / a
    print("Số năm cần để đạt được {variable} là {target_value}{unit}:".format(variable=description.lower(),
                                                                              target_value=target_value, unit=unit),
          round(years_to_reach_target, 2))

def generate_random_question():
    # Danh sách các chủ đề và thông số tương ứng
    topics = [
        ("Lãi suất ngân hàng", random.randint(2010, 2022), 2025, 2, 4.5, "%"),
        ("Tổng doanh thu công ty", 2015, 2020, 100000, 500000, "đ"),
        ("Số lượng người dùng mạng xã hội", 2010, 2020, 1000, 5000, "người"),
        ("Giá trị của cổ phiếu", 2010, 2020, 50, 150, "đồng"),
        ("Tổng số xe đăng ký mới", 2015, 2020, 5000, 15000, "xe"),
        ("Doanh thu từ bán hàng trực tuyến", 2018, 2022, 1000000, 5000000, "đ"),
        ("Số lượng khách du lịch", 2015, 2020, 10000, 50000, "người"),
        ("Tổng sản lượng nông nghiệp", 2010, 2020, 1000000, 5000000, "tấn"),
        ("Tổng doanh số bán hàng", 2015, 2020, 2000000, 10000000, "đ"),
        ("Số lượng người tham gia khóa học trực tuyến", 2017, 2022, 500, 5000, "người"),
        ("Tỉ lệ sinh viên tốt nghiệp", 2016, 2021, 40, 80, "%"),
        ("Số lượng sách được mượn từ thư viện", 2015, 2020, 1000, 5000, "quyển"),
        ("Điểm trung bình của học sinh", 2017, 2022, 6, 8, ""),
        ("Số lượng học sinh đậu kỳ thi tốt nghiệp", 2015, 2020, 800, 1200, "học sinh"),
        ("Tỉ lệ sinh viên được nhận học bổng", 2016, 2021, 10, 20, "%"),
        ("Số lượng khẩu phần ăn hàng ngày", 2018, 2023, 3, 5, ""),
        ("Tổng doanh số của nhà hàng", 2015, 2020, 500000, 2000000, "đ"),
        ("Giá trị nhập khẩu thực phẩm", 2010, 2020, 10000000, 50000000, "đ"),
        ("Tỉ lệ người tiêu thụ rau quả hàng ngày", 2015, 2020, 50, 70, "%"),
        ("Số lượng đồ uống bán ra từ cửa hàng", 2017, 2022, 1000, 5000, "ly"),
        ("Thời gian học trung bình hàng ngày", 2018, 2023, 2, 4, "giờ"),
        ("Số lượng câu hỏi đã làm trong bài tập", 2016, 2021, 500, 1500, "câu"),
        ("Tỉ lệ sinh viên tham gia các hoạt động ngoại khóa", 2015, 2020, 30, 60, "%"),
        ("Điểm trung bình của sinh viên", 2017, 2022, 7, 9, ""),
        ("Số lượng giờ ôn thi mỗi tuần", 2015, 2020, 5, 10, "giờ"),
        ("Số lượng sinh vật mới được phát hiện", 2010, 2020, 50, 150, "loài"),
        ("Tổng số lượng vi khuẩn trong mẫu đất", 2015, 2020, 100000, 500000, "vi khuẩn"),
        ("Tỉ lệ người tiêm vắc xin", 2017, 2022, 60, 80, "%"),
        ("Số lượng người tham gia nghiên cứu sinh học", 2016, 2021, 200, 800, "người"),
        ("Số lượng loại thuốc mới được phát triển", 2010, 2020, 20, 50, "loại"),
        ("Tổng công suất sản xuất điện năng", 2015, 2020, 10000, 50000, "MW"),
        ("Số lượng thiết bị điện tử bán ra", 2017, 2022, 50000, 150000, "cái"),
        ("Tổng số lượng phân tử trong mẫu chất", 2010, 2020, 1000000, 5000000, "phân tử"),
        ("Độ sáng trung bình của đèn đường", 2016, 2021, 50, 100, "lux"),
        ("Tỉ lệ tự nhiên khí CO2 trong không khí", 2015, 2020, 0.03, 0.05, "%"),
        # Thêm các chủ đề mới với tính ngẫu nhiên hơn
        ("Tỉ lệ sử dụng phần mềm di động", random.randint(2010, 2025), random.randint(2025, 2030), random.uniform(20, 50), random.uniform(60, 80), "%"),
        ("Số lượng đơn hàng mua sắm trực tuyến", random.randint(2015, 2020), random.randint(2020, 2025), random.randint(50000, 100000), random.randint(200000, 500000), "đơn hàng"),
        ("Tỉ lệ sử dụng internet hàng ngày", random.randint(2010, 2020), random.randint(2020, 2030), random.uniform(40, 70), random.uniform(80, 90), "%"),
        ("Số lượng người tham gia sự kiện trực tuyến", random.randint(2015, 2025), random.randint(2025, 2035), random.randint(200, 1000), random.randint(2000, 5000), "người"),
        ("Tổng doanh số bán hàng trên mạng xã hội", random.randint(2018, 2022), random.randint(2022, 2026), random.randint(5000000, 10000000), random.randint(20000000, 50000000), "đ")
    ]

    # Chọn một chủ đề ngẫu nhiên
    topic, start_year, end_year, initial_value, final_value, unit = random.choice(topics)

    # Tạo đề bài mới cho chủ đề được chọn
    generate_generic_question(topic, start_year, end_year, initial_value, final_value, unit)

# Tạo một đề bài mới với chủ đề ngẫu nhiên
generate_random_question()
