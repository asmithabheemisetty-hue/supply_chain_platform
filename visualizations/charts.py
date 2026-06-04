"""
Chart Visualizations
Various charts for supply chain analysis
"""

import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

class ChartVisualizer:
    """Creates various charts for supply chain visualization"""
    
    def __init__(self, shock_simulator, consumer_analyzer, investment_analyzer):
        """
        Initialize chart visualizer
        
        Args:
            shock_simulator: ShockSimulator instance
            consumer_analyzer: ConsumerImpactAnalyzer instance
            investment_analyzer: InvestmentAnalyzer instance
        """
        self.shock_simulator = shock_simulator
        self.consumer_analyzer = consumer_analyzer
        self.investment_analyzer = investment_analyzer
    
    def create_industry_impact_chart(self):
        """
        Create industry impact comparison chart
        
        Returns:
            Plotly figure object
        """
        industry_data = self.shock_simulator.industry_data
        
        industries = list(industry_data.keys())
        impact_scores = [data['impact_score'] for data in industry_data.values()]
        revenue_impacts = [abs(data['revenue_impact_pct']) for data in industry_data.values()]
        
        # Sort by impact score
        sorted_data = sorted(zip(industries, impact_scores, revenue_impacts), 
                           key=lambda x: x[1], reverse=True)
        industries, impact_scores, revenue_impacts = zip(*sorted_data)
        
        fig = make_subplots(
            rows=1, cols=2,
            subplot_titles=('Impact Score', 'Revenue Impact %'),
            specs=[[{"type": "bar"}, {"type": "bar"}]]
        )
        
        # Impact scores
        fig.add_trace(
            go.Bar(
                y=industries,
                x=impact_scores,
                orientation='h',
                marker=dict(
                    color=impact_scores,
                    colorscale='Reds',
                    showscale=False
                ),
                text=impact_scores,
                textposition='auto',
                name='Impact Score'
            ),
            row=1, col=1
        )
        
        # Revenue impacts
        fig.add_trace(
            go.Bar(
                y=industries,
                x=revenue_impacts,
                orientation='h',
                marker=dict(
                    color=revenue_impacts,
                    colorscale='Oranges',
                    showscale=False
                ),
                text=[f"{x}%" for x in revenue_impacts],
                textposition='auto',
                name='Revenue Impact'
            ),
            row=1, col=2
        )
        
        fig.update_layout(
            title='Industry Impact Analysis',
            height=600,
            showlegend=False
        )
        
        fig.update_xaxes(title_text="Score (0-100)", row=1, col=1)
        fig.update_xaxes(title_text="Revenue Impact %", row=1, col=2)
        
        return fig
    
    def create_consumer_impact_chart(self):
        """
        Create consumer product impact chart
        
        Returns:
            Plotly figure object
        """
        product_data = self.shock_simulator.product_data
        
        products = list(product_data.keys())
        price_increases = [data['price_increase_pct'] for data in product_data.values()]
        availability = [data['availability_pct'] for data in product_data.values()]
        
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            name='Price Increase %',
            x=products,
            y=price_increases,
            marker=dict(color='#e74c3c'),
            text=[f"+{x}%" for x in price_increases],
            textposition='auto'
        ))
        
        fig.add_trace(go.Bar(
            name='Availability %',
            x=products,
            y=availability,
            marker=dict(color='#3498db'),
            text=[f"{x}%" for x in availability],
            textposition='auto'
        ))
        
        fig.update_layout(
            title='Consumer Product Impact',
            xaxis_title='Product',
            yaxis_title='Percentage',
            barmode='group',
            height=500,
            xaxis_tickangle=-45
        )
        
        return fig
    
    def create_investment_opportunities_chart(self):
        """
        Create investment opportunities chart
        
        Returns:
            Plotly figure object
        """
        buy_opps = self.investment_analyzer.identify_buy_opportunities()
        high_risks = self.investment_analyzer.identify_high_risk_sectors()
        
        # Prepare data
        sectors = []
        growth_values = []
        colors = []
        
        # Add buy opportunities (positive)
        for opp in buy_opps:
            sectors.append(opp['sector'])
            growth_values.append(opp['expected_growth_pct'])
            colors.append('#2ecc71')  # Green
        
        # Add high risks (negative)
        for risk in high_risks:
            sectors.append(risk['sector'])
            growth_values.append(-risk['expected_loss_pct'])
            colors.append('#e74c3c')  # Red
        
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            x=sectors,
            y=growth_values,
            marker=dict(color=colors),
            text=[f"{x:+.1f}%" for x in growth_values],
            textposition='auto',
            hovertemplate='<b>%{x}</b><br>Expected Change: %{y:+.1f}%<extra></extra>'
        ))
        
        # Add zero line
        fig.add_hline(y=0, line_dash="dash", line_color="gray")
        
        fig.update_layout(
            title='Investment Opportunities & Risks',
            xaxis_title='Sector',
            yaxis_title='Expected Growth/Loss %',
            height=500,
            xaxis_tickangle=-45,
            showlegend=False
        )
        
        return fig
    
    def create_timeline_chart(self):
        """
        Create impact timeline chart
        
        Returns:
            Plotly figure object
        """
        timeline = self.shock_simulator.generate_timeline()
        
        phases = list(timeline.keys())
        
        # Extract metrics for each phase
        supply_disruption = []
        price_impact = []
        recovery_progress = []
        
        for phase_data in timeline.values():
            supply_disruption.append(phase_data['supply_disruption_pct'])
            price_impact.append(phase_data['price_impact_pct'])
            recovery_progress.append(phase_data['recovery_progress_pct'])
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=phases,
            y=supply_disruption,
            mode='lines+markers',
            name='Supply Disruption',
            line=dict(color='#e74c3c', width=3),
            marker=dict(size=10)
        ))
        
        fig.add_trace(go.Scatter(
            x=phases,
            y=price_impact,
            mode='lines+markers',
            name='Price Impact',
            line=dict(color='#f39c12', width=3),
            marker=dict(size=10)
        ))
        
        fig.add_trace(go.Scatter(
            x=phases,
            y=recovery_progress,
            mode='lines+markers',
            name='Recovery Progress',
            line=dict(color='#2ecc71', width=3),
            marker=dict(size=10)
        ))
        
        fig.update_layout(
            title='Supply Chain Disruption Timeline',
            xaxis_title='Phase',
            yaxis_title='Percentage',
            yaxis=dict(range=[0, 100]),
            height=500,
            hovermode='x unified'
        )
        
        return fig
    
    def create_gdp_impact_chart(self):
        """
        Create GDP impact by country chart
        
        Returns:
            Plotly figure object
        """
        countries_data = self.shock_simulator.countries_data
        
        countries = list(countries_data.keys())
        gdp_impacts = [data['gdp_impact_pct'] for data in countries_data.values()]
        
        # Sort by impact
        sorted_data = sorted(zip(countries, gdp_impacts), key=lambda x: x[1])
        countries, gdp_impacts = zip(*sorted_data)
        
        # Color based on impact severity
        colors = ['#e74c3c' if x < -1.5 else '#f39c12' if x < -0.5 else '#f1c40f' 
                 for x in gdp_impacts]
        
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            y=countries,
            x=gdp_impacts,
            orientation='h',
            marker=dict(color=colors),
            text=[f"{x}%" for x in gdp_impacts],
            textposition='auto',
            hovertemplate='<b>%{y}</b><br>GDP Impact: %{x}%<extra></extra>'
        ))
        
        fig.update_layout(
            title='GDP Impact by Country',
            xaxis_title='GDP Impact %',
            yaxis_title='Country',
            height=600,
            showlegend=False
        )
        
        return fig
    
    def create_sector_comparison_radar(self):
        """
        Create radar chart comparing sectors
        
        Returns:
            Plotly figure object
        """
        sector_scores = self.investment_analyzer.calculate_sector_scores()
        
        # Select top 6 sectors for clarity
        top_sectors = sorted(sector_scores.items(), 
                           key=lambda x: abs(x[1]['net_score']), 
                           reverse=True)[:6]
        
        fig = go.Figure()
        
        for sector, scores in top_sectors:
            fig.add_trace(go.Scatterpolar(
                r=[scores['opportunity_score'], scores['risk_score'], 
                   abs(scores['net_score'])],
                theta=['Opportunity', 'Risk', 'Net Score'],
                fill='toself',
                name=sector
            ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 100]
                )
            ),
            title='Sector Comparison: Opportunity vs Risk',
            height=500,
            showlegend=True
        )
        
        return fig
    
    def create_recovery_timeline_chart(self):
        """
        Create recovery timeline by industry
        
        Returns:
            Plotly figure object
        """
        industry_data = self.shock_simulator.industry_data
        
        industries = list(industry_data.keys())
        recovery_times = [data['recovery_time_months'] for data in industry_data.values()]
        
        # Sort by recovery time
        sorted_data = sorted(zip(industries, recovery_times), key=lambda x: x[1], reverse=True)
        industries, recovery_times = zip(*sorted_data)
        
        # Color based on recovery time
        colors = ['#e74c3c' if x > 18 else '#f39c12' if x > 12 else '#2ecc71' 
                 for x in recovery_times]
        
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            y=industries,
            x=recovery_times,
            orientation='h',
            marker=dict(color=colors),
            text=[f"{x} months" for x in recovery_times],
            textposition='auto',
            hovertemplate='<b>%{y}</b><br>Recovery Time: %{x} months<extra></extra>'
        ))
        
        fig.update_layout(
            title='Industry Recovery Timeline',
            xaxis_title='Recovery Time (months)',
            yaxis_title='Industry',
            height=600,
            showlegend=False
        )
        
        return fig
    
    def create_shortage_severity_chart(self):
        """
        Create product shortage severity chart
        
        Returns:
            Plotly figure object
        """
        shortages = self.consumer_analyzer.analyze_product_shortages()
        
        products = [s['product'] for s in shortages]
        severities = [s['shortage_severity_score'] for s in shortages]
        
        # Map severity to color
        color_map = {
            'Critical': '#c0392b',
            'High': '#e74c3c',
            'Medium': '#f39c12',
            'Low': '#f1c40f'
        }
        colors = [color_map.get(s['shortage_level'], '#95a5a6') for s in shortages]
        
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            x=products,
            y=severities,
            marker=dict(color=colors),
            text=[s['shortage_level'] for s in shortages],
            textposition='auto',
            hovertemplate='<b>%{x}</b><br>Severity: %{y}<br><extra></extra>'
        ))
        
        fig.update_layout(
            title='Product Shortage Severity',
            xaxis_title='Product',
            yaxis_title='Severity Score (0-100)',
            yaxis=dict(range=[0, 100]),
            height=500,
            xaxis_tickangle=-45,
            showlegend=False
        )
        
        return fig

# Made with Bob
