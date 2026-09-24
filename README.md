# 순간 — kgirls 사진 갤러리

ChatGPT 계정, 외부 API, 유료 저장 공간 없이 동작하는 정적 홈페이지입니다.
소스와 사진을 GitHub 공개 저장소에 보관하며, GitHub Pages의 현재 무료 한도 내에서 운영합니다. 영구 무료를 보장하지는 않습니다.

## 처음 공개하기
1. GitHub에 `kgirls`라는 공개 저장소를 만듭니다. 기본 브랜치는 `main`으로 둡니다.
2. 이 폴더 안의 파일과 폴더를 모두 올립니다. `.github/workflows/pages.yml`도 포함해야 합니다. `.env`나 기존 ChatGPT 서버 파일은 올리지 않습니다.
3. 저장소 Settings → Pages → Build and deployment → Source를 **GitHub Actions**로 선택합니다.
4. Actions → Publish photo gallery → Run workflow로 실행합니다.
5. 작업이 성공하면 Settings → Pages에 실제 주소가 표시됩니다. 보통 `https://계정이름.github.io/kgirls/`입니다.

## 사진 추가
1. 저장소의 `photos` 폴더를 엽니다.
2. Add file → Upload files로 JPG, PNG, WebP, AVIF, GIF 파일을 올립니다.
3. Commit changes를 누르면 갤러리가 다시 만들어지고 게시됩니다.
4. 갤러리는 파일 이름순으로 정렬됩니다. 순서를 정하려면 `001-바다.jpg`, `002-산.jpg`처럼 이름을 붙입니다.

파일 이름에서 확장자를 뺀 부분이 사진 제목이 됩니다. 별도의 제목을 원하면 `captions.json`에 `{"001-바다.jpg":"바닷가의 오후"}`와 같이 적습니다.
하위 폴더도 지원합니다. 이 경우 캡션 키는 `여행/001-바다.jpg`처럼 작성합니다.
사진을 삭제하려면 `photos`에서 해당 파일을 삭제하고 변경 사항을 저장합니다.

사진 원본과 코드가 공개 저장소에 공개됩니다. 공개할 사진만 올려주세요. 사이트 전체 크기는 GitHub Pages 한도인 1GB 이하로 유지하세요.

## 컴퓨터에서 확인
Python 3가 있는 환경에서 `python3 build.py`를 실행한 뒤 `_site/index.html`을 열면 됩니다.
외부 CDN이나 API에 접속하지 않으며 저장소 하위 경로에서도 작동합니다.

## 이전 상태
GitHub Pages에서 독립적으로 운영하도록 구성되어 있습니다.
기존 Sites의 공개 사진 목록을 확인했으며 현재 등록된 사진은 0장입니다. 이후 사진이 추가되었다면 이전 전에 다시 확인해야 합니다.
기존 사이트는 새 사이트 공개 및 사진 확인이 끝날 때까지 유지합니다.
