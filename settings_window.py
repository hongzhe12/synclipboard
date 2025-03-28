import keyboard
from PySide6.QtCore import QTimer
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout,  QPushButton,
    QCheckBox,  QFormLayout, QMessageBox, QLineEdit
)

from auto_start import enable_auto_start, disable_auto_start
from models import get_settings, update_settings




class SettingsWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # 在SettingsWindow的__init__中添加：
        print("设置窗口初始化完成！")
        # 如果看不到这个输出，说明构造失败
        self.setWindowTitle("剪贴板历史设置")
        self.setFixedSize(300, 250)

        # 主布局
        layout = QVBoxLayout()
        form_layout = QFormLayout()

        # 热键设置
        self.hotkey_edit = QPushButton("Alt+X")
        self.hotkey_edit.clicked.connect(self.change_hotkey)
        form_layout.addRow("快捷热键:", self.hotkey_edit)

        # 历史记录限制
        # 替换 QSpinBox 为 QLineEdit
        self.history_limit = QLineEdit()
        self.history_limit.setPlaceholderText("输入10-500的整数")  # 提示文本
        self.history_limit.setValidator(QIntValidator(1, 100000))  # 限制输入范围
        form_layout.addRow("最大记录数:", self.history_limit)

        # 自动启动
        self.auto_start = QCheckBox("开机自动启动")
        form_layout.addRow(self.auto_start)

        # 保存按钮
        save_btn = QPushButton("保存设置")
        save_btn.clicked.connect(self.save_settings)

        layout.addLayout(form_layout)
        layout.addWidget(save_btn)
        self.setLayout(layout)

        # 加载当前设置到界面
        settings = get_settings()
        # 访问具体设置项
        self.hotkey_edit.setText(settings.hotkey)
        self.history_limit.setText(str(settings.max_history))
        self.auto_start.setChecked(settings.auto_start)

        self.history_limit.textChanged.connect(self._on_history_changed)  # 使用 textChanged 而不是 valueChanged

        # ...其余代码...

    def _on_history_changed(self, text):
            """处理文本变化"""
            print(f"当前输入值: {text}")

    def change_hotkey(self):
        """修改热键（使用 keyboard 库实现全局监听）"""
        self.hotkey_edit.setText("正在等待按键...")
        self.hotkey_edit.setFocus()  # 确保焦点在输入框

        # 清除之前的监听（避免重复）
        if hasattr(self, '_hotkey_listener'):
            keyboard.unhook(self._hotkey_listener)

        # 监听键盘按键
        self._hotkey_listener = keyboard.on_press(self._on_key_press)

        # 设置超时自动取消（可选）
        QTimer.singleShot(5000, self._cancel_hotkey_listening)

    def _on_key_press(self, event):
        """键盘按键回调"""
        # 忽略单独的修饰键（Ctrl/Shift/Alt/Win）
        if event.name in ("ctrl", "shift", "alt", "windows"):
            return

        # 获取组合键
        modifiers = []
        if keyboard.is_pressed("ctrl"):
            modifiers.append("Ctrl")
        if keyboard.is_pressed("shift"):
            modifiers.append("Shift")
        if keyboard.is_pressed("alt"):
            modifiers.append("Alt")
        if keyboard.is_pressed("windows"):
            modifiers.append("Win")

        # 组合键 + 按键
        key_combination = "+".join(modifiers + [event.name.upper()])

        # 更新 UI
        self.hotkey_edit.setText(key_combination)

        # 取消监听
        keyboard.unhook(self._hotkey_listener)
        delattr(self, '_hotkey_listener')

        # 保存热键（可以在这里调用实际的热键注册逻辑）
        self._register_hotkey(key_combination)

        key_combination = "+".join(modifiers + [event.name.upper()])
        self.hotkey_edit.setText(key_combination)  # 确保这行被执行
        print(f"[DEBUG] 新热键: {key_combination}")  # 调试

    def _cancel_hotkey_listening(self):
        """取消热键监听（超时或手动取消）"""
        if hasattr(self, '_hotkey_listener'):
            keyboard.unhook(self._hotkey_listener)
            delattr(self, '_hotkey_listener')
            self.hotkey_edit.setText("未设置")  # 或恢复之前的热键

    def _register_hotkey(self, hotkey):
        """实际注册热键（示例）"""
        print(f"注册热键: {hotkey}")
        # 示例：使用 keyboard 注册热键
        try:
            if hasattr(self, '_current_hotkey'):
                keyboard.remove_hotkey(self._current_hotkey)
            self._current_hotkey = keyboard.add_hotkey(hotkey.lower(), self._on_hotkey_triggered)
        except ValueError as e:
            print(f"热键注册失败: {e}")
            self.hotkey_edit.setText("热键冲突！")

    def _on_hotkey_triggered(self):
        """热键触发时的回调"""
        print("热键被触发！")
        # 在这里执行你的功能，例如显示/隐藏窗口


    def save_settings(self):
        """保存设置"""
        try:
            # 校验最大记录数
            max_history = int(self.history_limit.text())  # 获取输入值
            if not 1 <= max_history <= 100000:
                QMessageBox.warning(self, "错误", "请输入1-100000之间的整数")
                return

            # 检查开关机配置
            if self.auto_start.isChecked():
                enable_auto_start()
            else:
                disable_auto_start()
            # 更新设置
            update_settings(
                max_history=max_history,
                hotkey=self.hotkey_edit.text(),
                auto_start=self.auto_start.isChecked()
            )
            # 是否更新了热键
            if self.hotkey_edit.text() !='Alt+X' and self.hotkey_edit.text() !='alt+x':

                QMessageBox.information(self, "提示", "热键修改后，需要重启好贴板！")
            else:
                QMessageBox.warning(self, "成功", "设置已保存！")

            self.hide()
        except ValueError:
            QMessageBox.warning(self, "错误", "请输入有效数字")


    def closeEvent(self, event):
        """重写关闭事件（点击X时最小化到托盘）"""
        if self.isVisible():
            self.hide()
            event.ignore()






