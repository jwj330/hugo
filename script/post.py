import os
import subprocess
import datetime

def main():
    # 确保内容目录存在
    os.makedirs('content/posts', exist_ok=True)
    
    # 生成时间戳文件名
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"content/posts/{timestamp}.md"
    
    # 创建新文章
    with open(filename, 'w') as f:
        f.write(f'''---
title: "文章 {timestamp}"
date: {datetime.datetime.now().isoformat()}
draft: false
---

## 自动生成的文章

这是由GitHub Actions自动生成的测试文章，时间戳: {timestamp}

### 功能说明
- 此文章通过工作流自动创建
- Hugo构建后部署到GitHub Pages
- 访问 https://jwj330.github.io 查看效果
''')
    
    print(f"✅ 新文章已创建: {filename}")
    print("🚀 工作流将自动构建并部署到GitHub Pages")

if __name__ == '__main__':
    main()
