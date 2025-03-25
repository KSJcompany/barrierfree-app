
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

void main() => runApp(BarrierFreeChatApp());

class BarrierFreeChatApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: '배리어프리 챗봇',
      theme: ThemeData(primarySwatch: Colors.blue),
      home: ChatScreen(),
    );
  }
}

class ChatScreen extends StatefulWidget {
  @override
  _ChatScreenState createState() => _ChatScreenState();
}

class _ChatScreenState extends State<ChatScreen> {
  final List<Map<String, String>> messages = [];
  final TextEditingController controller = TextEditingController();
  bool isLoading = false;

  void sendMessage() async {
    final place = controller.text.trim();
    if (place.isEmpty) return;

    setState(() {
      messages.add({"role": "user", "text": place});
      controller.clear();
      isLoading = true;
    });

    final response = await http.get(
      Uri.parse('http://your-api-url.com/get_accessibility_score?place=$place'),
    );

    if (response.statusCode == 200) {
      final data = json.decode(response.body);
      String reply;
      if (data.containsKey('error')) {
        reply = "❌ ${data['error']}";
      } else {
        reply = "📍 $place
"
                "🧾 Score: ${data['score']}%
"
                "🟢 ${data['positive_keywords'].join(', ')}
"
                "🔴 ${data['negative_keywords'].join(', ')}

"
                "🤖 ${data['chat_style_summary']}";
      }

      setState(() {
        messages.add({"role": "bot", "text": reply});
        isLoading = false;
      });
    } else {
      setState(() {
        messages.add({"role": "bot", "text": "⚠️ 서버 오류가 발생했어요."});
        isLoading = false;
      });
    }
  }

  Widget buildMessage(Map<String, String> msg) {
    final isUser = msg['role'] == 'user';
    return Align(
      alignment: isUser ? Alignment.centerRight : Alignment.centerLeft,
      child: Container(
        padding: EdgeInsets.all(12),
        margin: EdgeInsets.symmetric(vertical: 4, horizontal: 8),
        decoration: BoxDecoration(
          color: isUser ? Colors.blue[100] : Colors.grey[200],
          borderRadius: BorderRadius.circular(12),
        ),
        child: Text(msg['text'] ?? ''),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("🧠 배리어프리 챗봇")),
      body: Column(
        children: [
          Expanded(
            child: ListView(
              padding: EdgeInsets.all(8),
              children: messages.map(buildMessage).toList(),
            ),
          ),
          if (isLoading) Padding(
            padding: const EdgeInsets.all(8.0),
            child: CircularProgressIndicator(),
          ),
          Row(
            children: [
              Expanded(
                child: Padding(
                  padding: const EdgeInsets.only(left: 8.0),
                  child: TextField(
                    controller: controller,
                    onSubmitted: (_) => sendMessage(),
                    decoration: InputDecoration(
                      hintText: "Enter a place name...",
                    ),
                  ),
                ),
              ),
              IconButton(
                icon: Icon(Icons.send),
                onPressed: sendMessage,
              )
            ],
          )
        ],
      ),
    );
  }
}
