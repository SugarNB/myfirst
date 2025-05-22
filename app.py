from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(
    app.instance_path, 'workstation.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# 数据模型
class Bookmark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(500), nullable=False)
    category = db.Column(db.String(50), default='未分类')

def initialize():
    with app.app_context():
        os.makedirs(app.instance_path, exist_ok=True)
        db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 添加新书签
        new_item = Bookmark(
            name=request.form['name'],
            url=request.form['url'],
            category=request.form.get('category', '工具')
        )
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for('index'))
    
    bookmarks = Bookmark.query.all()
    return render_template('index.html', bookmarks=bookmarks)

@app.route('/delete/<int:id>')
def delete(id):
    item = Bookmark.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    initialize()  # 确保运行前初始化
    app.run(debug=True)