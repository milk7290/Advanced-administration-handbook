# 사진 즉석 인쇄 (YHK/WalkPrint 계열 BLE 프린터)

손님이 촬영하면 블루투스(BLE) 라벨프린터로 바로 인쇄하는 웹앱입니다. 단일 `index.html`이며 외부 의존성이 없습니다
(로고·날짜 글꼴도 파일 안에 내장되어 있어 **인터넷 없이** 동작합니다).

## 파일 종류
- `index.html` : 밥테일베이커리용(로고 내장)
- `index.public.html` : **배포용**. 밥테일 로고가 없고 상호명 글자가 기본입니다. 받은 매장은 ⚙ 설정에서 **상호명**을 입력하거나 **로고 변경**으로 자기 로고를 올리면 됩니다.
  (`python3 make_public.py`로 `index.html`에서 다시 만들 수 있어요. Pillow 필요)

## 사용법
- 손님: 장수 선택 → 📸 사진 찍기 → 인쇄 → "출력 완료" 후 사진을 뜯고 확인 → (다음 장)
- 관리자: 오른쪽 위 ⚙ → 비밀번호 `1234` → 프린터 연결, 로고/날짜/농도/대기시간 등 설정

## 실행 환경
Web Bluetooth/카메라는 **HTTPS 또는 `http://localhost`** 에서만 동작합니다.

| 기기 | 방법 |
|------|------|
| 안드로이드 | Chrome |
| 아이폰 | Bluefy 앱(App Store) |

## 안드로이드에서 인터넷 없이 쓰기 (Termux 로컬 서버)
`http://localhost` 는 보안 컨텍스트로 취급되어 블루투스/카메라가 허용됩니다.

1. (최초 1회, 인터넷 필요) F-Droid(f-droid.org)에서 **Termux** 설치
2. `index.html` 을 폰의 Download 폴더에 복사
3. Termux에서:
   ```sh
   pkg install python
   termux-setup-storage            # 저장소 권한 허용
   mkdir -p ~/app && cp ~/storage/downloads/index.html ~/app/
   cd ~/app && python -m http.server 8080
   ```
4. Chrome에서 `http://localhost:8080/` 열기 → 메뉴 → 홈 화면에 추가
5. 이후 사용할 때마다 Termux에서 `cd ~/app && python -m http.server 8080` 만 다시 실행
   (Termux 알림의 *Acquire wakelock* 을 켜고, 폰 설정에서 Termux 배터리 사용을 "제한 없음"으로 두세요)

## 배포 시 안내(받는 매장용)
1. 파일을 열고 ⚙ → 비밀번호 `1234` → **상호명** 입력(또는 로고 변경) → **비밀번호 변경**
2. 프린터 연결(YHK/WalkPrint 계열 BLE 프린터) → 테스트 인쇄
3. 다른 모델의 프린터는 인쇄 명령이 달라 동작하지 않을 수 있습니다.
