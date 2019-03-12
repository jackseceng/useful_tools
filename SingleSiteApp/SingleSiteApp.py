import sys
from PyQt4.QtWebKit import QWebView
from PyQt4.QtGui import QApplication
from PyQt4.QtCore import QUrl

app = QApplication(sys.argv)

browser = QWebView()
browser.load(QUrl('https://example.com'))  # Change this URL to the site/IP address you wish to monitor
browser.show()

app.exec_()
