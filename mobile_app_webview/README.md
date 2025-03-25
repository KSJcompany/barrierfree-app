# Barrier-Free WebView App

이 Flutter 앱은 Streamlit 웹앱을 WebView로 감싸서 앱처럼 보여주는 프로토타입입니다.

## 실행 방법

```bash
flutter pub get
flutter run
```

## WebView 연결 URL 수정

`lib/main.dart` 파일에서 `initialUrl`을 본인의 ngrok 주소로 변경하세요:

```dart
initialUrl: 'https://your-ngrok-url.ngrok.io',
```
