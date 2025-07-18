# 🤖 Enhanced Terminal Chatbot

> **⚡ Fast AI-powered terminal assistant with system integration capabilities**

A sophisticated command-line chatbot that combines conversational AI with real system interaction, powered by Groq's lightning-fast inference. Chat naturally, execute commands, manage files, and monitor your system - all from one intelligent terminal interface.

![Terminal Demo](https://img.shields.io/badge/Platform-macOS%20%7C%20Linux%20%7C%20Windows-brightgreen)
![Python Version](https://img.shields.io/badge/Python-3.7+-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active%20Development-orange)

## ✨ Features

### 🧠 **Intelligent Conversation**
- Natural language chat powered by Groq's Llama3 models
- Context-aware responses with conversation history
- Code generation and technical assistance

### 🖥️ **System Integration**
- **Command Execution**: Run shell commands directly from chat
- **File Operations**: Read, write, and manage files seamlessly  
- **System Monitoring**: Real-time system info, process management
- **Safety First**: Smart detection of dangerous commands with user confirmation

### 🎯 **Specialized Commands**
| Command | Description | Example |
|---------|-------------|---------|
| `/exec <command>` | Execute shell commands | `/exec ls -la` |
| `/read <filepath>` | Read file contents | `/read config.json` |
| `/write <filepath>` | Create/edit files | `/write script.py` |
| `/sysinfo` | System information | `/sysinfo` |
| `/processes` | List running processes | `/processes` |
| `/code <request>` | Generate code snippets | `/code python sort algorithm` |
| `/cmd <request>` | Generate shell commands | `/cmd find large files` |

## 🚀 Quick Start

### Prerequisites
- **Python 3.7+** 
- **Groq API Key** (Free at [console.groq.com](https://console.groq.com/))

### Installation

1. **Clone & Setup**
   ```bash
   git clone https://github.com/yourusername/terminal-chatbot.git
   cd terminal-chatbot
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Key**
   ```bash
   cp .env.example .env
   # Edit .env and add your Groq API key:
   # GROQ_API_KEY=your_actual_api_key_here
   ```

4. **Launch**
   ```bash
   python chatbot.py
   ```

## 💡 Usage Examples

### Basic Conversation
```
You > What's the best way to optimize Python code?
Chatbot > Here are some key Python optimization strategies...
```

### System Operations
```
You > /sysinfo
System > 🖥️ System Information:
  OS: macOS
  Memory: 16.00 GB
  CPU Cores: 8
  Disk Usage: 45.2% used
  Current Directory: /Users/you/projects

You > /exec echo "Hello from terminal!"
System > ✅ Command executed successfully:
Hello from terminal!
```

### File Management
```
You > /read package.json
System > 📄 File content of 'package.json':
{
  "name": "my-project",
  ...

You > /write notes.txt
Enter content to write (press Ctrl+D when done):
Today I learned about terminal automation
^D
System > ✅ Content written to 'notes.txt'
```

### Code Generation
```
You > /code python function to calculate fibonacci
Chatbot > def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

## 🔒 Security Features

- **🛡️ Dangerous Command Detection**: Automatically identifies risky operations
- **⚠️ User Confirmation**: Requires explicit approval for potentially harmful commands
- **⏱️ Timeout Protection**: Commands auto-terminate after 30 seconds
- **🔐 Permission Handling**: Graceful handling of access restrictions
- **🚫 Safe Defaults**: Conservative approach to system modifications

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   User Input    │───▶│  Command Router │───▶│  AI Processing  │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                               │
                               ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│ System Response │◀───│ Safety Checks   │◀───│ System Commands │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 🛠️ Technical Stack

- **AI Engine**: Groq (Llama3-8B-8192)
- **System Interface**: psutil, subprocess
- **Environment**: python-dotenv
- **Language**: Python 3.7+

## 🚧 Current Limitations & Future Improvements

This project is in **active development**. Here are known areas for enhancement:

### 🔧 **Planned Improvements**
- [ ] **Enhanced Security**: Sandboxed command execution
- [ ] **Plugin System**: Extensible architecture for custom commands
- [ ] **Configuration Management**: User-customizable settings and aliases
- [ ] **Command History**: Persistent history with search functionality
- [ ] **Multi-Model Support**: Integration with multiple AI providers
- [ ] **Advanced File Operations**: Syntax highlighting, diff views, backup creation
- [ ] **Network Operations**: SSH, SCP, and remote system management
- [ ] **Performance Monitoring**: Resource usage tracking and optimization
- [ ] **GUI Integration**: Optional web interface for visual users
- [ ] **Voice Interface**: Speech-to-text and text-to-speech capabilities

### 🐛 **Known Issues**
- Large file operations may timeout
- Some system commands may require elevated permissions
- Limited error recovery for network-dependent operations
- Process monitoring could be more detailed

### 🎯 **Contributing Areas**
- Security enhancements and vulnerability testing
- Cross-platform compatibility improvements
- Performance optimization for large-scale operations
- UI/UX improvements for better user experience
- Documentation and tutorial creation

## 🤝 Contributing

We welcome contributions! This project has significant potential for expansion:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### 🎯 **High-Impact Contribution Areas**
- **Security hardening** and sandboxing
- **Cross-platform testing** and compatibility
- **Performance optimization** for large operations
- **Documentation** and user guides
- **Plugin architecture** development

## 📊 Project Status

- **Phase**: Early Development
- **Stability**: Beta
- **Testing**: Manual (Automated testing needed)
- **Documentation**: In Progress
- **Community**: Growing

## � License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Groq** for providing incredibly fast AI inference
- **psutil** developers for excellent system monitoring capabilities
- **Python community** for robust libraries and tools
- **Contributors** and early adopters providing feedback

## 📬 Contact & Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/terminal-chatbot/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/terminal-chatbot/discussions)
- **Email**: your.email@example.com

---

⭐ **If you find this project useful, please give it a star!** ⭐

*Built with ❤️ for developers who love the terminal*
