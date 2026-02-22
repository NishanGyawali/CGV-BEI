"""
stock_config.py
Configuration file for stock tickers and sectors

This file contains all the stocks we'll visualize,
organized by market sector.
"""

# Stock tickers organized by sector
# Each sector contains 8 major stocks
STOCKS_BY_SECTOR = {
    'Technology': [
        'AAPL',  # Apple Inc.
        'MSFT',  # Microsoft Corporation
        'GOOGL',  # Alphabet Inc. (Google)
        'META',  # Meta Platforms (Facebook)
        'NVDA',  # NVIDIA Corporation
        'TSLA',  # Tesla Inc.
        'INTC',  # Intel Corporation
        'AMD'  # Advanced Micro Devices
    ],

    'Finance': [
        'JPM',  # JPMorgan Chase
        'BAC',  # Bank of America
        'WFC',  # Wells Fargo
        'GS',  # Goldman Sachs
        'MS',  # Morgan Stanley
        'C',  # Citigroup
        'BLK',  # BlackRock
        'AXP'  # American Express
    ],

    'Healthcare': [
        'JNJ',  # Johnson & Johnson
        'UNH',  # UnitedHealth Group
        'PFE',  # Pfizer
        'ABBV',  # AbbVie
        'TMO',  # Thermo Fisher Scientific
        'MRK',  # Merck & Co.
        'LLY',  # Eli Lilly
        'ABT'  # Abbott Laboratories
    ],

    'Consumer': [
        'AMZN',  # Amazon
        'WMT',  # Walmart
        'HD',  # Home Depot
        'MCD',  # McDonald's
        'NKE',  # Nike
        'SBUX',  # Starbucks
        'TGT',  # Target
        'COST'  # Costco
    ],

    'Energy': [
        'XOM',  # Exxon Mobil
        'CVX',  # Chevron
        'COP',  # ConocoPhillips
        'SLB',  # Schlumberger
        'EOG',  # EOG Resources
        'MPC',  # Marathon Petroleum
        'PSX',  # Phillips 66
        'VLO'  # Valero Energy
    ]
}

# Visualization settings
VISUALIZATION_CONFIG = {
    # 3D Layout
    'sector_spacing': 3.0,  # Space between sectors on X-axis
    'stock_spacing': 1.0,  # Space between stocks on Y-axis

    # Colors
    'positive_color': 'green',  # Color for gains
    'negative_color': 'red',  # Color for losses
    'neutral_color': 'yellow',  # Color for neutral

    # Refresh settings
    'refresh_interval': 60,  # Seconds between updates
    'auto_refresh': False,  # Start with auto-refresh off

    # Display settings
    'show_stock_labels': True,  # Show ticker symbols
    'show_tooltips': True,  # Show info on hover
    'camera_position': {
        'eye_x': 1.8,
        'eye_y': 1.8,
        'eye_z': 1.3
    }
}


# Get total number of stocks
def get_total_stocks():
    """Calculate total number of stocks across all sectors"""
    return sum(len(stocks) for stocks in STOCKS_BY_SECTOR.values())


# Get all tickers as a flat list
def get_all_tickers():
    """Get all stock tickers in a single list"""
    all_tickers = []
    for sector_stocks in STOCKS_BY_SECTOR.values():
        all_tickers.extend(sector_stocks)
    return all_tickers


# Get tickers by sector
def get_tickers_for_sector(sector_name):
    """Get tickers for a specific sector"""
    return STOCKS_BY_SECTOR.get(sector_name, [])


# Get all sector names
def get_sector_names():
    """Get list of all sector names"""
    return list(STOCKS_BY_SECTOR.keys())


# Test the configuration
if __name__ == "__main__":
    print("=" * 60)
    print("STOCK CONFIGURATION")
    print("=" * 60)

    print(f"\nTotal sectors: {len(STOCKS_BY_SECTOR)}")
    print(f"Total stocks: {get_total_stocks()}")

    print("\n📊 Stocks by Sector:")
    print("-" * 60)

    for sector, tickers in STOCKS_BY_SECTOR.items():
        print(f"\n{sector}: ({len(tickers)} stocks)")
        print(f"  {', '.join(tickers)}")

    print("\n" + "=" * 60)
    print("✅ Configuration loaded successfully!")
    print("=" * 60)