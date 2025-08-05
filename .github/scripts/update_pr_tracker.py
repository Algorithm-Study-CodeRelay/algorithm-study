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

# 최근 30일 날짜 리스트 생성 (created_at 기준)
today = datetime.utcnow().date()
all_dates = [str(today - timedelta(days=i)) for i in range(29, -1, -1)]  # 오래된 날짜부터

# 유저 목록 (PR 한 사람 기준)
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

# README 업데이트 (마커 기준)
with open("README.md", "r") as f:
    content = f.read()

start_marker = "<!--PR_TABLE_START-->"
end_marker = "<!--PR_TABLE_END-->"

start = content.find(start_marker) + len(start_marker)
end = content.find(end_marker)

new_table = "\n" + "\n".join(lines) + "\n"
updated = content[:start] + new_table + content[end:]

with open("README.md", "w") as f:
    f.write(updated)
