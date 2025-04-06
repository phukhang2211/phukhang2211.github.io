---
layout: documentation
title: "Installing Odoo"
date: 2025-04-06
categories: odoo tutorial
tags: [installation, setup, odoo]
excerpt: "A comprehensive guide to installing Odoo"
---

# Installing Odoo

## Prerequisites
- Python 3.7 or later
- PostgreSQL
- Node.js and npm
- Git

## Installation Steps

### 1. System Dependencies
```bash
# Update system
sudo apt update
sudo apt upgrade
```

### 2. PostgreSQL Setup
```bash
sudo apt install postgresql
sudo -u postgres createuser -s $USER
```

### 3. Python Dependencies
```bash
# Install Python dependencies
sudo apt install python3-pip python3-dev python3-venv
python3 -m venv odoo-venv
source odoo-venv/bin/activate
```

### 4. Clone Odoo
```bash
git clone https://github.com/odoo/odoo.git
cd odoo
git checkout 16.0  # or your desired version
```

### 5. Install Requirements
```bash
pip install -r requirements.txt
```

### 6. Configuration
Create a configuration file:
```bash
cp debian/odoo.conf /etc/odoo.conf
```

Edit the configuration:
```ini
[options]
admin_passwd = your_admin_password
db_host = localhost
db_port = 5432
db_user = your_user
db_password = your_password
```

### 7. Run Odoo
```bash
python3 odoo-bin -c /etc/odoo.conf
```

## Verification
- Access http://localhost:8069
- Create a new database
- Login with admin credentials

## Next Steps
1. Set up development environment
2. Create your first module
3. Configure security settings

## Common Issues
- Database connection errors
- Port conflicts
- Permission issues
- Python dependency conflicts