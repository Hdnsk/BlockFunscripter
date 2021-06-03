import sys
from PySide6 import QtCore, QtWidgets
from PySide6.QtGui import QFont, QScreen
from .plugins import loaded_plugins


class ListComponent(QtWidgets.QWidget):
    def __init__(self, name=None, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.label = QtWidgets.QLabel(
            text=name,
            alignment=QtCore.Qt.AlignCenter
        )
        self.label.setFont(QFont("Helvetica", 14))
        self.list = QtWidgets.QListWidget()
        self.fillList()

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.list)
        self.setBaseSize(QtCore.QSize(200, 400))

    def fillList(self):
        pass

    @QtCore.Slot()
    def handleShow(self):
        if self.isVisible():
            self.hide()
        else:
            self.show()


class PluginWidget(ListComponent):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(name="Plugins", *args, **kwargs)

    def fillList(self):
        for p in loaded_plugins:
            self.list.addItem(p.name)


class GeneratorsWidget(ListComponent):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(name="Generators", *args, **kwargs)

    def fillList(self):
        for p in loaded_plugins:
            for g in p.generators:
                self.list.addItem(g["name"])


class BlocksWidget(ListComponent):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(name="Blocks", *args, **kwargs)

    def fillList(self):
        for p in loaded_plugins:
            for b in p.blocks:
                self.list.addItem(b["name"])


class MainMenu(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.generators = QtWidgets.QPushButton("Generators")
        self.plugins = QtWidgets.QPushButton("Plugins")
        self.blocks = QtWidgets.QPushButton("Blocks")

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.plugins)
        self.layout.addWidget(self.generators)
        self.layout.addWidget(self.blocks)


def main():
    app = QtWidgets.QApplication([])
    app.setApplicationName("dev")

    m = MainMenu()
    m.resize(150, 100)
    m.show()
    m.move(800, 600)

    p = PluginWidget()
    g = GeneratorsWidget()
    b = BlocksWidget()

    m.plugins.clicked.connect(p.handleShow)
    m.generators.clicked.connect(g.handleShow)
    m.blocks.clicked.connect(b.handleShow)

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
