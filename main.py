import get_status as gs
import send_email as se

site = "https://www.microcenter.com/product/601213/corsair-sf750-750-watt-80-plus-platinum-sfx-fully-modular-power-supply?storeid=141"

def main():
    if gs.get_status(site) != 'Sold Out':
        se.send_email()

if __name__ == '__main__': main()