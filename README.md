# Global Supply Chain Shock Intelligence Platform

## Project Overview
A web-based platform that simulates and analyzes the impact of global supply chain disruptions, specifically focusing on the Taiwan semiconductor supply chain disruption scenario.

## Scenario
**Taiwan Semiconductor Supply Chain Disruption (40%)**
- Simulates a 40% disruption in Taiwan's semiconductor supply chain
- Analyzes impact on industries, companies, consumers, and investments globally

## Features
1. **Global Shock Simulator** - Select and simulate different supply chain shocks
2. **Supply Chain Risk Map** - Interactive visualization of affected countries and risk levels
3. **Consumer Impact Analyzer** - Predict product shortages and price changes
4. **Investment Intelligence Dashboard** - Identify opportunities and risks by sector
5. **Executive Summary Generator** - Generate CEO-ready reports

## Tech Stack
- **Backend**: Python, Pandas, NumPy, Plotly
- **Frontend**: Streamlit (for rapid development)
- **Data Visualization**: Plotly, Matplotlib

## Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd supply_chain_platform

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

## Project Structure
```
supply_chain_platform/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── README.md                       # This file
├── data/
│   ├── countries_data.py          # Country dependency data
│   ├── industry_data.py           # Industry impact data
│   └── product_data.py            # Product and pricing data
├── models/
│   ├── shock_simulator.py        # Shock simulation logic
│   ├── risk_analyzer.py           # Risk analysis engine
│   ├── consumer_impact.py         # Consumer impact predictions
│   └── investment_analyzer.py     # Investment opportunity analysis
├── visualizations/
│   ├── risk_map.py                # Interactive world map
│   ├── charts.py                  # Various charts and graphs
│   └── dashboard.py               # Dashboard components
└── utils/
    ├── report_generator.py        # Executive summary generator
    └── helpers.py                 # Utility functions
```

## Usage
1. Launch the application: `streamlit run app.py`
2. Select shock type (default: Semiconductor Shock - Taiwan)
3. Adjust disruption intensity (default: 40%)
4. View analysis across all features
5. Download executive summary report

## Evaluation Criteria Coverage
- ✅ Business Understanding (30%): Comprehensive scenario analysis
- ✅ Problem Solving (25%): Multi-dimensional impact assessment
- ✅ Technical Execution (20%): Clean, modular code architecture
- ✅ Data Visualization (15%): Interactive maps and charts
- ✅ Innovation (10%): Executive summary generator with AI-like insights

## Team
[Add your team members here]

## License
MIT License

## Deadline
June 5, 2026, 10:00 AM