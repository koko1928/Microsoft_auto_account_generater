
# Outlook Account Generator

                     ........
                ..gMMMMMMMMMMMMNJ,
              .MMMMMMMMMMMMMMMMMMMN,
             jMMMMMMMMMMMMMMMMMMMMMMN.
            JMMMMMMMMMMMMMMMMMMMMMMMMb
       `  ` MMMMMMMMMMMMMMMMMMMMMMMMMN    `  `
    `       MMMMMMMMMMMMMMMMMMMMMMMMM#
            ,MMMMM"""HMMMMMMM"""MMMMM%          `
             vM#`      vMMF       MMF       `
              Wb       (MMb       J#     `
    `  `      .Na.   .MMMMMN,    .N]
          `   MMMMMMMMMM=?MMMMMMMMMN          `
        ..    MMMMMMMMM'.,.MMMMMMMMM`   ..
   `  .MMMMh       MMMMMMMMMMMM.      JMMMMp
      dMMMMM,     ,MMMMMMMMMMMM\     .MMMMM#  `
    .MMMMMMMMMa,.  .7"WMMMMY""!  ..gMMMMMMMMN,
    JMMMMMMMMMMMMMNJ,        ..gMMMMMMMMMMMMMF
     ?WMM"?THMMMMMMMMMNa,.(MMMMMMMMMMM"=?MMB=
               7TMMMMMMMMMMMMMMMMB"`
                ..dMMMMMMMMMMMMNJ,
     .(g&, ..+MMMMMMMMMM#WMMMMMMMMMNg,. ..g&,
    .MMMMMMMMMMMMMMMB"`     ?YMMMMMMMMMMMMMMM[
    (MMMMMMMMMMM"^              ?TMMMMMMMMMMMF
      MMMMMM"!                      _TMMMMM#
      dMMMM#                          WMMMMF
       (""!                            .7"^

### Overview:

The **Outlook Account Generator** is a tool created by koko1928 for automating the generation of Microsoft accounts. It requires the pre-installation of Google Chrome.

### Key Features:

1. **Google Chrome Installation:**
   - Ensure Google Chrome is installed, as the tool uses the Google Chrome WebDriver.

2. **Headless Mode:**
   - Operates in headless mode using Selenium's Chrome WebDriver for automated, GUI-less execution.

3. **Random Username and Password Generation:**
   - Utilizes `random.choices` to generate random strings for both usernames and passwords.

4. **Thread-Safe Account Index:**
   - Manages the account index in a thread-safe manner using `threading.Lock`.

5. **Error Handling:**
   - Provides detailed error messages for exceptions that may occur during execution.

### Usage:

1. Run the program and input the desired number of accounts to create (between 1 and 3).
2. The tool will automatically generate the specified accounts and save the usernames and passwords to separate files.

### Instructions:

- Make sure Google Chrome is installed on your system.
- Execute the script, follow the prompt to input the number of accounts, and let the tool handle the rest.

### Disclaimer:

This tool is provided as-is, and the creator (koko1928) is not responsible for any misuse or unintended consequences. Use at your own discretion.

### Contributions:

Contributions and improvements are welcome. Feel free to fork the repository and submit pull requests.

### License:

This project is licensed under the [MIT License](LICENSE).

### Author:

- **koko1928**

### Acknowledgments:

Special thanks to the [Selenium](https://www.selenium.dev/) project for providing the WebDriver library.
