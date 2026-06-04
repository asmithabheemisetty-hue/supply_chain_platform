"""
Consumer Impact Analyzer
Predicts impact on consumer products, prices, and spending
"""

import pandas as pd
from datetime import datetime, timedelta

class ConsumerImpactAnalyzer:
    """Analyzes impact of supply chain shocks on consumers"""
    
    def __init__(self, shock_simulator, product_data):
        """
        Initialize consumer impact analyzer
        
        Args:
            shock_simulator: ShockSimulator instance
            product_data: Dictionary of product data
        """
        self.shock_simulator = shock_simulator
        self.product_data = product_data
        self.intensity = shock_simulator.intensity
        
    def analyze_product_shortages(self):
        """
        Analyze which products will face shortages
        
        Returns:
            List of products with shortage predictions
        """
        shortages = []
        multiplier = self.intensity / 100.0
        
        for product_name, product_info in self.product_data.items():
            shortage_pct = 100 - product_info['availability_pct']
            adjusted_shortage = shortage_pct * multiplier
            
            if adjusted_shortage > 20:  # Significant shortage
                shortages.append({
                    'product': product_name,
                    'category': product_info['category'],
                    'shortage_severity': product_info['shortage_severity'],
                    'shortage_pct': round(adjusted_shortage, 1),
                    'availability_pct': round(100 - adjusted_shortage, 1),
                    'timeline_months': round(product_info['timeline_months'] * multiplier, 1),
                    'consumer_impact': product_info['consumer_impact'],
                    'alternatives': product_info['alternatives']
                })
        
        # Sort by shortage percentage (descending)
        shortages.sort(key=lambda x: x['shortage_pct'], reverse=True)
        return shortages
    
    def predict_price_increases(self):
        """
        Predict price increases for consumer products
        
        Returns:
            List of products with price predictions
        """
        price_predictions = []
        multiplier = self.intensity / 100.0
        
        for product_name, product_info in self.product_data.items():
            adjusted_increase = product_info['price_increase_pct'] * multiplier
            new_price = product_info['current_price_usd'] * (1 + adjusted_increase / 100)
            price_diff = new_price - product_info['current_price_usd']
            
            price_predictions.append({
                'product': product_name,
                'category': product_info['category'],
                'current_price_usd': product_info['current_price_usd'],
                'predicted_price_usd': round(new_price, 2),
                'price_increase_pct': round(adjusted_increase, 1),
                'price_increase_usd': round(price_diff, 2),
                'timeline_months': round(product_info['timeline_months'] * multiplier, 1)
            })
        
        # Sort by price increase percentage (descending)
        price_predictions.sort(key=lambda x: x['price_increase_pct'], reverse=True)
        return price_predictions
    
    def estimate_spending_changes(self, spending_data):
        """
        Estimate changes in consumer spending patterns
        
        Args:
            spending_data: Dictionary of spending data by category
            
        Returns:
            Dictionary with spending predictions
        """
        multiplier = self.intensity / 100.0
        spending_changes = {}
        
        for category, data in spending_data.items():
            adjusted_change = data['change_pct'] * multiplier
            projected_spending = data['current_spending_billions'] * (1 + adjusted_change / 100)
            spending_diff = projected_spending - data['current_spending_billions']
            
            spending_changes[category] = {
                'current_spending_billions': data['current_spending_billions'],
                'projected_spending_billions': round(projected_spending, 2),
                'change_pct': round(adjusted_change, 1),
                'change_billions': round(spending_diff, 2),
                'affected_consumers_millions': round(data['affected_consumers_millions'] * multiplier, 1)
            }
        
        return spending_changes
    
    def generate_consumer_timeline(self, timeline_data):
        """
        Generate timeline of consumer impact
        
        Args:
            timeline_data: Dictionary of timeline phases
            
        Returns:
            List of timeline predictions
        """
        timeline = []
        multiplier = self.intensity / 100.0
        
        for phase, data in timeline_data.items():
            # Parse availability and price increase ranges
            availability = data['availability'].rstrip('%')
            price_range = data['price_increase']
            
            # Adjust based on intensity
            if '-' in price_range:
                low, high = price_range.rstrip('%').split('-')
                adjusted_low = float(low) * multiplier
                adjusted_high = float(high) * multiplier
                adjusted_price = f"{adjusted_low:.0f}-{adjusted_high:.0f}%"
            else:
                adjusted_price = price_range
            
            timeline.append({
                'phase': phase,
                'phase_name': data['phase'],
                'availability': data['availability'],
                'price_increase': adjusted_price,
                'consumer_behavior': data['consumer_behavior']
            })
        
        return timeline
    
    def get_most_affected_products(self, top_n=10):
        """
        Get the most affected products
        
        Args:
            top_n: Number of top products to return
            
        Returns:
            List of most affected products
        """
        shortages = self.analyze_product_shortages()
        return shortages[:top_n]
    
    def get_highest_price_increases(self, top_n=10):
        """
        Get products with highest price increases
        
        Args:
            top_n: Number of top products to return
            
        Returns:
            List of products with highest price increases
        """
        price_predictions = self.predict_price_increases()
        return price_predictions[:top_n]
    
    def calculate_consumer_burden(self, spending_data):
        """
        Calculate overall consumer financial burden
        
        Args:
            spending_data: Dictionary of spending data
            
        Returns:
            Dictionary with burden metrics
        """
        spending_changes = self.estimate_spending_changes(spending_data)
        
        total_current = sum(data['current_spending_billions'] for data in spending_changes.values())
        total_projected = sum(data['projected_spending_billions'] for data in spending_changes.values())
        total_affected = sum(data['affected_consumers_millions'] for data in spending_changes.values())
        
        return {
            'total_current_spending_billions': round(total_current, 2),
            'total_projected_spending_billions': round(total_projected, 2),
            'total_change_billions': round(total_projected - total_current, 2),
            'average_change_pct': round(((total_projected - total_current) / total_current) * 100, 2),
            'total_affected_consumers_millions': round(total_affected, 1),
            'per_consumer_impact_usd': round((total_projected - total_current) * 1000 / total_affected, 2) if total_affected > 0 else 0
        }
    
    def generate_recommendations(self):
        """
        Generate consumer recommendations
        
        Returns:
            List of recommendations for consumers
        """
        recommendations = [
            {
                'category': 'Immediate Actions',
                'recommendations': [
                    'Avoid panic buying - it worsens shortages',
                    'Consider purchasing essential electronics now before prices increase further',
                    'Explore refurbished or previous-generation products as alternatives',
                    'Delay non-essential tech purchases if possible'
                ]
            },
            {
                'category': 'Budget Planning',
                'recommendations': [
                    f'Expect {self.intensity}% higher prices on electronics over next 6-8 months',
                    'Allocate additional budget for essential tech replacements',
                    'Consider extended warranties to delay replacement needs',
                    'Look for bundle deals and promotions'
                ]
            },
            {
                'category': 'Alternative Solutions',
                'recommendations': [
                    'Use cloud services instead of upgrading hardware',
                    'Repair existing devices rather than replacing',
                    'Consider rental or subscription models for expensive electronics',
                    'Explore open-source and software-based alternatives'
                ]
            },
            {
                'category': 'Long-term Strategy',
                'recommendations': [
                    'Diversify technology ecosystem to reduce dependency',
                    'Invest in durable, repairable products',
                    'Stay informed about supply chain developments',
                    'Support local and alternative manufacturers'
                ]
            }
        ]
        
        return recommendations
    
    def get_summary_metrics(self):
        """
        Get summary metrics of consumer impact
        
        Returns:
            Dictionary with key metrics
        """
        shortages = self.analyze_product_shortages()
        price_predictions = self.predict_price_increases()
        
        critical_shortages = [s for s in shortages if s['shortage_severity'] == 'Critical']
        high_price_increases = [p for p in price_predictions if p['price_increase_pct'] > 25]
        
        return {
            'total_products_affected': len(self.product_data),
            'products_with_shortages': len(shortages),
            'critical_shortage_products': len(critical_shortages),
            'products_with_high_price_increase': len(high_price_increases),
            'average_price_increase_pct': round(sum(p['price_increase_pct'] for p in price_predictions) / len(price_predictions), 1) if price_predictions else 0,
            'average_shortage_pct': round(sum(s['shortage_pct'] for s in shortages) / len(shortages), 1) if shortages else 0,
            'average_timeline_months': round(sum(s['timeline_months'] for s in shortages) / len(shortages), 1) if shortages else 0
        }
    def analyze_consumer_spending_changes(self):
        """
        Analyze consumer spending changes by category
        
        Returns:
            Dictionary with spending changes
        """
        multiplier = self.intensity / 100.0
        
        spending_changes = {
            'Electronics': {
                'change_pct': round(-15 * multiplier, 1),
                'trend': 'Decreasing' if multiplier > 0.3 else 'Stable'
            },
            'Automotive': {
                'change_pct': round(-12 * multiplier, 1),
                'trend': 'Decreasing' if multiplier > 0.3 else 'Stable'
            },
            'Home Appliances': {
                'change_pct': round(-8 * multiplier, 1),
                'trend': 'Decreasing' if multiplier > 0.2 else 'Stable'
            },
            'Gaming': {
                'change_pct': round(-10 * multiplier, 1),
                'trend': 'Decreasing' if multiplier > 0.3 else 'Stable'
            },
            'Overall': {
                'change_pct': round(-11 * multiplier, 1),
                'trend': 'Decreasing' if multiplier > 0.3 else 'Stable'
            }
        }
        
        return spending_changes
    
    def analyze_product_shortages(self):
        """
        Analyze product shortages with detailed metrics
        
        Returns:
            List of products with shortage analysis
        """
        shortages = []
        multiplier = self.intensity / 100.0
        
        for product_name, product_info in self.product_data.items():
            shortage_severity_score = product_info.get('shortage_severity_score', 50) * multiplier
            availability_pct = max(0, 100 - (100 - product_info['availability_pct']) * multiplier)
            price_increase_pct = product_info['price_increase_pct'] * multiplier
            
            # Determine shortage level
            if shortage_severity_score >= 75:
                shortage_level = 'Critical'
            elif shortage_severity_score >= 60:
                shortage_level = 'High'
            elif shortage_severity_score >= 40:
                shortage_level = 'Medium'
            else:
                shortage_level = 'Low'
            
            shortages.append({
                'product': product_name,
                'category': product_info['category'],
                'shortage_severity_score': round(shortage_severity_score, 1),
                'shortage_level': shortage_level,
                'availability_pct': round(availability_pct, 1),
                'price_increase_pct': round(price_increase_pct, 1),
                'shortage_timeline': f"{round(product_info['timeline_months'] * multiplier, 1)} months",
                'recommendation': self._get_product_recommendation(shortage_level, price_increase_pct)
            })
        
        # Sort by shortage severity
        shortages.sort(key=lambda x: x['shortage_severity_score'], reverse=True)
        return shortages
    
    def _get_product_recommendation(self, shortage_level, price_increase):
        """Generate recommendation based on shortage and price"""
        if shortage_level == 'Critical':
            return 'Purchase immediately if needed, expect significant delays'
        elif shortage_level == 'High':
            return 'Consider purchasing soon, prices likely to increase further'
        elif shortage_level == 'Medium':
            return 'Monitor prices, consider alternatives'
        else:
            return 'Normal purchasing patterns recommended'
    
    def get_summary_metrics(self):
        """
        Get summary metrics of consumer impact
        
        Returns:
            Dictionary with key metrics
        """
        shortages = self.analyze_product_shortages()
        
        # Calculate averages
        avg_price_increase = sum(s['price_increase_pct'] for s in shortages) / len(shortages) if shortages else 0
        avg_availability = sum(s['availability_pct'] for s in shortages) / len(shortages) if shortages else 100
        
        # Count critical shortages
        critical_shortages = sum(1 for s in shortages if s['shortage_level'] in ['Critical', 'High'])
        
        return {
            'products_affected': len(self.product_data),
            'avg_price_increase_pct': round(avg_price_increase, 1),
            'avg_availability_pct': round(avg_availability, 1),
            'critical_shortages': critical_shortages
        }

# Made with Bob


