def calculate():
    print("\nStock Calculator\n")

    stock_symbol = str(input("Enter Stock Symbol: "))
    allotment = float(input("Enter Allotment (Number of Shares): "))
    final_share_price = float(input("Enter Final Share Price (in Dollars): "))
    sell_commission = float(input("Enter Sell Commission (in Dollars): "))
    initial_share_price = float(input("Enter initial Share Price (in Dollars): "))
    buy_commission = float(input("Enter Buy Commission (in Dollars): "))
    capital_gain_tax_rate = float(input("Enter Capital Gain Tax Rate (in %): "))

    proceeds = allotment * final_share_price
    total_purchase_price = allotment * initial_share_price
    capital_lost = total_purchase_price + sell_commission + buy_commission
    capital_gain = proceeds - capital_lost
    tax_on_capital_gain = round((capital_gain_tax_rate / 100) * capital_gain, 2)
    cost = capital_lost + tax_on_capital_gain
    net_profit = proceeds - cost
    roi = round((net_profit / cost) * 100, 2)
    break_even_price = round((cost - tax_on_capital_gain) / allotment, 2)

    # {:,} is used for comma separator after thousands
    print(f"\nStock Symbol: {stock_symbol}")
    print(f"\nProceeds: ${proceeds:,}")
    print(f"\nCost: ${cost:,}")
    print("\nCost Details:")
    print(f"Total Purchase Price: {allotment:,} x ${initial_share_price:,} = ${total_purchase_price:,}")
    print(f"Buy Commission: ${buy_commission:,}")
    print(f"Sell Commission: ${sell_commission:,}")
    print(f"Tax on Capital: {capital_gain_tax_rate}% of ${capital_gain:,} = ${tax_on_capital_gain:,}")
    print(f"\nNet Profit: ${net_profit:,}")
    print(f"\nReturn on Investment: {roi}%")
    print(f"\nBreak Even Price: ${break_even_price:,}")

# if __name__ == '__main__':
#     calculate()
