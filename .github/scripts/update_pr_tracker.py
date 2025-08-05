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
    if user == "github-actions[bot]":
        continue
    date_str = pr["created_at"][:10]
    activity[date_str][user] = "✅"
    # 아바타 저장
    if user not in user_avatars:
        user_avatars[user] = pr["user"]["avatar_url"]

# 최근 30일 날짜 리스트 생성 (created_at 기준)
today = datetime.utcnow().date()
all_dates = [str(today - timedelta(days=i)) for i in range(14, -1, -1)]

# 유저 목록 (PR 한 사람 기준)
all_users = sorted({u for d in activity.values() for u in d})

header_cells = []
for u in all_users:
    avatar = user_avatars.get(u, "")
    avatar_md = f"![]({avatar}&s=20)<br/>{u.capitalize()}" if avatar else u.capitalize()
    header_cells.append(avatar_md)

# 테이블 생성
lines = [
    "| Date       | " + " | ".join(header_cells) + " |",
    "|------------|" + "|".join([":---:" for _ in all_users]) + "|"
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
