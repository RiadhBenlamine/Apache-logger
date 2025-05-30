# Let's generate 200 lines of Apache combined log format for testing
import random
from datetime import datetime, timedelta

def random_ip():
    return ".".join(str(random.randint(1, 255)) for _ in range(4))

def random_date(start, end):
    return start + timedelta(seconds=random.randint(0, int((end - start).total_seconds())))

def random_method():
    return random.choice(["GET", "POST", "HEAD", "PUT", "DELETE"])

def random_url():
    urls = [
        "/index.html", "/login", "/wp-login.php", "/admin", "/robots.txt", 
        "/wp-admin/", "/xmlrpc.php", "/about", "/contact", "/search?q=test",
        "/category/news", "/api/v1/data", "/favicon.ico"
    ]
    return random.choice(urls)

def random_status():
    return random.choice(["200", "301", "302", "403", "404", "500", "503"])

def random_size():
    return str(random.randint(0, 5000))

def random_referrer():
    referrers = [
        "-", "http://google.com", "http://bing.com", "http://facebook.com", 
        "http://twitter.com", "http://example.com/page", "-"
    ]
    return random.choice(referrers)

def random_agent():
    agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
        "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
        "Mozilla/5.0 (compatible; Bingbot/2.0; +http://www.bing.com/bingbot.htm)",
        "curl/7.68.0",
        "Nikto/2.1.5",
        "sqlmap/1.4.4#stable (http://sqlmap.org)",
        "Mozilla/5.0 (Linux; Android 9; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36",
        "wpscan/3.8.25",
        "Mozilla/5.0 (compatible; Acunetix-Wvs/14.2; +http://www.acunetix.com/)"
    ]
    return random.choice(agents)

start_date = datetime.now() - timedelta(days=30)
end_date = datetime.now()

lines = []
for _ in range(200):
    ip = random_ip()
    identity = "-"
    user = random.choice(["-", "admin", "guest", "user1"])
    time_str = random_date(start_date, end_date).strftime('%d/%b/%Y:%H:%M:%S %z')
    # The time zone is usually like +0000, let's keep it static for simplicity
    time_str = time_str[:-6] + "+0000"
    method = random_method()
    url = random_url()
    protocol = "HTTP/1.1"
    request = f"{method} {url} {protocol}"
    status = random_status()
    size = random_size()
    referrer = random_referrer()
    agent = random_agent()
    log_line = f'{ip} {identity} {user} [{time_str}] "{request}" {status} {size} "{referrer}" "{agent}"'
    lines.append(log_line)

file_path = 'apache_sample_200.log'
with open(file_path, 'w') as f:
    f.write("\n".join(lines))


