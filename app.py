# 필수 라이브러리
"""
0. Flask : 웹서버를 시작할 수 있는 기능. app이라는 이름으로 플라스크를 시작한다
1. render_template : html파일을 가져와서 보여준다
"""
from flask_sqlalchemy import SQLAlchemy
import os
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# DB 기본 코드

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'database.db')

db = SQLAlchemy(app)


class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_card = db.Column(db.String, nullable=False)
    computer_card = db.Column(db.String, nullable=False)
    game_result = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"사용자 : {self.user_card}  컴퓨터 : {self.computer_card}  {self.game_result}"


with app.app_context():
    db.create_all()


@app.route('/')
def main():
    record_list = Record.query.order_by(Record.id.desc()).all()
    print(record_list)

    win_count = Record.query.filter_by(game_result="승").count()
    lost_count = Record.query.filter_by(game_result="패").count()
    draw_count = Record.query.filter_by(game_result="무").count()

    return render_template('index.html',data=record_list,win_count=win_count,lost_count=lost_count
                           ,draw_count=draw_count)


@app.route('/selectCard', methods=['POST'])
def select_card():
    user_card = request.form.get("user_card")
    computer_card = request.form.get("computer_card")
    game_result = ""

    if user_card == computer_card:
        game_result = "무"
    else:
        if user_card == "가위":
            if computer_card == "보":
                game_result = "승"
            else:
                game_result = "패"
        elif user_card == "바위":
            if computer_card == "가위":
                game_result = "승"
            else:
                game_result = "패"
        else:
            if computer_card == "바위":
                game_result = "승"
            else:
                game_result = "패"

    record = Record(user_card=user_card, computer_card=computer_card, game_result=game_result)
    db.session.add(record)
    db.session.commit()

    return redirect(url_for('main'))


if __name__ == '__main__':
    app.run(debug=True)
