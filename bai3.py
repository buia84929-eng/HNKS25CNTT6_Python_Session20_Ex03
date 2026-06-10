import logging

logging.basicConfig(
    filename="tournament_app.log",
    level=logging.INFO,
    format="[%(asctime)s] - [%(levelname)s] - %(message)s"
)

matches = [
    {
        "match_id": "M01",
        "team_a": "T1",
        "team_b": "GenG",
        "score_a": 2,
        "score_b": 1,
        "status": "Completed"
    },
    {
        "match_id": "M02",
        "team_a": "JDG",
        "team_b": "BLG",
        "score_a": 0,
        "score_b": 0,
        "status": "Pending"
    }
]


def display_matches(matches):
    if len(matches) == 0:
        print("Hiện chưa có trận đấu nào trong hệ thống.")
        return

    print("\n--- LỊCH THI ĐẤU & KẾT QUẢ ---")

    for match in matches:
        try:
            print(
                f"{match['match_id']} | "
                f"{match['team_a']} | "
                f"{match['team_b']} | "
                f"{match['score_a']}-{match['score_b']} | "
                f"{match['status']}"
            )
        except KeyError:
            logging.error("Thiếu dữ liệu trận đấu")

    logging.info("User viewed the match list.")


def add_match(matches):
    print("\n--- THÊM TRẬN ĐẤU MỚI ---")

    match_id = input("Nhập mã trận đấu: ").strip()

    if match_id == "":
        print("Mã trận đấu không được để trống.")
        logging.warning("User tried to add a match with empty match ID.")
        return

    for match in matches:
        if match["match_id"] == match_id:
            print(f"Lỗi: Mã trận đấu {match_id} đã tồn tại.")
            logging.warning(f"Match ID {match_id} already exists.")
            return

    team_a = input("Nhập tên Đội A: ").strip()
    team_b = input("Nhập tên Đội B: ").strip()

    if team_a == "" or team_b == "":
        print("Tên đội không được để trống.")
        logging.warning("User tried to add a match with empty team name.")
        return

    matches.append({
        "match_id": match_id,
        "team_a": team_a,
        "team_b": team_b,
        "score_a": 0,
        "score_b": 0,
        "status": "Pending"
    })

    print("Thêm thành công.")
    logging.info(f"Match {match_id} added successfully")


def update_score(matches):
    print("\n--- CẬP NHẬT TỶ SỐ ---")

    match_id = input("Nhập mã trận: ").strip()

    found = False

    for match in matches:
        if match["match_id"] == match_id:
            found = True

            while True:
                try:
                    score_a = int(input("Nhập điểm đội A: "))

                    if score_a < 0:
                        print("Điểm phải >= 0")
                        logging.error(f"Negative score input detected: {score_a}")
                        continue

                    break

                except ValueError as e:
                    print("Điểm số phải là số nguyên.")
                    logging.error(f"Invalid score input. Error: {e}")

            while True:
                try:
                    score_b = int(input("Nhập điểm đội B: "))

                    if score_b < 0:
                        print("Điểm phải >= 0")
                        logging.error(f"Negative score input detected: {score_b}")
                        continue

                    break

                except ValueError as e:
                    print("Điểm số phải là số nguyên.")
                    logging.error(f"Invalid score input. Error: {e}")

            match["score_a"] = score_a
            match["score_b"] = score_b

            if score_a == 0 and score_b == 0:
                confirm = input("Xác nhận hoàn thành? (y/n): ")

                if confirm.lower() == "y":
                    match["status"] = "Completed"
                else:
                    match["status"] = "Pending"
            else:
                match["status"] = "Completed"

            print("Cập nhật thành công.")
            logging.info(f"Match {match_id} score updated successfully")

    if not found:
        print("Không tìm thấy trận đấu.")
        logging.warning(
            f"User tried to update non-existing match {match_id}"
        )


def determine_winner(match):
    if match["status"] == "Pending":
        return "Not Started"

    if match["score_a"] > match["score_b"]:
        return match["team_a"]

    if match["score_b"] > match["score_a"]:
        return match["team_b"]

    return "Draw"


def generate_report(matches):
    print("\n--- BÁO CÁO ---")

    count = 0

    for match in matches:
        if match["status"] == "Completed":
            winner = determine_winner(match)

            print(
                f"{match['match_id']}: "
                f"{match['team_a']} "
                f"{match['score_a']}-{match['score_b']} "
                f"{match['team_b']} | {winner}"
            )

            count += 1

    if count == 0:
        print("Chưa có trận đấu nào hoàn thành.")

    print(f"Tổng số trận đã hoàn thành: {count}")

    logging.info("User generated tournament report.")


while True:
    print("\n===== MENU =====")
    print("1. Hiển thị")
    print("2. Thêm trận")
    print("3. Cập nhật tỷ số")
    print("4. Báo cáo")
    print("5. Thoát")

    choice = input("Chọn: ")

    if choice == "1":
        display_matches(matches)

    elif choice == "2":
        add_match(matches)

    elif choice == "3":
        update_score(matches)

    elif choice == "4":
        generate_report(matches)

    elif choice == "5":
        logging.info("Tournament management system closed.")
        print("Tạm biệt!")
        break

    else:
        print("Lựa chọn không hợp lệ.")
        logging.warning("Invalid menu choice selected")

# Clean Code
# Đặt tên theo PEP 8 (snake_case): match_id, display_matches(), update_score().
# Tên phải có ý nghĩa, tránh: x, a, ds

# Docstring
# Mô tả ngắn gọn:
# Hàm làm gì
# Nhận tham số gì
# Trả về gì

# ogging
# Ghi log vào file tournament_app.log
# Định dạng: [Thời gian] - [Cấp độ Log] - [Tin nhắn]
# INFO: thao tác thành công
# WARNING: dữ liệu/lựa chọn không hợp lệ
# ERROR: lỗi phát sinh

# Lợi ích
# Code dễ đọc
# Dễ bảo trì
# Dễ debug
# Theo dõi được lịch sử hoạt động của hệ thống