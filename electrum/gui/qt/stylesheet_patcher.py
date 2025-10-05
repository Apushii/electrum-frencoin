# -*- coding: utf-8 -*-
"""
Unified futuristic stylesheet patcher for Electrum fork
- Green-forward theme with blue secondary accents and white text
- Works across Linux, Windows, macOS
- API preserved: patch_qt_stylesheet(use_dark_theme: bool = True)
"""

from typing import Optional
import sys

# The same QSS is used for all OS-specific constants, so the theme is consistent.
CUSTOM_PATCH_FOR_DEFAULT_THEME_LINUX = r"""
/* ===== Frencoin Futuristic Theme (Green-forward, Blue secondary) =====
   Palette:
     - bg0: #0A0E12 (deep black-blue)
     - bg1: #0E141B
     - bg2: #111A24
     - text: #EAF2FF (soft white)
     - textMuted: #A7B3C5
     - accentBlue: #2DD4FF
     - accentGreen: #22E584 (PRIMARY accent)
     - warn: #F5A524
     - border: #1E2A36
     - borderFocus: #22E584 (more green focus)
     - borderAccent: #22E584
*/

@define-color bg0 #0A0E12;
@define-color bg1 #0E141B;
@define-color bg2 #111A24;
@define-color text #EAF2FF;
@define-color textMuted #A7B3C5;
@define-color accentBlue #2DD4FF;
@define-color accentGreen #22E584;
@define-color warn #F5A524;
@define-color border #1E2A36;
@define-color borderFocus #22E584;
@define-color borderAccent #22E584;

/* ---------- Global ---------- */
* {
  color: @text;
  background: transparent;
}

QWidget {
  background-color: @bg1;
  color: @text;
}

/* Headings and green text accents */
QGroupBox::title,
QDockWidget::title,
QTabBar::tab:selected,
QHeaderView::section:checked {
  color: @accentGreen;
}

QLabel[role="hint"],
QLabel[role="success"],
QLabel[class~="accent"],
QToolTip {
  color: @accentGreen;
}

/* Links */
QLabel[openExternalLinks="true"],
QTextBrowser,
QTextBrowser QTextItem,
QTextBrowser::item,
QTextEdit {
  color: @text;
}
QLabel[openExternalLinks="true"]::hover,
QTextBrowser a,
QTextEdit a {
  color: @accentGreen;
  text-decoration: none;
}

/* ---------- Panels / Cards ---------- */
QFrame, QGroupBox, QDockWidget, QToolBox, QStackedWidget, QListView, QTreeView, QTableView, QTextEdit, QPlainTextEdit {
  background-color: @bg0;
  border: 1px solid @border;
  border-radius: 8px;
}

/* Headers */
QHeaderView::section {
  background-color: @bg2;
  color: @textMuted;
  padding: 6px 8px;
  border: 1px solid @border;
}

/* Tables / Lists selection (green highlight) */
QTreeView::item:selected,
QListView::item:selected,
QTableView::item:selected,
QTextEdit::selection,
QPlainTextEdit::selection {
  background-color: #133B3F; /* deep teal-green */
  color: @text;
}

/* ---------- Buttons ---------- */
QPushButton {
  background-color: @bg2;
  color: @text;
  border: 1px solid @border;
  border-radius: 8px;
  padding: 7px 12px;
}
QPushButton:hover,
QToolButton:hover {
  border-color: @borderAccent;
}
QPushButton:pressed {
  background-color: @bg1;
}
/* Primary emphasis via green */
QPushButton[default="true"],
QPushButton:checked {
  background-color: @accentGreen;
  color: #0A0E12;
  border: 1px solid @accentGreen;
}
/* Secondary/ghost with green text accent */
QPushButton[flat="true"] {
  background: transparent;
  border-color: transparent;
  color: @accentGreen;
}
QPushButton[flat="true"]:hover {
  color: @text;
  border-color: @borderAccent;
}

/* ---------- Inputs ---------- */
QLineEdit, QSpinBox, QDoubleSpinBox, QComboBox, QTextEdit, QPlainTextEdit, QDateTimeEdit {
  background-color: @bg0;
  border: 1px solid @border;
  border-radius: 8px;
  padding: 6px 8px;
  selection-background-color: #133B3F;
  selection-color: @text;
}
QLineEdit:focus, QSpinBox:focus, QDoubleSpinBox:focus, QComboBox:focus, QTextEdit:focus, QPlainTextEdit:focus, QDateTimeEdit:focus {
  border: 1px solid @borderFocus;
  box-shadow: 0 0 0 2px rgba(34,229,132,0.15);
}

/* Dropdowns */
QComboBox::drop-down {
  border-left: 1px solid @border;
}
QComboBox::down-arrow { width: 10px; height: 10px; }
QComboBox QAbstractItemView {
  background-color: @bg0;
  border: 1px solid @border;
  selection-background-color: #133B3F;
}

/* ---------- Tabs ---------- */
QTabWidget::pane {
  border: 1px solid @border;
  border-radius: 8px;
  top: -1px;
}
QTabBar::tab {
  background: @bg2;
  color: @textMuted;
  border: 1px solid @border;
  border-bottom-color: @border;
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
  padding: 6px 10px;
  margin-right: 2px;
}
QTabBar::tab:hover {
  color: @text;
  border-color: @borderAccent;
}
QTabBar::tab:selected {
  background: @bg1;
  color: @accentGreen; /* green text accent when active */
  border-color: @borderAccent;
}

/* ---------- Checkboxes & Radios ---------- */
QCheckBox, QRadioButton { color: @text; }
QCheckBox::indicator, QRadioButton::indicator {
  width: 16px; height: 16px;
  border: 1px solid @border;
  border-radius: 4px;
  background: @bg2;
}
QCheckBox::indicator:checked,
QRadioButton::indicator:checked {
  background: @accentGreen;
  border: 1px solid @accentGreen;
}

/* ---------- Sliders / Progress ---------- */
QSlider::groove:horizontal {
  height: 6px;
  background: @bg2;
  border-radius: 3px;
}
QSlider::handle:horizontal {
  width: 14px; margin: -6px 0; border-radius: 7px;
  background: @accentGreen;
  border: 1px solid @accentGreen;
}
QProgressBar {
  background: @bg2;
  border: 1px solid @border;
  border-radius: 8px;
  text-align: center;
  color: @text;
}
QProgressBar::chunk { background-color: @accentGreen; border-radius: 8px; }

/* ---------- Scrollbars ---------- */
QScrollBar:vertical, QScrollBar:horizontal {
  background: @bg1;
  border: 1px solid @border;
  border-radius: 8px;
}
QScrollBar::handle:vertical, QScrollBar::handle:horizontal {
  background: @bg2;
  border: 1px solid @border;
  border-radius: 8px;
}
QScrollBar::handle:vertical:hover, QScrollBar::handle:horizontal:hover {
  border-color: @accentGreen;
}
QScrollBar::add-line, QScrollBar::sub-line {
  background: @bg1;
  border: none;
  height: 0px; width: 0px;
}

/* ---------- Toolbars / Status ---------- */
QToolBar {
  background: @bg1;
  border-bottom: 1px solid @border;
}
QStatusBar {
  background: @bg1;
  color: @textMuted;
  border-top: 1px solid @border;
}
QStatusBar QLabel[class~="ok"] { color: @accentGreen; }
QStatusBar QLabel[class~="warn"] { color: @warn; }

/* ---------- Menus ---------- */
QMenuBar {
  background: @bg1;
  color: @text;
}
QMenuBar::item:selected { background: @bg2; color: @accentGreen; }
QMenu {
  background: @bg0;
  border: 1px solid @border;
}
QMenu::item:selected {
  background: #133B3F;
  color: @text;
}

/* ---------- Tooltips ---------- */
QToolTip {
  background-color: @bg2;
  color: @accentGreen; /* readable green text hint */
  border: 1px solid @borderAccent;
  padding: 6px 10px;
  border-radius: 8px;
}
"""
CUSTOM_PATCH_FOR_DEFAULT_THEME_WINDOWS = CUSTOM_PATCH_FOR_DEFAULT_THEME_LINUX
CUSTOM_PATCH_FOR_DEFAULT_THEME_MACOS = CUSTOM_PATCH_FOR_DEFAULT_THEME_LINUX
CUSTOM_PATCH_FOR_DARK_THEME = CUSTOM_PATCH_FOR_DEFAULT_THEME_LINUX

def _choose_default_qss() -> str:
    if sys.platform.startswith("win"):
        return CUSTOM_PATCH_FOR_DEFAULT_THEME_WINDOWS
    elif sys.platform == "darwin":
        return CUSTOM_PATCH_FOR_DEFAULT_THEME_MACOS
    else:
        return CUSTOM_PATCH_FOR_DEFAULT_THEME_LINUX

def _apply_dark_palette(app) -> None:
    # Set a palette that matches our stylesheet for widgets that ignore QSS in places.
    try:
        from PyQt5 import QtGui  # type: ignore
    except Exception:
        try:
            from PySide2 import QtGui  # type: ignore
        except Exception:
            return

    text = QtGui.QColor("#EAF2FF")
    disabled = QtGui.QColor("#A7B3C5")
    window = QtGui.QColor("#0E141B")
    base = QtGui.QColor("#0A0E12")

    palette = app.palette()
    palette.setColor(QtGui.QPalette.Window, window)
    palette.setColor(QtGui.QPalette.WindowText, text)
    palette.setColor(QtGui.QPalette.Base, base)
    palette.setColor(QtGui.QPalette.AlternateBase, window)
    palette.setColor(QtGui.QPalette.ToolTipBase, window)
    palette.setColor(QtGui.QPalette.ToolTipText, text)
    palette.setColor(QtGui.QPalette.Text, text)
    palette.setColor(QtGui.QPalette.Button, window)
    palette.setColor(QtGui.QPalette.ButtonText, text)
    palette.setColor(QtGui.QPalette.BrightText, text)
    palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor("#133B3F"))
    palette.setColor(QtGui.QPalette.HighlightedText, text)
    palette.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.Text, disabled)
    palette.setColor(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, disabled)
    app.setPalette(palette)

def patch_qt_stylesheet(use_dark_theme: bool = True, app: Optional[object] = None) -> None:
    """Append our stylesheet to the running QApplication.
    Args:
        use_dark_theme: If True, use CUSTOM_PATCH_FOR_DARK_THEME; otherwise use per-OS default.
        app: optionally pass the QApplication; otherwise we will find the instance.
    """
    if app is None:
        try:
            from PyQt5 import QtWidgets  # type: ignore
        except Exception:
            try:
                from PySide2 import QtWidgets  # type: ignore
            except Exception:
                return
        qapp = QtWidgets.QApplication.instance()
    else:
        qapp = app

    if qapp is None:
        return

    # Use the exact same dark theme QSS everywhere for consistency and readability.
    qss = CUSTOM_PATCH_FOR_DARK_THEME
    _apply_dark_palette(qapp)
    existing = qapp.styleSheet() or ""
    qapp.setStyleSheet(existing + ("\n\n" if existing else "") + qss)