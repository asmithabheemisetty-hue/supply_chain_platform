"""
Helper Utilities
Common utility functions for the application
"""

import json
from datetime import datetime, timedelta

def format_percentage(value, decimals=1):
    """
    Format a number as percentage
    
    Args:
        value: Numeric value
        decimals: Number of decimal places
        
    Returns:
        Formatted percentage string
    """
    return f"{value:.{decimals}f}%"

def format_currency(value, currency="USD"):
    """
    Format a number as currency
    
    Args:
        value: Numeric value
        currency: Currency code
        
    Returns:
        Formatted currency string
    """
    if currency == "USD":
        return f"${value:,.2f}"
    elif currency == "EUR":
        return f"€{value:,.2f}"
    else:
        return f"{value:,.2f} {currency}"

def calculate_percentage_change(old_value, new_value):
    """
    Calculate percentage change between two values
    
    Args:
        old_value: Original value
        new_value: New value
        
    Returns:
        Percentage change
    """
    if old_value == 0:
        return 0
    return ((new_value - old_value) / old_value) * 100

def categorize_value(value, thresholds):
    """
    Categorize a value based on thresholds
    
    Args:
        value: Value to categorize
        thresholds: Dictionary with category names and threshold values
        
    Returns:
        Category name
    """
    sorted_thresholds = sorted(thresholds.items(), key=lambda x: x[1], reverse=True)
    
    for category, threshold in sorted_thresholds:
        if value >= threshold:
            return category
    
    return list(thresholds.keys())[-1]

def get_risk_color(risk_score):
    """
    Get color code based on risk score
    
    Args:
        risk_score: Risk score (0-100)
        
    Returns:
        Hex color code
    """
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

def get_risk_level(risk_score):
    """
    Get risk level based on score
    
    Args:
        risk_score: Risk score (0-100)
        
    Returns:
        Risk level string
    """
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

def calculate_weighted_average(values, weights):
    """
    Calculate weighted average
    
    Args:
        values: List of values
        weights: List of weights
        
    Returns:
        Weighted average
    """
    if len(values) != len(weights):
        raise ValueError("Values and weights must have same length")
    
    if sum(weights) == 0:
        return 0
    
    return sum(v * w for v, w in zip(values, weights)) / sum(weights)

def generate_date_range(start_date, end_date, interval_days=30):
    """
    Generate a range of dates
    
    Args:
        start_date: Start date
        end_date: End date
        interval_days: Days between dates
        
    Returns:
        List of dates
    """
    dates = []
    current = start_date
    
    while current <= end_date:
        dates.append(current)
        current += timedelta(days=interval_days)
    
    return dates

def format_large_number(value):
    """
    Format large numbers with K, M, B suffixes
    
    Args:
        value: Numeric value
        
    Returns:
        Formatted string
    """
    if abs(value) >= 1_000_000_000:
        return f"{value / 1_000_000_000:.1f}B"
    elif abs(value) >= 1_000_000:
        return f"{value / 1_000_000:.1f}M"
    elif abs(value) >= 1_000:
        return f"{value / 1_000:.1f}K"
    else:
        return f"{value:.0f}"

def calculate_compound_growth(initial_value, growth_rate, periods):
    """
    Calculate compound growth
    
    Args:
        initial_value: Starting value
        growth_rate: Growth rate per period (as decimal)
        periods: Number of periods
        
    Returns:
        Final value after compound growth
    """
    return initial_value * ((1 + growth_rate) ** periods)

def normalize_score(value, min_val, max_val, target_min=0, target_max=100):
    """
    Normalize a value to a target range
    
    Args:
        value: Value to normalize
        min_val: Minimum value in original range
        max_val: Maximum value in original range
        target_min: Minimum value in target range
        target_max: Maximum value in target range
        
    Returns:
        Normalized value
    """
    if max_val == min_val:
        return target_min
    
    normalized = ((value - min_val) / (max_val - min_val)) * (target_max - target_min) + target_min
    return max(target_min, min(target_max, normalized))

def create_summary_dict(data_list, key_field, value_field):
    """
    Create summary dictionary from list of dictionaries
    
    Args:
        data_list: List of dictionaries
        key_field: Field to use as key
        value_field: Field to use as value
        
    Returns:
        Dictionary with summarized data
    """
    return {item[key_field]: item[value_field] for item in data_list}

def filter_by_threshold(data_dict, threshold, comparison='>='):
    """
    Filter dictionary by threshold
    
    Args:
        data_dict: Dictionary to filter
        threshold: Threshold value
        comparison: Comparison operator ('>=', '>', '<=', '<', '==')
        
    Returns:
        Filtered dictionary
    """
    comparisons = {
        '>=': lambda x, y: x >= y,
        '>': lambda x, y: x > y,
        '<=': lambda x, y: x <= y,
        '<': lambda x, y: x < y,
        '==': lambda x, y: x == y
    }
    
    comp_func = comparisons.get(comparison, lambda x, y: x >= y)
    
    return {k: v for k, v in data_dict.items() if comp_func(v, threshold)}

def calculate_recovery_rate(initial_impact, current_impact, time_elapsed, total_time):
    """
    Calculate recovery rate
    
    Args:
        initial_impact: Initial impact percentage
        current_impact: Current impact percentage
        time_elapsed: Time elapsed since disruption
        total_time: Total expected recovery time
        
    Returns:
        Recovery rate percentage
    """
    if total_time == 0:
        return 0
    
    recovery = ((initial_impact - current_impact) / initial_impact) * 100
    expected_recovery = (time_elapsed / total_time) * 100
    
    return min(100, max(0, recovery))

def get_severity_emoji(severity):
    """
    Get emoji for severity level
    
    Args:
        severity: Severity level string
        
    Returns:
        Emoji string
    """
    emojis = {
        'Critical': '🔴',
        'High': '🟠',
        'Medium': '🟡',
        'Low': '🟢',
        'Minimal': '⚪'
    }
    return emojis.get(severity, '⚪')

def get_trend_emoji(value):
    """
    Get trend emoji based on value
    
    Args:
        value: Numeric value (positive or negative)
        
    Returns:
        Emoji string
    """
    if value > 0:
        return '📈'
    elif value < 0:
        return '📉'
    else:
        return '➡️'

def format_duration(months):
    """
    Format duration in months to readable string
    
    Args:
        months: Number of months
        
    Returns:
        Formatted duration string
    """
    if months < 1:
        return "Less than 1 month"
    elif months == 1:
        return "1 month"
    elif months < 12:
        return f"{months} months"
    else:
        years = months // 12
        remaining_months = months % 12
        if remaining_months == 0:
            return f"{years} year{'s' if years > 1 else ''}"
        else:
            return f"{years} year{'s' if years > 1 else ''} {remaining_months} month{'s' if remaining_months > 1 else ''}"

def create_color_scale(values, colorscale='RdYlGn_r'):
    """
    Create color scale for values
    
    Args:
        values: List of values
        colorscale: Name of colorscale
        
    Returns:
        List of colors
    """
    if not values:
        return []
    
    min_val = min(values)
    max_val = max(values)
    
    # Simple color mapping
    colors = []
    for value in values:
        normalized = normalize_score(value, min_val, max_val, 0, 1)
        colors.append(get_risk_color(normalized * 100))
    
    return colors

def export_to_json(data, filename):
    """
    Export data to JSON file
    
    Args:
        data: Data to export
        filename: Output filename
    """
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

def safe_divide(numerator, denominator, default=0):
    """
    Safely divide two numbers
    
    Args:
        numerator: Numerator
        denominator: Denominator
        default: Default value if division by zero
        
    Returns:
        Result of division or default
    """
    try:
        return numerator / denominator if denominator != 0 else default
    except (TypeError, ZeroDivisionError):
        return default

def truncate_text(text, max_length=50, suffix='...'):
    """
    Truncate text to maximum length
    
    Args:
        text: Text to truncate
        max_length: Maximum length
        suffix: Suffix to add if truncated
        
    Returns:
        Truncated text
    """
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix

# Made with Bob
