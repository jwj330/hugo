import os
import subprocess
import datetime
import re

def update_config(config_path, key, value):
    """更新或添加配置项到 config.toml"""
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            content = f.read()
    else:
        content = ""
    
    # 检查键是否已存在
    pattern = rf'^{key}\s*=\s*["\'](.*)["\']'
    match = re.search(pattern, content, re.MULTILINE)
    
    if match:
        # 替换现有值
        new_content = re.sub(pattern, f'{key} = "{value}"', content, flags=re.MULTILINE)
    else:
        # 添加新键值对
        new_content = content + f'\n{key} = "{value}"\n'
    
    with open(config_path, 'w') as f:
        f.write(new_content)

def main():
    print("🚀 开始初始化 Hugo 站点...")
    
    # 初始化 Hugo 站点（如果尚未初始化）
    if not os.path.exists('config.toml'):
        print("📝 创建新的 Hugo 站点...")
        subprocess.run(['hugo', 'new', 'site', '.', '--force'], check=True)
    
    # 添加默认主题 (Ananke)
    if not os.path.exists('themes/ananke'):
        print("🎨 添加 Ananke 主题...")
        subprocess.run(['git', 'submodule', 'add', 
                       'https://github.com/theNewDynamic/gohugo-theme-ananke.git', 
                       'themes/ananke'], check=True)
    
    # 更新配置文件
    config_path = 'config.toml'
    
    # 设置基本配置
    update_config(config_path, 'baseURL', 'https://jwj330.github.io/')
    update_config(config_path, 'languageCode', 'zh-cn')
    update_config(config_path, 'title', '我的 Hugo 博客')
    update_config(config_path, 'theme', 'ananke')
    
    # 创建欢迎页面
    content_dir = 'content'
    os.makedirs(content_dir, exist_ok=True)
    
    welcome_path = os.path.join(content_dir, '_index.md')
    with open(welcome_path, 'w') as f:
        f.write(f'''---
title: "欢迎来到我的博客"
date: {datetime.datetime.now().isoformat()}
draft: false
---

## 站点初始化成功！

您的 Hugo 站点已准备就绪，可以开始添加内容了。

- 主题: Ananke
- 部署平台: GitHub Pages
- 站点地址: https://jwj330.github.io
''')
    
    # 构建静态文件
    print("🔨 构建静态文件...")
    subprocess.run(['hugo', '--minify'], check=True)
    
    # 检查是否生成了 index.html
    if os.path.exists('public/index.html'):
        print("✅ 初始化完成！index.html 已生成")
    else:
        print("❌ 错误：index.html 未生成")
        # 列出 public 目录的内容以帮助调试
        if os.path.exists('public'):
            print("public 目录内容:")
            for item in os.listdir('public'):
                print(f"  - {item}")
    
    print("📋 下一步：检查 GitHub Pages 仓库是否有内容")

if __name__ == '__main__':
    main()
