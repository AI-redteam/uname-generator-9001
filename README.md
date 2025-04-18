# uname-generator-9001

# Username Generator for Penetration Testing

A Python tool that generates potential usernames based on common username formats from first and last names. Designed to aid in penetration testing and security assessments by creating username lists for credential testing.

## Features

- Generate usernames using 14 common username formats
- Create potential email addresses with custom domains
- Control output size with maximum limit option
- Random or deterministic output ordering
- Verbose mode for detailed operation information
- Flexible input via text files
- Output to file or stdout

## Installation

Clone this repository:

```bash
git clone https://github.com/yourusername/username-generator.git
cd username-generator
```

No additional dependencies are required beyond Python 3.

## Usage

Basic usage:

```bash
python username_generator.py -f first_names.txt -l last_names.txt
```

### Command Line Options

| Option | Long Form | Description |
|--------|-----------|-------------|
| `-f FILE` | `--first FILE` | File containing first names (one per line) |
| `-l FILE` | `--last FILE` | File containing last names (one per line) |
| `-o FILE` | `--output FILE` | Output file (default: stdout) |
| `-d DOMAIN` | `--domain DOMAIN` | Domain for email format (e.g., example.com) |
| `-e` | `--email` | Format output as email addresses |
| `-v` | `--verbose` | Show additional information |
| `-r` | `--no-random` | Disable randomization of output |
| `-m LIMIT` | `--max LIMIT` | Maximum number of usernames to generate |

### Examples

Generate usernames and output to console:
```bash
python username_generator.py -f first_names.txt -l last_names.txt
```

Generate email addresses with a specific domain:
```bash
python username_generator.py -f first_names.txt -l last_names.txt -e -d example.com
```

Generate a maximum of 100 usernames and save to a file:
```bash
python username_generator.py -f first_names.txt -l last_names.txt -m 100 -o usernames.txt
```

Generate usernames with detailed information displayed:
```bash
python username_generator.py -f first_names.txt -l last_names.txt -v
```

## Username Formats

The tool generates usernames in the following formats:

1. `firstname.lastname` (e.g., john.doe)
2. `firstnamelastname` (e.g., johndoe)
3. `flastname` (e.g., jdoe)
4. `firstnamel` (e.g., johnd)
5. `f.lastname` (e.g., j.doe)
6. `lastname.firstname` (e.g., doe.john)
7. `lastnamefirstname` (e.g., doejohn)
8. `lfirstname` (e.g., djohn)
9. `firstname_lastname` (e.g., john_doe)
10. `f_lastname` (e.g., j_doe)
11. `lastname_firstname` (e.g., doe_john)
12. `firstnamelast3` (e.g., johndoe)
13. `first3lastname` (e.g., johdoe)
14. `first3last3` (e.g., johdoe)

## Input File Format

Input files should contain one name per line:

```
# first_names.txt
John
Jane
Michael
Emma

# last_names.txt
Smith
Doe
Johnson
Williams
```

## Use Cases

- Security assessments and penetration testing
- User enumeration during security audits
- Password spraying testing
- Creating wordlists for authorized security testing

## Security and Ethical Use

This tool is intended for legitimate security testing with proper authorization. Never use this tool against systems without explicit permission. Unauthorized testing may violate computer fraud and abuse laws.

## License

[MIT License](LICENSE)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request
