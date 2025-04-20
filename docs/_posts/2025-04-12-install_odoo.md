---
layout: documentation
title: "Cài đặt debug Odoo cho máy Windows bằng WSL"
date: 2025-04-19
categories: odoo tutorial
tags: [installation, setup, odoo]
excerpt: "A comprehensive guide to installing Odoo"
---

# Cài đặt debug Odoo cho máy Windows bằng WSL

## Cài đặt WSL

Theo hướng dẫn của Microsoft ([WSL Installation Guide](https://learn.microsoft.com/en-us/windows/wsl/install)), thực hiện các bước sau:

1. Cài đặt WSL:
```bash
wsl --install
```

2. Khởi động lại máy để kích hoạt WSL

3. Cài đặt Ubuntu 24.04 LTS:
```bash
wsl.exe --install Ubuntu-24.04
```

4. Chạy Ubuntu từ Start Menu để thiết lập username và password

## Cài đặt phần mềm cần thiết

### Trên Windows
- Visual Studio Code, PyCharm, hoặc Cursor AI editor

### Trên WSL (Ubuntu)
Theo hướng dẫn của [Odoo Documentation](https://www.odoo.com/documentation/18.0/administration/on_premise/source.html)

1. Cập nhật hệ thống:
```bash
sudo apt update
sudo apt upgrade -y
```

2. Cài đặt PostgreSQL:
```bash
sudo apt install postgresql postgresql-client
```

3. Thiết lập database user:
```bash
sudo -u postgres createuser -d -R -S $USER
createdb $USER
```

## Cài đặt Odoo

1. Tạo thư mục làm việc:
```bash
mkdir 18odoo
cd 18odoo
mkdir custom_addons
```

2. Clone source code Odoo (Community Edition):
```bash
git clone https://github.com/odoo/odoo.git --branch 18.0 --depth 1 --single-branch odoo-server
```

3. Cài đặt các dependency:
```bash
sudo apt install -y python3.12-venv build-essential python3-dev libpq-dev libsasl2-dev libldap2-dev
```

4. Tạo và kích hoạt môi trường ảo Python:
```bash
python3 -m venv venv
source venv/bin/activate
```

5. Cài đặt Python packages:
```bash
pip3 install -r odoo-server/requirements.txt
```

6. Cài đặt các gói hệ thống cần thiết:
```bash
cd odoo-server
sudo ./setup/debinstall.sh
```

7. Cài đặt wkhtmltopdf dùng để in PDF:

## Cài đặt library libssl1.1
```bash
echo "deb http://security.ubuntu.com/ubuntu focal-security main" | sudo tee /etc/apt/sources.list.d/focal-security.list
sudo apt update
sudo apt install libssl1.1
```

## Cài đặt wkhtmltopdf
```bash
wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.5/wkhtmltox_0.12.5-1.focal_amd64.deb
sudo apt install ./wkhtmltox_0.12.5-1.focal_amd64.deb
```

## Kiểm tra cài đặt

Chạy thử Odoo:
```bash
python3 odoo-bin --addons-path=addons -d mydb
```

Truy cập [http://localhost:8069](http://localhost:8069) để kiểm tra.

## Cấu hình Debug

1. Tạo file `odoo.conf`:

```ini
[options]
admin_passwd = 1
db_host = False
db_port = False
db_user = wsl-user
db_password = False
addons_path = /home/wsl-user/18odoo/odoo-server/addons,/home/wsl-user/18odoo/custom_addons
```

2. Chạy Odoo với file config:
```bash
python3 odoo-bin -c /home/wsl-user/18odoo/odoo.conf
```

## Thiết lập VS Code với WSL

1. Kết nối VS Code với WSL:
   - Click vào biểu tượng `><` ở góc trái bên dưới
   - Chọn "Remote" và cài đặt WSL
   - Chọn "Open Folder" và mở thư mục `18odoo`

![Kết nối VS Code với WSL](/vscode_connect_wsl.png)

2. Cài đặt Python Debugger từ Extensions Marketplace

3. Tạo file `launch.json`:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "v18",
            "type": "debugpy",
            "request": "launch",
            "stopOnEntry": false,
            "python": "/home/wsl-user/18odoo/venv/bin/python3",
            "console": "integratedTerminal",
            "program": "${workspaceRoot}/odoo-server/odoo-bin",
            "args": [
                "--config=${workspaceRoot}/odoo.conf"
                // "--dev=xml",
                // "--database=mydb",
            ],
            "cwd": "${workspaceRoot}",
            "env": {
                "VIRTUAL_ENV": "/home/wsl-user/18odoo/venv",
                "PATH": "/home/wsl-user/18odoo/venv/bin:${env:PATH}",
                "PYDEVD_DISABLE_FILE_VALIDATION": "1"
            },
            "envFile": "${workspaceRoot}/.env",
            "justMyCode": false,
            "pythonArgs": [
                "-Xfrozen_modules=off"
            ]
        }
    ]
}
```

## Bắt đầu Debug

- Click nút chạy để bắt đầu debug
- Sử dụng nút restart để áp dụng các thay đổi Python code
- Thêm `--dev=xml` vào file config để tự động cập nhật code XML trong custom addons khi restart

Bây giờ bạn có thể bắt đầu tạo custom addons cho Odoo!