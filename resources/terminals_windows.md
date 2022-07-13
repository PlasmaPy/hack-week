---
tags: Hack Week, IDE, 2022, Terminals, Windows
---

# Terminals: Windows

## Objective:
Provide overview of the available terminals and how they impact collaborative development with git and git resources.

### tl;dr
Windows Terminal with Windows Subsystem Layer (WSL) provides a nice Linux Platfom for collaborative development.


## Four options:

| Terminal     | Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   | Appearance |
|--------------|-----|:--------------------------------:|
| Cmd Prompt | Original Windows Shell | ![Command Prompt](https://i.imgur.com/LDEVvjf.png)
| PowerShell | “PowerShell is a cross-platform task automation solution made up of a command-line shell, a scripting language, and a configuration management framework. PowerShell runs on Windows, Linux, and macOS.” Built on top of Microsoft .NET technology (Object-Oriented) | ![Powershell](https://i.imgur.com/fDc0cmb.png) |
| Cygwin Shell | A large collection of GNU and Open Source tools which provide functionality similar to a Linux distribution on Windows. DLL (cygwin1.dll) which provides substantial POSIX API functionality. | ![Cygwin Shell](https://i.imgur.com/cuXXQBO.png) |
| WSL/Ubuntu | Windows Subsystem for Linux (WSL) lets developers run a GNU/Linux environment -- including most command-line tools, utilities, and applications -- directly on Windows, unmodified, without the overhead of a traditional virtual machine or dual-boot setup. |![Ubuntu Shell](https://i.imgur.com/JszS6fG.png) |

## Feature Comparison
[Terminal Comparison for Windows](https://docs.google.com/presentation/d/1NV8e2VXIbJFe5452JOmlstfVDXav8XFhxbN1EBAeoig/edit#slide=id.p)

## Advantages and Disadvantages

[HyperPolyGlot Extensive Feature Breakdown](https://hyperpolyglot.org/shell)

## WSL Setup for Collaborative Development

1. [Install WSL](https://docs.microsoft.com/en-us/windows/wsl/install)
2. [Install Windows Terminal](https://apps.microsoft.com/store/detail/windows-terminal/9N0DX20HK701?hl=en-us&gl=US)
3. [Configure Windows Terminal](https://docs.microsoft.com/en-us/windows/terminal/install)
4. [Get started using Visual Studio Code](https://docs.microsoft.com/en-us/windows/wsl/tutorials/wsl-vscode)
5.  Install Extensions
    - Remote - SSH
    - Remote - SSH: Editing Configuration Files
    - Remote - WSL
    - Remote Development
    - vscode-icons
    - Git Extension Pack (Installed in WSL)
    - Git Graph
    - Git History
    - GitHub Pull Requests and Issues
    - gitignore
    - Python
    - Pylance
6. [Install and Configure Git in WSL](https://docs.microsoft.com/en-us/windows/wsl/tutorials/wsl-git)