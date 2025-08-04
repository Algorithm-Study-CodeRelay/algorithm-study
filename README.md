# 알고리즘 스터디

## 📁 폴더 구조

```
algorithm-study/
├── seojin/
│ ├── 2025-08-04_leetcode_123.py
│ └── ...
├── daewook/
│ ├── 2025-08-04_programmers_456.py
│ └── ...
```

- 각자의 폴더에 파일을 저장합니다.
- 파일 이름은 다음과 같이 작성합니다: `YYYY-MM-DD_플랫폼_문제이름.py`  
  예: `2025-08-04_leetcode_123.py`



## 브랜치 / PR / 리뷰 진행 방식

1. **브랜치 생성**

   ```bash
   git checkout main
   git pull origin main
   git checkout -b daewook/2025-08-04
   ```

2. **문제 풀이**

   ```bash
   daewook/2025-08-04_leetcode_123.py
   ```

3. **커밋 & 푸시**

   ```bash
   git add .
   git commit -m "feat: 2025-08-04 LeetCode 123 문제 풀이"
   git push origin daewook/2025-08-04
   ```

4. **GitHub에서 PR 생성** : PR을 만들면 자동으로 PR 템플릿이 생성되며, 문제 요약, 코드 설명, 리뷰 요청사항을 작성합니다.

   ```
   base: `main`
   compare: `본인 브랜치`
   reviewer: 상대방
   ```

5. **코드 리뷰**: 상대방은 PR의 코드 탭에서 줄 단위로 코멘트를 남기고, Approve 또는 Request changes를 선택합니다.

- 리뷰 시 고려할 사항

  ```
  ✔ 코드가 실행 가능하고, 예외 상황을 고려했는가?

  ✔ 알고리즘이 효율적인가?

  ✔ 변수명과 함수명이 명확한가?

  ✔ 중복 코드 없이 깔끔한가?
  ```

6. **Merge** : **리뷰어가 직접 Merge**를 진행합니다.

- PR 작성자는 코드 리뷰를 기다립니다.
- 리뷰어는 `Approve`를 누른 뒤 → GitHub에서 Merge 버튼을 클릭합니다.
- 머지 후, PR 작성자는 `main` 브랜치를 pull 받아 로컬을 최신 상태로 유지합니다

   ```bash
   git checkout main
   git pull origin main
   ```
