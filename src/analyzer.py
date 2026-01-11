#!/usr/bin/env python3
import csv
import argparse
from pathlib import Path
from datetime import datetime

def main():
    parser = argparse.ArgumentParser(
        description="Onchain Wallet Analyzer (starter)"
    )
    parser.add_argument(
        "--wallets",
        default="data/wallets.csv",
        help="CSV file with columns: label,address"
    )
    parser.add_argument(
        "--out",
        default="report",
        help="Output directory"
    )
    args = parser.parse_args()

    wallets_file = Path(args.wallets)
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    if not wallets_file.exists():
        print(f"❌ File not found: {wallets_file}")
        return

    rows = []
    with wallets_file.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append({
                "label": r.get("label", "").strip(),
                "address": r.get("address", "").strip()
            })

    output_file = out_dir / f"wallet_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    with output_file.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["label", "address"])
        writer.writeheader()
        writer.writerows(rows)

    print(f"✅ Report generated: {output_file}")

if __name__ == "__main__":
    main()
