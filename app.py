from flask import Flask, request, render_template

app = Flask(__name__)

# 建立題庫
zh_ko_dict = {
    "你好": "안녕하세요",
    "謝謝": "감사합니다",
    "對不起": "죄송합니다",
    "早安": "좋은 아침",
    "晚安": "안녕히 주무세요",
    "老師": "선생님",
    "學生": "학생",
    "朋友": "친구",
    "家人": "가족",
    "愛": "사랑"
}
# 建立中日文題庫
zh_ja_dict = {
    "你好": "こんにちは",
    "謝謝": "ありがとうございます",
    "對不起": "ごめんなさい",
    "早安": "おはようございます",
    "晚安": "おやすみなさい",
    "老師": "先生",
    "學生": "学生",
    "朋友": "友達",
    "家人": "家族",
    "愛": "愛"
}

@app.route('/translate', methods=['GET', 'POST'])
def translate():
    question = ""
    answer = ""
    language = ""

    if request.method == 'POST':
        question = request.form.get('question', '').strip()
        language = request.form.get('language', '')

        if language == 'ko':
            answer = zh_ko_dict.get(
                question, "查無韓文翻譯"
            )

        elif language == 'ja':
            answer = zh_ja_dict.get(
                question, "查無日文翻譯"
            )

    return render_template(
        'translate.html',
        question=question,
        answer=answer,
        language=language
    )
