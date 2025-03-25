import 'package:flutter/material.dart';
import 'package:webview_flutter/webview_flutter.dart';

void main() => runApp(BarrierFreeApp());

class BarrierFreeApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: '배리어프리 챗봇',
      theme: ThemeData(primarySwatch: Colors.blue),
      home: Scaffold(
        appBar: AppBar(title: Text("🧠 배리어프리 챗봇")),
        body: WebView(
          initialUrl: 'https://your-ngrok-url.ngrok.io', // ← 여기에 ngrok 주소 입력
          javascriptMode: JavascriptMode.unrestricted,
        ),
      ),
    );
  }
}
