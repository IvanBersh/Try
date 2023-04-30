''' Окно для редактирования вопросов '''
from PyQt5.QtWidgets import (
        QLineEdit, QFormLayout)

txt_Question = QLineEdit('')
txt_Answer = QLineEdit('')
txt_Wrong1 = QLineEdit('')
txt_Wrong2 = QLineEdit('')
txt_Wrong3 = QLineEdit('')

layout_form = QFormLayout()

layout_form.addRow('Вопрос:', txt_Question)
layout_form.addRow('Правильный ответ:', txt_Answer)
layout_form.addRow('Неверно:', txt_Wrong1)
layout_form.addRow('Неправильно:', txt_Wrong2)
layout_form.addRow('Неперекосяк:', txt_Wrong3)