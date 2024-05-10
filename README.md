# FTP Brute Force Tool
![carbon](https://github.com/Jon3sjns/FTPBF/assets/45759837/542c82bd-fc20-468f-b47c-10f14a6dfe54)

**FTP Brute Force Tool** is a simple Python script for conducting brute force attacks on FTP services. It allows you to test multiple passwords from a wordlist against an FTP server to attempt to gain access.

## Usage

Ensure you have Python installed on your system. Then, follow the steps below:

1. **Environment Setup:**
   - Make sure you have installed the required `ftplib` module. If not, install it by running the following command in the terminal:
     ```
     pip install ftplib
     ```

2. **Running the Script:**
   - Download this Repository.
   - Open a terminal or command prompt in the directory where the script is saved.
   - Run the script with the following command:
     ```
     python main.py -H [target_host] -u [target_username] -wl [wordlist_path]
     ```
     - `[target_host]`: The target FTP host address.
     - `[target_username]`: The target FTP username.
     - `[wordlist_path]` (optional): The path to the wordlist file containing the list of passwords to be tried. If not provided, the script will use the `wordlist.txt` file in the same directory.

## Example Usage

```
python main.py -H ftp.example.com -u user -wl wordlist.txt
```

## Notes

- This script is created for educational and security testing purposes. Use it wisely and only for testing on systems you have permission to conduct testing on.

- This script uses Python's built-in `argparse` module to handle command-line arguments. Make sure to run the script with the appropriate arguments as described in the "Running the Script" section.

## Contributions

If you find any bugs or have suggestions for improvements, feel free to create an "Issue" or "Pull Request" in this repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for more details.


