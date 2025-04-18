#!/usr/bin/env python3
"""
Username Generator for Penetration Testing

This script generates a list of potential usernames based on common username formats
from first and last names. It can also format the output as email addresses.

Usage:
    python username_generator.py -f first_names.txt -l last_names.txt [options]

Options:
    -f, --first FILE     File containing first names (one per line)
    -l, --last FILE      File containing last names (one per line)
    -o, --output FILE    Output file (default: stdout)
    -d, --domain DOMAIN  Domain for email format (e.g., example.com)
    -e, --email          Format output as email addresses
    -v, --verbose        Show additional information
    -r, --no-random      Disable randomization of output
    -m, --max LIMIT      Maximum number of usernames to generate
"""

import argparse
import sys
import random
from itertools import product


def read_names_from_file(filename):
    """Read names from a file, one per line."""
    try:
        with open(filename, 'r') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        sys.stderr.write(f"Error: File '{filename}' not found\n")
        sys.exit(1)
    except Exception as e:
        sys.stderr.write(f"Error reading file '{filename}': {e}\n")
        sys.exit(1)


def generate_usernames(first_names, last_names, randomize=True, max_usernames=None):
    """Generate usernames based on common formats."""
    usernames = []
    
    # Create a list of all first/last name combinations
    name_pairs = list(product(first_names, last_names))
    
    # Randomize the order of name pairs if requested
    if randomize:
        random.shuffle(name_pairs)
    
    for first, last in name_pairs:
        # Common username formats
        formats = [
            f"{first.lower()}.{last.lower()}",           # firstname.lastname
            f"{first.lower()}{last.lower()}",            # firstnamelastname
            f"{first[0].lower()}{last.lower()}",         # flastname
            f"{first.lower()}{last[0].lower()}",         # firstnamel
            f"{first[0].lower()}.{last.lower()}",        # f.lastname
            f"{last.lower()}.{first.lower()}",           # lastname.firstname
            f"{last.lower()}{first.lower()}",            # lastnamefirstname
            f"{last[0].lower()}{first.lower()}",         # lfirstname
            f"{first.lower()}_{last.lower()}",           # firstname_lastname
            f"{first[0].lower()}_{last.lower()}",        # f_lastname
            f"{last.lower()}_{first.lower()}",           # lastname_firstname
            f"{first.lower()}{last.lower()[:3]}",        # firstnamelast3
            f"{first[:3].lower()}{last.lower()}",        # first3lastname
            f"{first[:3].lower()}{last[:3].lower()}",    # first3last3
        ]
        
        usernames.extend(formats)
        
        # Check if we've reached the maximum limit
        if max_usernames and len(usernames) >= max_usernames:
            return usernames[:max_usernames]
    
    # Additionally randomize the order of the final username list if requested
    if randomize:
        random.shuffle(usernames)
        # Apply limit after shuffling
        if max_usernames:
            return usernames[:max_usernames]
    
    return usernames


def format_as_emails(usernames, domain):
    """Format usernames as email addresses."""
    return [f"{username}@{domain}" for username in usernames]


def main():
    parser = argparse.ArgumentParser(description="Generate usernames for penetration testing")
    parser.add_argument("-f", "--first", required=True, help="File containing first names")
    parser.add_argument("-l", "--last", required=True, help="File containing last names")
    parser.add_argument("-o", "--output", help="Output file (default: stdout)")
    parser.add_argument("-d", "--domain", help="Domain for email format (e.g., example.com)")
    parser.add_argument("-e", "--email", action="store_true", help="Format output as email addresses")
    parser.add_argument("-v", "--verbose", action="store_true", help="Show additional information")
    parser.add_argument("-r", "--no-random", action="store_true", help="Disable randomization of output")
    parser.add_argument("-m", "--max", type=int, help="Maximum number of usernames to generate")
    
    args = parser.parse_args()
    
    # Read names from files
    first_names = read_names_from_file(args.first)
    last_names = read_names_from_file(args.last)
    
    if args.verbose:
        total_possible = len(first_names) * len(last_names) * 14
        limit_message = f" (limiting to {args.max})" if args.max else ""
        sys.stderr.write(f"Loaded {len(first_names)} first names and {len(last_names)} last names\n")
        sys.stderr.write(f"Could generate up to {total_possible} potential usernames{limit_message}\n")
    
    # Generate usernames (randomized by default unless --no-random is specified)
    usernames = generate_usernames(first_names, last_names, 
                                  randomize=not args.no_random, 
                                  max_usernames=args.max)
    
    # Format as emails if requested
    if args.email:
        if not args.domain:
            sys.stderr.write("Error: Domain is required when using email format\n")
            sys.exit(1)
        usernames = format_as_emails(usernames, args.domain)
    
    # Output results
    if args.output:
        try:
            with open(args.output, 'w') as file:
                for username in usernames:
                    file.write(f"{username}\n")
            if args.verbose:
                sys.stderr.write(f"Wrote {len(usernames)} usernames to {args.output}\n")
        except Exception as e:
            sys.stderr.write(f"Error writing to file '{args.output}': {e}\n")
            sys.exit(1)
    else:
        for username in usernames:
            print(username)
    
    if args.verbose:
        sys.stderr.write(f"Generated {len(usernames)} usernames\n")


if __name__ == "__main__":
    main()
