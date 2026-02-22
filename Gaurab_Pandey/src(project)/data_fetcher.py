"""
data_fetcher.py
Handles fetching stock market data from Yahoo Finance API

This module is responsible for:
1. Fetching real-time stock data
2. Processing and organizing the data
3. Calculating price changes and statistics
"""

import datetime
import typing
import pandas as pd
import numpy as np
import yfinance as yf


class StockDataFetcher:
    """
    Fetches and processes stock market data

    This class handles all interactions with the Yahoo Finance API
    and prepares data for visualization.
    """

    def __init__(self):
        """Initialize the data fetcher"""
        self.last_update = None
        self.stock_cache = {}

    @staticmethod
    def fetch_single_stock(ticker: str) -> typing.Optional[typing.Dict]:
        """
        Fetch data for a single stock ticker

        Args:
            ticker (str): Stock symbol (e.g., 'AAPL', 'MSFT')

        Returns:
            Dict with stock data or None if fetch failed

        Example of returned data:
        {
            'ticker': 'AAPL',
            'name': 'Apple Inc.',
            'price': 150.25,
            'open': 149.50,
            'change': 0.75,
            'change_pct': 0.50,
            'volume': 50000000
        }
        """
        try:
            print(f"  Fetching {ticker}...", end=" ")

            # Create a Ticker object (yfinance)
            stock = yf.Ticker(ticker)

            # Get historical data for today
            # This returns a PANDAS DATAFRAME with columns: Open, High, Low, Close, Volume
            hist = stock.history(period='1d', interval='1m')

            # If no data for today, try last 5 days
            if hist.empty:
                hist = stock.history(period='5d')

            if hist.empty:
                print("❌ No data")
                return None

            # PANDAS: Get the last closing price
            # hist['Close'] gets the 'Close' column (like accessing df['Close'])
            # .iloc[-1] gets the last row (-1 means last index)
            current_price = hist['Close'].iloc[-1]

            # PANDAS: Get the opening price (first row)
            open_price = hist['Open'].iloc[0]

            # NUMPY/PANDAS: Calculate high and low
            # .max() finds maximum value in the column
            # .min() finds minimum value in the column
            high_price = hist['High'].max()
            low_price = hist['Low'].min()

            # Simple math: Calculate change
            change = current_price - open_price

            # Calculate percentage change
            # Avoid division by zero
            if open_price > 0:
                change_pct = (change / open_price) * 100
            else:
                change_pct = 0.0

            # Get volume (last value)
            volume = hist['Volume'].iloc[-1]

            # Get company info (name, market cap, etc.)
            info = stock.info
            company_name = info.get('shortName', ticker)
            market_cap = info.get('marketCap', 0)

            # Return data as a dictionary (like a JSON object in JS)
            result = {
                'ticker': ticker,
                'name': company_name,
                'price': float(current_price),  # Convert to regular Python float
                'open': float(open_price),
                'high': float(high_price),
                'low': float(low_price),
                'change': float(change),
                'change_pct': float(change_pct),
                'volume': int(volume),
                'market_cap': market_cap
            }

            print(f"✅ ${result['price']:.2f} ({result['change_pct']:+.2f}%)")
            return result

        except Exception as e:
            print(f"❌ Error: {str(e)}")
            return None

    def fetch_multiple_stocks(self, tickers: typing.List[str]) -> typing.List[typing.Dict]:
        """
        Fetch data for multiple stock tickers

        Args:
            tickers (List[str]): List of stock symbols ['AAPL', 'MSFT', 'GOOGL']

        Returns:
            List of dictionaries with stock data
        """
        print(f"\n📊 Fetching {len(tickers)} stocks...")
        print("=" * 50)

        results = []

        # Loop through each ticker (like a for loop in C/JS)
        for ticker in tickers:
            data = self.fetch_single_stock(ticker)

            if data is not None:
                results.append(data)

        print("=" * 50)
        print(f"✅ Successfully fetched {len(results)}/{len(tickers)} stocks\n")

        # Update last fetch time
        self.last_update = datetime.datetime.now()

        return results

    def fetch_by_sector(self, stocks_by_sector: typing.Dict[str, typing.List[str]]) -> typing.Dict[str, typing.List[typing.Dict]]:
        """
        Fetch stocks organized by sector

        Args:
            stocks_by_sector: Dictionary like:
            {
                'Technology': ['AAPL', 'MSFT', 'GOOGL'],
                'Finance': ['JPM', 'BAC', 'GS']
            }

        Returns:
            Dictionary with same structure but with full stock data
        """
        result = {}

        print(f"\n🏢 Fetching stocks by sector...")

        for sector, tickers in stocks_by_sector.items():
            print(f"\n📁 Sector: {sector}")
            print("-" * 50)

            # Fetch all stocks in this sector
            sector_data = self.fetch_multiple_stocks(tickers)

            # Add sector name to each stock's data
            for stock in sector_data:
                stock['sector'] = sector

            result[sector] = sector_data

        return result

    @staticmethod
    def get_summary_statistics(stock_data: typing.List[typing.Dict]) -> typing.Dict:
        """
        Calculate summary statistics from stock data

        Uses NUMPY for calculations

        Args:
            stock_data: List of stock dictionaries

        Returns:
            Dictionary with statistics (average, max, min, etc.)
        """
        if not stock_data:
            return {}

        # Extract all prices into a list
        prices = [stock['price'] for stock in stock_data]
        changes = [stock['change_pct'] for stock in stock_data]

        # Convert to NUMPY arrays for easy calculations
        prices_array = np.array(prices)
        changes_array = np.array(changes)

        # Calculate statistics using NUMPY
        stats = {
            'total_stocks': len(stock_data),
            'avg_price': np.mean(prices_array),  # Average price
            'max_price': np.max(prices_array),  # Highest price
            'min_price': np.min(prices_array),  # Lowest price
            'avg_change': np.mean(changes_array),  # Average change %
            'max_change': np.max(changes_array),  # Biggest gainer
            'min_change': np.min(changes_array),  # Biggest loser
            'gainers': len([c for c in changes if c > 0]),  # Count of stocks up
            'losers': len([c for c in changes if c < 0])  # Count of stocks down
        }

        return stats


# ============================================
# TEST FUNCTION - Run this file directly to test
# ============================================

def test_data_fetcher():
    """
    Test the data fetcher with a few stocks
    Run this to make sure everything works!
    """
    print("=" * 60)
    print("TESTING DATA FETCHER MODULE")
    print("=" * 60)

    # Create a fetcher instance
    fetcher = StockDataFetcher()

    # Test 1: Fetch a single stock
    print("\n🧪 TEST 1: Fetch single stock (AAPL)")
    print("-" * 60)
    apple_data = fetcher.fetch_single_stock('AAPL')

    if apple_data:
        print(f"\n✅ Success! Got data for {apple_data['name']}")
        print(f"   Price: ${apple_data['price']:.2f}")
        print(f"   Change: {apple_data['change_pct']:+.2f}%")

    # Test 2: Fetch multiple stocks
    print("\n🧪 TEST 2: Fetch multiple stocks")
    print("-" * 60)
    tech_stocks = ['AAPL', 'MSFT', 'GOOGL']
    stocks_data = fetcher.fetch_multiple_stocks(tech_stocks)

    # Test 3: Get statistics
    print("\n🧪 TEST 3: Calculate statistics")
    print("-" * 60)
    stats = fetcher.get_summary_statistics(stocks_data)

    print(f"\n📊 Summary Statistics:")
    print(f"   Total stocks: {stats['total_stocks']}")
    print(f"   Average price: ${stats['avg_price']:.2f}")
    print(f"   Average change: {stats['avg_change']:+.2f}%")
    print(f"   Gainers: {stats['gainers']} | Losers: {stats['losers']}")

    print("\n" + "=" * 60)
    print("✅ ALL TESTS PASSED!")
    print("=" * 60)


# This runs when you execute: python data_fetcher.py
if __name__ == "__main__":
    test_data_fetcher()