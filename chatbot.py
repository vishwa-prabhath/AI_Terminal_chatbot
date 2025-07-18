# -*- coding: utf-8 -*-
import os
import subprocess
import platform
import psutil
import json
from groq import Groq
from dotenv import load_dotenv

# load variables from .env file
load_dotenv()

# create Groq API client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Dangerous commands that require confirmation
DANGEROUS_COMMANDS = [
    "rm",
    "rmdir",
    "del",
    "format",
    "fdisk",
    "mkfs",
    "dd",
    "kill",
    "killall",
    "sudo rm",
    "sudo rmdir",
    "chmod 777",
    "chown",
    "passwd",
    "userdel",
    "shutdown",
    "reboot",
]


def is_dangerous_command(command):
    """Check if command contains dangerous operations"""
    command_lower = command.lower().strip()
    return any(dangerous in command_lower for dangerous in DANGEROUS_COMMANDS)


def connect_to_gpt(history):
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",  # Updated to current supported Groq model
            messages=history,
        )
        return response.choices[0].message.content
    except Exception as e:
        if "insufficient_quota" in str(e) or "rate_limit" in str(e).lower():
            return "⚠️ Groq API quota/rate limit reached. Please wait a moment and try again."
        elif "401" in str(e) or "unauthorized" in str(e).lower():
            return (
                "⚠️ Invalid Groq API key. Please check your GROQ_API_KEY in .env file."
            )
        else:
            return f"⚠️ Groq API Error: {str(e)}"


def execute_command(command):
    """Execute a shell command safely"""
    try:
        # Check for dangerous commands
        if is_dangerous_command(command):
            confirm = input(
                f"⚠️  WARNING: '{command}' could be dangerous. Execute anyway? (yes/no): "
            )
            if confirm.lower() not in ["yes", "y"]:
                return "❌ Command cancelled for safety."

        # Execute the command
        result = subprocess.run(
            command, shell=True, capture_output=True, text=True, timeout=30
        )

        if result.returncode == 0:
            output = result.stdout.strip()
            return (
                f"✅ Command executed successfully:\n{output}"
                if output
                else "✅ Command executed successfully (no output)"
            )
        else:
            error = result.stderr.strip()
            return (
                f"❌ Command failed:\n{error}"
                if error
                else f"❌ Command failed with exit code {result.returncode}"
            )

    except subprocess.TimeoutExpired:
        return "⏱️ Command timed out (30s limit)"
    except Exception as e:
        return f"❌ Error executing command: {str(e)}"


def read_file_content(filepath):
    """Read and return file content"""
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
            return f"📄 File content of '{filepath}':\n{content}"
    except FileNotFoundError:
        return f"❌ File '{filepath}' not found"
    except PermissionError:
        return f"❌ Permission denied to read '{filepath}'"
    except Exception as e:
        return f"❌ Error reading file: {str(e)}"


def write_file_content(filepath, content):
    """Write content to a file"""
    try:
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(content)
        return f"✅ Content written to '{filepath}'"
    except PermissionError:
        return f"❌ Permission denied to write to '{filepath}'"
    except Exception as e:
        return f"❌ Error writing file: {str(e)}"


def get_system_info():
    """Get system information"""
    try:
        os_name = platform.system()
        # Convert Darwin to macOS for user-friendly display
        if os_name == "Darwin":
            os_name = "macOS"

        info = {
            "OS": os_name,
            "OS Version": platform.version(),
            "Architecture": platform.architecture()[0],
            "Processor": platform.processor(),
            "CPU Cores": psutil.cpu_count(),
            "Memory": f"{psutil.virtual_memory().total / (1024**3):.2f} GB",
            "Disk Usage": f"{psutil.disk_usage('/').percent:.1f}% used",
            "Current Directory": os.getcwd(),
        }

        formatted_info = "🖥️ System Information:\n"
        for key, value in info.items():
            formatted_info += f"  {key}: {value}\n"

        return formatted_info
    except Exception as e:
        return f"❌ Error getting system info: {str(e)}"


def list_processes():
    """List running processes"""
    try:
        processes = []
        for proc in psutil.process_iter(["pid", "name", "cpu_percent"]):
            try:
                processes.append(proc.info)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass

        # Sort by CPU usage and get top 10
        processes = sorted(
            processes, key=lambda x: x["cpu_percent"] or 0, reverse=True
        )[:10]

        result = "🔄 Top 10 Processes by CPU Usage:\n"
        for proc in processes:
            result += f"  PID: {proc['pid']:<8} CPU: {proc['cpu_percent'] or 0:.1f}%  Name: {proc['name']}\n"

        return result
    except Exception as e:
        return f"❌ Error listing processes: {str(e)}"


if __name__ == "__main__":
    print("🤖 Enhanced Terminal Chatbot Ready! Type 'exit' to quit.")
    print("📋 Available commands:")
    print("   /exec <command>     - Execute shell command")
    print("   /read <filepath>    - Read file content")
    print("   /write <filepath>   - Write to file (will prompt for content)")
    print("   /sysinfo           - Show system information")
    print("   /processes         - List running processes")
    print("   /code <request>    - Generate code/commands (no execution)")
    print("   /cmd <request>     - Generate commands (no execution)")
    print()

    chat_history = []  # stores conversation history for normal chat

    while True:
        user_input = input("You > ").strip()

        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        # Execute shell command
        elif user_input.startswith("/exec "):
            command = user_input[6:]  # Remove "/exec "
            if command:
                result = execute_command(command)
                print(f"System > {result}\n")
            else:
                print("System > ❌ Please provide a command to execute\n")

        # Read file
        elif user_input.startswith("/read "):
            filepath = user_input[6:]  # Remove "/read "
            if filepath:
                result = read_file_content(filepath)
                print(f"System > {result}\n")
            else:
                print("System > ❌ Please provide a file path to read\n")

        # Write file
        elif user_input.startswith("/write "):
            filepath = user_input[7:]  # Remove "/write "
            if filepath:
                print("Enter content to write (press Ctrl+D or Ctrl+Z when done):")
                try:
                    content = ""
                    while True:
                        try:
                            line = input()
                            content += line + "\n"
                        except EOFError:
                            break
                    result = write_file_content(filepath, content)
                    print(f"System > {result}\n")
                except KeyboardInterrupt:
                    print("\nSystem > ❌ Write operation cancelled\n")
            else:
                print("System > ❌ Please provide a file path to write to\n")

        # System information
        elif user_input == "/sysinfo":
            result = get_system_info()
            print(f"System > {result}\n")

        # List processes
        elif user_input == "/processes":
            result = list_processes()
            print(f"System > {result}\n")

        # Generate code/commands (original functionality)
        elif user_input.startswith("/code") or user_input.startswith("/cmd"):
            prompt = user_input.split(" ", 1)[1] if " " in user_input else ""
            system_message = {
                "role": "system",
                "content": "You are a helpful assistant that ONLY responds with shell commands or code snippets. No explanations.",
            }

            # prepare messages with system instructions + user prompt
            messages = [system_message, {"role": "user", "content": prompt}]
            reply = connect_to_gpt(messages)
            print(f"Chatbot > {reply}\n")

        # Regular conversation
        else:
            chat_history.append({"role": "user", "content": user_input})
            reply = connect_to_gpt(chat_history)
            print(f"Chatbot > {reply}\n")
            chat_history.append({"role": "assistant", "content": reply})
