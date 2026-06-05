#!/bin/bash
# ============================================================
# 一键上传 GitHub 脚本
# Usage: bash upload-to-github.sh
# ============================================================

set -e

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

REPO_NAME="communication-growth-skill"
DEFAULT_USER="obsession-zhang"

echo ""
echo -e "${BLUE}╔══════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║     🚀 Communication Growth Skill - GitHub 一键上传     ║${NC}"
echo -e "${BLUE}╚══════════════════════════════════════════════════════════╝${NC}"
echo ""

# 检查 git
if ! command -v git &> /dev/null; then
    echo -e "${RED}❌ 错误：未安装 git${NC}"
    echo "请先安装 git: https://git-scm.com/downloads"
    exit 1
fi

# 检查 gh CLI
if ! command -v gh &> /dev/null; then
    echo -e "${YELLOW}⚠️ 未安装 GitHub CLI (gh)${NC}"
    echo "建议安装以简化流程: https://cli.github.com/"
    echo ""
    read -p "是否继续用 git 命令行方式上传? (y/n) " -n 1 -r
    echo ""
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
    USE_GH=false
else
    USE_GH=true
    # 检查登录状态
    if ! gh auth status &> /dev/null; then
        echo -e "${YELLOW}⚠️ 未登录 GitHub CLI${NC}"
        echo "运行: gh auth login"
        exit 1
    fi
fi

# 获取 GitHub 用户名
if [ "$USE_GH" = true ]; then
    GH_USER=$(gh api user -q .login 2>/dev/null || echo "")
    if [ -n "$GH_USER" ]; then
        DEFAULT_USER=$GH_USER
    fi
fi

# 询问仓库信息
echo ""
echo -e "${YELLOW}📋 请配置仓库信息:${NC}"
read -p "GitHub 用户名 [$DEFAULT_USER]: " USERNAME
USERNAME=${USERNAME:-$DEFAULT_USER}

read -p "仓库名称 [$REPO_NAME]: " REPO
REPO=${REPO:-$REPO_NAME}

read -p "仓库描述 [沟通成长计划 Skill - 输入聊天记录，输出缺陷分析与方法论修正]: " DESC
DESC=${DESC:-"沟通成长计划 Skill - 输入聊天记录，输出缺陷分析与方法论修正"}

read -p "是否设为私有仓库? (y/n) [n]: " -n 1 -r
echo ""
if [[ $REPLY =~ ^[Yy]$ ]]; then
    PRIVATE="--private"
    VISIBILITY="私有"
else
    PRIVATE="--public"
    VISIBILITY="公开"
fi

REMOTE_URL="https://github.com/$USERNAME/$REPO.git"

echo ""
echo -e "${BLUE}📦 配置确认:${NC}"
echo "  用户名: $USERNAME"
echo "  仓库:   $REPO"
echo "  可见性: $VISIBILITY"
echo "  URL:    $REMOTE_URL"
echo ""
read -p "确认上传? (y/n) " -n 1 -r
echo ""
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo -e "${YELLOW}已取消${NC}"
    exit 0
fi

# 初始化 git（如果不存在）
if [ ! -d .git ]; then
    echo -e "${BLUE}🔧 初始化 git 仓库...${NC}"
    git init
    git branch -M main
else
    echo -e "${BLUE}📁 已存在 git 仓库${NC}"
fi

# 配置 git 用户信息（如果未设置）
if [ -z "$(git config user.name)" ]; then
    git config user.name "$USERNAME"
fi
if [ -z "$(git config user.email)" ]; then
    git config user.email "$USERNAME@users.noreply.github.com"
fi

# 创建 .gitignore
echo -e "${BLUE}📝 创建 .gitignore...${NC}"
cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Project specific
*.zip
release/
EOF

# 添加所有文件
echo -e "${BLUE}➕ 添加文件到暂存区...${NC}"
git add -A

# 检查是否有变更
if git diff --cached --quiet; then
    echo -e "${YELLOW}⚠️ 没有需要提交的变更${NC}"
else
    # 提交
    echo -e "${BLUE}💾 提交变更...${NC}"
    git commit -m "🚀 feat: initial release of Communication Growth Skill v1.0.0

- 6-stage prompt pipeline for communication analysis
- 10-category weakness taxonomy
- Python tool suite (sanitizer, scorer, generator)
- 2 complete example scenarios (workplace + couple)
- Methodology library (DESC, Broken Record, NVC, BATNA, etc.)
- Pattern mining across conversations
- Growth planning with SMART goals
- GitHub Actions CI/CD + Issue templates

Core philosophy: reject people-pleasing, embrace healthy conflict,
objective rationality, methodology-driven feedback."
fi

# 创建远程仓库并推送
if [ "$USE_GH" = true ]; then
    echo -e "${BLUE}🌐 使用 GitHub CLI 创建远程仓库...${NC}"

    # 检查仓库是否已存在
    if gh repo view "$USERNAME/$REPO" &> /dev/null; then
        echo -e "${YELLOW}⚠️ 仓库已存在，直接推送...${NC}"
    else
        echo -e "${BLUE}📦 创建新仓库...${NC}"
        gh repo create "$REPO" $PRIVATE --description "$DESC" --source=. --remote=origin --push
        echo -e "${GREEN}✅ 仓库创建并推送完成！${NC}"
        echo ""
        echo -e "${GREEN}🎉 上传成功！${NC}"
        echo ""
        echo -e "${BLUE}📎 仓库地址: ${NC}https://github.com/$USERNAME/$REPO"
        echo -e "${BLUE}📦 下载命令: ${NC}git clone https://github.com/$USERNAME/$REPO.git"
        echo ""
        echo -e "${YELLOW}💡 接下来:${NC}"
        echo "  1. 访问 GitHub 页面设置 Topics (tags): communication, self-improvement, conflict"
        echo "  2. 在 README 顶部添加 GitHub badges"
        echo "  3. 打 tag 发布 Release: git tag v1.0.0 && git push origin v1.0.0"
        exit 0
    fi
fi

# 手动设置 remote
echo -e "${BLUE}🔗 设置远程仓库...${NC}"
if git remote | grep -q "origin"; then
    git remote set-url origin "$REMOTE_URL"
else
    git remote add origin "$REMOTE_URL"
fi

# 推送
echo -e "${BLUE}📤 推送到 GitHub...${NC}"
if git push -u origin main 2>/dev/null; then
    echo -e "${GREEN}✅ 推送成功！${NC}"
else
    echo -e "${YELLOW}⚠️ 推送失败，尝试用 token 或密码...${NC}"
    echo "请确保:"
    echo "  1. 已在 GitHub 创建仓库: https://github.com/new"
    echo "  2. 有推送权限（检查 SSH key 或 Personal Access Token）"
    echo ""
    echo -e "${BLUE}手动推送命令:${NC}"
    echo "  git push -u origin main"
fi

echo ""
echo -e "${GREEN}🎉 完成！${NC}"
echo -e "${BLUE}📎 仓库地址: ${NC}https://github.com/$USERNAME/$REPO"
echo ""
echo -e "${YELLOW}💡 建议下一步:${NC}"
echo "  1. 访问 GitHub 完善仓库信息"
echo "  2. 添加 Topics: communication, self-improvement, emotional-intelligence"
echo "  3. 发布 Release: git tag v1.0.0 && git push origin v1.0.0"
echo "  4. 分享给你的朋友！"
