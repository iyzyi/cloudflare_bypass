# cloudflare_bypass

[Eng](https://github.com/iyzyi/cloudflare_bypass) | 中文

通过DrissionPage操纵真实的Chromium浏览器，自动完成目标站点的Cloudflare真人验证，返回可用于请求目标站点任意资源的User-Agent和Cookies。

## 用法

```python
# 支持的浏览器: Chromium 内核 (如Chrome和Edge)
browser_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

# 受Cloudflare保护的目标站点
url = 'https://nopecha.com/demo/cloudflare'

# 获取用于绕过Cloudflare真人检测的User-Agent和Cookie
cf = CloudflareBypass(browser_path, url)
user_agent, cookie = cf.bypass()

# 现在我们可以使用User-Agent和Cookie来请求受Cloudflare保护的目标站点任意资源
headers = {
    'user-agent': user_agent,
    'cookie': cookie,
}
res = requests.get(url, headers=headers)
```

## 注意

1. 该脚本只会在一开始的时候自动操纵一次浏览器来通过Cloudflare真人检测，后续操作完全不需要浏览器的参与，只需要使用获取到的User-Agent和Cookie来对目标站点的资源发起请求（比如使用requests库）即可。
2. User-Agent和Cookie必须相对应。如果后续请求时使用的User-Agent与使用浏览器通过Cloudflare真人检测时使用的User-Agent不一致，则后续请求亦会触发Cloudflare真人检测。

## 依赖

```
pip install -r requirements.txt
```

