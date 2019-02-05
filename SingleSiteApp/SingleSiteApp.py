# This contains borrowed code from https://pawelmhm.github.io/python/pyqt/qt/webkit/2015/09/08/browser.html
# This is designed to be a direct interface to your SOC web interfaces, and not as a fully functioning web browser.

import sys
from PyQt4.QtWebKit import QWebView
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl

app = QApplication(sys.argv)

browser = QWebView()
browser.load(QUrl('https://example.com'))  # Change this URL to the site/IP address you wish to monitor
browser.show()

app.exec_()
