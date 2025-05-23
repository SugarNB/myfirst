# 导入sqlite3模块 - Python内置库，无需额外安装
import sqlite3

# 连接到数据库（如果不存在会自动创建）
# 这会创建一个名为'mydatabase.db'的数据库文件
conn = sqlite3.connect('mydatabase.db')

# 创建一个游标对象 - 用于执行SQL命令
cursor = conn.cursor()

# 执行SQL命令创建表
cursor.execute('''CREATE TABLE IF NOT EXISTS bookmarks
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   url TEXT NOT NULL,
                   category TEXT DEFAULT '未分类')''')

# 插入一条数据
cursor.execute("INSERT INTO bookmarks (name, url, category) VALUES (?, ?, ?)",
               ('GitHub', 'https://github.com', '工具'))

# 提交事务 - 将更改保存到数据库
conn.commit()

# 查询数据
cursor.execute("SELECT * FROM bookmarks")
rows = cursor.fetchall()  # 获取所有记录

# 打印查询结果
print("当前书签:")
for row in rows:
    print(f"ID: {row[0]}, 名称: {row[1]}, URL: {row[2]}, 分类: {row[3]}")

# 关闭连接
conn.close()
