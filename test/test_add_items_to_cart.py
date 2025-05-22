import requests

from allure import step, attach
from allure_commons.types import AttachmentType

from selene import browser, be, have

@@ -22,6 +23,7 @@ def open_browser_with_added_item(url=None, data=None):
                                    data=data)

            cookies = results.cookies.get('Nop.customer')
            attach(body=cookies, name='cookies', attachment_type=AttachmentType.TEXT)

            browser.open('/')
            browser.driver.add_cookie({'name': 'Nop.customer', 'value': cookies})