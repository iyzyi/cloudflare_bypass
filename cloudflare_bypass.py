from DrissionPage import ChromiumPage, ChromiumOptions
import requests


class CloudflareBypass():

    # Welcome to submit a pull request or open an issue to support more language versions.
    language_dict = {
        'en-us': {'title': 'Just a moment'},
        'zh-cn': {'title': '请稍候'},
    }

    def __init__(self, browser_path, url):
        self.browser_path = browser_path
        self.url = url
        self.is_clicked = False

        options = ChromiumOptions()
        # options = ChromiumOptions().auto_port()
        options.set_paths(self.browser_path)

        args = [
            "-no-first-run",
            "-force-color-profile=srgb",
            "-metrics-recording-only",
            "-password-store=basic",
            "-use-mock-keychain",
            "-export-tagged-pdf",
            "-no-default-browser-check",
            "-disable-background-mode",
            "-enable-features=NetworkService,NetworkServiceInProcess,LoadCryptoTokenExtension,PermuteTLSExtensions",
            "-disable-features=FlashDeprecationWarning,EnablePasswordsAccountStorage",
            "-deny-permission-prompts",
            "-disable-gpu",
        ]

        for arg in args:
            options.set_argument(arg)

        self.driver = ChromiumPage(addr_driver_opts=options)


    def _is_bypassed(self):
        for dict in self.language_dict.values():
            if dict['title'] in self.driver.title:
                return False
        return True


    def _click_button(self):
        try:
            print('try to bypass cloudflare...')
            iframe = self.driver('xpath://div/iframe')
            if iframe:
                button = iframe.ele('css:input[type=checkbox]')
                if button:
                    print('click verify human button')
                    button.click()
                    self.is_clicked = True
        except Exception:
            pass


    def _cookie_format_convert(self, driver_cookie):
        requests_cookie = ''
        for dict in driver_cookie:
            requests_cookie += f'{dict["name"]}={dict["value"]}; '
        return requests_cookie


    def bypass(self):
        self.driver.get(self.url)

        while not self._is_bypassed():
            if not self.is_clicked:
                self._click_button()

        user_agent = self.driver.user_agent
        cookie = self.driver.get_cookies()
        cookie = self._cookie_format_convert(cookie)

        self.driver.quit()

        return user_agent, cookie


if __name__ == '__main__':
    # Supported browsers: Chromium-based (such as Chrome and Edge)
    browser_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
    # browser_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    # browser_path = r'/usr/bin/google-chrome'

    # Target site protected by Cloudflare
    url = 'https://nopecha.com/demo/cloudflare'

    # Get the user-agent and cookie that can be used to bypass Cloudflare
    cf = CloudflareBypass(browser_path, url)
    user_agent, cookie = cf.bypass()
    print(f'user_agent: {user_agent}')
    print(f'cookie: {cookie}')

    # Now we can use user-agent and cookie to request any resource of the target site protected by Cloudflare
    headers = {
        'user-agent': user_agent,
        'cookie': cookie,
    }
    res = requests.get(url, headers=headers)

    print(res)
    print(res.text)
    with open(r'test.html', 'wb') as f:
        f.write(res.content)
