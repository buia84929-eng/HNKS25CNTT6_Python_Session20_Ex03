import unittest
from ss20bai3 import determine_winner


class TestDetermineWinner(unittest.TestCase):

    def test_team_a_win(self):
        match = {
            "score_a": 2,
            "score_b": 0,
            "status": "Completed",
            "team_a": "T1",
            "team_b": "GenG"
        }

        self.assertEqual(determine_winner(match), "T1")

    def test_draw(self):
        match = {
            "score_a": 1,
            "score_b": 1,
            "status": "Completed",
            "team_a": "T1",
            "team_b": "GenG"
        }

        self.assertEqual(determine_winner(match), "Draw")

    def test_pending(self):
        match = {
            "score_a": 0,
            "score_b": 0,
            "status": "Pending",
            "team_a": "T1",
            "team_b": "GenG"
        }

        self.assertEqual(determine_winner(match), "Not Started")


if __name__ == "__main__":
    unittest.main()

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