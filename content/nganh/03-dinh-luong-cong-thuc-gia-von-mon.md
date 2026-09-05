---
title: "Định lượng công thức (BOM) và tính giá vốn món ăn trong Odoo"
date: 2026-09-05
draft: false
categories: [fnb]
tags: [odoo, fnb, manufacturing, gia-von]
description: "Dùng Bill of Materials để định lượng nguyên liệu mỗi món, tự động trừ kho và ra giá vốn thực tế."
---

<!-- Bài 3/7 nhánh F&B — đây là mảng chuyên sâu ít tutorial nào nói tới: dùng app
     Manufacturing (BoM) cho ngành dịch vụ ăn uống chứ không chỉ sản xuất. -->

## Mục tiêu bài viết

Trả lời câu hỏi mọi chủ quán đều hỏi: "1 ly cà phê này tốn bao nhiêu tiền nguyên liệu, lời bao nhiêu?"

## Nội dung cần có

- [ ] Vì sao dùng Bill of Materials (BOM) cho món ăn/đồ uống dù không phải nhà máy
- [ ] Setup nguyên liệu là sản phẩm Storable, món bán là sản phẩm có BOM
- [ ] Định lượng: 1 ly cà phê sữa = X gram cà phê + Y ml sữa + Z gram đường
- [ ] Kết nối bán hàng ở POS → tự động trừ nguyên liệu trong kho theo BOM
- [ ] Tính giá vốn (Cost) tự động từ BOM, so sánh với giá bán ra lợi nhuận từng món
- [ ] Xử lý hao hụt nguyên liệu thực tế (đổ bỏ, làm hỏng) — Scrap trong Odoo
- [ ] Báo cáo món nào lời nhất/lỗ nhất

## Tài liệu tham khảo

-
