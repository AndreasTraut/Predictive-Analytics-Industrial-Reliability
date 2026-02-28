"""
Crane Maintenance Dataset Generator / Kran-Wartungs-Datensatz-Generator

Generates a synthetic predictive maintenance dataset for a crane drive system,
with injected fault patterns suitable for Root Cause Analysis (RCA) and
Predictive Maintenance (PdM) demonstrations.

*Erzeugt einen synthetischen Predictive-Maintenance-Datensatz für einen Kranantrieb
mit eingebetteten Fehlermustern für Root Cause Analysis (RCA) und Predictive
Maintenance (PdM).*
"""

import argparse
import os
from pathlib import Path

import numpy as np
import pandas as pd


def generate_crane_dataset(n_rows: int = 1000, seed: int = 42) -> pd.DataFrame:
    """
    Generate a synthetic crane maintenance dataset with injected fault patterns.

    The dataset simulates sensor readings from a bridge or tower crane hoist
    unit over time.  Three fault classes are embedded:
    - ``E102_Motor_Overheat``: triggered by high load combined with high temperature.
    - ``E505_Bearing_Issue``: triggered by excessive vibration.
    - ``Normal``: all remaining observations.

    Args:
        n_rows: Number of hourly observations to generate.
        seed: Random seed for reproducibility.

    Returns:
        A DataFrame with columns:
        Timestamp, Load_kg, Motor_Temp, Vibration, Brake_Wear, Error_Code.
    """
    np.random.seed(seed)

    data = {
        # Hourly timestamps starting from 2024-01-01
        "Timestamp": pd.date_range(start="2024-01-01", periods=n_rows, freq="h"),
        # Load around 5 tonnes (kg)
        "Load_kg": np.random.normal(5000, 1500, n_rows),
        # Normal motor temperature 60 °C
        "Motor_Temp": np.random.normal(60, 5, n_rows),
        # Normal vibration 2 mm/s
        "Vibration": np.random.normal(2.0, 0.5, n_rows),
        # Brake pad wears from 10 mm down to 2 mm over the observation window
        "Brake_Wear": np.maximum(
            0,
            np.linspace(10, 2, n_rows) + np.random.normal(0, 0.1, n_rows),
        ),
    }

    df = pd.DataFrame(data)

    # Inject fault: high load AND high temperature -> motor overheat
    df.loc[
        (df["Load_kg"] > 8000) & (df["Motor_Temp"] > 70),
        "Error_Code",
    ] = "E102_Motor_Overheat"

    # Inject fault: excessive vibration -> bearing issue
    df.loc[df["Vibration"] > 3.5, "Error_Code"] = "E505_Bearing_Issue"

    # All remaining observations are normal
    df["Error_Code"] = df["Error_Code"].fillna("Normal")

    return df


def main() -> None:
    """Parse CLI arguments and write the dataset to a CSV file."""
    parser = argparse.ArgumentParser(
        description="Generate synthetic crane maintenance dataset."
    )
    parser.add_argument(
        "--output",
        default=str(Path(__file__).parents[1] / "data" / "kran_wartung_daten.csv"),
        help="Output CSV path (default: data/kran_wartung_daten.csv)",
    )
    parser.add_argument(
        "--rows",
        type=int,
        default=1000,
        help="Number of rows to generate (default: 1000)",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Random seed (default: 42)",
    )
    args = parser.parse_args()

    output_path = Path(args.output)
    os.makedirs(output_path.parent, exist_ok=True)

    df = generate_crane_dataset(n_rows=args.rows, seed=args.seed)
    df.to_csv(output_path, index=False)
    print(f"✅ Crane dataset saved to: {output_path}  ({len(df)} rows)")


if __name__ == "__main__":
    main()
