from kite_utils import initialize_kite

kite = initialize_kite()

if kite:
    print("📦 Orders:", kite.orders())
    print("📊 Holdings:", kite.holdings())
    holdings = kite.holdings()
