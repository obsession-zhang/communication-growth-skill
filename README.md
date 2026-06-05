# 🎯 Communication Growth Skill

> **你的聊天记录和通话录音，是你最被忽视的成长素材。**
>
> 大多数人从不回看自己说了什么。他们重复同样的错误：太好说话、回避冲突、该直接时绕弯子、该冷静时情绪化。这个 Skill 把你的原始对话数据，变成一份**毫不留情、方法论扎实**的沟通成长报告。

---

## 一句话介绍

输入聊天记录 / 通话录音转文字 → 输出一份**指出沟通缺陷 + 给出方法论级修正**的成长报告。

风格：**拒绝老好人，不怕冲突，客观理性，方法论导向。**

---

## 为什么你需要这个

你有没有过这些时刻：

- 聊完之后越想越气，觉得自己**没发挥好**
- 明明占理，结果**越解释越被动**
- 对方提了个不合理要求，你**下意识就说"好"**
- 本来想拒绝，结果**绕了八百圈还在绕**
- 情绪上头，**说了后悔的话**
- 对方在**试探你的边界**，你**假装没感觉到**

这些不是"性格问题"。这是**沟通技能的缺陷**，而且可以被训练。

这个 Skill 不做心理咨询，不给鸡汤，不帮你"被所有人喜欢"。它只做一件事：**把你的对话拆开，告诉你哪里烂了，以及怎么修。**

---

## 核心特点

| 特点 | 说明 |
|------|------|
| 🔪 **拒绝老好人** | 不教你"如何让人舒服"，教你"如何让人尊重" |
| ⚔️ **拥抱冲突** | 区分"破坏性冲突"和"建设性冲突"，后者是技能 |
| 🧠 **客观理性** | 用策略价值评价话语，不用情绪舒适度 |
| 📐 **方法论导向** | 每处缺陷都有**具体改写 + 底层逻辑**，不是"你情商低了"这种废话 |
| 🔁 **模式识别** | 跨对话提取你的**重复性沟通 DNA**，治标更治本 |

---



---

## 📥 下载与安装

### 方式一：GitHub 下载（推荐）

```bash
# 克隆仓库
git clone https://github.com/obsession-zhang/communication-growth-skill.git

# 进入目录
cd communication-growth-skill

# 一键安装
bash install.sh
```

### 方式二：Release 下载

访问 [Releases 页面](https://github.com/obsession-zhang/communication-growth-skill/releases) 下载最新版本的 zip 包。

### 方式三：一键上传到你自己仓库

```bash
cd communication-growth-skill
bash upload-to-github.sh
```

按提示输入你的 GitHub 用户名即可一键创建仓库并上传。

---
## 快速开始

### 方式一：一键安装（推荐）

```bash
git clone https://github.com/obsession-zhang/communication-growth-skill.git
cd communication-growth-skill
bash install.sh
```

### 方式二：手动使用 Prompt

1. 把聊天记录或通话录音转文字，粘贴到 `examples/input-template.txt`
2. 按顺序运行 6 个 Prompt（见 `prompts/` 目录）
3. 最终输出一份完整报告

### 方式三：Python 工具链

```bash
# 预处理 + 分析 + 生成报告，一条命令
python tools/run_pipeline.py --input my_chat.txt --output report.md
```

---

## 报告长什么样

一份完整的沟通成长报告包含：

### 01 对话拆解
逐轮分析：你说了什么 → 对方接收了什么 → 你**应该**说什么 → 为什么

### 02 缺陷分类
把你的问题按 10 个维度归类：
- 🟡 过度软弱（ excessive softness ）
- 🔴 情绪劫持（ emotional hijack ）
- 🟣 结构混乱（ structural chaos ）
- 🔵 回避冲突（ conflict avoidance ）
- 🟢 过度解释（ over-explaining ）
- 🟠 主张不足（ under-asserting ）
- ⚫ 读不懂空气（ tone deafness ）
- ⚪ 战略盲区（ strategic blindness ）
- 🟤 互惠失败（ reciprocity failure ）
- 🔘 边界崩塌（ boundary collapse ）

### 03 方法论修正
**原文**："那个...不好意思，我想问一下，这个需求能不能稍微改一下？"

**问题诊断**：
- 三重道歉前缀（"那个...不好意思...想问一下"）
- "能不能" 把主动权交给对方
- "稍微" 弱化了自己的合理性
- 整体传递："我知道我不该提这个要求"

**最优改写**："这个需求变更会影响交付节奏，我需要确认两点：一是优先级，二是资源补偿。我们 5 分钟后对齐？"

**底层逻辑**：
- 陈述事实，不道歉
- 把开放式问题变成封闭式选择
- 设定时间边界，防止无限拖延
- 用"我需要"而非"能不能"，夺回话语权

### 04 模式识别
跨 3-5 次对话后，提取你的**重复性模式**：
> "你在面对上级时，有 73% 的概率使用弱化前缀（'可能/也许/想请问'）。这不是礼貌，这是权力让渡。"

### 05 成长计划
按优先级排序的**可执行训练项**：
1. **本周**：删除所有消息中的弱化前缀（练习 50 条）
2. **本月**：在 3 次对话中主动发起一次建设性冲突
3. **本季**：建立"拒绝话术库"，覆盖 80% 常见不合理请求

---

## 示例

| 场景 | 输入 | 输出报告 |
|------|------|----------|
| 职场撕逼 | [example-work-chat.txt](examples/example-work-chat.txt) | [example-work-report.md](examples/example-work-report.md) |
| 亲密关系 | [example-couple-chat.txt](examples/example-couple-chat.txt) | [example-couple-report.md](examples/example-couple-report.md) |

---

## 技术栈

- **Prompt Engineering**: 6 阶段分析流水线
- **Python Tools**: 文本预处理、缺陷评分、报告生成
- **Markdown**: 纯文本输出，随处可读

---

## 贡献

欢迎提交：
- 新的对话场景示例
- 更精准的缺陷分类
- 更锋利的修正话术
- 跨文化沟通适配

详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

---

## 许可

MIT License — 拿去用，拿去改，拿去赚钱，不用问我。

---

> **最后一句：** 沟通不是天赋，是手艺。手艺可以练。这个 Skill 是你的砂纸。
