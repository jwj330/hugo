import os
import subprocess
import datetime

def main():
    # 初始化Hugo站点
    if not os.path.exists('config.toml'):
        subprocess.run(['hugo', 'new', 'site', '.', '--force'], check=True)
    
    # 添加默认主题 (Ananke)
    if not os.path.exists('themes/ananke'):
        subprocess.run(['git', 'submodule', 'add', 
                       'https://github.com/theNewDynamic/gohugo-theme-ananke', 
                       'themes/ananke'], check=True)
    
    # 配置主题
    with open('config.toml', 'a') as f:
        f.write('\ntheme = "ananke"\n')
    
    # 创建欢迎页面
    if not os.path.exists('content/_index.md'):
        subprocess.run(['hugo', 'new', '_index.md'], check=True)
        with open('content/_index.md', 'w') as f:
            f.write('''---
title: "欢迎来到我的博客"
date: %s
draft: false
---

### 站点初始化成功！
您的Hugo站点已准备就绪，可以开始添加内容了。
''' % datetime.datetime.now().isoformat())
    
    # 构建静态文件
    subprocess.run(['hugo', '--minify'], check=True)
    print("✅ 初始化完成！静态文件已生成到public目录")

if __name__ == '__main__':
    main()
