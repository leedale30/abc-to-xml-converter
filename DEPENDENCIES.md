# ABC+ Converter Dependencies

## Overview
This document explains how to install the required dependencies for the ABC+ Converter to support all file formats.

## Dependencies

### 1. Python Dependencies
The ABC+ Converter requires the following Python packages:

- Flask
- music21
- requests

These dependencies are typically installed using pip:

```bash
pip install Flask music21 requests
```

### 2. abcmidi (for MIDI format support)
abcmidi is required for generating high-quality MIDI files. It provides the `abc2midi` command-line tool.

#### Installation on macOS
```bash
# Using Homebrew
brew install abcmidi

# Verify installation
abc2midi --version
```

#### Installation on Windows
Download the abcmidi installer from https://ifdo.ca/~seymour/runabc/top.html and follow the installation instructions.

#### Installation on Linux
```bash
# Ubuntu/Debian
sudo apt-get install abcmidi

# Fedora/CentOS
sudo dnf install abcmidi
```

### 3. LilyPond (for LilyPond format support)
LilyPond is required for generating LilyPond format files. It provides the `abc2ly` command-line tool.

#### Installation on macOS
```bash
# Using Homebrew
brew install lilypond

# Verify installation
lilypond --version
abc2ly --version
```

#### Installation on Windows
Download the LilyPond installer from https://lilypond.org/download.html and follow the installation instructions.

#### Installation on Linux
```bash
# Ubuntu/Debian
sudo apt-get install lilypond

# Fedora/CentOS
sudo dnf install lilypond
```

### 4. MEI Support
MEI (Music Encoding Initiative) support is not yet implemented in music21 9.9.1. The converter will skip MEI format until support is added in a future version.

## Verifying Dependencies

To verify that all dependencies are installed correctly, run the following commands:

```bash
# Check Python dependencies
pip list | grep -E "Flask|music21|requests"

# Check abcmidi installation
abc2midi --version

# Check LilyPond installation
lilypond --version
abc2ly --version
```

## Troubleshooting

### abcmidi not found in PATH
If you get an error that abcmidi is not found, ensure that abcmidi is added to your system PATH.

### LilyPond not found in PATH
If you get an error that LilyPond is not found, ensure that LilyPond is added to your system PATH.

### MEI export not working
MEI support is not yet implemented in music21 9.9.1. This is a limitation of the current version of music21.

## Supported Formats

With all dependencies installed, the ABC+ Converter should support the following formats:

- [x] MIDI (using abcmidi)
- [x] MusicXML
- [x] LilyPond (using abc2ly)
- [ ] MEI (not yet supported in music21 9.9.1)
- [x] ABC