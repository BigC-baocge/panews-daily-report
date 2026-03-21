# 财经热点必读日报 by PANews

自动获取 PANews 热点榜单和每日必读，生成加密货币/区块链行业日报。

---

## 触发方式

- 说"财经热点日报"
- 说"PANews 日报"
- 说"热点追踪"
- 说"生成日报"

---

## 功能说明

### 1. 热点榜单（24小时内）

自动获取 PANews 热度榜单 Top 10，按热度排序

### 2. 每日必读

获取当日 PANews 编辑精选的必读文章

### 3. 今日要闻

提取当日重要加密货币/区块链新闻：
- BTC/ETH ETF 资金流向
- 挖矿难度变化
- 重大融资事件
- 监管动态

---

## 输出模版

```
📊 PANews 日报 - YYYY年MM月DD日

🔥 今日热点 Top 10
| # | 标题 | 时间 | 类型 |
---|---|---|---
1 | xxx | MM-DD HH:MM | 类型 |

📌 今日必读
| 标题 | 摘要 |
---|---
xxx | xxx |

💰 今日要闻
| 热点 | 详情 |
---|---
xxx | xxx |

📈 市场情绪
| 指标 | 状态 |
---|---
xxx | xxx |
```

---

## 安装步骤

### 第1步：安装依赖 skill（PANews）

```bash
cd ~/.openclaw/workspace/skills
git clone https://github.com/panewslab/skills.git panews
```

### 第2步：安装主 skill

```bash
cd ~/.openclaw/workspace/skills
git clone https://github.com/BigC-baocge/财经热点必读日报by-panews.git
```

---

## 使用方法

```bash
# 直接运行
python3 ~/.openclaw/workspace/skills/财经热点必读日报by_panews/scripts/daily_report.py
```

---

## 依赖

- Python 3
- panews skill（必须先安装）

---

**最后更新**：2026-03-21  
**作者**：Jeff
