"""
Dashboard Components
Reusable dashboard components for the application
"""

import streamlit as st

class Dashboard:
    """Dashboard component builder"""
    
    @staticmethod
    def create_metric_card(title, value, delta=None, delta_color="normal"):
        """
        Create a metric card
        
        Args:
            title: Metric title
            value: Metric value
            delta: Change value (optional)
            delta_color: Color for delta (normal, inverse, off)
        """
        st.metric(label=title, value=value, delta=delta, delta_color=delta_color)
    
    @staticmethod
    def create_kpi_row(metrics):
        """
        Create a row of KPI metrics
        
        Args:
            metrics: List of dictionaries with 'title', 'value', 'delta' keys
        """
        cols = st.columns(len(metrics))
        for col, metric in zip(cols, metrics):
            with col:
                delta = metric.get('delta')
                delta_color = metric.get('delta_color', 'normal')
                st.metric(
                    label=metric['title'],
                    value=metric['value'],
                    delta=delta,
                    delta_color=delta_color
                )
    
    @staticmethod
    def create_info_box(title, content, box_type="info"):
        """
        Create an information box
        
        Args:
            title: Box title
            content: Box content (can be string or list)
            box_type: Type of box (info, success, warning, error)
        """
        if box_type == "info":
            st.info(f"**{title}**\n\n{content}")
        elif box_type == "success":
            st.success(f"**{title}**\n\n{content}")
        elif box_type == "warning":
            st.warning(f"**{title}**\n\n{content}")
        elif box_type == "error":
            st.error(f"**{title}**\n\n{content}")
    
    @staticmethod
    def create_data_table(data, title=None):
        """
        Create a data table
        
        Args:
            data: DataFrame or dictionary
            title: Optional title
        """
        if title:
            st.subheader(title)
        st.dataframe(data, use_container_width=True)
    
    @staticmethod
    def create_expandable_section(title, content_func):
        """
        Create an expandable section
        
        Args:
            title: Section title
            content_func: Function to call to render content
        """
        with st.expander(title):
            content_func()
    
    @staticmethod
    def create_tabs(tab_names, tab_contents):
        """
        Create tabs
        
        Args:
            tab_names: List of tab names
            tab_contents: List of functions to render tab content
        """
        tabs = st.tabs(tab_names)
        for tab, content_func in zip(tabs, tab_contents):
            with tab:
                content_func()
    
    @staticmethod
    def create_sidebar_filters(shock_types, default_intensity=40):
        """
        Create sidebar filters
        
        Args:
            shock_types: List of shock type options
            default_intensity: Default intensity value
            
        Returns:
            Dictionary with selected values
        """
        st.sidebar.header("Simulation Parameters")
        
        selected_shock = st.sidebar.selectbox(
            "Shock Scenario",
            shock_types,
            index=2  # Default to Taiwan scenario
        )
        
        intensity = st.sidebar.slider(
            "Shock Intensity (%)",
            min_value=10,
            max_value=100,
            value=default_intensity,
            step=5,
            help="Adjust the severity of the supply chain disruption"
        )
        
        st.sidebar.markdown("---")
        
        return {
            'shock_type': selected_shock,
            'intensity': intensity
        }
    
    @staticmethod
    def create_risk_badge(risk_level):
        """
        Create a colored risk badge
        
        Args:
            risk_level: Risk level string
            
        Returns:
            HTML string for badge
        """
        colors = {
            'Critical': '#c0392b',
            'High': '#e74c3c',
            'Medium': '#f39c12',
            'Low': '#f1c40f',
            'Minimal': '#2ecc71'
        }
        
        color = colors.get(risk_level, '#95a5a6')
        return f'<span style="background-color: {color}; color: white; padding: 5px 10px; border-radius: 5px; font-weight: bold;">{risk_level}</span>'
    
    @staticmethod
    def create_recommendation_card(recommendation, rec_type="BUY"):
        """
        Create a recommendation card
        
        Args:
            recommendation: Dictionary with recommendation details
            rec_type: Type of recommendation (BUY, HOLD, SELL)
        """
        colors = {
            'BUY': '#2ecc71',
            'HOLD': '#f39c12',
            'SELL': '#e74c3c',
            'Strong Buy': '#27ae60',
            'Strong Sell': '#c0392b'
        }
        
        color = colors.get(rec_type, '#95a5a6')
        
        st.markdown(f"""
        <div style="border-left: 5px solid {color}; padding: 10px; margin: 10px 0; background-color: #f8f9fa;">
            <h4 style="margin: 0; color: {color};">{recommendation.get('sector', 'N/A')}</h4>
            <p style="margin: 5px 0;"><strong>Recommendation:</strong> {rec_type}</p>
            <p style="margin: 5px 0;">{recommendation.get('reason', 'N/A')}</p>
        </div>
        """, unsafe_allow_html=True)
    
    @staticmethod
    def create_progress_indicator(label, value, max_value=100):
        """
        Create a progress indicator
        
        Args:
            label: Progress label
            value: Current value
            max_value: Maximum value
        """
        st.write(f"**{label}**")
        st.progress(value / max_value)
        st.write(f"{value}/{max_value}")
    
    @staticmethod
    def create_comparison_columns(left_data, right_data, left_title="Before", right_title="After"):
        """
        Create side-by-side comparison columns
        
        Args:
            left_data: Data for left column
            right_data: Data for right column
            left_title: Title for left column
            right_title: Title for right column
        """
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader(left_title)
            if isinstance(left_data, dict):
                for key, value in left_data.items():
                    st.write(f"**{key}:** {value}")
            else:
                st.write(left_data)
        
        with col2:
            st.subheader(right_title)
            if isinstance(right_data, dict):
                for key, value in right_data.items():
                    st.write(f"**{key}:** {value}")
            else:
                st.write(right_data)
    
    @staticmethod
    def create_timeline_view(timeline_data):
        """
        Create a timeline view
        
        Args:
            timeline_data: Dictionary with timeline phases
        """
        for phase, data in timeline_data.items():
            with st.container():
                st.markdown(f"### {phase}")
                st.markdown(f"**Duration:** {data.get('duration', 'N/A')}")
                
                if 'description' in data:
                    st.write(data['description'])
                
                if 'metrics' in data:
                    cols = st.columns(len(data['metrics']))
                    for col, (key, value) in zip(cols, data['metrics'].items()):
                        with col:
                            st.metric(key, value)
                
                st.markdown("---")
    
    @staticmethod
    def create_alert_banner(message, alert_type="info"):
        """
        Create an alert banner
        
        Args:
            message: Alert message
            alert_type: Type of alert (info, success, warning, error)
        """
        colors = {
            'info': '#3498db',
            'success': '#2ecc71',
            'warning': '#f39c12',
            'error': '#e74c3c'
        }
        
        icons = {
            'info': 'ℹ️',
            'success': '✅',
            'warning': '⚠️',
            'error': '❌'
        }
        
        color = colors.get(alert_type, '#3498db')
        icon = icons.get(alert_type, 'ℹ️')
        
        st.markdown(f"""
        <div style="background-color: {color}; color: white; padding: 15px; border-radius: 5px; margin: 10px 0;">
            <strong>{icon} {message}</strong>
        </div>
        """, unsafe_allow_html=True)
    
    @staticmethod
    def create_stat_grid(stats, columns=3):
        """
        Create a grid of statistics
        
        Args:
            stats: List of dictionaries with 'label' and 'value' keys
            columns: Number of columns in grid
        """
        rows = [stats[i:i+columns] for i in range(0, len(stats), columns)]
        
        for row in rows:
            cols = st.columns(columns)
            for col, stat in zip(cols, row):
                with col:
                    st.markdown(f"""
                    <div style="text-align: center; padding: 20px; background-color: #f8f9fa; border-radius: 10px; margin: 5px;">
                        <h2 style="margin: 0; color: #2c3e50;">{stat['value']}</h2>
                        <p style="margin: 5px 0; color: #7f8c8d;">{stat['label']}</p>
                    </div>
                    """, unsafe_allow_html=True)
    
    @staticmethod
    def create_download_button(data, filename, label="Download Report"):
        """
        Create a download button
        
        Args:
            data: Data to download (string or bytes)
            filename: Name of file to download
            label: Button label
        """
        st.download_button(
            label=label,
            data=data,
            file_name=filename,
            mime='text/plain' if isinstance(data, str) else 'application/octet-stream'
        )

# Made with Bob
