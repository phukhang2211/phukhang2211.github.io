---
title: "Quản lý nhiều chi nhánh, đồng bộ tồn kho & doanh thu trong Odoo"
categories: fnb
tags: [odoo, fnb, da-chi-nhanh, pos]
excerpt: "Setup nhiều quầy POS/chi nhánh dùng chung 1 database, so sánh doanh thu giữa các chi nhánh."
date: 2027-01-11
published: true
---

<!-- Bài 4/7 nhánh F&B — cho chủ quán đã mở rộng từ 1 lên nhiều điểm bán. -->

## Mục tiêu bài viết

Giúp chủ chuỗi 2-3 chi nhánh quản lý tập trung thay vì mỗi quán một sổ sách riêng.

## Nội dung cần có

- [ ] Cấu trúc Warehouse riêng cho từng chi nhánh, POS Config riêng nhưng chung Company
- [ ] Nguyên liệu điều chuyển giữa các chi nhánh (Internal Transfer)
- [ ] Giá bán có nên giống nhau giữa các chi nhánh hay khác theo khu vực
- [ ] Báo cáo so sánh doanh thu/lợi nhuận giữa các chi nhánh (Pivot theo Warehouse/POS Config)
- [ ] Phân quyền: nhân viên chi nhánh A không thấy được dữ liệu chi nhánh B
- [ ] Khi nào nên tách Company riêng thay vì dùng chung 1 Company nhiều Warehouse

## Tài liệu tham khảo

-
