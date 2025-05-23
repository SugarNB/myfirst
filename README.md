```markdown
# 苏哥的工作站 - 书签管理系统

## 项目概述
一个基于Flask和SQLite的简单书签管理系统，可以分类管理常用网址。

## 技术栈
- **后端框架**: Flask
- **数据库**: SQLite (通过SQLAlchemy ORM)
- **前端框架**: Bootstrap 5
- **模板引擎**: Jinja2

## 功能特性
1. **书签管理**
   - 添加书签（名称、URL、分类）
   - 删除书签
   - 分类展示（工具、学习、娱乐）

2. **用户界面**
   - 响应式设计，适配各种设备
   - 简洁美观的卡片式布局
   - 直观的分类展示

## 文件结构

<pre>
project/
├── app.py                # Flask主应用文件
├── templates/
│   └── index.html        # 前端模板文件
└── instance/
    └── workstation.db    # SQLite数据库文件
</pre>

## 快速开始

### 环境准备
1. 确保已安装Python 3.x
2. 安装依赖：
   ```bash
   pip install flask flask-sqlalchemy
   ```

### 运行应用
```bash
python app.py
```
应用将运行在 `http://127.0.0.1:5000/`

### 使用说明
1. **添加书签**
   - 填写名称、URL
   - 选择分类（工具/学习/娱乐）
   - 点击"添加"按钮

2. **访问书签**
   - 点击书签名称将在新标签页打开链接

3. **删除书签**
   - 点击书签右侧的"×"按钮

## 代码说明

### 后端 (app.py)
- 使用SQLAlchemy定义`Bookmark`数据模型
- 实现CRUD操作：
  - `index()`: 显示和添加书签
  - `delete()`: 删除书签
- 自动初始化数据库

### 前端 (index.html)
- 使用Bootstrap 5构建响应式界面
- 主要组件：
  - 添加表单（名称、URL输入框，分类下拉菜单）
  - 分类展示卡片（工具、学习、娱乐）
- 功能：
  - 表单验证（必填字段、URL格式）
  - 删除按钮与后端交互

## 扩展建议
1. 增加用户认证功能
2. 添加书签编辑功能
3. 实现书签搜索
4. 添加更多分类选项
5. 支持书签导入/导出

## 许可证
MIT License
```
