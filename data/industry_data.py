"""
Industry impact data for semiconductor supply chain disruption
"""

# Industry-specific impact data
INDUSTRY_IMPACTS = {
    'Electronics': {
        'impact_score': 95,
        'risk_level': 'Critical',
        'revenue_impact_pct': -35,
        'production_delay_months': 6,
        'affected_products': ['Smartphones', 'Laptops', 'Tablets', 'Gaming Consoles', 'Smart TVs'],
        'major_companies': ['Apple', 'Samsung', 'Sony', 'Dell', 'HP', 'Lenovo'],
        'recovery_time_months': 18,
        'mitigation_strategies': ['Diversify suppliers', 'Increase inventory', 'Redesign products']
    },
    'Automotive': {
        'impact_score': 88,
        'risk_level': 'Critical',
        'revenue_impact_pct': -28,
        'production_delay_months': 5,
        'affected_products': ['Electric Vehicles', 'Smart Cars', 'Autonomous Vehicles', 'Infotainment Systems'],
        'major_companies': ['Tesla', 'Toyota', 'Volkswagen', 'GM', 'Ford', 'BMW'],
        'recovery_time_months': 15,
        'mitigation_strategies': ['Alternative chip sources', 'Simplify electronics', 'Stockpile chips']
    },
    'Telecommunications': {
        'impact_score': 82,
        'risk_level': 'High',
        'revenue_impact_pct': -25,
        'production_delay_months': 4,
        'affected_products': ['5G Equipment', 'Network Infrastructure', 'Routers', 'Modems'],
        'major_companies': ['Cisco', 'Huawei', 'Ericsson', 'Nokia', 'Qualcomm'],
        'recovery_time_months': 14,
        'mitigation_strategies': ['Upgrade existing equipment', 'Delay 5G rollout', 'Import alternatives']
    },
    'Healthcare': {
        'impact_score': 75,
        'risk_level': 'High',
        'revenue_impact_pct': -20,
        'production_delay_months': 4,
        'affected_products': ['Medical Devices', 'Diagnostic Equipment', 'Monitoring Systems', 'Imaging Machines'],
        'major_companies': ['Medtronic', 'GE Healthcare', 'Siemens Healthineers', 'Philips Healthcare'],
        'recovery_time_months': 12,
        'mitigation_strategies': ['Prioritize critical devices', 'Extend equipment life', 'Manual alternatives']
    },
    'Defense': {
        'impact_score': 78,
        'risk_level': 'High',
        'revenue_impact_pct': -22,
        'production_delay_months': 5,
        'affected_products': ['Military Electronics', 'Radar Systems', 'Communication Equipment', 'Drones'],
        'major_companies': ['Lockheed Martin', 'Raytheon', 'Northrop Grumman', 'BAE Systems'],
        'recovery_time_months': 16,
        'mitigation_strategies': ['Domestic production', 'Strategic reserves', 'Simplified systems']
    },
    'Consumer Goods': {
        'impact_score': 65,
        'risk_level': 'Medium',
        'revenue_impact_pct': -18,
        'production_delay_months': 3,
        'affected_products': ['Smart Home Devices', 'Wearables', 'IoT Devices', 'Smart Appliances'],
        'major_companies': ['Amazon', 'Google', 'Xiaomi', 'LG', 'Samsung'],
        'recovery_time_months': 10,
        'mitigation_strategies': ['Reduce smart features', 'Focus on basics', 'Alternative suppliers']
    },
    'Industrial': {
        'impact_score': 70,
        'risk_level': 'High',
        'revenue_impact_pct': -24,
        'production_delay_months': 4,
        'affected_products': ['Industrial Robots', 'Automation Systems', 'Control Systems', 'Sensors'],
        'major_companies': ['Siemens', 'ABB', 'Schneider Electric', 'Rockwell Automation'],
        'recovery_time_months': 13,
        'mitigation_strategies': ['Retrofit old equipment', 'Manual processes', 'Phased upgrades']
    },
    'Aerospace': {
        'impact_score': 72,
        'risk_level': 'High',
        'revenue_impact_pct': -21,
        'production_delay_months': 5,
        'affected_products': ['Avionics', 'Flight Control Systems', 'Navigation Systems', 'Communication Systems'],
        'major_companies': ['Boeing', 'Airbus', 'Honeywell', 'Collins Aerospace'],
        'recovery_time_months': 14,
        'mitigation_strategies': ['Extend aircraft life', 'Delay new models', 'Certified alternatives']
    },
    'Energy': {
        'impact_score': 58,
        'risk_level': 'Medium',
        'revenue_impact_pct': -15,
        'production_delay_months': 3,
        'affected_products': ['Smart Grid Systems', 'Solar Inverters', 'Wind Turbine Controllers', 'Battery Management'],
        'major_companies': ['Tesla Energy', 'Siemens Energy', 'GE Renewable Energy', 'Vestas'],
        'recovery_time_months': 9,
        'mitigation_strategies': ['Delay smart grid', 'Basic controllers', 'Extend maintenance cycles']
    },
    'Finance': {
        'impact_score': 45,
        'risk_level': 'Low',
        'revenue_impact_pct': -8,
        'production_delay_months': 2,
        'affected_products': ['Data Centers', 'Trading Systems', 'ATMs', 'Payment Terminals'],
        'major_companies': ['JPMorgan', 'Goldman Sachs', 'Visa', 'Mastercard'],
        'recovery_time_months': 6,
        'mitigation_strategies': ['Cloud migration', 'Extend hardware life', 'Software optimization']
    },
    'Retail': {
        'impact_score': 52,
        'risk_level': 'Medium',
        'revenue_impact_pct': -12,
        'production_delay_months': 2,
        'affected_products': ['POS Systems', 'Inventory Management', 'E-commerce Infrastructure', 'Digital Signage'],
        'major_companies': ['Amazon', 'Walmart', 'Alibaba', 'Target'],
        'recovery_time_months': 7,
        'mitigation_strategies': ['Manual processes', 'Delay upgrades', 'Cloud solutions']
    },
    'Gaming': {
        'impact_score': 85,
        'risk_level': 'High',
        'revenue_impact_pct': -32,
        'production_delay_months': 5,
        'affected_products': ['Gaming Consoles', 'Graphics Cards', 'Gaming PCs', 'VR Headsets'],
        'major_companies': ['Sony', 'Microsoft', 'Nintendo', 'Nvidia', 'AMD'],
        'recovery_time_months': 15,
        'mitigation_strategies': ['Focus on software', 'Extend console life', 'Cloud gaming']
    }
}

# Investment opportunities and risks
INVESTMENT_ANALYSIS = {
    'Buy Opportunities': {
        'Logistics': {
            'reason': 'Increased demand for alternative shipping routes and warehousing',
            'expected_growth': '+25%',
            'companies': ['FedEx', 'UPS', 'DHL', 'Maersk']
        },
        'Alternative Semiconductor Manufacturers': {
            'reason': 'Companies outside Taiwan will gain market share',
            'expected_growth': '+40%',
            'companies': ['Intel', 'Samsung', 'GlobalFoundries', 'SMIC']
        },
        'Cloud Services': {
            'reason': 'Shift from hardware to cloud-based solutions',
            'expected_growth': '+30%',
            'companies': ['AWS', 'Microsoft Azure', 'Google Cloud', 'Alibaba Cloud']
        }
    },
    'Hold Opportunities': {
        'Diversified Tech': {
            'reason': 'Companies with diverse supply chains will weather the storm',
            'expected_impact': '-5% to +5%',
            'companies': ['Microsoft', 'Google', 'IBM', 'Oracle']
        },
        'Software Companies': {
            'reason': 'Less dependent on hardware, focus on optimization',
            'expected_impact': '0% to +10%',
            'companies': ['Adobe', 'Salesforce', 'SAP', 'ServiceNow']
        }
    },
    'High Risk': {
        'Electronics': {
            'reason': 'Heavily dependent on Taiwan semiconductors',
            'expected_loss': '-35%',
            'companies': ['Apple', 'Samsung Electronics', 'Sony', 'Dell']
        },
        'EV Manufacturers': {
            'reason': 'Critical chip shortage for electric vehicles',
            'expected_loss': '-28%',
            'companies': ['Tesla', 'Rivian', 'Lucid', 'NIO']
        },
        'Gaming': {
            'reason': 'Console and GPU production severely impacted',
            'expected_loss': '-32%',
            'companies': ['Sony', 'Microsoft Gaming', 'Nintendo', 'Nvidia']
        },
        'FMCG with Smart Products': {
            'reason': 'Smart appliances and IoT products affected',
            'expected_loss': '-18%',
            'companies': ['LG', 'Samsung Home', 'Whirlpool', 'Electrolux']
        }
    }
}

def get_industry_data(industry_name):
    """Get data for a specific industry"""
    return INDUSTRY_IMPACTS.get(industry_name, None)

def get_all_industries():
    """Get list of all industries"""
    return list(INDUSTRY_IMPACTS.keys())

def get_high_risk_industries():
    """Get industries with high or critical risk"""
    return [industry for industry, data in INDUSTRY_IMPACTS.items() 
            if data['risk_level'] in ['High', 'Critical']]

def get_investment_opportunities():
    """Get investment analysis data"""
    return INVESTMENT_ANALYSIS

def get_industries_by_risk(risk_level):
    """Get industries filtered by risk level"""
    return [industry for industry, data in INDUSTRY_IMPACTS.items() 
            if data['risk_level'] == risk_level]
# Export for app.py
INDUSTRY_DATA = INDUSTRY_IMPACTS
INVESTMENT_DATA = INVESTMENT_ANALYSIS

# Made with Bob
