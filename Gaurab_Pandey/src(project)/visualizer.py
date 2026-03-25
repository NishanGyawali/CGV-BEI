"""
visualizer.py
Creates 3D visualizations of stock market data

This module handles:
1. Creating 3D bar charts
2. Color mapping (Red -> Yellow -> Green)
3. Interactive camera controls
4. Hover tooltips with stock information
"""

import plotly.graph_objects as go
import numpy as np
from typing import Dict, List
from datetime import datetime


class StockVisualizer:
    """
    Creates interactive 3D visualizations of stock data

    Converts stock data into beautiful 3D graphics using Plotly
    """

    def __init__(self, sector_spacing=3.0, stock_spacing=1.0, enable_animations=True):
        """
        Initialize the visualizer

        Args:
            sector_spacing: Distance between sectors on X-axis
            stock_spacing: Distance between stocks on Y-axis
            enable_animations: Enable smooth animations and transitions
        """
        self.sector_spacing = sector_spacing
        self.stock_spacing = stock_spacing
        self.enable_animations = enable_animations
        self.fig = None

    @staticmethod
    def calculate_color(change_pct: float) -> str:
        """
        Map percentage change to RGB color

        Color gradient:
        -5% or less  → Pure Red    (255, 0, 0)
        0%           → Yellow      (255, 255, 0)
        +5% or more  → Pure Green  (0, 255, 0)

        Args:
            change_pct: Percentage change (e.g., 2.5 for +2.5%)

        Returns:
            RGB color string like 'rgb(255, 128, 0)'
        """
        # Clamp the value between -5 and +5 for color mapping
        # This prevents extreme values from breaking the gradient
        clamped = max(-5.0, min(5.0, change_pct))

        # Normalize to 0-1 range
        # -5% becomes 0, 0% becomes 0.5, +5% becomes 1
        normalized = (clamped + 5) / 10

        # Calculate RGB values
        if normalized < 0.5:
            # Red to Yellow gradient (losses to neutral)
            r = 1.0  # Red stays at 100%
            g = normalized * 2  # Green increases from 0% to 100%
            b = 0.0  # Blue stays at 0%
        else:
            # Yellow to Green gradient (neutral to gains)
            r = 1.0 - (normalized - 0.5) * 2  # Red decreases from 100% to 0%
            g = 1.0  # Green stays at 100%
            b = 0.0  # Blue stays at 0%

        # Convert to 0-255 range and return as RGB string
        return f'rgb({int(r * 255)}, {int(g * 255)}, {int(b * 255)})'

    def create_3d_bars(self, stock_data: Dict[str, List[Dict]]) -> go.Figure:
        """
        Create 3D bar chart visualization

        Args:
            stock_data: Dictionary organized by sector
            Example:
            {
                'Technology': [
                    {'ticker': 'AAPL', 'price': 150.5, 'change_pct': 1.2, ...},
                    {'ticker': 'MSFT', 'price': 380.2, 'change_pct': -0.5, ...}
                ],
                'Finance': [...]
            }

        Returns:
            Plotly Figure object with 3D visualization
        """
        print("\n🎨 Creating 3D visualization...")

        # Lists to store all the 3D positions and properties
        x_positions = []  # X coordinate (sector position)
        y_positions = []  # Y coordinate (stock index within sector)
        z_heights = []  # Z coordinate (stock price)
        colors = []  # Color for each bar
        hover_texts = []  # Tooltip text for each stock
        ticker_labels = []  # Stock ticker symbols

        # Track sector positions for axis labels
        sector_labels = []
        sector_positions = []

        # Process each sector
        sector_idx = 0
        for sector, stocks in stock_data.items():
            # Remember this sector's position for labels
            sector_labels.append(sector)
            sector_positions.append(sector_idx * self.sector_spacing)

            # Process each stock in this sector
            stock_idx = 0
            for stock in stocks:
                # Calculate 3D position
                x = sector_idx * self.sector_spacing
                y = stock_idx * self.stock_spacing
                z = stock['price']

                # Store positions
                x_positions.append(x)
                y_positions.append(y)
                z_heights.append(z)

                # Calculate color based on percentage change
                color = self.calculate_color(stock['change_pct'])
                colors.append(color)

                # Store ticker for labels
                ticker_labels.append(stock['ticker'])

                # Create hover tooltip with detailed information
                hover_text = (
                    f"<b>{stock['ticker']}</b> - {stock['name']}<br>"
                    f"<b>Price:</b> ${stock['price']:.2f}<br>"
                    f"<b>Change:</b> ${stock['change']:.2f} "
                    f"({stock['change_pct']:+.2f}%)<br>"
                    f"<b>Day Range:</b> ${stock['low']:.2f} - ${stock['high']:.2f}<br>"
                    f"<b>Volume:</b> {stock['volume']:,}<br>"
                    f"<b>Sector:</b> {sector}"
                )
                hover_texts.append(hover_text)

                stock_idx += 1

            sector_idx += 1

        print(f"  📍 Positioned {len(x_positions)} stocks in 3D space")

        # Create the Plotly figure
        self.fig = go.Figure()

        # Add marker points at the top of each bar with enhanced styling
        self.fig.add_trace(go.Scatter3d(
            x=x_positions,
            y=y_positions,
            z=z_heights,
            mode='markers+text',
            marker=dict(
                size=16,  # slightly bigger
                color=colors,
                opacity=0.95,
                line=dict(color='white', width=1.5),  # cleaner border
                symbol='circle',
            ),
            text=ticker_labels,
            textposition='top center',
            textfont=dict(size=9, color='black', family='Arial Black'),
            hovertext=hover_texts,
            hovertemplate='%{hovertext}<extra></extra>',
            name='Stocks',
            # Add hover animation
            hoverlabel=dict(
                bgcolor='white',
                font_size=12,
                font_family='Arial'
            )
        ))

        print(f"  ✅ Added {len(x_positions)} stock markers")

        # Add vertical bars (stems) from ground to each marker with gradient
        for i in range(len(x_positions)):
            # Add slight transparency gradient from bottom to top
            self.fig.add_trace(go.Scatter3d(
                x=[x_positions[i], x_positions[i]],
                y=[y_positions[i], y_positions[i]],
                z=[0, z_heights[i]],
                mode='lines',
                line=dict(
                    color=colors[i],
                    width=12,
                    # Add depth with opacity
                ),
                opacity=0.85,
                showlegend=False,
                hoverinfo='skip'
            ))

        print(f"  ✅ Added {len(x_positions)} vertical bars")

        # Configure the 3D scene layout
        self.fig.update_layout(
            title=dict(
                text=f'<b>Real-Time 3D Stock Market Visualizer</b><br>'
                     f'<sub>Updated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</sub>',
                x=0.5,
                xanchor='center',
                font=dict(size=20)
            ),
            scene=dict(
                xaxis=dict(
                    title='<b>Sector</b>',
                    ticktext=sector_labels,
                    tickvals=sector_positions,
                    backgroundcolor='rgb(240, 240, 245)',
                    gridcolor='white',
                    showgrid=True
                ),
                yaxis=dict(
                    title='<b>Stock Index</b>',
                    backgroundcolor='rgb(240, 240, 245)',
                    gridcolor='white',
                    showgrid=True
                ),
                zaxis=dict(
                    title='<b>Price ($)</b>',
                    backgroundcolor='rgb(240, 240, 245)',
                    gridcolor='white',
                    showgrid=True
                ),
                camera=dict(
                    eye=dict(x=1.8, y=1.8, z=1.3)
                )
            ),
            height=800,
            showlegend=False,
            hovermode='closest',
            paper_bgcolor='rgb(250, 250, 250)',
            plot_bgcolor='rgb(250, 250, 250)'
        )

        print("  ✅ Configured 3D scene and layout")
        print("🎨 Visualization complete!\n")

        return self.fig

    def show(self):
        """Display the visualization in a browser window"""
        if self.fig is None:
            print("❌ No visualization to show. Create one first!")
            return

        print("🌐 Opening visualization in browser...")
        self.fig.show()

    def save_html(self, filename: str):
        """
        Save the visualization as an HTML file

        Args:
            filename: Output filename (e.g., 'stock_viz.html')
        """
        if self.fig is None:
            print("❌ No visualization to save. Create one first!")
            return

        self.fig.write_html(filename)
        print(f"💾 Saved visualization to {filename}")

    def create_heatmap(self, stock_data: Dict[str, List[Dict]]) -> go.Figure:
        """
        Create 3D heat map visualization

        Each stock is a colored tile in a grid, arranged by sector.
        Color intensity shows percentage change.
        Height shows stock price.

        Args:
            stock_data: Dictionary organized by sector

        Returns:
            Plotly Figure with 3D heat map
        """
        print("\n🌡️ Creating 3D heat map...")

        # Prepare data for heatmap bars
        x_positions = []
        y_positions = []
        z_heights = []
        colors = []
        hover_texts = []
        ticker_labels = []

        sector_labels = []
        sector_positions = []

        sector_idx = 0
        for sector, stocks in stock_data.items():
            sector_labels.append(sector)
            sector_positions.append(sector_idx * self.sector_spacing + self.sector_spacing / 2)

            stock_idx = 0
            for stock in stocks:
                x = sector_idx * self.sector_spacing
                y = stock_idx * self.stock_spacing
                z = stock['price']

                x_positions.append(x)
                y_positions.append(y)
                z_heights.append(z)

                # Color based on percentage - more intense for bigger changes
                colors.append(self.calculate_color(stock['change_pct']))
                ticker_labels.append(stock['ticker'])

                hover_text = (
                    f"<b>{stock['ticker']}</b> - {stock['name']}<br>"
                    f"<b>Sector:</b> {sector}<br>"
                    f"<b>Price:</b> ${stock['price']:.2f}<br>"
                    f"<b>Change:</b> ${stock['change']:.2f} ({stock['change_pct']:+.2f}%)<br>"
                    f"<b>Volume:</b> {stock['volume']:,}"
                )
                hover_texts.append(hover_text)

                stock_idx += 1

            sector_idx += 1

        print(f"  📊 Created heat map with {len(x_positions)} tiles")

        # Create figure
        self.fig = go.Figure()

        # Add 3D bars that look like heat map tiles
        bar_width = 0.8
        for i in range(len(x_positions)):
            # Create a cube/box for each stock
            self.fig.add_trace(go.Mesh3d(
                x=[x_positions[i] - bar_width / 2, x_positions[i] + bar_width / 2,
                   x_positions[i] + bar_width / 2, x_positions[i] - bar_width / 2,
                   x_positions[i] - bar_width / 2, x_positions[i] + bar_width / 2,
                   x_positions[i] + bar_width / 2, x_positions[i] - bar_width / 2],
                y=[y_positions[i] - bar_width / 2, y_positions[i] - bar_width / 2,
                   y_positions[i] + bar_width / 2, y_positions[i] + bar_width / 2,
                   y_positions[i] - bar_width / 2, y_positions[i] - bar_width / 2,
                   y_positions[i] + bar_width / 2, y_positions[i] + bar_width / 2],
                z=[0, 0, 0, 0, z_heights[i], z_heights[i], z_heights[i], z_heights[i]],
                i=[0, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
                j=[1, 2, 3, 4, 5, 6, 5, 2, 0, 1, 6, 3],
                k=[2, 3, 0, 5, 6, 7, 1, 1, 5, 5, 7, 6],
                color=colors[i],
                opacity=0.95,
                showlegend=False,
                hovertext=hover_texts[i],
                hoverinfo='text'
            ))

        # Configure layout with smooth animations
        self.fig.update_layout(
            title=dict(
                text=f'<b>3D Heat Map View</b><br><sub>Color Intensity = Performance | Height = Price</sub>',
                x=0.5,
                xanchor='center',
                font=dict(size=20)
            ),
            scene=dict(
                xaxis=dict(
                    title='<b>Sector</b>',
                    ticktext=sector_labels,
                    tickvals=sector_positions,
                    backgroundcolor='rgb(240, 240, 245)',
                    gridcolor='white'
                ),
                yaxis=dict(
                    title='<b>Stock Index</b>',
                    backgroundcolor='rgb(240, 240, 245)',
                    gridcolor='white'
                ),
                zaxis=dict(
                    title='<b>Price ($)</b>',
                    backgroundcolor='rgb(240, 240, 245)',
                    gridcolor='white'
                ),
                camera=dict(eye=dict(x=1.8, y=1.8, z=1.3))
            ),
            height=800,
            showlegend=False,
            hovermode='closest',
            paper_bgcolor='rgb(250, 250, 250)',
            # Add smooth transitions
            transition=dict(
                duration=500,
                easing='cubic-in-out'
            ) if self.enable_animations else None
        )

        print("  ✅ Heat map complete!\n")
        return self.fig

    def create_bubble_chart(self, stock_data: Dict[str, List[Dict]]) -> go.Figure:
        """
        Create 3D bubble chart visualization

        Each stock is a bubble where:
        - X position = sector
        - Y position = percentage change
        - Z position = price
        - Bubble size = market capitalization

        Args:
            stock_data: Dictionary organized by sector

        Returns:
            Plotly Figure with 3D scatter plot
        """
        print("\n🫧 Creating 3D bubble chart...")

        x_positions = []
        y_positions = []
        z_heights = []
        sizes = []
        colors = []
        hover_texts = []

        sector_idx = 0
        sector_labels = []
        sector_positions = []

        for sector, stocks in stock_data.items():
            sector_labels.append(sector)
            sector_positions.append(sector_idx)

            for stock in stocks:
                x_positions.append(sector_idx)
                y_positions.append(stock['change_pct'])
                z_heights.append(stock['price'])

                # Size based on market cap (logarithmic scale)
                if stock['market_cap'] > 0:
                    size = np.log10(stock['market_cap']) * 3
                else:
                    size = 10
                sizes.append(size)

                # Color based on change
                colors.append(self.calculate_color(stock['change_pct']))

                hover_text = (
                    f"<b>{stock['ticker']}</b> - {stock['name']}<br>"
                    f"<b>Price:</b> ${stock['price']:.2f}<br>"
                    f"<b>Change:</b> {stock['change_pct']:+.2f}%<br>"
                    f"<b>Market Cap:</b> ${stock['market_cap']:,.0f}<br>"
                    f"<b>Sector:</b> {sector}"
                )
                hover_texts.append(hover_text)

            sector_idx += 1

        print(f"  ✅ Created {len(x_positions)} bubbles")

        # Create bubble chart with enhanced visuals
        self.fig = go.Figure(data=[go.Scatter3d(
            x=x_positions,
            y=y_positions,
            z=z_heights,
            mode='markers',
            marker=dict(
                size=sizes,
                color=colors,
                opacity=0.85,
                line=dict(color='rgba(0, 0, 0, 0.2)', width=1),
                # Add lighting effect
                symbol='circle'
            ),
            text=hover_texts,
            hovertemplate='%{text}<extra></extra>',
            hoverlabel=dict(
                bgcolor='white',
                font_size=12
            )
        )])

        # Configure layout with smooth transitions
        self.fig.update_layout(
            title=dict(
                text='<b>3D Bubble Chart</b><br><sub>Bubble Size = Market Capitalization</sub>',
                x=0.5,
                xanchor='center',
                font=dict(size=20)
            ),
            scene=dict(
                xaxis=dict(
                    title='Sector',
                    ticktext=sector_labels,
                    tickvals=sector_positions,
                    backgroundcolor='rgb(230, 230, 230)'
                ),
                yaxis=dict(
                    title='Change %',
                    backgroundcolor='rgb(230, 230, 230)'
                ),
                zaxis=dict(
                    title='Price ($)',
                    backgroundcolor='rgb(230, 230, 230)'
                ),
                camera=dict(eye=dict(x=1.5, y=1.5, z=1.2))
            ),
            height=800,
            # Add smooth transitions
            transition=dict(
                duration=500,
                easing='cubic-in-out'
            ) if self.enable_animations else None
        )

        print("  ✅ Bubble chart complete!\n")
        return self.fig


# ============================================
# TEST FUNCTION
# ============================================

def test_visualizer():
    """Test the visualizer with sample data"""
    print("=" * 60)
    print("TESTING VISUALIZER MODULE")
    print("=" * 60)

    # Create sample stock data
    sample_data = {
        'Technology': [
            {
                'ticker': 'AAPL', 'name': 'Apple Inc.',
                'price': 150.25, 'open': 149.5, 'high': 151.0, 'low': 149.0,
                'change': 0.75, 'change_pct': 0.50, 'volume': 50000000
            },
            {
                'ticker': 'MSFT', 'name': 'Microsoft Corp',
                'price': 380.50, 'open': 378.0, 'high': 382.0, 'low': 377.5,
                'change': 2.50, 'change_pct': 0.66, 'volume': 30000000
            }
        ],
        'Finance': [
            {
                'ticker': 'JPM', 'name': 'JPMorgan Chase',
                'price': 155.75, 'open': 157.0, 'high': 157.5, 'low': 155.0,
                'change': -1.25, 'change_pct': -0.80, 'volume': 20000000
            }
        ]
    }

    # Create visualizer
    viz = StockVisualizer()

    # Test color calculation
    print("\n🎨 Testing color calculation:")
    print(f"  +5%: {viz.calculate_color(5.0)}")
    print(f"   0%: {viz.calculate_color(0.0)}")
    print(f"  -5%: {viz.calculate_color(-5.0)}")

    # Create visualization
    print("\n📊 Creating 3D visualization...")
    viz.create_3d_bars(sample_data)

    # Show it
    viz.show()

    print("\n" + "=" * 60)
    print("✅ TEST COMPLETE - Check your browser!")
    print("=" * 60)


if __name__ == "__main__":
    test_visualizer()