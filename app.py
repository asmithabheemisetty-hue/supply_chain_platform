"""
Global Supply Chain Shock Intelligence Platform
Main Streamlit Application

Scenario: Taiwan Semiconductor Supply Chain Disruption (40% intensity)
Features:
1. Global Shock Simulator
2. Supply Chain Risk Map
3. Consumer Impact Analyzer
4. Investment Intelligence Dashboard
5. Executive Summary Generator
"""

import streamlit as st
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# Import data
from data.countries_data import COUNTRIES_DATA
from data.industry_data import INDUSTRY_DATA, INVESTMENT_DATA
from data.product_data import PRODUCT_DATA

# Import models
from models.shock_simulator import ShockSimulator
from models.risk_analyzer import RiskAnalyzer
from models.consumer_impact import ConsumerImpactAnalyzer
from models.investment_analyzer import InvestmentAnalyzer

# Import visualizations
from visualizations.risk_map import RiskMap
from visualizations.charts import ChartVisualizer
from visualizations.dashboard import Dashboard

# Import utilities
from utils.report_generator import ReportGenerator
from utils.helpers import format_percentage, get_risk_level, get_severity_emoji

# Page configuration
st.set_page_config(
    page_title="Supply Chain Intelligence Platform",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #2c3e50;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #7f8c8d;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #3498db;
    }
</style>
""", unsafe_allow_html=True)

def initialize_models(shock_type, intensity):
    """Initialize all models with given parameters"""
    # Initialize shock simulator
    simulator = ShockSimulator(
        shock_type=shock_type,
        intensity=intensity,
        countries_data=COUNTRIES_DATA,
        industry_data=INDUSTRY_DATA,
        product_data=PRODUCT_DATA
    )
    
    # Initialize analyzers
    risk_analyzer = RiskAnalyzer(simulator, COUNTRIES_DATA, INDUSTRY_DATA)
    consumer_analyzer = ConsumerImpactAnalyzer(simulator, PRODUCT_DATA)
    investment_analyzer = InvestmentAnalyzer(simulator, INDUSTRY_DATA, INVESTMENT_DATA)
    
    # Initialize visualizations
    risk_map = RiskMap(COUNTRIES_DATA, risk_analyzer)
    chart_viz = ChartVisualizer(simulator, consumer_analyzer, investment_analyzer)
    
    # Initialize report generator
    report_gen = ReportGenerator(simulator, risk_analyzer, consumer_analyzer, investment_analyzer)
    
    return {
        'simulator': simulator,
        'risk_analyzer': risk_analyzer,
        'consumer_analyzer': consumer_analyzer,
        'investment_analyzer': investment_analyzer,
        'risk_map': risk_map,
        'chart_viz': chart_viz,
        'report_gen': report_gen
    }

def render_home_page(models):
    """Render home page with overview"""
    st.markdown('<div class="main-header">🌐 Global Supply Chain Shock Intelligence Platform</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Taiwan Semiconductor Disruption Analysis</div>', unsafe_allow_html=True)
    
    # Get summary statistics
    stats = models['report_gen'].get_summary_statistics()
    
    # Display key metrics
    Dashboard.create_kpi_row([
        {
            'title': '🎯 Vulnerability Index',
            'value': f"{stats['vulnerability_index']}/100",
            'delta': f"{get_risk_level(stats['vulnerability_index'])}"
        },
        {
            'title': '🛡️ Resilience Score',
            'value': f"{stats['resilience_score']}/100",
            'delta': None
        },
        {
            'title': '⚠️ Critical Nodes',
            'value': stats['critical_nodes'],
            'delta': 'Countries + Industries'
        },
        {
            'title': '📦 Products Affected',
            'value': stats['products_affected'],
            'delta': f"+{stats['avg_price_increase']}% avg price"
        }
    ])
    
    st.markdown("---")
    
    # Overview sections
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Scenario Overview")
        st.write(f"""
        **Disruption Type:** Taiwan Semiconductor Supply Chain
        
        **Intensity Level:** {models['simulator'].intensity}%
        
        **Impact Summary:**
        - {stats['critical_nodes']} critical supply chain nodes affected
        - {stats['products_affected']} consumer products experiencing shortages
        - Average price increase: {stats['avg_price_increase']}%
        - Market sentiment: {stats['market_sentiment']}
        """)
    
    with col2:
        st.subheader("💡 Key Insights")
        st.write(f"""
        **Investment Opportunities:** {stats['buy_opportunities']} sectors identified
        
        **High-Risk Sectors:** {stats['high_risk_sectors']} sectors to avoid
        
        **Recommended Strategy:** Defensive with Selective Growth
        
        **Recovery Timeline:** 12-24 months for most sectors
        """)
    
    st.markdown("---")
    
    # Quick navigation
    st.subheader("🧭 Navigate to Features")
    
    cols = st.columns(5)
    
    with cols[0]:
        if st.button("🎮 Shock Simulator", use_container_width=True):
            st.session_state.page = 'simulator'
            st.rerun()
    
    with cols[1]:
        if st.button("🗺️ Risk Map", use_container_width=True):
            st.session_state.page = 'risk_map'
            st.rerun()
    
    with cols[2]:
        if st.button("🛒 Consumer Impact", use_container_width=True):
            st.session_state.page = 'consumer'
            st.rerun()
    
    with cols[3]:
        if st.button("💼 Investment Intel", use_container_width=True):
            st.session_state.page = 'investment'
            st.rerun()
    
    with cols[4]:
        if st.button("📄 Executive Summary", use_container_width=True):
            st.session_state.page = 'summary'
            st.rerun()

def render_simulator_page(models):
    """Render Feature 1: Global Shock Simulator"""
    st.title("🎮 Feature 1: Global Shock Simulator")
    
    st.write("""
    Simulate different supply chain disruption scenarios and analyze their impacts across 
    countries, industries, and products.
    """)
    
    # Timeline visualization
    st.subheader("📅 Disruption Timeline")
    timeline_chart = models['chart_viz'].create_timeline_chart()
    st.plotly_chart(timeline_chart, use_container_width=True)
    
    # Industry impact
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🏭 Industry Impact Analysis")
        industry_chart = models['chart_viz'].create_industry_impact_chart()
        st.plotly_chart(industry_chart, use_container_width=True)
    
    with col2:
        st.subheader("⏱️ Recovery Timeline by Industry")
        recovery_chart = models['chart_viz'].create_recovery_timeline_chart()
        st.plotly_chart(recovery_chart, use_container_width=True)
    
    # GDP Impact
    st.subheader("💰 GDP Impact by Country")
    gdp_chart = models['chart_viz'].create_gdp_impact_chart()
    st.plotly_chart(gdp_chart, use_container_width=True)

def render_risk_map_page(models):
    """Render Feature 2: Supply Chain Risk Map"""
    st.title("🗺️ Feature 2: Supply Chain Risk Map")
    
    st.write("""
    Interactive visualization of global supply chain risks, showing affected countries, 
    risk levels, and regional impacts.
    """)
    
    # Global risk map
    st.subheader("🌍 Global Risk Distribution")
    global_map = models['risk_map'].create_global_risk_map()
    st.plotly_chart(global_map, use_container_width=True)
    
    # Regional comparison and dependency network
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🌏 Regional Risk Comparison")
        regional_chart = models['risk_map'].create_regional_risk_chart()
        st.plotly_chart(regional_chart, use_container_width=True)
    
    with col2:
        st.subheader("🔗 Critical Dependencies")
        dependency_chart = models['risk_map'].create_dependency_network()
        st.plotly_chart(dependency_chart, use_container_width=True)
    
    # Risk evolution timeline
    st.subheader("📈 Risk Evolution Over Time")
    timeline_chart = models['risk_map'].create_risk_timeline()
    st.plotly_chart(timeline_chart, use_container_width=True)
    
    # Risk assessment details
    st.subheader("📊 Detailed Risk Assessment")
    vulnerability = models['risk_analyzer'].calculate_supply_chain_vulnerability_index()
    
    cols = st.columns(4)
    with cols[0]:
        st.metric("Vulnerability Index", f"{vulnerability['vulnerability_index']}/100")
    with cols[1]:
        st.metric("Resilience Score", f"{vulnerability['resilience_score']}/100")
    with cols[2]:
        st.metric("Critical Countries", vulnerability['critical_country_nodes'])
    with cols[3]:
        st.metric("Critical Industries", vulnerability['critical_industry_nodes'])

def render_consumer_page(models):
    """Render Feature 3: Consumer Impact Analyzer"""
    st.title("🛒 Feature 3: Consumer Impact Analyzer")
    
    st.write("""
    Analyze the impact on consumer products, including shortages, price increases, 
    and spending pattern changes.
    """)
    
    # Summary metrics
    consumer_metrics = models['consumer_analyzer'].get_summary_metrics()
    
    Dashboard.create_kpi_row([
        {
            'title': '📦 Products Affected',
            'value': consumer_metrics['products_affected'],
            'delta': None
        },
        {
            'title': '💵 Avg Price Increase',
            'value': f"{consumer_metrics['avg_price_increase_pct']}%",
            'delta': None
        },
        {
            'title': '📊 Avg Availability',
            'value': f"{consumer_metrics['avg_availability_pct']}%",
            'delta': None
        },
        {
            'title': '⚠️ Critical Shortages',
            'value': consumer_metrics['critical_shortages'],
            'delta': 'High severity'
        }
    ])
    
    st.markdown("---")
    
    # Product impact charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📈 Consumer Product Impact")
        consumer_chart = models['chart_viz'].create_consumer_impact_chart()
        st.plotly_chart(consumer_chart, use_container_width=True)
    
    with col2:
        st.subheader("⚠️ Shortage Severity Analysis")
        shortage_chart = models['chart_viz'].create_shortage_severity_chart()
        st.plotly_chart(shortage_chart, use_container_width=True)
    
    # Product shortage details
    st.subheader("📋 Product Shortage Details")
    shortages = models['consumer_analyzer'].analyze_product_shortages()
    
    for shortage in shortages[:10]:  # Show top 10
        with st.expander(f"{shortage['product']} - {get_severity_emoji(shortage['shortage_level'])} {shortage['shortage_level']}"):
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Shortage Score", f"{shortage['shortage_severity_score']}/100")
            with col2:
                st.metric("Price Increase", f"+{shortage['price_increase_pct']}%")
            with col3:
                st.metric("Availability", f"{shortage['availability_pct']}%")
            
            st.write(f"**Timeline:** {shortage['shortage_timeline']}")
            st.write(f"**Recommendation:** {shortage['recommendation']}")
    
    # Consumer spending analysis
    st.subheader("💳 Consumer Spending Changes")
    spending = models['consumer_analyzer'].analyze_consumer_spending_changes()
    
    spending_data = []
    for category, data in spending.items():
        spending_data.append({
            'Category': category,
            'Change': f"{data['change_pct']:+.1f}%",
            'Trend': data['trend']
        })
    
    st.table(spending_data)

def render_investment_page(models):
    """Render Feature 4: Investment Intelligence Dashboard"""
    st.title("💼 Feature 4: Investment Intelligence Dashboard")
    
    st.write("""
    Identify investment opportunities and risks across sectors, with actionable 
    recommendations and portfolio strategies.
    """)
    
    # Investment summary
    investment_metrics = models['investment_analyzer'].get_summary_metrics()
    portfolio_rec = models['investment_analyzer'].generate_portfolio_recommendations()
    
    Dashboard.create_kpi_row([
        {
            'title': '📈 Buy Opportunities',
            'value': investment_metrics['buy_opportunities'],
            'delta': f"+{investment_metrics['average_buy_growth_pct']}% avg growth"
        },
        {
            'title': '📉 High Risk Sectors',
            'value': investment_metrics['high_risk_sectors'],
            'delta': f"{investment_metrics['average_risk_loss_pct']}% avg loss"
        },
        {
            'title': '🎯 Market Sentiment',
            'value': investment_metrics['market_sentiment'],
            'delta': None
        },
        {
            'title': '💼 Strategy',
            'value': portfolio_rec['strategy'],
            'delta': None
        }
    ])
    
    st.markdown("---")
    
    # Investment opportunities chart
    st.subheader("📊 Investment Opportunities & Risks")
    investment_chart = models['chart_viz'].create_investment_opportunities_chart()
    st.plotly_chart(investment_chart, use_container_width=True)
    
    # Sector comparison
    st.subheader("🎯 Sector Comparison: Opportunity vs Risk")
    radar_chart = models['chart_viz'].create_sector_comparison_radar()
    st.plotly_chart(radar_chart, use_container_width=True)
    
    # Detailed recommendations
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("✅ Buy Opportunities")
        buy_opps = models['investment_analyzer'].identify_buy_opportunities()
        
        for opp in buy_opps[:5]:
            Dashboard.create_recommendation_card(opp, 'BUY')
            st.write(f"**Expected Growth:** +{opp['expected_growth_pct']}%")
            st.write(f"**Confidence:** {opp['confidence_level']}")
            st.write(f"**Key Companies:** {', '.join(opp['key_companies'][:3])}")
            st.markdown("---")
    
    with col2:
        st.subheader("❌ High Risk Sectors")
        high_risks = models['investment_analyzer'].identify_high_risk_sectors()
        
        for risk in high_risks[:5]:
            Dashboard.create_recommendation_card(risk, 'SELL')
            st.write(f"**Expected Loss:** -{risk['expected_loss_pct']}%")
            st.write(f"**Severity:** {risk['severity']}")
            st.write(f"**Key Companies:** {', '.join(risk['key_companies'][:3])}")
            st.markdown("---")
    
    # Portfolio recommendations
    st.subheader("💼 Portfolio Strategy")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Asset Allocation:**")
        for asset, allocation in portfolio_rec['asset_allocation'].items():
            st.write(f"- {asset}: {allocation}")
    
    with col2:
        st.write("**Risk Management:**")
        for tip in portfolio_rec['risk_management'][:4]:
            st.write(f"- {tip}")

def render_summary_page(models):
    """Render Feature 5: Executive Summary Generator"""
    st.title("📄 Feature 5: Executive Summary Generator")
    
    st.write("""
    Comprehensive executive summary with key findings, recommendations, and 
    downloadable report.
    """)
    
    # Generate summary
    summary = models['report_gen'].generate_executive_summary()
    
    # Header
    st.markdown(f"## {summary['title']}")
    st.markdown(f"### {summary['subtitle']}")
    st.markdown(f"*Generated: {summary['date']}*")
    
    st.markdown("---")
    
    # Executive Overview
    section = summary['sections']['executive_overview']
    st.subheader(section['title'])
    st.write(section['content'])
    
    st.markdown("---")
    
    # Key Findings
    section = summary['sections']['key_findings']
    st.subheader(section['title'])
    for i, finding in enumerate(section['findings'], 1):
        st.write(f"{i}. {finding}")
    
    st.markdown("---")
    
    # Risk Assessment
    section = summary['sections']['risk_assessment']
    st.subheader(section['title'])
    
    cols = st.columns(4)
    with cols[0]:
        st.metric("Vulnerability", f"{section['vulnerability_index']}/100")
    with cols[1]:
        st.metric("Resilience", f"{section['resilience_score']}/100")
    with cols[2]:
        st.metric("Critical Countries", section['critical_nodes']['countries'])
    with cols[3]:
        st.metric("Critical Industries", section['critical_nodes']['industries'])
    
    st.write("**Top Risk Countries:**")
    for country in section['top_risk_countries'][:5]:
        st.write(f"- {country['country']}: {country['risk_score']}/100 ({country['risk_level']}) - Recovery: {country['recovery_months']} months")
    
    st.markdown("---")
    
    # Strategic Recommendations
    section = summary['sections']['strategic_recommendations']
    st.subheader(section['title'])
    
    tabs = st.tabs(["Immediate Actions", "Short-term", "Long-term", "Investment Priorities"])
    
    with tabs[0]:
        for action in section['immediate_actions']:
            st.write(f"• {action}")
    
    with tabs[1]:
        for strategy in section['short_term_strategies']:
            st.write(f"• {strategy}")
    
    with tabs[2]:
        for strategy in section['long_term_strategies']:
            st.write(f"• {strategy}")
    
    with tabs[3]:
        for priority in section['investment_priorities']:
            st.write(f"• {priority}")
    
    st.markdown("---")
    
    # Download report
    st.subheader("📥 Download Report")
    text_report = models['report_gen'].generate_text_report()
    
    Dashboard.create_download_button(
        data=text_report,
        filename=f"supply_chain_report_{summary['date'].replace(' ', '_')}.txt",
        label="📄 Download Full Report (TXT)"
    )

def main():
    """Main application"""
    
    # Initialize session state
    if 'page' not in st.session_state:
        st.session_state.page = 'home'
    
    # Sidebar
    st.sidebar.title("🌐 Supply Chain Intelligence")
    
    # Simulation parameters
    filters = Dashboard.create_sidebar_filters(
        shock_types=[
            "Natural Disaster (Earthquake/Tsunami)",
            "Geopolitical Conflict",
            "Taiwan Semiconductor Disruption",
            "Pandemic Outbreak",
            "Cyber Attack"
        ],
        default_intensity=40
    )
    
    # Initialize models
    models = initialize_models(filters['shock_type'], filters['intensity'])
    
    # Navigation
    st.sidebar.markdown("---")
    st.sidebar.subheader("📍 Navigation")
    
    pages = {
        'home': '🏠 Home',
        'simulator': '🎮 Shock Simulator',
        'risk_map': '🗺️ Risk Map',
        'consumer': '🛒 Consumer Impact',
        'investment': '💼 Investment Intel',
        'summary': '📄 Executive Summary'
    }
    
    for page_key, page_name in pages.items():
        if st.sidebar.button(page_name, use_container_width=True):
            st.session_state.page = page_key
            st.rerun()
    
    # Render selected page
    if st.session_state.page == 'home':
        render_home_page(models)
    elif st.session_state.page == 'simulator':
        render_simulator_page(models)
    elif st.session_state.page == 'risk_map':
        render_risk_map_page(models)
    elif st.session_state.page == 'consumer':
        render_consumer_page(models)
    elif st.session_state.page == 'investment':
        render_investment_page(models)
    elif st.session_state.page == 'summary':
        render_summary_page(models)
    
    # Footer
    st.sidebar.markdown("---")
    st.sidebar.markdown("""
    <div style="text-align: center; color: #7f8c8d; font-size: 0.8rem;">
        <p>Global Supply Chain Intelligence Platform</p>
        <p>© 2026 | Built with Streamlit</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

# Made with Bob
