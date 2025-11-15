#!/usr/bin/env python3
"""
Quick Start Script for Kansas City Data Center Impact Analysis

This script runs the complete analysis pipeline:
1. Generates forecast data
2. Creates visualizations
3. Outputs summary statistics

Usage:
    python run_analysis.py
"""

import sys
import os
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

def main():
    """Run complete analysis pipeline."""
    
    print("="*80)
    print("KANSAS CITY DATA CENTER IMPACT ANALYSIS")
    print("Machine Learning Forecasting Models (2025-2035)")
    print("="*80)
    print()
    
    # Step 1: Run ML models
    print("STEP 1: Running ML forecasting models...")
    print("-"*80)
    try:
        from src import kc_ml_models
        print("✓ ML models executed successfully")
        print()
    except Exception as e:
        print(f"✗ Error running ML models: {e}")
        return 1
    
    # Step 2: Generate visualizations
    print("STEP 2: Generating visualizations...")
    print("-"*80)
    try:
        from src import create_visualizations
        print("✓ Visualizations created successfully")
        print()
    except Exception as e:
        print(f"✗ Error creating visualizations: {e}")
        return 1
    
    # Step 3: Display summary
    print("="*80)
    print("ANALYSIS COMPLETE!")
    print("="*80)
    print()
    print("Generated files:")
    print("  • data/kc_datacenter_forecast.csv - Complete forecast dataset")
    print("  • data/kc_datacenter_summary.csv - Key metrics summary")
    print("  • outputs/charts/*.jpg - High-resolution visualizations")
    print()
    print("Next steps:")
    print("  1. Review outputs/charts/ for visualizations")
    print("  2. Explore data/kc_datacenter_forecast.csv for detailed data")
    print("  3. Read docs/METHODOLOGY.md for technical details")
    print()
    print("For questions or issues:")
    print("  • Open an issue: https://github.com/yourusername/kc-datacenter-impact/issues")
    print("  • Email: [your-email@example.com]")
    print()
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
