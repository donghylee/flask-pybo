from datetime import datetime
from flask import Blueprint, request, redirect, url_for, render_template

from pybo.forms import AnswerForm
from pybo import db
from pybo.models import Question, Answer

bp = Blueprint('answer', __name__, url_prefix='/answer')

@bp.route('/create/<int:question_id>', methods=['POST'])
def create(question_id):
    question = Question.query.get_or_404(question_id)
    form = AnswerForm(request.form)
    if form.validate_on_submit():
        content = form.content.data  # 폼모듈로 입력된 값 받을 때.
      # content = request.form['content'] 폼태그 입력된 값 받을 때.

        answer = Answer(question=question, content=content, create_date=datetime.now())
        question.answer_set.append(answer)
        db.session.commit()

        return redirect(url_for('question.detail', question_id=question_id))
    return render_template('question/question_detail.html', question=question, form=form)