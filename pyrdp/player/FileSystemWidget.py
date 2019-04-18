#
# This file is part of the PyRDP project.
# Copyright (C) 2019 GoSecure Inc.
# Licensed under the GPLv3 or later.
#

from pathlib import Path

from PySide2.QtCore import QObject
from PySide2.QtWidgets import QFrame, QLabel, QListWidget, QVBoxLayout, QWidget

from pyrdp.player.filesystem import Directory, DirectoryObserver, FileSystemItemType
from pyrdp.player.FileSystemItem import FileSystemItem


class FileSystemWidget(QWidget, DirectoryObserver):
    """
    Widget for display directories, using the pyrdp.core.filesystem classes.
    """

    def __init__(self, root: Directory, parent: QObject = None):
        """
        :param root: root of all directories. Directories in root will be displayed with drive icons.
        :param parent: parent object.
        """

        super().__init__(parent)
        self.root = root
        self.breadcrumbLabel = QLabel()

        self.titleLabel = QLabel()
        self.titleLabel.setStyleSheet("font-weight: bold")

        self.titleSeparator: QFrame = QFrame()
        self.titleSeparator.setFrameShape(QFrame.HLine)

        self.listWidget = QListWidget()
        self.listWidget.setSortingEnabled(True)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.addWidget(self.breadcrumbLabel)
        self.verticalLayout.addWidget(self.listWidget)

        self.setLayout(self.verticalLayout)
        self.listWidget.itemDoubleClicked.connect(self.onItemDoubleClicked)

        self.currentPath: Path = Path("/")
        self.currentDirectory: Directory = root
        self.listCurrentDirectory()

        self.currentDirectory.addObserver(self)

    def setWindowTitle(self, title: str):
        """
        Set the window title. When the title is not blank, a title label and a separator is displayed.
        :param title: the new title.
        """

        previousTitle = self.windowTitle()

        super().setWindowTitle(title)

        self.titleLabel.setText(title)

        if previousTitle == "" and title != "":
            self.verticalLayout.insertWidget(0, self.titleLabel)
            self.verticalLayout.insertWidget(1, self.titleSeparator)
        elif title == "" and previousTitle != "":
            self.verticalLayout.removeWidget(self.titleLabel)
            self.verticalLayout.removeWidget(self.titleSeparator)

            # noinspection PyTypeChecker
            self.titleLabel.setParent(None)

            # noinspection PyTypeChecker
            self.titleSeparator.setParent(None)

    def onItemDoubleClicked(self, item: FileSystemItem):
        """
        Handle double-clicks on items in the list.
        :param item: the item that was clicked.
        """

        if not item.isDirectory() and not item.isDrive():
            return

        if item.text() == "..":
            self.currentPath = self.currentPath.parent
        else:
            self.currentPath = self.currentPath / item.text()

        self.listCurrentDirectory()

    def listCurrentDirectory(self):
        """
        Refresh the list widget with the current directory's contents.
        """

        node = self.root

        for part in self.currentPath.parts[1 :]:
            node = next(d for d in node.directories if d.name == part)

        self.listWidget.clear()
        self.breadcrumbLabel.setText(f"Location: {str(self.currentPath)}")

        if node != self.root:
            self.listWidget.addItem(FileSystemItem("..", FileSystemItemType.Directory))

        for directory in node.directories:
            self.listWidget.addItem(FileSystemItem(directory.name, directory.type))

        for file in node.files:
            self.listWidget.addItem(FileSystemItem(file.name, file.type))

        if node is not self.currentDirectory:
            self.currentDirectory.removeObserver(self)
            node.addObserver(self)
            self.currentDirectory = node
            node.list()

    def onDirectoryChanged(self):
        """
        Refresh the directory view when the directory has changed.
        """

        self.listCurrentDirectory()