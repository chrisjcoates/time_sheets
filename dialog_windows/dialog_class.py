import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

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

from database.database_connection import DatabaseConnection


class DialogWindow(QDialog):
    def __init__(self, title, description):
        super().__init__()

        self.window_title = title
        self.description = description

        self.database = DatabaseConnection()
        self.database.filepath = "/Users/chris/Documents/Projects/production_timesheets/database/time_sheets.db"
        self.database.table = "cnc_process"
        self.database.columns = ["process_name", "door_time", "frame_time"]

        # Create list for line edits
        self.line_edits = []

        # Set window title
        self.setWindowTitle(self.window_title)

        # Create layout of window
        self.create_layout()

        # Addd input fields
        self.create_line_edits("Door time:")
        self.create_line_edits("Frame time:")

        # Submit button click
        self.submit_button.clicked.connect(self.submit_data)

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

        # Add process name label
        process_name = QLineEdit()
        self.layout.addRow("Process name:", process_name)
        self.line_edits.append(process_name)

        # Add main widget to main layout
        self.main_layout.addWidget(main_widget)

        # Add submit button
        self.submit_button = QPushButton("Submit")
        self.main_layout.addWidget(self.submit_button)

        # Set window layout
        self.setLayout(self.main_layout)

    def create_line_edits(self, label_name):

        # Create regex
        input_regex = QRegExp(r"^[0-9]+[.][0-9]+$")

        # Create line edit
        line_edit = QLineEdit()

        # Create and set input validator
        input_validator = QRegExpValidator(input_regex, line_edit)
        line_edit.setValidator(input_validator)

        # Add widget to FormLayout
        self.layout.addRow(label_name, line_edit)

        # Add line widget to list of line edits
        self.line_edits.append(line_edit)

    def submit_data(self):
        # Create a list for vaues from the line edits
        values = []

        # Append the first line edit (always a string)
        values.append(self.line_edits[0].text())

        # Append the folat values for the rest of the line edits
        for line_edit in self.line_edits[1:]:
            values.append(float(line_edit.text()))

        # Insert the record into the database
        self.database.insert_record(values)

        # Clear the line edit text values
        for line_edit in self.line_edits:
            line_edit.clear()


app = QApplication([])
window = DialogWindow("Door Process", "Input CNC door process times.")
window.show()
app.exec_()
