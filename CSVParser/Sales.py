import argparse
import csv
import sys
from statistics import mean, median, mode, StatisticsError

def parse_args():
    parser = argparse.ArgumentParser(
        description="Compute summary statistics (mean, median, mode) for a numeric column in a CSV file."
    )
    
    parser.add_argument(
        "file",
        metavar="FILE",
        help="Path to the input CSV file",
        type=str
    )
    
    parser.add_argument(
        "--column", "-c",
        metavar="COLUMN",
        help="Name of the numeric column to analyze",
        required=True,
        type=str
    )
    
    parser.add_argument(
        "--delimiter", "-d",
        metavar="DELIM",
        help="CSV delimiter (default: comma)",
        default=","
    )
    
    return parser.parse_args()

def read_values(path, column, delimiter):
    values = []
    
    try:
        with open(path, newline="") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=delimiter)
            
            if column not in reader.fieldnames:
                sys.exit(f"Error: Column '{column}' not found in CSV headers: {reader.fieldnames}")
                
            for row in reader:
                try:
                    val = float(row[column])
                except ValueError:
                    continue  # skip non-numeric or missing entries
                    
                values.append(val)
    except FileNotFoundError:
        sys.exit(f"Error: File not found: {path}")
        
    return values

def compute_stats(values):
    if not values:
        sys.exit("Error: No numeric data found to analyze.")
        
    stats = {}
    stats['count'] = len(values)
    stats['mean'] = mean(values)
    stats['median'] = median(values)
    
    try:
        stats['mode'] = mode(values)
    except StatisticsError:
        stats['mode'] = None  # No unique mode
        
    return stats

def main():
    args = parse_args()
    values = read_values(args.file, args.column, args.delimiter)
    stats = compute_stats(values)

    print(f"Summary statistics for column '{args.column}' on file '{args.file}':")
    print(f"  Count : {stats['count']}")
    print(f"  Mean  : {stats['mean']:.2f}")
    print(f"  Median: {stats['median']:.2f}")
    
    if stats['mode'] is not None:
        print(f"  Mode  : {stats['mode']:.2f}")
    else:
        print("  Mode  : None (no unique mode)")

if __name__ == '__main__':
    main()