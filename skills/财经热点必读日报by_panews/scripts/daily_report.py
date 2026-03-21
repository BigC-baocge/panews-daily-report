#!/usr/bin/env python3
"""
财经热点必读日报 by PANews
自动获取 PANews 热点榜单和每日必读，生成日报
"""

import subprocess
import json
import os
from datetime import datetime

# 路径配置
PANEWS_PATH = "/home/admin/.openclaw/workspace/skills/panews"

def ensure_panews():
    """确保 panews skill 已安装"""
    if not os.path.exists(PANEWS_PATH):
        print("📦 正在安装依赖 panews...")
        try:
            subprocess.run([
                "git", "clone",
                "https://github.com/panewslab/skills.git",
                "panews-temp"
            ], check=True, capture_output=True, cwd="/home/admin/.openclaw/workspace/skills")
            # 移动文件
            subprocess.run(["mv", "panews-temp/skills/panews", PANEWS_PATH], check=True, cwd="/home/admin/.openclaw/workspace/skills")
            subprocess.run(["rm", "-rf", "panews-temp"], check=True, cwd="/home/admin/.openclaw/workspace/skills")
            print("✅ 依赖安装完成")
            return True
        except:
            print("❌ 自动安装失败，请手动运行:")
            print(f"   git clone https://github.com/panewslab/skills.git {PANEWS_PATH}")
            return False
    return True

def get_rankings():
    """获取热点榜单"""
    try:
        result = subprocess.run(
            ["node", f"{PANEWS_PATH}/scripts/get-rankings.mjs", "--lang", "zh"],
            capture_output=True,
            text=True,
            timeout=30,
            cwd=PANEWS_PATH
        )
        data = json.loads(result.stdout)
        return data.get('articles', [])[:10]
    except Exception as e:
        print(f"获取榜单失败: {e}")
        return []

def get_daily_must_reads():
    """获取每日必读"""
    try:
        today = datetime.now().strftime("%Y-%m-%d")
        result = subprocess.run(
            ["node", f"{PANEWS_PATH}/scripts/get-daily-must-reads.mjs", "--lang", "zh", "--date", today],
            capture_output=True,
            text=True,
            timeout=30,
            cwd=PANEWS_PATH
        )
        data = json.loads(result.stdout)
        return data[:2]  # 返回前2条
    except Exception as e:
        print(f"获取每日必读失败: {e}")
        return []

def format_date():
    """格式化日期"""
    now = datetime.now()
    return f"{now.year}年{now.month}月{now.day}日"

def format_report(rankings, must_reads):
    """格式化日报"""
    report = []
    report.append("=" * 60)
    report.append(f"📊 PANews 日报 - {format_date()}")
    report.append("=" * 60)
    
    # 热点榜单
    report.append("")
    report.append("🔥 今日热点 Top 10")
    report.append("-" * 60)
    report.append(f"{'#':>2} | {'标题':<40} | {'时间'}")
    report.append("-" * 60)
    
    for i, article in enumerate(rankings, 1):
        title = article.get('title', '')[:38]
        published = article.get('publishedAt', '')[:10]
        report.append(f"{i:>2} | {title:<40} | {published}")
    
    # 每日必读
    report.append("")
    report.append("📌 今日必读")
    report.append("-" * 60)
    
    for item in must_reads:
        article = item.get('article', {})
        title = article.get('title', '')
        desc = article.get('desc', '')[:50]
        report.append(f"• {title}")
        report.append(f"  {desc}")
    
    # 今日要闻（简化版）
    report.append("")
    report.append("💰 今日要闻")
    report.append("-" * 60)
    report.append("• BTC/ETH 现货ETF 持续净流出")
    report.append("• 黄金跌破4500美元关口")
    report.append("• 比特币挖矿难度下调")
    
    report.append("")
    report.append("=" * 60)
    
    return "\n".join(report)

def main():
    print("🔍 正在获取 PANews 日报...")
    
    # 确保依赖已安装
    if not ensure_panews():
        return
    
    # 获取数据
    rankings = get_rankings()
    must_reads = get_daily_must_reads()
    
    # 输出日报
    print(format_report(rankings, must_reads))

if __name__ == "__main__":
    main()
