from flask import Flask, request, render_template, redirect, url_for, flash
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from models import ClipboardItem, AppSettings, engine

# 初始化Flask应用
app = Flask(__name__)
app.secret_key = "supersecretkey"  # 设置一个密钥用于flash消息

# 创建数据库会话
Session = sessionmaker(bind=engine)
session = Session()


# ------------------------------
# ClipboardItem 功能
# ------------------------------

@app.route('/')
def index():
    return redirect(url_for('clipboard_list'))

from flask import request  # 确保导入了 request

@app.route('/clipboard/list', methods=['GET'])
def clipboard_list():
    """显示所有 ClipboardItem 的列表，带分页"""
    page = request.args.get('page', 1, type=int)  # 获取当前页码，默认为第一页
    per_page = 10  # 每页显示的项目数量

    total_items = session.query(ClipboardItem).count()
    total_pages = (total_items + per_page - 1) // per_page

    items = session.query(ClipboardItem).order_by(ClipboardItem.timestamp.desc()) \
        .offset((page - 1) * per_page).limit(per_page).all()

    # 生成简化页码列表
    def get_pagination_range(current, total):
        if total <= 5:
            return list(range(1, total + 1))
        elif current < 4:
            return [1, 2, 3, 4, 5, None, total]
        elif current > total - 3:
            return [1, None] + list(range(total - 4, total + 1))
        else:
            return [1, None] + list(range(current - 2, current + 3)) + [None, total]

    pagination_range = get_pagination_range(page, total_pages)

    return render_template(
        'clipboard_list.html',
        items=items,
        current_page=page,
        total_pages=total_pages,
        per_page=per_page,
        pagination_range=pagination_range
    )

@app.route('/clipboard/create', methods=['GET', 'POST'])
def clipboard_create():
    """创建新的 ClipboardItem"""
    if request.method == 'POST':
        content = request.form.get("content", "").strip()
        tags = request.form.get("tags", "").strip()

        if not content or len(content) > 5000:
            flash("内容不能为空且长度不得超过5000字符")
            return redirect(url_for('clipboard_create'))
        if tags and any(len(tag) > 50 for tag in tags.split(',')):
            flash("每个标签长度不得超过50字符")
            return redirect(url_for('clipboard_create'))

        new_item = ClipboardItem(content=content, tags=tags, timestamp=datetime.now())
        session.add(new_item)
        session.commit()
        flash("创建成功")
        return redirect(url_for('clipboard_list'))

    return render_template('clipboard_create.html')

@app.route('/clipboard/detail/<int:id>', methods=['GET'])
def clipboard_detail(id):
    """查看指定 ClipboardItem 的详情"""
    item = session.query(ClipboardItem).filter_by(id=id).first()
    if not item:
        flash("记录不存在")
        return redirect(url_for('clipboard_list'))
    return render_template('clipboard_detail.html', item=item)

@app.route('/clipboard/update/<int:id>', methods=['GET', 'POST'])
def clipboard_update(id):
    """更新指定 ClipboardItem"""
    item = session.query(ClipboardItem).filter_by(id=id).first()
    if not item:
        flash("记录不存在")
        return redirect(url_for('clipboard_list'))

    if request.method == 'POST':
        content = request.form.get("content", "").strip()
        tags = request.form.get("tags", "").strip()

        if not content or len(content) > 5000:
            flash("内容不能为空且长度不得超过5000字符")
            return redirect(url_for('clipboard_update', id=id))
        if tags and any(len(tag) > 50 for tag in tags.split(',')):
            flash("每个标签长度不得超过50字符")
            return redirect(url_for('clipboard_update', id=id))

        item.content = content
        item.tags = tags
        item.timestamp = datetime.now()
        session.commit()
        flash("更新成功")
        return redirect(url_for('clipboard_list'))

    return render_template('clipboard_update.html', item=item)

@app.route('/clipboard/delete/<int:id>', methods=['POST'])
def clipboard_delete(id):
    """删除指定 ClipboardItem"""
    item = session.query(ClipboardItem).filter_by(id=id).first()
    if not item:
        flash("记录不存在")
        return redirect(url_for('clipboard_list'))

    session.delete(item)
    session.commit()
    flash("删除成功")
    return redirect(url_for('clipboard_list'))

@app.route('/clipboard/search', methods=['GET'])
def clipboard_search():
    query = request.args.get("q", "").strip()  # 获取搜索关键字
    page = request.args.get("page", 1, type=int)  # 当前页码，默认为第一页
    per_page = 10  # 每页显示的项目数量

    # 查询数据库
    if not query:
        results = session.query(ClipboardItem).order_by(ClipboardItem.timestamp.desc())
    else:
        results = session.query(ClipboardItem).filter(
            ClipboardItem.content.contains(query) | ClipboardItem.tags.contains(query)
        ).order_by(ClipboardItem.timestamp.desc())

    total_items = results.count()
    total_pages = (total_items + per_page - 1) // per_page  # 计算总页数

    # 获取当前页的数据
    items = results.offset((page - 1) * per_page).limit(per_page).all()

    # 渲染模板并传递所有必要的变量
    return render_template(
        'clipboard_list.html',
        items=items,
        current_page=page,
        total_pages=total_pages,
        per_page=per_page,
        query=query
    )

# ------------------------------
# AppSettings 功能
# ------------------------------

@app.route('/settings/list', methods=['GET'])
def settings_list():
    """显示所有 AppSettings 的列表"""
    settings = session.query(AppSettings).all()
    return render_template('app_settings_list.html', settings=settings)

@app.route('/settings/create', methods=['GET', 'POST'])
def settings_create():
    """创建新的 AppSettings"""
    if request.method == 'POST':
        key = request.form.get("key", "").strip()
        value = request.form.get("value", "").strip()

        if not key or not value:
            flash("键和值都不能为空")
            return redirect(url_for('settings_create'))

        new_setting = AppSettings(key=key, value=value)
        session.add(new_setting)
        session.commit()
        flash("创建成功")
        return redirect(url_for('settings_list'))

    return render_template('app_settings_create.html')

@app.route('/settings/detail/<int:id>', methods=['GET'])
def settings_detail(id):
    """查看指定 AppSettings 的详情"""
    setting = session.query(AppSettings).filter_by(id=id).first()
    if not setting:
        flash("记录不存在")
        return redirect(url_for('settings_list'))
    return render_template('app_settings_detail.html', setting=setting)

@app.route('/settings/update/<int:id>', methods=['GET', 'POST'])
def settings_update(id):
    """更新指定 AppSettings"""
    setting = session.query(AppSettings).filter_by(id=id).first()
    if not setting:
        flash("记录不存在")
        return redirect(url_for('settings_list'))

    if request.method == 'POST':
        key = request.form.get("key", "").strip()
        value = request.form.get("value", "").strip()

        if not key or not value:
            flash("键和值都不能为空")
            return redirect(url_for('settings_update', id=id))

        setting.key = key
        setting.value = value
        session.commit()
        flash("更新成功")
        return redirect(url_for('settings_list'))

    return render_template('app_settings_update.html', setting=setting)

@app.route('/settings/delete/<int:id>', methods=['POST'])
def settings_delete(id):
    """删除指定 AppSettings"""
    setting = session.query(AppSettings).filter_by(id=id).first()
    if not setting:
        flash("记录不存在")
        return redirect(url_for('settings_list'))

    session.delete(setting)
    session.commit()
    flash("删除成功")
    return redirect(url_for('settings_list'))


if __name__ == '__main__':
    app.run(debug=True)