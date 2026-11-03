# bug_hunter.py - Python 3.11+, Termux Android
# Author: MR ROBERTO
import sys, socket, subprocess, os, requests, urllib3
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style, init

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
init(autoreset=True)

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

# GAMBAR 94f...
BG_IMAGE = "/storage/emulated/0/avg/94faef9a35ff42e55c12a6aaf5503697.jpg"

def banner():
    os.system("clear")
    if os.path.exists(BG_IMAGE):
        try:
            subprocess.run(["chafa", "--size", "60x30", BG_IMAGE], check=True)
        except Exception:
            pass
            
    print(f"""{Fore.BLUE}
    ╔══════════════════════════════════════════════╗
    ║           Bug Hunter - Recon Tool            ║
    ║             Author: MR ROBERTO               ║
    ║               Termux Edition                 ║
    ╚══════════════════════════════════════════════╝
{Style.RESET_ALL}""")

def check_subdomain(sub, domain):
    host = f"{sub}.{domain}"
    result = {"host": host, "ip": None, "status": None, "title": None}
    
    try:
        result["ip"] = socket.gethostbyname(host)
    except:
        return None 

    for scheme in ["https", "http"]:
        try:
            r = requests.get(f"{scheme}://{host}", headers=HEADERS, timeout=5, verify=False, allow_redirects=True)
            result["status"] = r.status_code
            if "<title>" in r.text:
                start = r.text.find("<title>") + 7
                end = r.text.find("</title>", start)
                if end != -1:
                    result["title"] = r.text[start:end].strip()[:50]
            break
        except:
            continue
            
    return result

def main():
    if len(sys.argv) < 2:
        print(f"{Fore.RED}Usage: python bug_hunter.py <domain>{Style.RESET_ALL}")
        sys.exit(1)
        
    domain = sys.argv[1]
    subs = ["www", "api", "dev", "staging", "admin", "portal", "test", "vpn", "mail", "blog", "shop", "git", "jenkins", "dashboard"]
    
    banner()
    print(f"{Fore.BLUE}[*] Target: {domain}")
    print(f"[*] Mengecek {len(subs)} subdomain...\n")
    
    found = []
    with ThreadPoolExecutor(max_workers=10) as ex:
        results = ex.map(lambda s: check_subdomain(s, domain), subs)
        for res in results:
            if res:
                found.append(res)
                print(f"{Fore.BLUE}[+] {res['host']}")
                print(f"    IP: {res['ip']} | Status: {res['status']}")
                if res['title']:
                    print(f"    Title: {res['title']}")
                print()
                
    print(f"{Fore.BLUE}[*] Selesai. Ditemukan {len(found)} subdomain aktif.")

if __name__ == "__main__":
    main()
