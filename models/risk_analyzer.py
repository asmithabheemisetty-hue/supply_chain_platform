"""
Supply Chain Risk Analyzer
Analyzes and quantifies supply chain risks across countries and industries
"""

import math

class RiskAnalyzer:
    """Analyzes supply chain risks and dependencies"""
    
    def __init__(self, shock_simulator, countries_data, industry_data):
        """
        Initialize risk analyzer
        
        Args:
            shock_simulator: ShockSimulator instance
            countries_data: Dictionary of country data
            industry_data: Dictionary of industry data
        """
        self.shock_simulator = shock_simulator
        self.countries_data = countries_data
        self.industry_data = industry_data
        self.intensity = shock_simulator.intensity
        
    def calculate_country_risk_scores(self):
        """
        Calculate comprehensive risk scores for each country
        
        Returns:
            Dictionary with country risk scores and analysis
        """
        risk_scores = {}
        multiplier = self.intensity / 100.0
        
        for country, data in self.countries_data.items():
            # Base risk from dependency score
            dependency_risk = data['dependency_score'] * multiplier
            
            # GDP impact risk
            gdp_impact = abs(data['gdp_impact_pct'])
            gdp_risk = gdp_impact * multiplier
            
            # Calculate composite risk score (0-100)
            composite_risk = min(100, (dependency_risk * 0.6 + gdp_risk * 0.4))
            
            # Determine risk level
            risk_level = self._categorize_risk(composite_risk)
            
            # Calculate recovery timeline
            recovery_months = self._estimate_recovery_time(composite_risk)
            
            risk_scores[country] = {
                'composite_risk_score': round(composite_risk, 1),
                'dependency_risk': round(dependency_risk, 1),
                'gdp_risk': round(gdp_risk, 1),
                'risk_level': risk_level,
                'risk_category': data['risk_level'],
                'estimated_recovery_months': recovery_months,
                'gdp_impact_pct': data['gdp_impact_pct'],
                'dependency_score': data['dependency_score'],
                'mitigation_priority': self._calculate_priority(composite_risk)
            }
        
        return risk_scores
    
    def identify_critical_dependencies(self):
        """
        Identify critical supply chain dependencies
        
        Returns:
            List of critical dependencies with analysis
        """
        dependencies = []
        
        # Analyze country dependencies
        for country, data in self.countries_data.items():
            if data['dependency_score'] >= 70:
                dependencies.append({
                    'type': 'Country',
                    'name': country,
                    'dependency_score': data['dependency_score'],
                    'impact': f"{data['gdp_impact_pct']}% GDP impact",
                    'criticality': 'Critical',
                    'mitigation_needed': True
                })
        
        # Analyze industry dependencies
        for industry, data in self.industry_data.items():
            if data['impact_score'] >= 80:
                dependencies.append({
                    'type': 'Industry',
                    'name': industry,
                    'dependency_score': data['impact_score'],
                    'impact': f"{data['revenue_impact_pct']}% revenue impact",
                    'criticality': 'Critical',
                    'mitigation_needed': True
                })
        
        # Sort by dependency score
        dependencies.sort(key=lambda x: x['dependency_score'], reverse=True)
        return dependencies
    
    def analyze_geographic_risk_distribution(self):
        """
        Analyze risk distribution across geographic regions
        
        Returns:
            Dictionary with regional risk analysis
        """
        regions = {
            'East Asia': ['China', 'South Korea', 'Japan', 'Taiwan'],
            'North America': ['United States', 'Mexico'],
            'Europe': ['Germany', 'United Kingdom', 'Netherlands'],
            'Southeast Asia': ['Vietnam', 'Malaysia', 'Singapore', 'Thailand', 'India']
        }
        
        regional_risks = {}
        
        for region, countries in regions.items():
            total_risk = 0
            country_count = 0
            high_risk_countries = []
            
            for country in countries:
                if country in self.countries_data:
                    country_data = self.countries_data[country]
                    risk_score = country_data['dependency_score'] * (self.intensity / 100.0)
                    total_risk += risk_score
                    country_count += 1
                    
                    if risk_score >= 60:
                        high_risk_countries.append(country)
            
            avg_risk = total_risk / country_count if country_count > 0 else 0
            
            regional_risks[region] = {
                'average_risk_score': round(avg_risk, 1),
                'risk_level': self._categorize_risk(avg_risk),
                'countries_analyzed': country_count,
                'high_risk_countries': high_risk_countries,
                'exposure_level': self._calculate_exposure(avg_risk)
            }
        
        return regional_risks
    
    def calculate_supply_chain_vulnerability_index(self):
        """
        Calculate overall supply chain vulnerability index
        
        Returns:
            Dictionary with vulnerability metrics
        """
        # Calculate average country risk
        country_risks = [data['dependency_score'] for data in self.countries_data.values()]
        avg_country_risk = sum(country_risks) / len(country_risks)
        
        # Calculate average industry risk
        industry_risks = [data['impact_score'] for data in self.industry_data.values()]
        avg_industry_risk = sum(industry_risks) / len(industry_risks)
        
        # Calculate vulnerability index (0-100)
        vulnerability_index = (avg_country_risk * 0.5 + avg_industry_risk * 0.5) * (self.intensity / 100.0)
        
        # Count critical nodes
        critical_countries = sum(1 for data in self.countries_data.values() if data['dependency_score'] >= 70)
        critical_industries = sum(1 for data in self.industry_data.values() if data['impact_score'] >= 80)
        
        return {
            'vulnerability_index': round(vulnerability_index, 1),
            'vulnerability_level': self._categorize_risk(vulnerability_index),
            'critical_country_nodes': critical_countries,
            'critical_industry_nodes': critical_industries,
            'total_nodes_analyzed': len(self.countries_data) + len(self.industry_data),
            'resilience_score': round(100 - vulnerability_index, 1),
            'shock_intensity': self.intensity,
            'assessment': self._get_vulnerability_assessment(vulnerability_index)
        }
    
    def identify_mitigation_strategies(self):
        """
        Identify mitigation strategies based on risk analysis
        
        Returns:
            Dictionary with mitigation recommendations
        """
        risk_scores = self.calculate_country_risk_scores()
        vulnerability = self.calculate_supply_chain_vulnerability_index()
        
        strategies = {
            'immediate_actions': [],
            'short_term_strategies': [],
            'long_term_strategies': [],
            'investment_priorities': []
        }
        
        # Immediate actions based on vulnerability level
        if vulnerability['vulnerability_index'] >= 60:
            strategies['immediate_actions'] = [
                'Activate emergency supply chain protocols',
                'Increase inventory buffers for critical components',
                'Establish direct communication with key suppliers',
                'Implement demand management strategies'
            ]
        else:
            strategies['immediate_actions'] = [
                'Monitor supply chain closely',
                'Review contingency plans',
                'Assess inventory levels'
            ]
        
        # Short-term strategies (0-12 months)
        strategies['short_term_strategies'] = [
            'Diversify supplier base across multiple regions',
            'Negotiate flexible contracts with suppliers',
            'Build strategic inventory reserves',
            'Develop alternative sourcing options',
            'Implement real-time supply chain monitoring'
        ]
        
        # Long-term strategies (12+ months)
        strategies['long_term_strategies'] = [
            'Invest in domestic manufacturing capabilities',
            'Develop regional supply chain hubs',
            'Build strategic partnerships with alternative suppliers',
            'Invest in supply chain digitalization and AI',
            'Create redundant supply chain pathways'
        ]
        
        # Investment priorities
        high_risk_countries = [country for country, data in risk_scores.items() 
                              if data['composite_risk_score'] >= 60]
        
        if high_risk_countries:
            strategies['investment_priorities'] = [
                f'Reduce dependency on {", ".join(high_risk_countries[:3])}',
                'Invest in alternative semiconductor sources',
                'Build regional manufacturing capacity',
                'Develop supply chain resilience infrastructure'
            ]
        
        return strategies
    
    def calculate_cascading_risk_impact(self):
        """
        Calculate cascading effects of supply chain disruption
        
        Returns:
            Dictionary with cascading impact analysis
        """
        # Primary impact (direct semiconductor shortage)
        primary_industries = ['Electronics', 'Automotive', 'Telecommunications']
        
        # Secondary impact (industries dependent on primary)
        secondary_industries = ['Gaming', 'Consumer Electronics', 'Industrial Equipment']
        
        # Tertiary impact (broader economic effects)
        tertiary_industries = ['Retail', 'Logistics', 'Finance']
        
        multiplier = self.intensity / 100.0
        
        return {
            'primary_impact': {
                'industries': primary_industries,
                'impact_level': 'Critical',
                'estimated_impact_pct': round(35 * multiplier, 1),
                'timeline': '0-3 months'
            },
            'secondary_impact': {
                'industries': secondary_industries,
                'impact_level': 'High',
                'estimated_impact_pct': round(25 * multiplier, 1),
                'timeline': '3-9 months'
            },
            'tertiary_impact': {
                'industries': tertiary_industries,
                'impact_level': 'Medium',
                'estimated_impact_pct': round(15 * multiplier, 1),
                'timeline': '9-18 months'
            },
            'total_cascading_effect': round((35 + 25 + 15) * multiplier / 3, 1)
        }
    
    def _categorize_risk(self, risk_score):
        """Categorize risk level based on score"""
        if risk_score >= 75:
            return 'Critical'
        elif risk_score >= 60:
            return 'High'
        elif risk_score >= 40:
            return 'Medium'
        elif risk_score >= 20:
            return 'Low'
        else:
            return 'Minimal'
    
    def _estimate_recovery_time(self, risk_score):
        """Estimate recovery time based on risk score"""
        # Base recovery time in months
        base_time = 12
        risk_factor = risk_score / 100.0
        return round(base_time * (1 + risk_factor))
    
    def _calculate_priority(self, risk_score):
        """Calculate mitigation priority"""
        if risk_score >= 75:
            return 'Urgent'
        elif risk_score >= 60:
            return 'High'
        elif risk_score >= 40:
            return 'Medium'
        else:
            return 'Low'
    
    def _calculate_exposure(self, risk_score):
        """Calculate exposure level"""
        if risk_score >= 60:
            return 'High Exposure'
        elif risk_score >= 40:
            return 'Moderate Exposure'
        else:
            return 'Low Exposure'
    
    def _get_vulnerability_assessment(self, vulnerability_index):
        """Get vulnerability assessment text"""
        if vulnerability_index >= 75:
            return 'Supply chain is critically vulnerable. Immediate action required.'
        elif vulnerability_index >= 60:
            return 'Supply chain faces high vulnerability. Urgent mitigation needed.'
        elif vulnerability_index >= 40:
            return 'Supply chain has moderate vulnerability. Proactive measures recommended.'
        elif vulnerability_index >= 20:
            return 'Supply chain shows low vulnerability. Continue monitoring.'
        else:
            return 'Supply chain is resilient. Maintain current strategies.'

# Made with Bob
