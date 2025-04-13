---
layout: documentation
title: "Installing Odoo"
date: 2025-04-06
categories: odoo tutorial
tags: [installation, setup, odoo]
excerpt: "A comprehensive guide to installing Odoo"
---

# Installing Odoo

Để bắt đầu cài đặt Odoo, người dùng có thể thực hiện theo các trường hợp dưới đây:

1. **Người dùng thử:** Cài đặt lên cloud server.
2. **Lập trình viên debug:** Cài đặt môi trường để debug.
3. **Lập trình viên local:** Chạy container local.

## Phần 1: Cloud Server

Ưu điểm: Cài đặt nhanh và có thể dùng cho live production.

### Phương pháp 1: Cài bằng bash script

- **Cài Odoo:** [Yenthe666/InstallScript](https://github.com/Yenthe666/InstallScript/blob/17.0/README.md)
- **Cài nginx**

### Phương pháp 2: Cài docker compose

- **Cài docker Odoo:** [minhng92/odoo-18-docker-compose](https://github.com/minhng92/odoo-18-docker-compose)
- **Cài nginx proxy manager hoặc nginx**

## Phần 2: Cài ở máy local

- **Cài bằng Odoo file exe từ website của Odoo**
- **Download source code và debug bằng VS Code**
- **Cài đặt Odoo trong WSL trên Windows và kết nối bằng VS Code**
- **Cài đặt Odoo trong container để debug bằng VS Code**