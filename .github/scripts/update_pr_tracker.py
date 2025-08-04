import requests
from collections import defaultdict
from datetime import datetime, timedelta
import os

REPO = os.getenv("GITHUB_REPOSITORY", "your-org/algorithm-study")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # 자동 설정됨
HEADERS = {"Authorization": f"Bearer {GITHUB_TOKEN}"}
API_URL = f"https://api.github.com/repos/{REPO}/pulls?state=closed&per_page=100"

# 날짜별 사용자별 PR 기록
activity = defaultdict(lambda: defaultdict(str))

def get_prs():
    r = requests.get(API_URL, headers=HEADERS)
    r.raise_for_status()
    return r.json()

prs = get_prs()

for pr in prs:
    if not pr["merged_at"]:
        continue  # 병합 안된 PR 제외

    user = pr["user"]["login"].lower()
    date_str = pr["created_at"][:10]
    activity[date_str][user] = "✅"

# 날짜 정렬
all_dates = sorted(activity.keys())
all_users = sorted({u for d in activity.values() for u in d})

# 테이블 생성
lines = [
    "| Date       | " + " | ".join(u.capitalize() for u in all_users) + " |",
    "|------------|" + "|".join(["-------"] * len(all_users)) + "|"
]

for date in all_dates:
    row = [date]
    for user in all_users:
        row.append(activity[date].get(user, "❌"))
    lines.append("| " + " | ".join(row) + " |")

# README 업데이트
with open("README.md", "r") as f:
    content = f.read()

start = content.find("| Date")
end = content.find("\n", content.find("---", start))

new_table = "\n".join(lines)
updated = content[:start] + new_table + content[end:]

with open("README.md", "w") as f:
    f.write(updated)
