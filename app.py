from flask import Flask, render_template, request

app = Flask(__name__)

# =========================
# 中文 → 韓文翻譯字典
# =========================

zh_ko_dict = {
    "你好": "안녕하세요",
    "謝謝": "감사합니다",
    "再見": "안녕히 가세요",
    "早安": "좋은 아침",
    "晚安": "안녕히 주무세요",
    "我愛你": "사랑해요",
    "朋友": "친구",
    "學校": "학교",
    "老師": "선생님",
    "學生": "학생",
    "吃飯": "밥 먹기",
    "水": "물",
    "咖啡": "커피",
    "今天": "오늘",
    "明天": "내일"
}


# =========================
# 中文 → 日文翻譯字典
# =========================

zh_ja_dict = {
    "你好": "こんにちは",
    "謝謝": "ありがとう",
    "再見": "さようなら",
    "早安": "おはようございます",
    "晚安": "おやすみなさい",
    "我愛你": "愛しています",
    "朋友": "友達",
    "學校": "学校",
    "老師": "先生",
    "學生": "学生",
    "吃飯": "食事",
    "水": "水",
    "咖啡": "コーヒー",
    "今天": "今日",
    "明天": "明日"
}


# =========================
# 首頁
# =========================

@app.route('/')
def index():
    return render_template('index.html')


# =========================
# 韓文 / 日文翻譯
# =========================

@app.route('/ask', methods=['GET', 'POST'])
def ask():
    question = ""
    answer = ""
    language = "ko"
    language_name = "韓文"

    if request.method == 'POST':
        question = request.form.get('question', '').strip()
        language = request.form.get('language', 'ko')

        if language == 'ko':
            dictionary = zh_ko_dict
            language_name = "韓文"

        elif language == 'ja':
            dictionary = zh_ja_dict
            language_name = "日文"

        else:
            language = 'ko'
            dictionary = zh_ko_dict
            language_name = "韓文"

        answer = dictionary.get(
            question,
            f"抱歉，我目前沒有「{question}」的{language_name}對應。"
        )

    return render_template(
        'ask.html',
        question=question,
        answer=answer,
        language=language
    )
@app.route('/cc')
def cc():
    return render_template('cc.html')

# =========================
# 啟動 Flask
# =========================

if __name__ == '__main__':
    app.run(debug=True)
