# ABC+ Converter Dependencies - Product Requirement Document

## Overview
- **Summary**: Ensure all required dependencies are installed for the ABC+ Converter to support all file formats (MIDI, MusicXML, LilyPond, MEI, ABC).
- **Purpose**: Resolve the issue where some file formats are missing from the output zip file due to missing dependencies.
- **Target Users**: Users of the ABC+ Converter application who need to convert ABC+ notation to various music file formats.

## Goals
- Install all required dependencies for the ABC+ Converter
- Ensure all file formats (MIDI, MusicXML, LilyPond, MEI, ABC) are generated successfully
- Verify that the MIDI file is not empty and contains valid music data

## Non-Goals (Out of Scope)
- Modifying the core functionality of the ABC+ Converter
- Adding new features to the application
- Changing the user interface of the application

## Background & Context
- The ABC+ Converter currently generates only MIDI, MusicXML, and ABC files
- LilyPond and MEI formats are missing due to missing dependencies
- The MIDI file appears to be small and may be empty

## Functional Requirements
- **FR-1**: Install LilyPond music typesetting software
- **FR-2**: Install MEI dependencies
- **FR-3**: Verify all file formats are generated successfully
- **FR-4**: Verify the MIDI file contains valid music data

## Non-Functional Requirements
- **NFR-1**: The installation process should be automated and documented
- **NFR-2**: The converter should handle missing dependencies gracefully
- **NFR-3**: The output files should be valid and usable

## Constraints
- **Technical**: macOS operating system
- **Dependencies**: External software (LilyPond) and Python packages

## Assumptions
- The user has administrative privileges to install software
- The ABC+ Converter code is already functional

## Acceptance Criteria

### AC-1: LilyPond Installation
- **Given**: The ABC+ Converter is installed
- **When**: LilyPond is installed on the system
- **Then**: The converter should generate LilyPond files
- **Verification**: `programmatic`
- **Notes**: LilyPond is required for generating LilyPond format files

### AC-2: MEI Dependencies Installation
- **Given**: The ABC+ Converter is installed
- **When**: MEI dependencies are installed
- **Then**: The converter should generate MEI files
- **Verification**: `programmatic`
- **Notes**: MEI dependencies are required for generating MEI format files

### AC-3: All Formats Generated
- **Given**: All dependencies are installed
- **When**: The user clicks "Download all formats as zip"
- **Then**: The zip file should contain all five formats (MIDI, MusicXML, LilyPond, MEI, ABC)
- **Verification**: `programmatic`

### AC-4: MIDI File Validation
- **Given**: The converter generates a MIDI file
- **When**: The MIDI file is examined
- **Then**: The MIDI file should not be empty and should contain valid music data
- **Verification**: `programmatic`

## Open Questions
- [ ] What version of LilyPond should be installed?
- [ ] What are the specific MEI dependencies needed?