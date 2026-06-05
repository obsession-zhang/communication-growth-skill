# GitHub 发布指南

## 🚀 一键上传

```bash
cd communication-growth-skill
bash upload-to-github.sh
```

脚本会引导你：
1. 配置 GitHub 用户名和仓库名
2. 选择公开/私有
3. 自动初始化 git、提交、创建远程仓库、推送

## 📦 手动上传（备用）

### 方式一：GitHub CLI（推荐）

```bash
# 1. 安装 GitHub CLI
# macOS: brew install gh
# Linux: sudo apt install gh
# Windows: winget install --id GitHub.cli

# 2. 登录
gh auth login

# 3. 创建仓库并推送
gh repo create communication-growth-skill --public --source=. --push

# 4. 打 tag 发布 Release
git tag v1.0.0
git push origin v1.0.0
```

### 方式二：传统 Git

```bash
# 1. 在 GitHub 创建空仓库（不要初始化 README）
# https://github.com/new

# 2. 本地初始化
git init
git add -A
git commit -m "Initial release v1.0.0"
git branch -M main

# 3. 添加远程并推送
git remote add origin https://github.com/YOUR_USERNAME/communication-growth-skill.git
git push -u origin main

# 4. 打 tag 触发 Release Action
git tag v1.0.0
git push origin v1.0.0
```

## 🏷️ 发布 Release

打 tag 后会自动触发 GitHub Actions：
- 运行测试
- 打包 zip
- 创建 Release 并附带下载文件

```bash
git tag v1.0.0
git push origin v1.0.0
```

## 📎 仓库设置建议

上传后在 GitHub 页面设置：

1. **Topics (标签)**：`communication` `self-improvement` `emotional-intelligence` `conflict-resolution` `chat-analysis`
2. **Description**：沟通成长计划 Skill - 输入聊天记录/通话录音，输出缺陷分析与方法论修正
3. **Social Preview**：上传一张封面图（推荐尺寸 1280×640）
4. **Website**：可以填你的博客或文档站

## 🌟 推广建议

发布后可以分享到：
- V2EX / 即刻 / 小红书 / 公众号
- 技术社区：GitHub Trending、Product Hunt
- 相关社群：沟通/职场/自我提升类微信群

分享文案模板：

```
做了一个「沟通成长计划 Skill」，输入聊天记录/通话录音，
AI 帮你分析沟通缺陷，给出方法论级修正。

不鸡汤、不安慰、不贴标签。
拒绝老好人，拥抱冲突，客观理性。

GitHub: https://github.com/YOUR_USERNAME/communication-growth-skill

#沟通 #自我提升 #职场
```
