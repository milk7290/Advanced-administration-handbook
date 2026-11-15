# 사진 → 블루투스 라벨프린터 즉시 인쇄

촬영하면 바로 블루투스(BLE) 라벨프린터로 인쇄하는 웹앱(단일 `index.html`, 의존성 없음).

## 실행 방법
Web Bluetooth/카메라는 **HTTPS**(또는 localhost)에서만 동작합니다.

- 가장 쉬운 방법: 이 폴더를 GitHub Pages / Netlify / Vercel 등에 올리고 휴대폰에서 URL 접속
- 개발 중: `python3 -m http.server 8000` 후 같은 PC의 Chrome에서 `http://localhost:8000/photo-label-printer/`

## 기기별 브라우저
| 기기 | 브라우저 |
|------|----------|
| 안드로이드 | Chrome (그대로 사용 가능) |
| 아이폰 | **Bluefy** 앱(App Store, 무료) — Safari/Chrome은 Web Bluetooth 미지원 |

## 사용법
1. 프린터 전원 ON → **프린터 연결** → 목록에서 프린터 선택
2. **촬영** (또는 "촬영 즉시 인쇄" 체크 시 촬영과 동시에 인쇄)
3. 안 나오거나 깨지면 ⚙ 설정에서 프로토콜(ESC/POS ↔ TSPL), 용지 폭, 전송 단위 변경

## 주의
- 알리 Walkprinter 계열은 모델별 프로토콜이 달라 **실기기 테스트가 필요**합니다. 하단 로그에 발견된 서비스/특성 UUID가 표시되므로, 안 되면 그 로그를 알려주세요.
- 클래식 블루투스(SPP) 전용 프린터는 웹에서 접근할 수 없습니다(BLE 필요).
