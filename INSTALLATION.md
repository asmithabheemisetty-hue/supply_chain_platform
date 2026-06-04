# Installation and Setup Guide

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (for cloning the repository)

## Installation Steps

### 1. Clone or Download the Repository

```bash
# If using Git
git clone <repository-url>
cd supply_chain_platform

# Or download and extract the ZIP file
```

### 2. Create a Virtual Environment (Recommended)

```bash
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- streamlit (web application framework)
- pandas (data manipulation)
- numpy (numerical computing)
- plotly (interactive visualizations)
- matplotlib (plotting)
- seaborn (statistical visualizations)
- scikit-learn (machine learning utilities)

### 4. Verify Installation

```bash
python -c "import streamlit; import pandas; import plotly; print('All dependencies installed successfully!')"
```

## Running the Application

### Start the Streamlit Application

```bash
streamlit run app.py
```

The application will automatically open in your default web browser at `http://localhost:8501`

### Alternative: Specify Port

```bash
streamlit run app.py --server.port 8080
```

## Project Structure

```
supply_chain_platform/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
├── INSTALLATION.md                 # This file
│
├── data/                           # Data modules
│   ├── __init__.py
│   ├── countries_data.py          # Country dependency data
│   ├── industry_data.py           # Industry impact data
│   └── product_data.py            # Consumer product data
│
├── models/                         # Analysis models
│   ├── __init__.py
│   ├── shock_simulator.py         # Shock simulation engine
│   ├── risk_analyzer.py           # Risk analysis
│   ├── consumer_impact.py         # Consumer impact analysis
│   └── investment_analyzer.py     # Investment analysis
│
├── visualizations/                 # Visualization components
│   ├── __init__.py
│   ├── risk_map.py                # Interactive maps
│   ├── charts.py                  # Various charts
│   └── dashboard.py               # Dashboard components
│
└── utils/                          # Utility functions
    ├── __init__.py
    ├── report_generator.py        # Report generation
    └── helpers.py                 # Helper functions
```

## Features

The platform includes 5 main features:

1. **Global Shock Simulator** - Simulate supply chain disruptions
2. **Supply Chain Risk Map** - Interactive global risk visualization
3. **Consumer Impact Analyzer** - Product shortage and price analysis
4. **Investment Intelligence Dashboard** - Investment opportunities and risks
5. **Executive Summary Generator** - Comprehensive reports

## Usage

1. **Adjust Parameters**: Use the sidebar to select shock scenario and intensity
2. **Navigate Features**: Click on feature buttons or use sidebar navigation
3. **Explore Visualizations**: Interactive charts and maps
4. **Download Reports**: Generate and download executive summaries

## Troubleshooting

### Import Errors

If you encounter import errors:

```bash
# Ensure you're in the project directory
cd supply_chain_platform

# Reinstall dependencies
pip install --upgrade -r requirements.txt
```

### Port Already in Use

If port 8501 is already in use:

```bash
streamlit run app.py --server.port 8502
```

### Browser Doesn't Open Automatically

Manually navigate to: `http://localhost:8501`

### Module Not Found Errors

Ensure you're running the app from the correct directory:

```bash
# Should be in supply_chain_platform directory
pwd  # or cd on Windows

# Run from project root
streamlit run app.py
```

## Performance Tips

- The application loads all data on startup
- First visualization may take a few seconds
- Use Chrome or Firefox for best performance
- Close unused browser tabs to free memory

## System Requirements

- **RAM**: Minimum 4GB, recommended 8GB
- **CPU**: Any modern processor
- **Browser**: Chrome, Firefox, Safari, or Edge (latest versions)
- **Internet**: Not required (runs locally)

## Support

For issues or questions:
1. Check this installation guide
2. Review the README.md file
3. Verify all dependencies are installed
4. Ensure Python version is 3.8+

## Next Steps

After installation:
1. Start the application: `streamlit run app.py`
2. Explore the home page overview
3. Navigate through the 5 features
4. Adjust simulation parameters in the sidebar
5. Generate and download reports

Enjoy exploring the Global Supply Chain Intelligence Platform!