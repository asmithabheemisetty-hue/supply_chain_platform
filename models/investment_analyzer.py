"""
Investment Intelligence Analyzer
Identifies investment opportunities and risks by sector
"""

class InvestmentAnalyzer:
    """Analyzes investment opportunities and risks during supply chain shocks"""
    
    def __init__(self, shock_simulator, industry_data, investment_data):
        """
        Initialize investment analyzer
        
        Args:
            shock_simulator: ShockSimulator instance
            industry_data: Dictionary of industry data
            investment_data: Dictionary of investment opportunities/risks
        """
        self.shock_simulator = shock_simulator
        self.industry_data = industry_data
        self.investment_data = investment_data
        self.intensity = shock_simulator.intensity
        
    def identify_buy_opportunities(self):
        """
        Identify sectors with buy opportunities
        
        Returns:
            List of buy opportunities with analysis
        """
        opportunities = []
        multiplier = self.intensity / 100.0
        
        buy_data = self.investment_data.get('Buy Opportunities', {})
        
        for sector, data in buy_data.items():
            # Parse expected growth
            growth_str = data['expected_growth'].rstrip('%')
            if growth_str.startswith('+'):
                growth_pct = float(growth_str[1:])
            else:
                growth_pct = float(growth_str)
            
            # Adjust growth based on shock intensity
            adjusted_growth = growth_pct * multiplier
            
            opportunities.append({
                'sector': sector,
                'reason': data['reason'],
                'expected_growth_pct': round(adjusted_growth, 1),
                'confidence_level': self._calculate_confidence(adjusted_growth),
                'investment_horizon': 'Medium-term (12-24 months)',
                'key_companies': data['companies'],
                'risk_level': 'Low to Medium',
                'recommendation': 'BUY'
            })
        
        # Sort by expected growth
        opportunities.sort(key=lambda x: x['expected_growth_pct'], reverse=True)
        return opportunities
    
    def identify_hold_opportunities(self):
        """
        Identify sectors to hold
        
        Returns:
            List of hold recommendations with analysis
        """
        holds = []
        
        hold_data = self.investment_data.get('Hold Opportunities', {})
        
        for sector, data in hold_data.items():
            holds.append({
                'sector': sector,
                'reason': data['reason'],
                'expected_impact': data['expected_impact'],
                'confidence_level': 'Medium',
                'investment_horizon': 'Long-term (24+ months)',
                'key_companies': data['companies'],
                'risk_level': 'Medium',
                'recommendation': 'HOLD'
            })
        
        return holds
    
    def identify_high_risk_sectors(self):
        """
        Identify high-risk sectors to avoid or sell
        
        Returns:
            List of high-risk sectors with analysis
        """
        risks = []
        multiplier = self.intensity / 100.0
        
        risk_data = self.investment_data.get('High Risk', {})
        
        for sector, data in risk_data.items():
            # Parse expected loss
            loss_str = data['expected_loss'].rstrip('%')
            if loss_str.startswith('-'):
                loss_pct = float(loss_str[1:])
            else:
                loss_pct = float(loss_str)
            
            # Adjust loss based on shock intensity
            adjusted_loss = loss_pct * multiplier
            
            risks.append({
                'sector': sector,
                'reason': data['reason'],
                'expected_loss_pct': round(adjusted_loss, 1),
                'severity': self._calculate_severity(adjusted_loss),
                'investment_horizon': 'Short-term (0-12 months)',
                'key_companies': data['companies'],
                'risk_level': 'High to Critical',
                'recommendation': 'SELL or AVOID'
            })
        
        # Sort by expected loss (descending)
        risks.sort(key=lambda x: x['expected_loss_pct'], reverse=True)
        return risks
    
    def calculate_sector_scores(self):
        """
        Calculate opportunity and risk scores for all sectors
        
        Returns:
            Dictionary with sector scores
        """
        scores = {}
        multiplier = self.intensity / 100.0
        
        for industry_name, industry_info in self.industry_data.items():
            # Calculate opportunity score (inverse of impact)
            impact_score = industry_info['impact_score']
            revenue_impact = abs(industry_info['revenue_impact_pct'])
            
            # Lower impact = higher opportunity
            opportunity_score = max(0, 100 - (impact_score * multiplier))
            risk_score = impact_score * multiplier
            
            scores[industry_name] = {
                'opportunity_score': round(opportunity_score, 1),
                'risk_score': round(risk_score, 1),
                'net_score': round(opportunity_score - risk_score, 1),
                'recommendation': self._get_recommendation(opportunity_score, risk_score),
                'confidence': self._calculate_confidence(abs(opportunity_score - risk_score))
            }
        
        return scores
    
    def generate_portfolio_recommendations(self):
        """
        Generate overall portfolio recommendations
        
        Returns:
            Dictionary with portfolio strategy
        """
        buy_opps = self.identify_buy_opportunities()
        high_risks = self.identify_high_risk_sectors()
        
        return {
            'strategy': 'Defensive with Selective Growth',
            'asset_allocation': {
                'Growth Sectors (Buy)': '40%',
                'Stable Sectors (Hold)': '35%',
                'Cash/Bonds': '25%'
            },
            'top_buy_sectors': [opp['sector'] for opp in buy_opps[:3]],
            'sectors_to_avoid': [risk['sector'] for risk in high_risks[:3]],
            'rebalancing_frequency': 'Quarterly',
            'risk_management': [
                'Diversify across multiple sectors',
                'Avoid overexposure to semiconductor-dependent industries',
                'Maintain higher cash reserves for opportunities',
                'Use stop-loss orders on high-risk positions'
            ],
            'timeline': {
                'Short-term (0-6 months)': 'Defensive positioning, reduce high-risk exposure',
                'Medium-term (6-18 months)': 'Selective buying in opportunity sectors',
                'Long-term (18+ months)': 'Return to growth strategy as supply chains normalize'
            }
        }
    
    def analyze_sector_correlation(self):
        """
        Analyze correlation between sectors
        
        Returns:
            Dictionary with correlation insights
        """
        correlations = {
            'Highly Correlated': {
                'sectors': ['Electronics', 'Automotive', 'Gaming'],
                'reason': 'All heavily dependent on semiconductors',
                'implication': 'Diversification within these sectors provides limited protection'
            },
            'Negatively Correlated': {
                'sectors': ['Logistics', 'Cloud Services', 'Alternative Semiconductors'],
                'reason': 'Benefit from supply chain disruptions',
                'implication': 'Good hedge against semiconductor-dependent sectors'
            },
            'Low Correlation': {
                'sectors': ['Finance', 'Healthcare Services', 'Energy'],
                'reason': 'Less dependent on semiconductors',
                'implication': 'Provide portfolio stability'
            }
        }
        
        return correlations
    
    def _calculate_confidence(self, score):
        """Calculate confidence level based on score magnitude"""
        abs_score = abs(score)
        if abs_score >= 30:
            return 'High'
        elif abs_score >= 15:
            return 'Medium'
        else:
            return 'Low'
    
    def _calculate_severity(self, loss_pct):
        """Calculate severity level based on expected loss"""
        if loss_pct >= 30:
            return 'Critical'
        elif loss_pct >= 20:
            return 'High'
        elif loss_pct >= 10:
            return 'Medium'
        else:
            return 'Low'
    
    def _get_recommendation(self, opportunity_score, risk_score):
        """Get investment recommendation based on scores"""
        net_score = opportunity_score - risk_score
        
        if net_score > 20:
            return 'Strong Buy'
        elif net_score > 10:
            return 'Buy'
        elif net_score > -10:
            return 'Hold'
        elif net_score > -20:
            return 'Sell'
        else:
            return 'Strong Sell'
    
    def get_summary_metrics(self):
        """
        Get summary metrics for investment analysis
        
        Returns:
            Dictionary with key metrics
        """
        buy_opps = self.identify_buy_opportunities()
        high_risks = self.identify_high_risk_sectors()
        
        avg_buy_growth = sum(opp['expected_growth_pct'] for opp in buy_opps) / len(buy_opps) if buy_opps else 0
        avg_risk_loss = sum(risk['expected_loss_pct'] for risk in high_risks) / len(high_risks) if high_risks else 0
        
        return {
            'total_sectors_analyzed': len(self.industry_data),
            'buy_opportunities': len(buy_opps),
            'hold_recommendations': len(self.identify_hold_opportunities()),
            'high_risk_sectors': len(high_risks),
            'average_buy_growth_pct': round(avg_buy_growth, 1),
            'average_risk_loss_pct': round(avg_risk_loss, 1),
            'market_sentiment': self._determine_market_sentiment(avg_buy_growth, avg_risk_loss),
            'recommended_strategy': 'Defensive with Selective Growth'
        }
    
    def _determine_market_sentiment(self, avg_growth, avg_loss):
        """Determine overall market sentiment"""
        if avg_growth > avg_loss:
            return 'Cautiously Optimistic'
        elif avg_growth > avg_loss * 0.5:
            return 'Neutral'
        else:
            return 'Defensive'

# Made with Bob
