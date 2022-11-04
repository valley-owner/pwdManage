""" Author: duckweed    Contact: valley-ov@qq.com  Time: 2022/10/30-17:57 """

HEADER_BACKGROUND = 'background-color: rgb(60, 63, 65);'
BOTTOM_BACKGROUND = 'background-color: rgb(43, 43, 43);'

WINDOWS_SHOW_BUTTON = 'QPushButton { border:none; } QPushButton:hover { background-color: rgb(255, 0, 0); } QPushButton:pressed { background-color: rgb(255, 237, 252); border-top:5px; border-left:5px; }'

# 进度条
PROGRESSBAR = 'QProgressBar { min-height: 8px; max-height: 8px; border-radius: 4px; } QProgressBar::chunk { border-radius: 4px; background-color: #009688; }'

# 菜单按钮

MENU_URL = {
        'extend': 'url(:/blue/images/blue/icon-indent-right.svg);',
        'manage': 'url(:/blue/images/blue/icon-sale.svg);',
        'setting': 'url(:/blue/images/blue/icon-set.svg);',
        'about': 'url(:/blue/images/blue/ic_body.svg);',
        'exit': 'url(:/blue/images/blue/ic_bowout.svg);',
    }


def get_menu(value, position='center', click=False):
    if click:
        style = 'border:2px solid rgb(0, 255, 255);'
    else:
        style = 'border:1px solid rgba(204, 204, 204, 150);'
    """扩展后样式"""
    return 'QPushButton{ background-image:' + MENU_URL.get(value) + \
           ' background-repeat: repeat-no-repeat; background-position: ' + position + '; ' \
           'background-origin:content; background-size:25px; text-align : center; ' \
           ' ' + style + ' border-radius:10px; } ' \
           'QPushButton:hover { background-color: rgba(204, 204, 204, 60); border-radius:10px; } ' \
           'QPushButton:pressed { background-color: rgba(85, 255, 255, 60); border-top:5px; ' \
           'border-left:5px; border-radius:10px; }'


input_error = '''QLineEdit{
	border: 2px;
	border-style: solid;
	
	border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 42, 0, 255), stop:0.238636 rgba(255, 140, 61, 255), stop:0.545455 rgba(255, 115, 139, 255), stop:1 rgba(255, 0, 144, 255));
}'''
