#!/bin/bash

# 创建根目录
mkdir -p app

# 创建根目录下的文件
touch app/main.py
touch app/config.py

# 创建 utils 目录及其文件
mkdir -p app/utils
touch app/utils/__init__.py
touch app/utils/http_client.py

# 创建 api 目录及其文件
mkdir -p app/api
touch app/api/__init__.py
touch app/api/message.py
touch app/api/login.py
touch app/api/personal.py
touch app/api/group.py
touch app/api/label.py
touch app/api/favor.py
touch app/api/download.py
touch app/api/contact.py

# 创建 routers 目录及其文件
mkdir -p app/routers
touch app/routers/__init__.py
touch app/routers/message.py
touch app/routers/login.py
touch app/routers/personal.py
touch app/routers/group.py
touch app/routers/label.py
touch app/routers/favor.py
touch app/routers/download.py
touch app/routers/contact.py

# 输出成功信息
echo "App directory structure created successfully!"