#!/bin/bash

# 部署脚本 - 使用GitHub token推送代码

echo "🚀 开始部署网站到GitHub Pages..."

# 检查token文件是否存在
if [ ! -f "github_token.txt" ]; then
    echo "❌ 错误：找不到 github_token.txt 文件"
    echo "请先创建 github_token.txt 文件并添加你的GitHub token"
    exit 1
fi

# 读取token
TOKEN=$(grep "GITHUB_TOKEN=" github_token.txt | cut -d'=' -f2)

# 检查token是否已设置
if [ "$TOKEN" = "YOUR_GITHUB_TOKEN" ] || [ -z "$TOKEN" ]; then
    echo "❌ 错误：请在 github_token.txt 文件中设置你的GitHub token"
    echo "将 YOUR_GITHUB_TOKEN 替换为你的实际token"
    exit 1
fi

echo "✅ Token已读取"

# 添加所有文件
echo "📁 添加文件到Git..."
git add .

# 提交更改
echo "💾 提交更改..."
git commit -m "Update portfolio website"

# 使用token推送
echo "🚀 推送到GitHub..."
git push https://shaozhang1861:${TOKEN}@github.com/shaozhang1861/websites.git main

echo "✅ 部署完成！"
echo "🌐 你的网站地址：https://shaozhang1861.github.io/websites"
echo "⏰ 请等待几分钟让GitHub Pages完成部署"
