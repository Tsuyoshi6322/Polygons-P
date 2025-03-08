# Fancy ASCII colours for the terminal output

def output_message(message_type, message):
    RESET = '\033[0m'
    CYAN = '\033[38;5;51m'

    match message_type:
        case "input":
            return (f"[{CYAN}Input]:   {RESET}{message}: ")

        case "error":
            RED = '\033[38;5;196m'
            print(f"[{RED}Error{RESET}]:   {message}. Exiting...")
            exit()

        case "warning":
            ORANGE = '\033[38;5;214m'
            print(f"[{ORANGE}Warning{RESET}]: {message}!")

        case "ok":
            GREEN = '\033[38;5;46m'
            print(f"[{GREEN}OK{RESET}]:      {message}.")

        case "status":
            print(f"[{CYAN}Status{RESET}]:  {message}...")

        case "exit":
            print(f"[{CYAN}Exit{RESET}]:    {message}. Exiting...")

        case _:
            output_message("error", f"The function output_message() could not match the message type")