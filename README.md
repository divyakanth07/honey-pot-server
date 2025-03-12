# HoneypotPie

HoneypotPie is a simple honeypot implementation written in Python, designed to simulate a vulnerable system that captures and logs interactions with potential attackers. This project creates a mock shell environment, logs credential attempts, and responds to a limited set of commands (like `ls`, `pwd`, and `whoami`). It's ideal for studying and detecting attack patterns, as well as experimenting with network security.

## Features

- **Simulated Shell Environment:** Emulates a basic Kali Linux shell with a limited set of commands.
- **Credential Logging:** Captures login attempts (username/password pairs) and logs them for further analysis.
- **Command Simulation:** Fake responses are generated for commands like `ls`, `pwd`, and `whoami`.
- **Multi-threaded:** Can handle multiple simultaneous connections using Python's threading module.
- **Logging:** All interactions, including login attempts and commands executed, are logged to a file (`honeypotpiev1.log`).

## Requirements

- Python 3.x
- No external dependencies are required (standard library modules are used).

## How to Run

1. Clone the repository or download the `honeypotpie.py` file.
2. Open a terminal and navigate to the directory containing `honeypotpie.py`.
3. Run the following command to start the honeypot server:

   ```bash
   python honeypotpie.py
   ```

4. The server will start listening on `127.0.0.1` (localhost) on port `12345`.

   - You can connect to it using any telnet or netcat client to simulate an attack. For example:

     ```bash
     nc 127.0.0.1 12345
     ```

## How It Works

- The server listens for incoming connections on `127.0.0.1:12345`.
- When a client connects, it simulates a Kali Linux shell and prompts for a username and password.
- If the username and password contain the word "admin", the client is granted access and can issue a limited set of commands (`ls`, `pwd`, `whoami`).
- Invalid credentials or commands result in an error message.
- All login attempts and executed commands are logged to a file (`honeypotpiev1.log`).

## Commands

- `ls` - Simulated output of directory contents.
- `pwd` - Simulated current directory path.
- `whoami` - Simulated user identity.
- `exit` - Ends the connection.

## Logging

- All connection attempts, including login credentials, are logged into the file `honeypotpiev1.log` located in the same directory as the script.
- Example log entry:
  ```
  2025-03-12 10:30:00:Connection from ('127.0.0.1', 50500) with username: admin and password: admin
  ```

## Customization

- **Port and Host:** You can modify the `host` and `port` variables in the script to change the listening address and port.
- **Command Set:** To add more simulated commands, simply expand the `cmdTerm` function to include new command handling logic.
- **Logging:** Modify the `logging.basicConfig` settings to change the log file format, location, or logging level.

## Security Disclaimer

This honeypot is intended for educational and research purposes only. It is not a fully secured or production-ready system. Use it in a controlled environment where it cannot be used for malicious purposes. Always make sure to understand the legal and ethical implications of using honeypots in your network.

## Contributing

Feel free to fork the repository and submit pull requests. Contributions to improve the honeypot or add additional features are always welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
