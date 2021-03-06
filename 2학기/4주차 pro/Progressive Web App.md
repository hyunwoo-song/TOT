# Progressive Web App

* PWA는 지원하는 웹 브라우저를 통해 설치 없이 페이지 접속 후 바탕화면에 앱 아이콘을 추가할 수 있고 언제든지 푸시 알림을 통해 재참여가 가능하고 오프라인에서도 웹 앱 접근 가능

### 특징

* 프로그레시브 - 점진적인 개선을 통해 작성되므로, 어떤 브라우저를 선택하든 상관없이 모든 사용자에게 적합합니다.
* 반응형 - 데스크톱, 모바일, 태블릿 등 모든 폼 팩터에 맞습니다.
* 연결 독립적 - 서비스 워커를 사용하여 오프라인이나 느린 네트워크에서 작동하도록 향상됩니다.
* 앱과 유사 - 앱 셀 모드에서 작성되기 때문에 앱 스타일의 상호작용 및 탐색 기능을 사용자에게 제공합니다.
* 최신 상태 - 서비스 워커 업데이트 프로세스 덕분에 항상 최신 상태로 유지됩니다.
* 안전 - HTTPS를 통해 제공되므로 스누핑이 차단되며, 콘텐츠가 변조되지 않도록 보장합니다.
* 검색 가능 - W3C 매니페스트 및 서비스 워커 등록 범위 덕분에 '애플리케이션'으로 식별되므로, 검색 엔진에서 검색이 가능합니다.
* 재참여 가능 - 푸시 알림과 같은 기능을 통해 쉽게 재참여가 가능합니다.
* 설치 가능 - 앱 스토어에서 씨름할 필요 없이 사용자가 자신에게 가장 유용한 앱을 홈 화면에 유지할 수 있습니다.
* 링크 연결 가능 - URL을 통해 손쉽게 공유할 수 있으며 복잡한 설치 작업이 불필요 합니다.





#### 서비스 워커

* 서비스 워커는 브라우저가 백그라운드에서 실행하는 스크립트이며 웹페이지와 별개로 작동
* 웹 푸시(알림), 백그라운드 동기화, 캐싱 등의 기술적 기반을 제공
* 