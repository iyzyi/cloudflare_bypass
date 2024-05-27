# cloudflare_bypass

Eng | [中文](https://github.com/iyzyi/cloudflare_bypass/blob/master/README_CN.md)

Using DrissionPage to manipulate a real Chromium browser, automatically complete Cloudflare human verification of the target site, and return the User-Agent and Cookies which can be used to request any resource of the target site.

## Usage

```python
# Supported browsers: Chromium-based (such as Chrome and Edge)
browser_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

# Target site protected by Cloudflare
url = 'https://nopecha.com/demo/cloudflare'

# Get the user-agent and cookie that can be used to bypass Cloudflare
cf = CloudflareBypass(browser_path, url)
user_agent, cookie = cf.bypass()

# Now we can use user-agent and cookie to request any resource of the target site protected by Cloudflare
headers = {
    'user-agent': user_agent,
    'cookie': cookie,
}
res = requests.get(url, headers=headers)
```

## Note

1. The script will only automatically manipulate the browser once at the beginning to pass through Cloudflare human verification. Subsequent operations do not require the browser's involvement at all. You only need to use the acquired User-Agent and Cookie to initiate requests (e.g., using the requests library) to the target site's resources.
2. The User-Agent and Cookie must correspond to each other. If the User-Agent used in subsequent requests is inconsistent with the User-Agent used when passing through Cloudflare human verification via the browser, subsequent requests will also trigger Cloudflare human verification.

## Dependency

```
pip install -r requirements.txt
```

