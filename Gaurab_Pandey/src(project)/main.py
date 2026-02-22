"""
main.py
Main application - Real-Time 3D Stock Market Visualizer

This brings together:
- data_fetcher.py (gets stock data)
- stock_config.py (stock lists)
- visualizer.py (creates 3D graphics)

Run this to see your complete stock visualizer!
"""

import os

# Fix OpenBLAS memory issue
os.environ['OPENBLAS_NUM_THREADS'] = '1'

from data_fetcher import StockDataFetcher
from stock_config import STOCKS_BY_SECTOR, VISUALIZATION_CONFIG
from visualizer import StockVisualizer
import time
from datetime import datetime


def print_header():
    """Print application header"""
    print("\n" + "=" * 70)
    print(" " * 15 + "REAL-TIME 3D STOCK MARKET VISUALIZER")
    print(" " * 20 + "Computer Graphics Final Project")
    print("=" * 70)


def print_menu():
    """Display main menu options"""
    print("\n📋 MENU:")
    print("=" * 70)
    print("1. Visualize ALL sectors - 3D Bars (40 stocks)")
    print("2. Visualize ALL sectors - Heat Map")
    print("3. Visualize ALL sectors - Bubble Chart")
    print("4. Visualize specific sectors")
    print("5. Quick demo (Technology sector only)")
    print("6. View statistics only")
    print("7. Exit")
    print("=" * 70)


def visualize_3d_bars():
    """Fetch and visualize all stocks from all sectors - 3D Bars"""
    print("\n🌐 FETCHING ALL SECTORS - 3D BARS VIEW")
    print("This will fetch 40 stocks - may take 1-2 minutes...")
    print("-" * 70)

    # Create data fetcher
    fetcher = StockDataFetcher()

    # Fetch all stock data organized by sector
    stock_data = fetcher.fetch_by_sector(STOCKS_BY_SECTOR)

    # Check if we got data
    total_stocks = sum(len(stocks) for stocks in stock_data.values())
    if total_stocks == 0:
        print("❌ Failed to fetch stock data. Check internet connection.")
        return

    print(f"\n✅ Successfully fetched {total_stocks} stocks!")

    # Get statistics
    all_stocks = []
    for sector_stocks in stock_data.values():
        all_stocks.extend(sector_stocks)

    stats = fetcher.get_summary_statistics(all_stocks)
    print_statistics(stats)

    # Create visualization
    print("\n🎨 Creating 3D Bar visualization...")
    viz = StockVisualizer(
        sector_spacing=VISUALIZATION_CONFIG['sector_spacing'],
        stock_spacing=VISUALIZATION_CONFIG['stock_spacing']
    )

    viz.create_3d_bars(stock_data)

    # Save HTML file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"stock_viz_bars_{timestamp}.html"
    viz.save_html(filename)

    # Show in browser
    viz.show()

    print(f"\n✅ Visualization complete!")
    print(f"💾 Saved to: {filename}")


def visualize_heatmap():
    """Fetch and visualize all stocks as 3D heat map"""
    print("\n🌡️ FETCHING ALL SECTORS - HEAT MAP VIEW")
    print("This will fetch 40 stocks - may take 1-2 minutes...")
    print("-" * 70)

    # Create data fetcher
    fetcher = StockDataFetcher()

    # Fetch all stock data
    stock_data = fetcher.fetch_by_sector(STOCKS_BY_SECTOR)

    total_stocks = sum(len(stocks) for stocks in stock_data.values())
    if total_stocks == 0:
        print("❌ Failed to fetch stock data.")
        return

    print(f"\n✅ Successfully fetched {total_stocks} stocks!")

    # Create heat map visualization
    viz = StockVisualizer()
    viz.create_heatmap(stock_data)

    # Save and show
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"stock_viz_heatmap_{timestamp}.html"
    viz.save_html(filename)
    viz.show()

    print(f"\n✅ Visualization complete!")
    print(f"💾 Saved to: {filename}")


def visualize_bubble_chart():
    """Fetch and visualize all stocks as 3D bubble chart"""
    print("\n🫧 FETCHING ALL SECTORS - BUBBLE CHART VIEW")
    print("This will fetch 40 stocks - may take 1-2 minutes...")
    print("-" * 70)

    # Create data fetcher
    fetcher = StockDataFetcher()

    # Fetch all stock data
    stock_data = fetcher.fetch_by_sector(STOCKS_BY_SECTOR)

    total_stocks = sum(len(stocks) for stocks in stock_data.values())
    if total_stocks == 0:
        print("❌ Failed to fetch stock data.")
        return

    print(f"\n✅ Successfully fetched {total_stocks} stocks!")

    # Create bubble chart visualization
    viz = StockVisualizer()
    viz.create_bubble_chart(stock_data)

    # Save and show
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"stock_viz_bubbles_{timestamp}.html"
    viz.save_html(filename)
    viz.show()

    print(f"\n✅ Visualization complete!")
    print(f"💾 Saved to: {filename}")


def visualize_selected_sectors():
    """Let user choose which sectors to visualize"""
    print("\n📂 SELECT SECTORS TO VISUALIZE")
    print("-" * 70)

    sectors = list(STOCKS_BY_SECTOR.keys())

    # Display sectors with numbers
    for i, sector in enumerate(sectors, 1):
        stock_count = len(STOCKS_BY_SECTOR[sector])
        print(f"{i}. {sector} ({stock_count} stocks)")

    print(f"{len(sectors) + 1}. All sectors")

    # Get user choice
    try:
        choice = input("\nEnter sector numbers (comma-separated, e.g., 1,3,5): ").strip()

        if not choice:
            print("❌ No selection made.")
            return

        # Parse choices
        if choice == str(len(sectors) + 1):
            selected_sectors = sectors
        else:
            indices = [int(x.strip()) - 1 for x in choice.split(',')]
            selected_sectors = [sectors[i] for i in indices if 0 <= i < len(sectors)]

        if not selected_sectors:
            print("❌ Invalid selection.")
            return

        print(f"\n✅ Selected: {', '.join(selected_sectors)}")

        # Create filtered stock dictionary
        filtered_stocks = {
            sector: STOCKS_BY_SECTOR[sector]
            for sector in selected_sectors
        }

        # Fetch data
        fetcher = StockDataFetcher()
        stock_data = fetcher.fetch_by_sector(filtered_stocks)

        # Create visualization
        viz = StockVisualizer()
        viz.create_3d_bars(stock_data)

        # Save and show
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"stock_viz_custom_{timestamp}.html"
        viz.save_html(filename)
        viz.show()

        print(f"\n✅ Visualization complete!")
        print(f"💾 Saved to: {filename}")

    except (ValueError, IndexError):
        print("❌ Invalid input. Please enter numbers separated by commas.")
    except KeyboardInterrupt:
        print("\n❌ Cancelled by user.")


def quick_demo():
    """Quick demo with just Technology sector"""
    print("\n⚡ QUICK DEMO - Technology Sector")
    print("-" * 70)

    tech_stocks = {'Technology': STOCKS_BY_SECTOR['Technology']}

    fetcher = StockDataFetcher()
    stock_data = fetcher.fetch_by_sector(tech_stocks)

    if not stock_data.get('Technology'):
        print("❌ Failed to fetch data.")
        return

    print(f"\n✅ Fetched {len(stock_data['Technology'])} tech stocks!")

    viz = StockVisualizer()
    viz.create_3d_bars(stock_data)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"stock_viz_demo_{timestamp}.html"
    viz.save_html(filename)
    viz.show()

    print(f"\n✅ Demo complete!")
    print(f"💾 Saved to: {filename}")


def view_statistics():
    """Fetch data and show statistics without visualization"""
    print("\n📊 FETCHING STATISTICS")
    print("-" * 70)

    fetcher = StockDataFetcher()

    # Ask user which sectors
    print("\n1. All sectors")
    print("2. Technology only (faster)")

    choice = input("\nChoice (1 or 2): ").strip()

    if choice == "2":
        stocks_dict = {'Technology': STOCKS_BY_SECTOR['Technology']}
    else:
        stocks_dict = STOCKS_BY_SECTOR

    # Fetch data
    stock_data = fetcher.fetch_by_sector(stocks_dict)

    # Combine all stocks
    all_stocks = []
    for sector_stocks in stock_data.values():
        all_stocks.extend(sector_stocks)

    if not all_stocks:
        print("❌ No data fetched.")
        return

    # Calculate and display statistics
    stats = fetcher.get_summary_statistics(all_stocks)
    print_statistics(stats)

    # Show top gainers and losers
    print_top_movers(all_stocks)


def print_statistics(stats: dict):
    """Print formatted statistics"""
    print("\n" + "=" * 70)
    print(" " * 25 + "📊 MARKET STATISTICS")
    print("=" * 70)
    print(f"Total Stocks:        {stats['total_stocks']}")
    print(f"Average Price:       ${stats['avg_price']:.2f}")
    print(f"Price Range:         ${stats['min_price']:.2f} - ${stats['max_price']:.2f}")
    print(f"Average Change:      {stats['avg_change']:+.2f}%")
    print(f"Best Performance:    {stats['max_change']:+.2f}%")
    print(f"Worst Performance:   {stats['min_change']:+.2f}%")
    print(f"Gainers:             {stats['gainers']} stocks ⬆")
    print(f"Losers:              {stats['losers']} stocks ⬇")
    print("=" * 70)


def print_top_movers(stocks: list):
    """Print top 5 gainers and losers"""
    # Sort by percentage change
    sorted_stocks = sorted(stocks, key=lambda x: x['change_pct'], reverse=True)

    print("\n🚀 TOP 5 GAINERS:")
    print("-" * 70)
    for i, stock in enumerate(sorted_stocks[:5], 1):
        print(f"{i}. {stock['ticker']:6} ${stock['price']:8.2f}  {stock['change_pct']:+6.2f}%  ({stock['name']})")

    print("\n📉 TOP 5 LOSERS:")
    print("-" * 70)
    for i, stock in enumerate(sorted_stocks[-5:], 1):
        print(f"{i}. {stock['ticker']:6} ${stock['price']:8.2f}  {stock['change_pct']:+6.2f}%  ({stock['name']})")


def main():
    """Main application loop"""
    print_header()

    print("\n💡 TIP: This application fetches REAL stock data from Yahoo Finance")
    print("   Fetching may take time depending on your internet connection.")

    while True:
        print_menu()

        try:
            choice = input("\nYour choice (1-7): ").strip()

            if choice == '1':
                visualize_3d_bars()
            elif choice == '2':
                visualize_heatmap()
            elif choice == '3':
                visualize_bubble_chart()
            elif choice == '4':
                visualize_selected_sectors()
            elif choice == '5':
                quick_demo()
            elif choice == '6':
                view_statistics()
            elif choice == '7':
                print("\n👋 Goodbye! Thanks for using the Stock Visualizer!")
                print("=" * 70 + "\n")
                break
            else:
                print("❌ Invalid choice. Please enter 1-7.")

            # Pause before showing menu again
            input("\n⏸  Press Enter to continue...")

        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")
            print("Please try again.")


if __name__ == "__main__":
    main()