from flask import Flask, request, render_template
import requests

app = Flask(__name__)


# =========================
# 中韓翻譯題庫
# =========================
zh_ko_dict = {
    "你好": "안녕하세요",
    "안녕하세요": "你好",
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


# =========================
# 首頁
# =========================
@app.route('/')
def index():
    return render_template('index.html')


# =========================
# 競賽
# =========================
@app.route('/competition')
def competition():
    return render_template('competition.html')


# =========================
# 中韓翻譯
# =========================
@app.route('/ask', methods=['GET', 'POST'])
def ask():

    if request.method == 'POST':

        question = request.form.get('question', '').strip()

        # 從題庫查詢
        answer = zh_ko_dict.get(
            question,
            "抱歉，我目前沒有這個詞的韓文對應。"
        )

        return render_template(
            'ask.html',
            question=question,
            answer=answer
        )

    # GET
    return render_template(
        'ask.html',
        question="",
        answer=""
    )


# =========================
# 活動
# =========================
@app.route('/activities', methods=['GET', 'POST'])
def activities():

    if request.method == 'POST':

        question = request.form.get('question', '').strip()

        answer = "抱歉，我目前沒有這個詞的韓文對應。"

        return render_template(
            'activities.html',
            question=question,
            answer=answer
        )

    return render_template(
        'activities.html',
        question="",
        answer=""
    )


# =========================
# 股票查詢
# =========================
@app.route('/stock', methods=['GET', 'POST'])
def stock():

    if request.method == 'POST':

        # 取得股票代號
        stock_no = request.form.get('question', '').strip()

        # 沒有輸入
        if not stock_no:
            return render_template(
                'stock.html',
                question="",
                answer="請輸入股票代號，例如 2330"
            )

        # 台灣證券交易所 API
        url = (
            "https://www.twse.com.tw/exchangeReport/"
            f"STOCK_DAY?response=json&stockNo={stock_no}"
        )

        try:

            # 發送請求
            res = requests.get(url, timeout=10)

            # 轉成 JSON
            data = res.json()

            # 判斷 API 是否成功
            if data.get("stat") == "OK" and data.get("data"):

                # 取得最後一筆資料
                latest_data = data["data"][-1]

                # 第 7 欄是收盤價
                answer = latest_data[6]

            else:

                answer = "查無資料，請確認股票代號是否正確。"

        except Exception as e:

            answer = f"查詢失敗：{e}"

        # 回傳結果
        return render_template(
            'stock.html',
            question=stock_no,
            answer=answer
        )

    # GET
    return render_template(
        'stock.html',
        question="",
        answer=""
    )


# =========================
# 領導
# =========================
@app.route('/leadership')
def leadership():
    return render_template('leadership.html')


# =========================
# 社團
# =========================
@app.route('/club')
def club():
    return render_template('club.html')


# =========================
# 選修
# =========================
@app.route('/electives')
def electives():
    return render_template('electives.html')


# =========================
# AI
# =========================
@app.route('/ai')
def ai():
    return render_template('ai.html')


# =========================
# CC 頁面
# =========================
@app.route('/cc')
def cc():
    return render_template('cc.html')


# =========================
# 啟動 Flask
# =========================
if __name__ == '__main__':
    app.run(debug=True)
