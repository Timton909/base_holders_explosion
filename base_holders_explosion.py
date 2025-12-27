import requests, time

def holders_explosion():
    print("Base — Holders Explosion (100+ new holders in <30 sec)")
    history = {}

    while True:
        try:
            r = requests.get("https://api.dexscreener.com/latest/dex/pairs/base")
            now = time.time()

            for pair in r.json().get("pairs", []):
                addr = pair["pairAddress"]
                holders = pair.get("holders", 0) or 0
                age = now - pair.get("pairCreatedAt", 0) / 1000

                if age > 600: continue

                if addr not in history:
                    history[addr] = (now, holders)
                    continue

                last_t, last_h = history[addr]
                delta_t = now - last_t
                if delta_t < 30:
                    new = holders - last_h
                    if new >= 100:
                        token = pair["baseToken"]["symbol"]
                        print(f"HOLDERS EXPLOSION\n"
                              f"{token} +{new} holders in {delta_t:.0f}s\n"
                              f"Total: {holders:,}\n"
                              f"https://dexscreener.com/base/{addr}\n"
                              f"→ Viral spread starting now\n"
                              f"{'EXPLOSION'*20}")

                history[addr] = (now, holders)

        except:
            pass
        time.sleep(3.3)

if __name__ == "__main__":
    holders_explosion()
