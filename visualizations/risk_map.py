"""
Interactive Supply Chain Risk Map
Visualizes global supply chain risks on an interactive world map
"""

import plotly.graph_objects as go
import plotly.express as px

class RiskMap:
    """Creates interactive risk maps for supply chain visualization"""
    
    def __init__(self, countries_data, risk_analyzer):
        """
        Initialize risk map
        
        Args:
            countries_data: Dictionary of country data
            risk_analyzer: RiskAnalyzer instance
        """
        self.countries_data = countries_data
        self.risk_analyzer = risk_analyzer
        
    def create_global_risk_map(self):
        """
        Create interactive global risk map
        
        Returns:
            Plotly figure object
        """
        # Get risk scores
        risk_scores = self.risk_analyzer.calculate_country_risk_scores()
        
        # Prepare data for map
        countries = []
        lats = []
        lons = []
        risk_values = []
        hover_texts = []
        colors = []
        
        for country, data in self.countries_data.items():
            risk_data = risk_scores[country]
            
            countries.append(country)
            lats.append(data['lat'])
            lons.append(data['lon'])
            risk_values.append(risk_data['composite_risk_score'])
            
            # Create hover text
            hover_text = f"<b>{country}</b><br>"
            hover_text += f"Risk Score: {risk_data['composite_risk_score']}/100<br>"
            hover_text += f"Risk Level: {risk_data['risk_level']}<br>"
            hover_text += f"GDP Impact: {data['gdp_impact_pct']}%<br>"
            hover_text += f"Dependency: {data['dependency_score']}/100<br>"
            hover_text += f"Recovery: {risk_data['estimated_recovery_months']} months"
            hover_texts.append(hover_text)
            
            # Assign color based on risk level
            colors.append(self._get_risk_color(risk_data['composite_risk_score']))
        
        # Create figure
        fig = go.Figure()
        
        # Add scatter geo for countries
        fig.add_trace(go.Scattergeo(
            lon=lons,
            lat=lats,
            text=countries,
            mode='markers+text',
            marker=dict(
                size=[max(10, r/5) for r in risk_values],
                color=risk_values,
                colorscale=[
                    [0, '#2ecc71'],      # Green (low risk)
                    [0.25, '#f1c40f'],   # Yellow
                    [0.5, '#e67e22'],    # Orange
                    [0.75, '#e74c3c'],   # Red
                    [1, '#c0392b']       # Dark red (critical)
                ],
                cmin=0,
                cmax=100,
                colorbar=dict(
                    title="Risk Score",
                    thickness=15,
                    len=0.7,
                    x=1.02
                ),
                line=dict(width=1, color='white')
            ),
            textposition="top center",
            textfont=dict(size=8, color='black'),
            hovertext=hover_texts,
            hoverinfo='text',
            name='Countries'
        ))
        
        # Update layout
        fig.update_layout(
            title={
                'text': 'Global Supply Chain Risk Map<br><sub>Taiwan Semiconductor Disruption Impact</sub>',
                'x': 0.5,
                'xanchor': 'center',
                'font': {'size': 20}
            },
            geo=dict(
                projection_type='natural earth',
                showland=True,
                landcolor='rgb(243, 243, 243)',
                coastlinecolor='rgb(204, 204, 204)',
                showocean=True,
                oceancolor='rgb(230, 245, 255)',
                showcountries=True,
                countrycolor='rgb(204, 204, 204)',
                showlakes=True,
                lakecolor='rgb(230, 245, 255)'
            ),
            height=600,
            margin=dict(l=0, r=0, t=80, b=0)
        )
        
        return fig
    
    def create_regional_risk_chart(self):
        """
        Create regional risk comparison chart
        
        Returns:
            Plotly figure object
        """
        regional_risks = self.risk_analyzer.analyze_geographic_risk_distribution()
        
        regions = list(regional_risks.keys())
        risk_scores = [data['average_risk_score'] for data in regional_risks.values()]
        risk_levels = [data['risk_level'] for data in regional_risks.values()]
        
        # Create color mapping
        colors = [self._get_risk_color(score) for score in risk_scores]
        
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            x=regions,
            y=risk_scores,
            text=[f"{score}<br>{level}" for score, level in zip(risk_scores, risk_levels)],
            textposition='auto',
            marker=dict(
                color=colors,
                line=dict(color='white', width=2)
            ),
            hovertemplate='<b>%{x}</b><br>Risk Score: %{y}<br><extra></extra>'
        ))
        
        fig.update_layout(
            title='Regional Risk Comparison',
            xaxis_title='Region',
            yaxis_title='Average Risk Score',
            yaxis=dict(range=[0, 100]),
            height=400,
            showlegend=False
        )
        
        return fig
    
    def create_dependency_network(self):
        """
        Create dependency network visualization
        
        Returns:
            Plotly figure object
        """
        # Get critical dependencies
        dependencies = self.risk_analyzer.identify_critical_dependencies()
        
        # Separate by type
        country_deps = [d for d in dependencies if d['type'] == 'Country']
        industry_deps = [d for d in dependencies if d['type'] == 'Industry']
        
        # Create sunburst chart
        labels = ['Supply Chain']
        parents = ['']
        values = [100]
        colors_list = ['#3498db']
        
        # Add countries
        if country_deps:
            labels.append('Countries')
            parents.append('Supply Chain')
            values.append(50)
            colors_list.append('#e74c3c')
            
            for dep in country_deps[:5]:  # Top 5
                labels.append(dep['name'])
                parents.append('Countries')
                values.append(dep['dependency_score'])
                colors_list.append(self._get_risk_color(dep['dependency_score']))
        
        # Add industries
        if industry_deps:
            labels.append('Industries')
            parents.append('Supply Chain')
            values.append(50)
            colors_list.append('#f39c12')
            
            for dep in industry_deps[:5]:  # Top 5
                labels.append(dep['name'])
                parents.append('Industries')
                values.append(dep['dependency_score'])
                colors_list.append(self._get_risk_color(dep['dependency_score']))
        
        fig = go.Figure(go.Sunburst(
            labels=labels,
            parents=parents,
            values=values,
            marker=dict(colors=colors_list),
            branchvalues="total",
            hovertemplate='<b>%{label}</b><br>Score: %{value}<br><extra></extra>'
        ))
        
        fig.update_layout(
            title='Critical Supply Chain Dependencies',
            height=500
        )
        
        return fig
    
    def create_risk_timeline(self):
        """
        Create risk evolution timeline
        
        Returns:
            Plotly figure object
        """
        # Simulate risk evolution over time
        months = list(range(0, 25, 3))  # 0 to 24 months
        
        # Different risk trajectories
        critical_risk = [80, 85, 82, 75, 65, 55, 45, 35, 25]
        high_risk = [60, 65, 62, 55, 48, 40, 32, 25, 20]
        medium_risk = [40, 42, 40, 35, 30, 25, 20, 15, 12]
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=months,
            y=critical_risk,
            mode='lines+markers',
            name='Critical Risk Countries',
            line=dict(color='#e74c3c', width=3),
            marker=dict(size=8)
        ))
        
        fig.add_trace(go.Scatter(
            x=months,
            y=high_risk,
            mode='lines+markers',
            name='High Risk Countries',
            line=dict(color='#f39c12', width=3),
            marker=dict(size=8)
        ))
        
        fig.add_trace(go.Scatter(
            x=months,
            y=medium_risk,
            mode='lines+markers',
            name='Medium Risk Countries',
            line=dict(color='#f1c40f', width=3),
            marker=dict(size=8)
        ))
        
        # Add risk zones
        fig.add_hrect(y0=75, y1=100, fillcolor="red", opacity=0.1, line_width=0)
        fig.add_hrect(y0=60, y1=75, fillcolor="orange", opacity=0.1, line_width=0)
        fig.add_hrect(y0=40, y1=60, fillcolor="yellow", opacity=0.1, line_width=0)
        fig.add_hrect(y0=0, y1=40, fillcolor="green", opacity=0.1, line_width=0)
        
        fig.update_layout(
            title='Supply Chain Risk Evolution Timeline',
            xaxis_title='Months from Disruption',
            yaxis_title='Risk Score',
            yaxis=dict(range=[0, 100]),
            height=400,
            hovermode='x unified'
        )
        
        return fig
    
    def _get_risk_color(self, risk_score):
        """Get color based on risk score"""
        if risk_score >= 75:
            return '#c0392b'  # Dark red
        elif risk_score >= 60:
            return '#e74c3c'  # Red
        elif risk_score >= 40:
            return '#e67e22'  # Orange
        elif risk_score >= 20:
            return '#f1c40f'  # Yellow
        else:
            return '#2ecc71'  # Green

# Made with Bob
