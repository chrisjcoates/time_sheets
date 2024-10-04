from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QDialog,
    QFormLayout,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QLabel,
)
from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtGui import QRegExpValidator


class DialogWindow(QDialog):
    def __init__(self, title, description):
        super().__init__()

        self.window_title = title
        self.description = description

        self.setWindowTitle(self.window_title)

        self.create_layout()

        self.create_line_edits("Process name:")
        self.create_line_edits("Door time:")
        self.create_line_edits("Frame time:")

    def create_layout(self):

        # Input widget layout
        self.layout = QFormLayout()
        self.layout.setLabelAlignment(Qt.AlignLeft)
        self.layout.setHorizontalSpacing(20)

        layout2 = QFormLayout()

        # Input main widget
        main_widget = QWidget()
        main_widget.setLayout(self.layout)

        # Window layout
        self.main_layout = QVBoxLayout()

        # Add description label
        description_label = QLabel(self.description)
        description_label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(description_label)

        # Add main widget to main layout
        self.main_layout.addWidget(main_widget)

        # Add submit button
        submit_button = QPushButton("Submit")
        self.main_layout.addWidget(submit_button)

        # Set window layout
        self.setLayout(self.main_layout)

    def create_line_edits(self, label_name):

        # Create regex
        input_regex = QRegExp(r"^[0-9]+[.][0-9]+$")

        line_edit = QLineEdit()

        # Create and set input validator
        input_validator = QRegExpValidator(input_regex, line_edit)
        line_edit.setValidator(input_validator)

        self.layout.addRow(label_name, line_edit)


app = QApplication([])
window = DialogWindow("Door Process", "Input CNC door process times.")
window.show()
app.exec_()
