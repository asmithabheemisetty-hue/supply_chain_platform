"""
Executive Summary Report Generator
Generates comprehensive executive summaries and reports
"""

from datetime import datetime

class ReportGenerator:
    """Generates executive summaries and detailed reports"""
    
    def __init__(self, shock_simulator, risk_analyzer, consumer_analyzer, investment_analyzer):
        """
        Initialize report generator
        
        Args:
            shock_simulator: ShockSimulator instance
            risk_analyzer: RiskAnalyzer instance
            consumer_analyzer: ConsumerImpactAnalyzer instance
            investment_analyzer: InvestmentAnalyzer instance
        """
        self.shock_simulator = shock_simulator
        self.risk_analyzer = risk_analyzer
        self.consumer_analyzer = consumer_analyzer
        self.investment_analyzer = investment_analyzer
    
    def generate_executive_summary(self):
        """
        Generate comprehensive executive summary
        
        Returns:
            Dictionary with executive summary sections
        """
        # Get key metrics
        vulnerability = self.risk_analyzer.calculate_supply_chain_vulnerability_index()
        consumer_metrics = self.consumer_analyzer.get_summary_metrics()
        investment_metrics = self.investment_analyzer.get_summary_metrics()
        portfolio_rec = self.investment_analyzer.generate_portfolio_recommendations()
        
        summary = {
            'title': 'Global Supply Chain Shock Intelligence Report',
            'subtitle': f'Taiwan Semiconductor Disruption Analysis - {self.shock_simulator.intensity}% Intensity',
            'date': datetime.now().strftime('%B %d, %Y'),
            'sections': {}
        }
        
        # Executive Overview
        summary['sections']['executive_overview'] = self._generate_executive_overview(
            vulnerability, consumer_metrics, investment_metrics
        )
        
        # Key Findings
        summary['sections']['key_findings'] = self._generate_key_findings(
            vulnerability, consumer_metrics, investment_metrics
        )
        
        # Risk Assessment
        summary['sections']['risk_assessment'] = self._generate_risk_assessment(vulnerability)
        
        # Consumer Impact
        summary['sections']['consumer_impact'] = self._generate_consumer_impact_summary(consumer_metrics)
        
        # Investment Recommendations
        summary['sections']['investment_recommendations'] = self._generate_investment_summary(
            investment_metrics, portfolio_rec
        )
        
        # Strategic Recommendations
        summary['sections']['strategic_recommendations'] = self._generate_strategic_recommendations()
        
        # Timeline and Recovery
        summary['sections']['timeline'] = self._generate_timeline_summary()
        
        return summary
    
    def _generate_executive_overview(self, vulnerability, consumer_metrics, investment_metrics):
        """Generate executive overview section"""
        return {
            'title': 'Executive Overview',
            'content': f"""
A {self.shock_simulator.intensity}% disruption in Taiwan's semiconductor supply chain poses significant 
risks to global supply chains. Our analysis reveals a vulnerability index of {vulnerability['vulnerability_index']}/100, 
indicating {vulnerability['vulnerability_level'].lower()} risk levels across affected regions.

**Key Impact Areas:**
- {vulnerability['critical_country_nodes']} countries face critical supply chain disruptions
- {vulnerability['critical_industry_nodes']} industries experience severe revenue impacts
- {consumer_metrics['products_affected']} consumer products face shortages and price increases
- {investment_metrics['high_risk_sectors']} sectors present high investment risks

**Overall Assessment:** {vulnerability['assessment']}

This report provides comprehensive analysis across five critical dimensions: shock simulation, 
risk mapping, consumer impact, investment intelligence, and strategic recommendations.
            """.strip()
        }
    
    def _generate_key_findings(self, vulnerability, consumer_metrics, investment_metrics):
        """Generate key findings section"""
        findings = []
        
        # Vulnerability finding
        findings.append(f"Supply chain vulnerability index: {vulnerability['vulnerability_index']}/100 ({vulnerability['vulnerability_level']})")
        
        # Consumer finding
        findings.append(f"Average consumer price increase: {consumer_metrics['avg_price_increase_pct']}%")
        findings.append(f"Average product availability: {consumer_metrics['avg_availability_pct']}%")
        
        # Investment finding
        findings.append(f"Investment opportunities identified: {investment_metrics['buy_opportunities']} sectors")
        findings.append(f"High-risk sectors to avoid: {investment_metrics['high_risk_sectors']} sectors")
        
        # Market sentiment
        findings.append(f"Market sentiment: {investment_metrics['market_sentiment']}")
        
        return {
            'title': 'Key Findings',
            'findings': findings
        }
    
    def _generate_risk_assessment(self, vulnerability):
        """Generate risk assessment section"""
        risk_scores = self.risk_analyzer.calculate_country_risk_scores()
        cascading = self.risk_analyzer.calculate_cascading_risk_impact()
        
        # Get top 5 high-risk countries
        top_risks = sorted(risk_scores.items(), 
                          key=lambda x: x[1]['composite_risk_score'], 
                          reverse=True)[:5]
        
        return {
            'title': 'Risk Assessment',
            'vulnerability_index': vulnerability['vulnerability_index'],
            'vulnerability_level': vulnerability['vulnerability_level'],
            'resilience_score': vulnerability['resilience_score'],
            'critical_nodes': {
                'countries': vulnerability['critical_country_nodes'],
                'industries': vulnerability['critical_industry_nodes']
            },
            'top_risk_countries': [
                {
                    'country': country,
                    'risk_score': data['composite_risk_score'],
                    'risk_level': data['risk_level'],
                    'recovery_months': data['estimated_recovery_months']
                }
                for country, data in top_risks
            ],
            'cascading_impact': {
                'primary': cascading['primary_impact']['estimated_impact_pct'],
                'secondary': cascading['secondary_impact']['estimated_impact_pct'],
                'tertiary': cascading['tertiary_impact']['estimated_impact_pct']
            }
        }
    
    def _generate_consumer_impact_summary(self, consumer_metrics):
        """Generate consumer impact summary"""
        shortages = self.consumer_analyzer.analyze_product_shortages()
        spending = self.consumer_analyzer.analyze_consumer_spending_changes()
        
        # Get critical shortages
        critical_shortages = [s for s in shortages if s['shortage_level'] in ['Critical', 'High']]
        
        return {
            'title': 'Consumer Impact Analysis',
            'products_affected': consumer_metrics['products_affected'],
            'avg_price_increase': consumer_metrics['avg_price_increase_pct'],
            'avg_availability': consumer_metrics['avg_availability_pct'],
            'critical_shortages': len(critical_shortages),
            'spending_impact': {
                'electronics': spending['Electronics']['change_pct'],
                'automotive': spending['Automotive']['change_pct'],
                'overall': spending['Overall']['change_pct']
            },
            'top_affected_products': [
                {
                    'product': s['product'],
                    'shortage_level': s['shortage_level'],
                    'price_increase': s['price_increase_pct']
                }
                for s in critical_shortages[:5]
            ]
        }
    
    def _generate_investment_summary(self, investment_metrics, portfolio_rec):
        """Generate investment recommendations summary"""
        buy_opps = self.investment_analyzer.identify_buy_opportunities()
        high_risks = self.investment_analyzer.identify_high_risk_sectors()
        
        return {
            'title': 'Investment Intelligence',
            'strategy': portfolio_rec['strategy'],
            'market_sentiment': investment_metrics['market_sentiment'],
            'asset_allocation': portfolio_rec['asset_allocation'],
            'buy_opportunities': [
                {
                    'sector': opp['sector'],
                    'expected_growth': opp['expected_growth_pct'],
                    'confidence': opp['confidence_level']
                }
                for opp in buy_opps[:5]
            ],
            'sectors_to_avoid': [
                {
                    'sector': risk['sector'],
                    'expected_loss': risk['expected_loss_pct'],
                    'severity': risk['severity']
                }
                for risk in high_risks[:5]
            ],
            'risk_management': portfolio_rec['risk_management']
        }
    
    def _generate_strategic_recommendations(self):
        """Generate strategic recommendations"""
        mitigation = self.risk_analyzer.identify_mitigation_strategies()
        
        return {
            'title': 'Strategic Recommendations',
            'immediate_actions': mitigation['immediate_actions'],
            'short_term_strategies': mitigation['short_term_strategies'],
            'long_term_strategies': mitigation['long_term_strategies'],
            'investment_priorities': mitigation['investment_priorities']
        }
    
    def _generate_timeline_summary(self):
        """Generate timeline summary"""
        timeline = self.shock_simulator.generate_timeline()
        
        return {
            'title': 'Timeline and Recovery Outlook',
            'phases': [
                {
                    'phase': phase,
                    'duration': data['duration'],
                    'supply_disruption': data['supply_disruption_pct'],
                    'recovery_progress': data['recovery_progress_pct'],
                    'key_events': data['key_events']
                }
                for phase, data in timeline.items()
            ]
        }
    
    def generate_text_report(self):
        """
        Generate text-based report
        
        Returns:
            String with formatted report
        """
        summary = self.generate_executive_summary()
        
        report = []
        report.append("=" * 80)
        report.append(summary['title'].center(80))
        report.append(summary['subtitle'].center(80))
        report.append(f"Generated: {summary['date']}".center(80))
        report.append("=" * 80)
        report.append("")
        
        # Executive Overview
        section = summary['sections']['executive_overview']
        report.append(section['title'].upper())
        report.append("-" * 80)
        report.append(section['content'])
        report.append("")
        
        # Key Findings
        section = summary['sections']['key_findings']
        report.append(section['title'].upper())
        report.append("-" * 80)
        for i, finding in enumerate(section['findings'], 1):
            report.append(f"{i}. {finding}")
        report.append("")
        
        # Risk Assessment
        section = summary['sections']['risk_assessment']
        report.append(section['title'].upper())
        report.append("-" * 80)
        report.append(f"Vulnerability Index: {section['vulnerability_index']}/100 ({section['vulnerability_level']})")
        report.append(f"Resilience Score: {section['resilience_score']}/100")
        report.append(f"Critical Country Nodes: {section['critical_nodes']['countries']}")
        report.append(f"Critical Industry Nodes: {section['critical_nodes']['industries']}")
        report.append("")
        report.append("Top Risk Countries:")
        for country in section['top_risk_countries']:
            report.append(f"  - {country['country']}: {country['risk_score']}/100 ({country['risk_level']}) - Recovery: {country['recovery_months']} months")
        report.append("")
        
        # Consumer Impact
        section = summary['sections']['consumer_impact']
        report.append(section['title'].upper())
        report.append("-" * 80)
        report.append(f"Products Affected: {section['products_affected']}")
        report.append(f"Average Price Increase: {section['avg_price_increase']}%")
        report.append(f"Average Availability: {section['avg_availability']}%")
        report.append(f"Critical Shortages: {section['critical_shortages']}")
        report.append("")
        
        # Investment Recommendations
        section = summary['sections']['investment_recommendations']
        report.append(section['title'].upper())
        report.append("-" * 80)
        report.append(f"Strategy: {section['strategy']}")
        report.append(f"Market Sentiment: {section['market_sentiment']}")
        report.append("")
        report.append("Buy Opportunities:")
        for opp in section['buy_opportunities']:
            report.append(f"  - {opp['sector']}: +{opp['expected_growth']}% ({opp['confidence']} confidence)")
        report.append("")
        report.append("Sectors to Avoid:")
        for risk in section['sectors_to_avoid']:
            report.append(f"  - {risk['sector']}: {risk['expected_loss']}% ({risk['severity']} severity)")
        report.append("")
        
        # Strategic Recommendations
        section = summary['sections']['strategic_recommendations']
        report.append(section['title'].upper())
        report.append("-" * 80)
        report.append("Immediate Actions:")
        for action in section['immediate_actions']:
            report.append(f"  • {action}")
        report.append("")
        report.append("Short-term Strategies (0-12 months):")
        for strategy in section['short_term_strategies']:
            report.append(f"  • {strategy}")
        report.append("")
        report.append("Long-term Strategies (12+ months):")
        for strategy in section['long_term_strategies']:
            report.append(f"  • {strategy}")
        report.append("")
        
        report.append("=" * 80)
        report.append("END OF REPORT".center(80))
        report.append("=" * 80)
        
        return "\n".join(report)
    
    def get_summary_statistics(self):
        """
        Get summary statistics for dashboard
        
        Returns:
            Dictionary with key statistics
        """
        vulnerability = self.risk_analyzer.calculate_supply_chain_vulnerability_index()
        consumer_metrics = self.consumer_analyzer.get_summary_metrics()
        investment_metrics = self.investment_analyzer.get_summary_metrics()
        
        return {
            'vulnerability_index': vulnerability['vulnerability_index'],
            'resilience_score': vulnerability['resilience_score'],
            'critical_nodes': vulnerability['critical_country_nodes'] + vulnerability['critical_industry_nodes'],
            'products_affected': consumer_metrics['products_affected'],
            'avg_price_increase': consumer_metrics['avg_price_increase_pct'],
            'buy_opportunities': investment_metrics['buy_opportunities'],
            'high_risk_sectors': investment_metrics['high_risk_sectors'],
            'market_sentiment': investment_metrics['market_sentiment']
        }

# Made with Bob
