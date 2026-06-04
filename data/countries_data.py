"""
Country dependency data for semiconductor supply chain
"""

# Countries and their dependency on Taiwan semiconductors
COUNTRY_DEPENDENCIES = {
    'United States': {
        'dependency_score': 85,
        'risk_level': 'Critical',
        'semiconductor_imports_pct': 65,
        'affected_industries': ['Electronics', 'Automotive', 'Defense', 'Healthcare'],
        'gdp_impact_pct': -2.8,
        'lat': 37.0902,
        'lon': -95.7129
    },
    'China': {
        'dependency_score': 92,
        'risk_level': 'Critical',
        'semiconductor_imports_pct': 75,
        'affected_industries': ['Electronics', 'Telecommunications', 'Automotive', 'Consumer Goods'],
        'gdp_impact_pct': -3.5,
        'lat': 35.8617,
        'lon': 104.1954
    },
    'Japan': {
        'dependency_score': 78,
        'risk_level': 'High',
        'semiconductor_imports_pct': 58,
        'affected_industries': ['Electronics', 'Automotive', 'Robotics'],
        'gdp_impact_pct': -2.3,
        'lat': 36.2048,
        'lon': 138.2529
    },
    'South Korea': {
        'dependency_score': 72,
        'risk_level': 'High',
        'semiconductor_imports_pct': 52,
        'affected_industries': ['Electronics', 'Automotive', 'Shipbuilding'],
        'gdp_impact_pct': -2.1,
        'lat': 35.9078,
        'lon': 127.7669
    },
    'Germany': {
        'dependency_score': 68,
        'risk_level': 'High',
        'semiconductor_imports_pct': 48,
        'affected_industries': ['Automotive', 'Industrial Machinery', 'Electronics'],
        'gdp_impact_pct': -1.9,
        'lat': 51.1657,
        'lon': 10.4515
    },
    'Taiwan': {
        'dependency_score': 100,
        'risk_level': 'Source',
        'semiconductor_imports_pct': 0,
        'affected_industries': ['Semiconductor Manufacturing', 'Electronics'],
        'gdp_impact_pct': -8.5,
        'lat': 23.6978,
        'lon': 120.9605
    },
    'United Kingdom': {
        'dependency_score': 62,
        'risk_level': 'Medium',
        'semiconductor_imports_pct': 42,
        'affected_industries': ['Automotive', 'Aerospace', 'Electronics'],
        'gdp_impact_pct': -1.5,
        'lat': 55.3781,
        'lon': -3.4360
    },
    'France': {
        'dependency_score': 58,
        'risk_level': 'Medium',
        'semiconductor_imports_pct': 38,
        'affected_industries': ['Automotive', 'Aerospace', 'Defense'],
        'gdp_impact_pct': -1.4,
        'lat': 46.2276,
        'lon': 2.2137
    },
    'India': {
        'dependency_score': 55,
        'risk_level': 'Medium',
        'semiconductor_imports_pct': 35,
        'affected_industries': ['Electronics', 'Telecommunications', 'Automotive'],
        'gdp_impact_pct': -1.2,
        'lat': 20.5937,
        'lon': 78.9629
    },
    'Brazil': {
        'dependency_score': 45,
        'risk_level': 'Medium',
        'semiconductor_imports_pct': 28,
        'affected_industries': ['Electronics', 'Automotive'],
        'gdp_impact_pct': -0.9,
        'lat': -14.2350,
        'lon': -51.9253
    },
    'Mexico': {
        'dependency_score': 52,
        'risk_level': 'Medium',
        'semiconductor_imports_pct': 32,
        'affected_industries': ['Electronics', 'Automotive', 'Manufacturing'],
        'gdp_impact_pct': -1.1,
        'lat': 23.6345,
        'lon': -102.5528
    },
    'Vietnam': {
        'dependency_score': 70,
        'risk_level': 'High',
        'semiconductor_imports_pct': 50,
        'affected_industries': ['Electronics', 'Manufacturing'],
        'gdp_impact_pct': -1.8,
        'lat': 14.0583,
        'lon': 108.2772
    },
    'Singapore': {
        'dependency_score': 75,
        'risk_level': 'High',
        'semiconductor_imports_pct': 55,
        'affected_industries': ['Electronics', 'Logistics', 'Finance'],
        'gdp_impact_pct': -2.0,
        'lat': 1.3521,
        'lon': 103.8198
    },
    'Malaysia': {
        'dependency_score': 65,
        'risk_level': 'High',
        'semiconductor_imports_pct': 45,
        'affected_industries': ['Electronics', 'Manufacturing'],
        'gdp_impact_pct': -1.6,
        'lat': 4.2105,
        'lon': 101.9758
    },
    'Thailand': {
        'dependency_score': 60,
        'risk_level': 'Medium',
        'semiconductor_imports_pct': 40,
        'affected_industries': ['Electronics', 'Automotive'],
        'gdp_impact_pct': -1.3,
        'lat': 15.8700,
        'lon': 100.9925
    }
}

# Supply chain dependency chains
DEPENDENCY_CHAINS = {
    'Taiwan -> China -> USA': {
        'description': 'Semiconductors from Taiwan to Chinese manufacturers to US consumers',
        'value_usd_billions': 450,
        'disruption_impact': 'Critical'
    },
    'Taiwan -> Japan -> Global': {
        'description': 'Advanced chips for Japanese electronics and automotive',
        'value_usd_billions': 280,
        'disruption_impact': 'High'
    },
    'Taiwan -> South Korea -> Global': {
        'description': 'Memory chips and processors for Korean tech giants',
        'value_usd_billions': 220,
        'disruption_impact': 'High'
    },
    'Taiwan -> USA -> Global': {
        'description': 'Direct semiconductor imports for US tech companies',
        'value_usd_billions': 380,
        'disruption_impact': 'Critical'
    },
    'Taiwan -> Europe -> Global': {
        'description': 'Automotive and industrial chips for European manufacturers',
        'value_usd_billions': 190,
        'disruption_impact': 'High'
    }
}

def get_country_data(country_name):
    """Get data for a specific country"""
    return COUNTRY_DEPENDENCIES.get(country_name, None)

def get_all_countries():
    """Get list of all countries"""
    return list(COUNTRY_DEPENDENCIES.keys())

def get_high_risk_countries():
    """Get countries with high or critical risk"""
    return [country for country, data in COUNTRY_DEPENDENCIES.items() 
            if data['risk_level'] in ['High', 'Critical']]

def get_countries_by_risk_level(risk_level):
    """Get countries filtered by risk level"""
    return [country for country, data in COUNTRY_DEPENDENCIES.items() 
            if data['risk_level'] == risk_level]
# Export for app.py
COUNTRIES_DATA = COUNTRY_DEPENDENCIES
# Made with Bob

# Made with Bob
