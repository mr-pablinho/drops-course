"""
Regenerate all data/samples/ files from live sources.

Run this manually ~quarterly or when a dataset's schema/API changes.
Each output is a small Parquet file (<5 MB) committed to the repo.
These files are used by notebooks when HYDRO_ML_CI=1.

Usage:
    python scripts/refresh_samples.py

Requirements: dataretrieval, pandas, gcsfs, xarray
"""

from pathlib import Path
import pandas as pd

SAMPLES_DIR = Path(__file__).parent.parent / "data" / "samples"
SAMPLES_DIR.mkdir(parents=True, exist_ok=True)


def fetch_usgs_daily(site: str, start: str, end: str, out_name: str):
    """Fetch USGS daily streamflow and save to Parquet."""
    try:
        import dataretrieval.nwis as nwis
        df, _ = nwis.get_dv(sites=site, parameterCd="00060", start=start, end=end)
        df = df.reset_index()
        out = SAMPLES_DIR / out_name
        df.to_parquet(out, index=False)
        print(f"  Saved {out} ({len(df)} rows, {out.stat().st_size / 1024:.1f} KB)")
    except Exception as e:
        print(f"  FAILED {out_name}: {e}")


def fetch_usgs_groundwater(site: str, start: str, end: str, out_name: str):
    """Fetch USGS groundwater levels and save to Parquet."""
    try:
        import dataretrieval.nwis as nwis
        df, _ = nwis.get_gwlevels(sites=site, start=start, end=end)
        df = df.reset_index()
        out = SAMPLES_DIR / out_name
        df.to_parquet(out, index=False)
        print(f"  Saved {out} ({len(df)} rows, {out.stat().st_size / 1024:.1f} KB)")
    except Exception as e:
        print(f"  FAILED {out_name}: {e}")


def main():
    print("Refreshing data samples...\n")

    print("USGS streamflow samples:")

    # Module 1 (01-colab-intro): Missouri River at Omaha — 2000-2015 includes 2011 flood
    fetch_usgs_daily(
        site="06803495",
        start="2000-01-01",
        end="2015-12-31",
        out_name="usgs_06803495_daily_2000_2015.parquet",
    )

    # Module 2 (01-usgs-nwis): same gauge, shorter window for data-sources lesson
    fetch_usgs_daily(
        site="06803495",
        start="2000-01-01",
        end="2010-12-31",
        out_name="usgs_06803495_daily_2000_2010.parquet",
    )

    # Module 3/4: Additional gauge for comparison (American River at Fair Oaks)
    fetch_usgs_daily(
        site="11446500",
        start="2000-01-01",
        end="2010-12-31",
        out_name="usgs_11446500_daily_2000_2010.parquet",
    )

    # Module 7: Groundwater well (Nebraska)
    print("\nUSGS groundwater samples:")
    fetch_usgs_groundwater(
        site="400443096545001",
        start="2000-01-01",
        end="2020-12-31",
        out_name="usgs_gw_400443096545001_2000_2020.parquet",
    )

    # Caravan: small subset of CAMELS-US catchments (pre-downloaded CSV)
    # Note: Caravan is hosted on Zenodo/HydroShare — download once and cache here.
    # This script only handles the USGS API fetches; Caravan samples must be
    # manually refreshed from https://zenodo.org/record/7540792 (see CONTRIBUTING.md).
    print("\nCaravan: manual refresh required (see CONTRIBUTING.md)")

    print("\nDone. Commit the updated data/samples/ directory.")


if __name__ == "__main__":
    main()
