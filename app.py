# 导入必要的模块
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

# 创建Flask应用实例
app = Flask(__name__)

# 配置数据库URI（使用SQLite数据库）
# 数据库文件将存储在instance文件夹下，名为workstation.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(
    app.instance_path, 'workstation.db')

# 关闭SQLAlchemy事件系统，可以提高性能
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 初始化SQLAlchemy数据库对象
db = SQLAlchemy(app)

# 定义数据模型（书签表）
class Bookmark(db.Model):
    # 表名会自动设置为bookmark（小写）
    
    # 主键ID，自增长整数
    id = db.Column(db.Integer, primary_key=True)
    
    # 书签名称，字符串类型，最大长度100，不能为空
    name = db.Column(db.String(100), nullable=False)
    
    # 书签URL，字符串类型，最大长度500，不能为空
    url = db.Column(db.String(500), nullable=False)
    
    # 书签分类，字符串类型，最大长度50，默认值为'未分类'
    category = db.Column(db.String(50), default='未分类')

# 初始化数据库函数
def initialize():
    # 使用应用上下文
    with app.app_context():
        # 创建instance文件夹（如果不存在）
        os.makedirs(app.instance_path, exist_ok=True)
        
        # 创建所有数据库表
        db.create_all()

# 定义根路由，支持GET和POST方法
@app.route('/', methods=['GET', 'POST'])
def index():
    # 如果是POST请求（提交表单）
    if request.method == 'POST':
        # 创建新的书签对象
        new_item = Bookmark(
            name=request.form['name'],  # 从表单获取名称
            url=request.form['url'],    # 从表单获取URL
            category=request.form.get('category', '工具')  # 从表单获取分类，默认为'工具'
        )
        
        # 添加到数据库会话
        db.session.add(new_item)
        
        # 提交会话到数据库
        db.session.commit()
        
        # 重定向到首页（防止表单重复提交）
        return redirect(url_for('index'))
    
    # 如果是GET请求，查询所有书签
    bookmarks = Bookmark.query.all()
    
    # 渲染模板，传入书签数据
    return render_template('index.html', bookmarks=bookmarks)

# 定义删除路由，接收书签ID参数
@app.route('/delete/<int:id>')
def delete(id):
    # 根据ID查询书签，如果不存在返回404错误
    item = Bookmark.query.get_or_404(id)
    
    # 从数据库中删除该书签
    db.session.delete(item)
    
    # 提交更改
    db.session.commit()
    
    # 重定向回首页
    return redirect(url_for('index'))

# 主程序入口
if __name__ == '__main__':
    # 初始化数据库
    initialize()  # 确保运行前初始化
    
    # 启动Flask开发服务器，开启调试模式
    app.run(debug=True)