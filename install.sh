#!/bin/bash
# Communication Growth Skill - One-command installer
# Usage: bash install.sh

set -e

SKILL_NAME="communication-growth-skill"
INSTALL_DIR="${HOME}/.agents/skills/${SKILL_NAME}"

echo "🔧 Installing Communication Growth Skill..."

# Create directory
mkdir -p "${INSTALL_DIR}"

# Copy all files
cp -r . "${INSTALL_DIR}/"

# Make Python tools executable
chmod +x "${INSTALL_DIR}/tools/"*.py

echo "✅ Installed to ${INSTALL_DIR}"
echo ""
echo "📁 Structure:"
ls -la "${INSTALL_DIR}/"
echo ""
echo "🚀 Quick start:"
echo "  1. Paste your conversation into a text file"
echo "  2. python ${INSTALL_DIR}/tools/input_sanitizer.py your_chat.txt colleague 'request_resource' user_has_less"
echo "  3. python ${INSTALL_DIR}/tools/weakness_scorer.py output.json"
echo "  4. python ${INSTALL_DIR}/tools/report_generator.py structured.json weakness.json"
echo ""
echo "📖 Or manually run the 6 prompts in ${INSTALL_DIR}/prompts/"
echo ""
echo "💡 Remember: 沟通不是天赋，是手艺。"
