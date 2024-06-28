# משתנה עם רשימת בעיות V
# להראות את רשימת הבעיות V
# לסכם את עלות הטיפול ברכב + עלויות הבעיותV


problems_prices = {
    "Engine": 2000,
    "Breaks": 1000,
    "5000 km treatment": 500,
    "10,000 km treatment": 1000,
    "Filters + Oil": 250,
    "Gear": 1000
}

def get_all_problems():
    return list(problems_prices.keys())

def calculate_total_price(problems):
    return sum(problems_prices[problem] for problem in problems)
# 
