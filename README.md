```
╔═════════════════════════════════════════════════════════════════════╗
║                                                                     ║
║   ██╗     ██╗███╗   ██╗ ██████╗ ██╗   ██╗ █████╗                   ║
║   ██║     ██║████╗  ██║██╔════╝ ██║   ██║██╔══██╗                  ║
║   ██║     ██║██╔██╗ ██║██║  ███╗██║   ██║███████║                  ║
║   ██║     ██║██║╚██╗██║██║   ██║██║   ██║██╔══██║                  ║
║   ███████╗██║██║ ╚████║╚██████╔╝╚██████╔╝██║  ██║                  ║
║   ╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝                  ║
║                                                                     ║
║   ███╗   ███╗ █████╗ ████████╗███████╗                              ║
║   ████╗ ████║██╔══██╗╚══██╔══╝██╔════╝                              ║
║   ██╔████╔██║███████║   ██║   █████╗                                ║
║   ██║╚██╔╝██║██╔══██║   ██║   ██╔══╝                                ║
║   ██║ ╚═╝ ██║██║  ██║   ██║   ███████╗                              ║
║   ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝                              ║
║                                                                     ║
║       🌍  Speak Every Language. Hear Every Voice.  🗣️               ║
╚═════════════════════════════════════════════════════════════════════╝
```

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-FF6B6B?style=for-the-badge&logo=python&logoColor=white)
![Google Translate](https://img.shields.io/badge/Google%20Translate-API-4285F4?style=for-the-badge&logo=googletranslate&logoColor=white)
![pyttsx3](https://img.shields.io/badge/pyttsx3-Voice%20Output-FFE66D?style=for-the-badge)
![Languages](https://img.shields.io/badge/Languages-100%2B-A8E6CF?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-C3B1E1?style=for-the-badge)

**[⭐ Star this repo](https://github.com/laraib776/LinguaMate-UniversalVoice-Translation-)** · **[🐛 Report a Bug](https://github.com/laraib776/LinguaMate-UniversalVoice-Translation-/issues)** · **[🤝 Contribute](#-contributing)**

</div>

---

## 🌍 100+ Languages. One App. Zero Language Barriers.

> **Type it in English. Hear it back in Japanese. Or French. Or Arabic. Or all three.**
> LinguaMate doesn't just translate words — it gives them a voice, a speed, and a personality.
>
> ### 👉 **Type. Translate. Listen. In any language on Earth.** 👈
>
> *Because language should never be the reason you can't connect.*

> [!NOTE]
> LinguaMate is a fully **offline-capable desktop application** — translation uses the Google Translate API but voice output via `pyttsx3` works completely locally on your machine.

---

## ✦ About LinguaMate

> **LinguaMate** is a comprehensive language translation and text-to-speech desktop application built with **Python**, **Tkinter**, and the **Google Translate API**. It allows users to translate text across 100+ languages and instantly hear the result spoken aloud — with full control over voice, speed, and gender of the output.
>
> Clean interface. Powerful engine. Every language, at your fingertips.

---

## ┌─── ✨ Key Features

| 🌟 Feature | Details |
|---|---|
| 🌐 **100+ Language Support** | Translate between over 100 world languages instantly |
| 🔊 **Text-to-Speech** | Hear the translated text spoken in a natural voice |
| 🎚️ **Voice Customization** | Control the voice, speed, and gender of spoken output |
| ⚡ **Real-Time Translation** | Powered by Google Translate API for accurate results |
| 🖥️ **User-Friendly GUI** | Clean Tkinter interface — intuitive for all users |

---

## ┌─── 🛠️ Technology Stack

```
  ╭──────────────────┬──────────────────────────────────────────────╮
  │  Layer           │  Technology                                  │
  ├──────────────────┼──────────────────────────────────────────────┤
  │  🐍  Language     │  Python 3.x                                 │
  │  🖥️  GUI          │  Tkinter  (desktop interface)               │
  │  🌐  Translation  │  Google Translate API  (googletrans)        │
  │  🔊  Voice        │  pyttsx3  (text-to-speech engine)           │
  │  ⚙️  System       │  ctypes  (system-level integration)         │
  ╰──────────────────┴──────────────────────────────────────────────╯
```

---

## ┌─── 🚀 Installation & Setup

### Step 1 — Install Python

Download Python 3.x from the official site:
```
🔗  https://www.python.org/downloads/
```

### Step 2 — Install Required Libraries

```bash
pip install googletrans==4.0.0-rc1 pyttsx3
```

> 💡 `tkinter` and `ctypes` come **pre-bundled** with Python — no extra install needed!

> [!WARNING]
> Use `googletrans==4.0.0-rc1` specifically — newer or unversioned installs can cause connection issues with the Google Translate API.

### Step 3 — Clone the Repository

```bash
git clone https://github.com/laraib776/LinguaMate-UniversalVoice-Translation-.git
cd LinguaMate-UniversalVoice-Translation-
```

### Step 4 — Run the Application

```bash
python main.py
```

> 🎉 The LinguaMate GUI will launch and you're ready to translate!

---

## ┌─── 🎮 Usage Guide

Once the application is running:

```
  ✏️   Step 1  →  Type or paste your text into the input field
  🌐  Step 2  →  Select the source language
  🎯  Step 3  →  Select the destination language
  ⚡  Step 4  →  Hit Translate — see the result instantly
  🔊  Step 5  →  Press Listen — hear the translation spoken aloud
  🎚️   Step 6  →  Adjust voice, speed, and gender as preferred
```

---

## ┌─── 📁 Project Structure

```
📦 LinguaMate-UniversalVoice-Translation/
 │
 ├── 📄 main.py               ← Entry point — launches the application
 ├── 📄 translator.py         ← Google Translate API integration
 ├── 📄 voice.py              ← pyttsx3 voice engine and customization
 ├── 📄 README.md             ← You are here 👋
 └── 📄 LICENSE               ← MIT License
```

---

## ┌─── 🌐 Supported Languages  *(a few highlights)*

```
  🇬🇧 English    🇸🇦 Arabic     🇨🇳 Chinese    🇫🇷 French
  🇩🇪 German     🇮🇳 Hindi      🇯🇵 Japanese   🇰🇷 Korean
  🇵🇹 Portuguese 🇷🇺 Russian    🇪🇸 Spanish    🇹🇷 Turkish
                    + 90 more languages 🌍
```

---

## ┌─── 🤝 Contributing

Contributions are always welcome and appreciated! 💖

```
  1. 🍴  Fork the repository
  2. 🌿  Create your feature branch
  3. 💾  Commit your changes
  4. 📬  Open a Pull Request
```

Ideas we'd love to see: auto language detection, translation history, a dark mode UI, pronunciation guides, or offline language packs — all PRs are warmly welcome!

---

## ┌─── 📜 License

LinguaMate is licensed under the **MIT License** — free to use, modify, and share.
See the `LICENSE` file for full details.

---

<div align="center">

```
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║   Every language is a window into a different world.         ║
║                                                              ║
║      LinguaMate opens all 100 of them.  🌍🗣️💬              ║
║                                                              ║
║                Made with ❤️  by  Laraib Khalid               ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

*⭐ Drop a star if LinguaMate helped you speak the world's languages!*

</div>
