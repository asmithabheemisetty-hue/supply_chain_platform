"""
Product-specific data for consumer impact analysis
"""

# Consumer products affected by semiconductor shortage
CONSUMER_PRODUCTS = {
    'Smartphones': {
        'category': 'Electronics',
        'current_price_usd': 800,
        'shortage_severity': 'Critical',
        'availability_pct': 45,  # 55% shortage
        'price_increase_pct': 35,
        'new_price_usd': 1080,
        'timeline_months': 8,
        'alternatives': ['Refurbished phones', 'Older models', 'Feature phones'],
        'consumer_impact': 'High - Essential communication device'
    },
    'Laptops': {
        'category': 'Electronics',
        'current_price_usd': 1200,
        'shortage_severity': 'Critical',
        'availability_pct': 50,
        'price_increase_pct': 32,
        'new_price_usd': 1584,
        'timeline_months': 7,
        'alternatives': ['Tablets', 'Desktop computers', 'Chromebooks'],
        'consumer_impact': 'High - Essential for work and education'
    },
    'Gaming Consoles': {
        'category': 'Gaming',
        'current_price_usd': 500,
        'shortage_severity': 'Critical',
        'availability_pct': 35,
        'price_increase_pct': 40,
        'new_price_usd': 700,
        'timeline_months': 9,
        'alternatives': ['Cloud gaming', 'Mobile gaming', 'Previous generation consoles'],
        'consumer_impact': 'Medium - Entertainment device'
    },
    'Smart TVs': {
        'category': 'Electronics',
        'current_price_usd': 600,
        'shortage_severity': 'High',
        'availability_pct': 55,
        'price_increase_pct': 28,
        'new_price_usd': 768,
        'timeline_months': 6,
        'alternatives': ['Regular TVs', 'Streaming devices', 'Projectors'],
        'consumer_impact': 'Medium - Entertainment device'
    },
    'Electric Vehicles': {
        'category': 'Automotive',
        'current_price_usd': 45000,
        'shortage_severity': 'Critical',
        'availability_pct': 40,
        'price_increase_pct': 25,
        'new_price_usd': 56250,
        'timeline_months': 12,
        'alternatives': ['Hybrid vehicles', 'Gas vehicles', 'Public transport'],
        'consumer_impact': 'High - Major purchase, environmental impact'
    },
    'Smart Home Devices': {
        'category': 'Consumer Goods',
        'current_price_usd': 150,
        'shortage_severity': 'Medium',
        'availability_pct': 60,
        'price_increase_pct': 22,
        'new_price_usd': 183,
        'timeline_months': 5,
        'alternatives': ['Manual devices', 'Basic automation', 'Smartphone apps'],
        'consumer_impact': 'Low - Convenience device'
    },
    'Tablets': {
        'category': 'Electronics',
        'current_price_usd': 500,
        'shortage_severity': 'High',
        'availability_pct': 48,
        'price_increase_pct': 30,
        'new_price_usd': 650,
        'timeline_months': 7,
        'alternatives': ['Laptops', 'Smartphones', 'E-readers'],
        'consumer_impact': 'Medium - Education and entertainment'
    },
    'Smartwatches': {
        'category': 'Wearables',
        'current_price_usd': 400,
        'shortage_severity': 'Medium',
        'availability_pct': 58,
        'price_increase_pct': 25,
        'new_price_usd': 500,
        'timeline_months': 6,
        'alternatives': ['Fitness trackers', 'Regular watches', 'Smartphone apps'],
        'consumer_impact': 'Low - Convenience device'
    },
    'Graphics Cards': {
        'category': 'Gaming',
        'current_price_usd': 600,
        'shortage_severity': 'Critical',
        'availability_pct': 30,
        'price_increase_pct': 45,
        'new_price_usd': 870,
        'timeline_months': 10,
        'alternatives': ['Integrated graphics', 'Cloud gaming', 'Console gaming'],
        'consumer_impact': 'Medium - Gaming and professional work'
    },
    'Smart Appliances': {
        'category': 'Consumer Goods',
        'current_price_usd': 1200,
        'shortage_severity': 'Medium',
        'availability_pct': 62,
        'price_increase_pct': 20,
        'new_price_usd': 1440,
        'timeline_months': 5,
        'alternatives': ['Regular appliances', 'Manual operation', 'Repair old appliances'],
        'consumer_impact': 'Low - Convenience feature'
    },
    'Wireless Earbuds': {
        'category': 'Electronics',
        'current_price_usd': 200,
        'shortage_severity': 'Medium',
        'availability_pct': 65,
        'price_increase_pct': 18,
        'new_price_usd': 236,
        'timeline_months': 4,
        'alternatives': ['Wired earphones', 'Over-ear headphones', 'Speakers'],
        'consumer_impact': 'Low - Convenience device'
    },
    'Home Security Systems': {
        'category': 'Consumer Goods',
        'current_price_usd': 500,
        'shortage_severity': 'Medium',
        'availability_pct': 58,
        'price_increase_pct': 24,
        'new_price_usd': 620,
        'timeline_months': 6,
        'alternatives': ['Basic alarm systems', 'Manual locks', 'Neighborhood watch'],
        'consumer_impact': 'Medium - Safety concern'
    },
    'Drones': {
        'category': 'Electronics',
        'current_price_usd': 800,
        'shortage_severity': 'High',
        'availability_pct': 45,
        'price_increase_pct': 35,
        'new_price_usd': 1080,
        'timeline_months': 8,
        'alternatives': ['Photography equipment', 'Action cameras', 'Rental services'],
        'consumer_impact': 'Low - Hobby device'
    },
    'VR Headsets': {
        'category': 'Gaming',
        'current_price_usd': 400,
        'shortage_severity': 'High',
        'availability_pct': 42,
        'price_increase_pct': 38,
        'new_price_usd': 552,
        'timeline_months': 9,
        'alternatives': ['Traditional gaming', 'Mobile VR', 'AR apps'],
        'consumer_impact': 'Low - Entertainment device'
    },
    'Digital Cameras': {
        'category': 'Electronics',
        'current_price_usd': 1000,
        'shortage_severity': 'Medium',
        'availability_pct': 60,
        'price_increase_pct': 22,
        'new_price_usd': 1220,
        'timeline_months': 5,
        'alternatives': ['Smartphone cameras', 'Film cameras', 'Rental services'],
        'consumer_impact': 'Low - Professional/hobby device'
    }
}

# Consumer spending patterns
CONSUMER_SPENDING_IMPACT = {
    'Electronics': {
        'current_spending_billions': 450,
        'projected_spending_billions': 292,
        'change_pct': -35,
        'affected_consumers_millions': 180
    },
    'Automotive': {
        'current_spending_billions': 380,
        'projected_spending_billions': 274,
        'change_pct': -28,
        'affected_consumers_millions': 25
    },
    'Gaming': {
        'current_spending_billions': 85,
        'projected_spending_billions': 58,
        'change_pct': -32,
        'affected_consumers_millions': 95
    },
    'Consumer Goods': {
        'current_spending_billions': 220,
        'projected_spending_billions': 180,
        'change_pct': -18,
        'affected_consumers_millions': 150
    }
}

# Timeline of impact
IMPACT_TIMELINE = {
    'Month 1-2': {
        'phase': 'Initial Shock',
        'availability': '70%',
        'price_increase': '5-10%',
        'consumer_behavior': 'Panic buying, hoarding'
    },
    'Month 3-4': {
        'phase': 'Shortage Peak',
        'availability': '45%',
        'price_increase': '20-30%',
        'consumer_behavior': 'Seeking alternatives, delaying purchases'
    },
    'Month 5-8': {
        'phase': 'Adaptation',
        'availability': '55%',
        'price_increase': '25-35%',
        'consumer_behavior': 'Accepting higher prices, using alternatives'
    },
    'Month 9-12': {
        'phase': 'Gradual Recovery',
        'availability': '65%',
        'price_increase': '15-25%',
        'consumer_behavior': 'Cautious purchasing, waiting for deals'
    },
    'Month 13-18': {
        'phase': 'Stabilization',
        'availability': '80%',
        'price_increase': '5-15%',
        'consumer_behavior': 'Return to normal, pent-up demand'
    }
}

def get_product_data(product_name):
    """Get data for a specific product"""
    return CONSUMER_PRODUCTS.get(product_name, None)

def get_all_products():
    """Get list of all products"""
    return list(CONSUMER_PRODUCTS.keys())

def get_products_by_severity(severity):
    """Get products filtered by shortage severity"""
    return [product for product, data in CONSUMER_PRODUCTS.items() 
            if data['shortage_severity'] == severity]

def get_critical_products():
    """Get products with critical shortage"""
    return get_products_by_severity('Critical')

def get_spending_impact():
    """Get consumer spending impact data"""
    return CONSUMER_SPENDING_IMPACT

def get_impact_timeline():
    """Get timeline of impact phases"""
    return IMPACT_TIMELINE
# Export for app.py
PRODUCT_DATA = CONSUMER_PRODUCTS
# Made with Bob
