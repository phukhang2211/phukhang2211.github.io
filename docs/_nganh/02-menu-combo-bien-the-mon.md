---
title: "Cấu hình menu, combo và biến thể món trong Odoo POS cho quán F&B"
categories: fnb
tags: [odoo, fnb, pos, menu]
excerpt: "Setup menu nhiều size/topping, combo, món theo khung giờ trong Odoo POS."
date: 2026-12-28
published: true
---

<!-- Bài 2/7 nhánh F&B — chuyên sâu, không lặp lại setup POS cơ bản, xem [[13-cau-hinh-pos-ban-le]] bên tutorials trước. -->

## Mục tiêu bài viết

Giải quyết bài toán riêng của F&B: 1 món có nhiều size/topping/độ ngọt, bán theo combo, đổi menu theo khung giờ (sáng/trưa/tối).

## Nội dung cần có

- [ ] Product Variants cho size/topping/độ đường-đá — vì sao nên dùng variant thay vì tạo sản phẩm riêng lẻ
- [ ] Combo/set món: dùng Combo Choice (nếu bản Odoo hỗ trợ) hoặc kit sản phẩm
- [ ] Menu theo khung giờ: dùng POS Category kết hợp ẩn/hiện sản phẩm, hoặc nhiều POS Config cho từng ca
- [ ] Giá bán khác nhau giữa mang đi/tại chỗ/giao hàng — dùng Pricelist hay Fiscal Position
- [ ] Note ghi chú món (ít đường, không đá) — Order Line notes trong POS
- [ ] Lỗi thường gặp khi setup biến thể quá nhiều (quản lý tồn kho theo variant phức tạp)

## Tài liệu tham khảo

-
