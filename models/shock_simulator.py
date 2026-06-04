"""
Global Supply Chain Shock Simulator
Simulates different types of supply chain disruptions
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

class ShockSimulator:
    """Simulates global supply chain shocks"""
    
    SHOCK_TYPES = {
        'Semiconductor Shock': {
            'description': 'Taiwan semiconductor supply chain disruption',
            'default_intensity': 40,
            'affected_sectors': ['Electronics', 'Automotive', 'Telecommunications', 'Gaming'],
            'geographic_focus': 'Taiwan',
            'duration_months': 18
        },
        'Oil Shock': {
            'description': 'Middle East crude oil price increase',
            'default_intensity': 35,
            'affected_sectors': ['Energy', 'Transportation', 'Manufacturing', 'Logistics'],
            'geographic_focus': 'Middle East',
            'duration_months': 12
        },
        'Shipping Crisis': {
            'description': 'Global shipping and logistics disruption',
            'default_intensity': 30,
            'affected_sectors': ['Retail', 'Manufacturing', 'Consumer Goods', 'Automotive'],
            'geographic_focus': 'Global',
            'duration_months': 10
        },
        'Trade Restriction': {
            'description': 'International trade restrictions and tariffs',
            'default_intensity': 25,
            'affected_sectors': ['Manufacturing', 'Retail', 'Agriculture', 'Technology'],
            'geographic_focus': 'Multiple Regions',
            'duration_months': 24
        },
        'Currency Shock': {
            'description': 'Major currency volatility and devaluation',
            'default_intensity': 20,
            'affected_sectors': ['Finance', 'Retail', 'Import/Export', 'Tourism'],
            'geographic_focus': 'Global',
            'duration_months': 8
        }
    }
    
    def __init__(self, shock_type='Semiconductor Shock', intensity=40, countries_data=None, industry_data=None, product_data=None):
        """
        Initialize shock simulator
        
        Args:
            shock_type: Type of shock to simulate
            intensity: Intensity of shock (0-100%)
            countries_data: Dictionary of country data
            industry_data: Dictionary of industry data
            product_data: Dictionary of product data
        """
        self.shock_type = shock_type
        self.intensity = intensity
        self.shock_config = self.SHOCK_TYPES.get(shock_type, self.SHOCK_TYPES['Semiconductor Shock'])
        self.start_date = datetime.now()
        
        # Store data
        self.countries_data = countries_data or {}
        self.industry_data = industry_data or {}
        self.product_data = product_data or {}
        
    def calculate_impact_multiplier(self):
        """Calculate impact multiplier based on intensity"""
        return self.intensity / 100.0
    
    def get_shock_details(self):
        """Get detailed information about the shock"""
        return {
            'type': self.shock_type,
            'description': self.shock_config['description'],
            'intensity': self.intensity,
            'affected_sectors': self.shock_config['affected_sectors'],
            'geographic_focus': self.shock_config['geographic_focus'],
            'duration_months': self.shock_config['duration_months'],
            'start_date': self.start_date.strftime('%Y-%m-%d'),
            'estimated_end_date': (self.start_date + timedelta(days=30 * self.shock_config['duration_months'])).strftime('%Y-%m-%d')
        }
    
    def simulate_country_impact(self, country_data):
        """
        Simulate impact on a specific country
        
        Args:
            country_data: Dictionary with country information
            
        Returns:
            Dictionary with simulated impact
        """
        multiplier = self.calculate_impact_multiplier()
        
        # Calculate adjusted impacts
        adjusted_gdp_impact = country_data['gdp_impact_pct'] * multiplier
        adjusted_dependency = country_data['dependency_score'] * multiplier / 100
        
        return {
            'country': country_data,
            'simulated_gdp_impact_pct': round(adjusted_gdp_impact, 2),
            'simulated_dependency_score': round(adjusted_dependency * 100, 1),
            'risk_level': self._calculate_risk_level(adjusted_dependency * 100),
            'estimated_recovery_months': self._estimate_recovery_time(country_data['dependency_score'])
        }
    
    def simulate_industry_impact(self, industry_data):
        """
        Simulate impact on a specific industry
        
        Args:
            industry_data: Dictionary with industry information
            
        Returns:
            Dictionary with simulated impact
        """
        multiplier = self.calculate_impact_multiplier()
        
        # Check if industry is in affected sectors
        is_directly_affected = any(sector in industry_data.get('major_companies', []) 
                                   for sector in self.shock_config['affected_sectors'])
        
        impact_factor = 1.0 if is_directly_affected else 0.6
        
        adjusted_revenue_impact = industry_data['revenue_impact_pct'] * multiplier * impact_factor
        adjusted_delay = industry_data['production_delay_months'] * multiplier * impact_factor
        
        return {
            'industry': industry_data,
            'simulated_revenue_impact_pct': round(adjusted_revenue_impact, 2),
            'simulated_production_delay_months': round(adjusted_delay, 1),
            'is_directly_affected': is_directly_affected,
            'estimated_recovery_months': round(industry_data['recovery_time_months'] * multiplier, 1)
        }
    
    def simulate_product_impact(self, product_data):
        """
        Simulate impact on consumer products
        
        Args:
            product_data: Dictionary with product information
            
        Returns:
            Dictionary with simulated impact
        """
        multiplier = self.calculate_impact_multiplier()
        
        # Calculate adjusted impacts
        adjusted_availability = 100 - ((100 - product_data['availability_pct']) * multiplier)
        adjusted_price_increase = product_data['price_increase_pct'] * multiplier
        new_price = product_data['current_price_usd'] * (1 + adjusted_price_increase / 100)
        
        return {
            'product': product_data['category'],
            'product_name': list(product_data.keys())[0] if isinstance(product_data, dict) else 'Unknown',
            'simulated_availability_pct': round(adjusted_availability, 1),
            'simulated_price_increase_pct': round(adjusted_price_increase, 1),
            'current_price_usd': product_data['current_price_usd'],
            'simulated_new_price_usd': round(new_price, 2),
            'estimated_shortage_duration_months': round(product_data['timeline_months'] * multiplier, 1)
        }
    
    def generate_timeline(self):
        """Generate timeline of disruption phases"""
        phases = {
            'Immediate Impact (0-3 months)': {
                'duration': '0-3 months',
                'supply_disruption_pct': round(self.intensity * 0.8, 1),
                'price_impact_pct': round(self.intensity * 0.6, 1),
                'recovery_progress_pct': 0,
                'key_events': [
                    'Initial supply chain disruption',
                    'Inventory depletion begins',
                    'Price increases start'
                ]
            },
            'Peak Disruption (3-9 months)': {
                'duration': '3-9 months',
                'supply_disruption_pct': round(self.intensity, 1),
                'price_impact_pct': round(self.intensity * 0.9, 1),
                'recovery_progress_pct': 10,
                'key_events': [
                    'Maximum supply shortage',
                    'Peak price increases',
                    'Alternative sourcing begins'
                ]
            },
            'Recovery Phase (9-18 months)': {
                'duration': '9-18 months',
                'supply_disruption_pct': round(self.intensity * 0.5, 1),
                'price_impact_pct': round(self.intensity * 0.4, 1),
                'recovery_progress_pct': 50,
                'key_events': [
                    'Supply gradually improves',
                    'Prices begin to stabilize',
                    'New supply chains established'
                ]
            },
            'Stabilization (18-24 months)': {
                'duration': '18-24 months',
                'supply_disruption_pct': round(self.intensity * 0.2, 1),
                'price_impact_pct': round(self.intensity * 0.15, 1),
                'recovery_progress_pct': 85,
                'key_events': [
                    'Near-normal supply levels',
                    'Prices return to baseline',
                    'Market stabilizes'
                ]
            }
        }
        return phases
    
    def _calculate_risk_level(self, dependency_score):
        """Calculate risk level based on dependency score"""
        if dependency_score >= 80:
            return 'Critical'
        elif dependency_score >= 60:
            return 'High'
        elif dependency_score >= 40:
            return 'Medium'
        else:
            return 'Low'
    
    def _estimate_recovery_time(self, dependency_score):
        """Estimate recovery time based on dependency"""
        base_recovery = self.shock_config['duration_months']
        dependency_factor = dependency_score / 100
        return round(base_recovery * (0.5 + dependency_factor), 1)
    
    def generate_timeline_projection(self, months=18):
        """
        Generate timeline projection of shock impact
        
        Args:
            months: Number of months to project
            
        Returns:
            DataFrame with timeline data
        """
        timeline_data = []
        multiplier = self.calculate_impact_multiplier()
        
        for month in range(1, months + 1):
            # Impact follows a curve: peaks at 1/3 duration, then gradually recovers
            peak_month = self.shock_config['duration_months'] / 3
            
            if month <= peak_month:
                # Escalation phase
                impact_factor = (month / peak_month) * multiplier
            else:
                # Recovery phase
                remaining_months = self.shock_config['duration_months'] - month
                if remaining_months > 0:
                    impact_factor = multiplier * (remaining_months / (self.shock_config['duration_months'] - peak_month))
                else:
                    impact_factor = multiplier * 0.1  # Residual impact
            
            timeline_data.append({
                'month': month,
                'date': (self.start_date + timedelta(days=30 * month)).strftime('%Y-%m'),
                'impact_intensity': round(impact_factor * 100, 1),
                'phase': self._get_phase(month, peak_month)
            })
        
        return pd.DataFrame(timeline_data)
    
    def _get_phase(self, month, peak_month):
        """Determine which phase of the shock we're in"""
        if month <= 2:
            return 'Initial Shock'
        elif month <= peak_month:
            return 'Escalation'
        elif month <= self.shock_config['duration_months']:
            return 'Peak Impact'
        elif month <= self.shock_config['duration_months'] * 1.5:
            return 'Recovery'
        else:
            return 'Stabilization'
    
    def get_summary_statistics(self):
        """Get summary statistics of the shock"""
        multiplier = self.calculate_impact_multiplier()
        
        return {
            'shock_type': self.shock_type,
            'intensity': self.intensity,
            'duration_months': self.shock_config['duration_months'],
            'affected_sectors_count': len(self.shock_config['affected_sectors']),
            'estimated_global_gdp_impact_pct': round(-2.5 * multiplier, 2),
            'estimated_affected_countries': round(15 * multiplier),
            'estimated_affected_industries': round(12 * multiplier),
            'peak_impact_month': round(self.shock_config['duration_months'] / 3, 1),
            'recovery_completion_month': self.shock_config['duration_months']
        }

def get_available_shocks():
    """Get list of available shock types"""
    return list(ShockSimulator.SHOCK_TYPES.keys())

def get_shock_description(shock_type):
    """Get description of a specific shock type"""
    return ShockSimulator.SHOCK_TYPES.get(shock_type, {}).get('description', 'Unknown shock type')

# Made with Bob

