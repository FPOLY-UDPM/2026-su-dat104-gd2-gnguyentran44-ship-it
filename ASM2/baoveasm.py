-- Mức 1
--	Cho biết danh sách các loại điểm
SELECT 
    maLoaiDiem      AS [Mã Loại Điểm],
    TenLoaiDiem     AS [Tên Loại Điểm],
    TrongSo         AS [Trọng Số]
FROM [dbo].[LoaiDiem]
ORDER BY maLoaiDiem ASC;
--	Cho biết toàn bộ các dòng trong bảng “DIEM”
SELECT 
    d.ID                        AS [STT],
    d.MASV                      AS [Mã Sinh Viên],
    ld.TenLoaiDiem              AS [Loại Điểm],
    d.DiemSo                    AS [Điểm Số],
    ld.TrongSo                  AS [Trọng Số],
    d.DiemSo * ld.TrongSo       AS [Điểm Có Trọng Số],
    d.Lan                       AS [Lần Thi],
    d.Ngay                      AS [Ngày]
FROM [dbo].[Diem] d
JOIN [dbo].[LoaiDiem] ld ON d.maloaidiem = ld.maLoaiDiem
ORDER BY d.MASV, ld.TenLoaiDiem;
--3.	Thêm điểm cho sinh viên
INSERT INTO [dbo].[Diem] (MASV, DiemSo, maloaidiem, Lan, Ngay, GhiChu)
VALUES ('PS12345', 9.5, 1, 1, GETDATE(), 1);

-- Kiểm tra vừa thêm
SELECT 
    d.MASV              AS [Mã Sinh Viên],
    ld.TenLoaiDiem      AS [Loại Điểm],
    d.DiemSo            AS [Điểm Số],
    d.Lan               AS [Lần Thi],
    d.Ngay              AS [Ngày Nhập]
FROM [dbo].[Diem] d
JOIN [dbo].[LoaiDiem] ld ON d.maloaidiem = ld.maLoaiDiem
WHERE d.MASV = 'PS12345';
--5.	Xóa điểm không phù hợp
SELECT 
    d.ID                AS [ID],
    d.MASV              AS [Mã Sinh Viên],
    ld.TenLoaiDiem      AS [Loại Điểm],
    d.DiemSo            AS [Điểm Số],
    d.Lan               AS [Lần Thi],
    d.Ngay              AS [Ngày]
FROM [dbo].[Diem] d
JOIN [dbo].[LoaiDiem] ld ON d.maloaidiem = ld.maLoaiDiem
WHERE d.MASV = 'PS12345'
  AND ld.TenLoaiDiem = N'Quiz';
  --6.	Lấy danh sách sinh viên có điểm Lab < 5
--Lấy danh sách sinh viên có tuổi dưới 20
SELECT DISTINCT
    sv.MASV                     AS [Mã Sinh Viên],
    sv.Ho + N' ' + sv.TenLot + N' ' + sv.Ten  AS [Họ Tên],
    sv.NgaySinh                 AS [Ngày Sinh],
    sv.Email                    AS [Email],
    sv.DienThoai                AS [Điện Thoại],
    d.DiemSo                    AS [Điểm Lab]
FROM [dbo].[ThongTinSinhVien] sv
JOIN [dbo].[Diem] d        ON sv.MASV = d.MASV
JOIN [dbo].[LoaiDiem] ld   ON d.maloaidiem = ld.maLoaiDiem
WHERE ld.TenLoaiDiem = N'Lab'
  AND d.DiemSo < 5
ORDER BY d.DiemSo ASC;
-- Danh sách sinh viên tuổi dưới 20
SELECT *
FROM [dbo].[ThongTinSinhVien]
WHERE YEAR(NgaySinh) > 2006;  -- 2026 - 20 = 2006
--7.	Cập nhật thông tin ghi chú cho tất cả sinh viên có điểm Quiz < 5
-- TRƯỚC KHI CẬP NHẬT - Xem điểm Quiz < 5
SELECT 
    d.ID                AS [ID],
    d.MASV              AS [Mã Sinh Viên],
    ld.TenLoaiDiem      AS [Loại Điểm],
    d.DiemSo            AS [Điểm Số],
    d.GhiChu            AS [Ghi Chú Cũ]
FROM [dbo].[Diem] d
JOIN [dbo].[LoaiDiem] ld ON d.maloaidiem = ld.maLoaiDiem
WHERE ld.TenLoaiDiem = N'Quiz'
  AND d.DiemSo < 5;
  --Mức 2
 -- 8.	Dùng lệnh INSERT để thêm 1 sinh viên mới vào danh sách
INSERT INTO [dbo].[ThongTinSinhVien] 
    (Ho, TenLot, Ten, NgaySinh, DiaChi, Email, DienThoai, MASV)
VALUES 
 (N'Võ', N'Thị', N'Hương', '2004-12-10', N'Bình Dương', 'huong.vt@gmail.com', '0933333333', 'SV021');
 --9.Tính điểm Quiz (hoặc Lab, Assignment) trung bình theo từng sinh viên
--Lấy danh sách sinh viên có điểm trung bình Quiz (hay Lab) < 5
-- Tính điểm QUIZ trung bình theo từng sinh viên
SELECT 
    sv.MASV                                         AS [Mã Sinh Viên],
    sv.Ho + N' ' + sv.TenLot + N' ' + sv.Ten       AS [Họ Tên],
    ld.TenLoaiDiem                                  AS [Loại Điểm],
    ROUND(AVG(d.DiemSo), 2)                         AS [Điểm Trung Bình]
FROM [dbo].[ThongTinSinhVien] sv
JOIN [dbo].[Diem] d      ON sv.MASV = d.MASV
JOIN [dbo].[LoaiDiem] ld ON d.maloaidiem = ld.maLoaiDiem
WHERE ld.TenLoaiDiem = N'Quiz'
GROUP BY sv.MASV, sv.Ho, sv.TenLot, sv.Ten, ld.TenLoaiDiem
ORDER BY [Điểm Trung Bình] ASC;
--Mức 3
--11.	Lấy sinh viên có điểm Lab cao hơn điểm trung bình (tính trên điểm Lab toàn bộ sinh viên)
SELECT 
    ROUND(AVG(d.DiemSo), 2)    AS [Điểm TB Lab Toàn Bộ]
FROM [dbo].[Diem] d
JOIN [dbo].[LoaiDiem] ld ON d.maloaidiem = ld.maLoaiDiem
WHERE ld.TenLoaiDiem = N'Lab';