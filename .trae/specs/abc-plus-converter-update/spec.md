# ABC+ Converter - Product Requirement Document

## Overview
- **Summary**: An update to the ABC+ Converter web application to support converting ABC+ notation to various music file formats without using the music21 library.
- **Purpose**: To expand the functionality of the ABC+ Converter to generate multiple music file formats directly from ABC+ notation, providing users with more flexible output options.
- **Target Users**: Musicians, music educators, and composers who need to convert ABC+ notation to different music file formats for various use cases.

## Goals
- Add support for converting ABC+ to MIDI format
- Add support for converting ABC+ to LilyPond format
- Add support for converting ABC+ to MusicXML format
- Implement a feature to convert to all supported formats at once
- Ensure the conversion process is efficient and reliable

## Non-Goals (Out of Scope)
- Using music21 library for conversion
- Converting from other formats to ABC+
- Adding support for MEI format
- Implementing real-time conversion during editing

## Background & Context
- The current ABC+ Converter app can convert ABC+ to MusicXML format
- The app is built using Flask as the backend and standard web technologies for the frontend
- The app has a simple interface with text input for ABC+ content and conversion functionality

## Functional Requirements
- **FR-1**: Convert ABC+ notation to MIDI format
- **FR-2**: Convert ABC+ notation to LilyPond format
- **FR-3**: Convert ABC+ notation to MusicXML format (existing functionality to be maintained)
- **FR-4**: Convert ABC+ notation to all supported formats at once and package as a zip file
- **FR-5**: Provide a user interface for selecting the desired output format
- **FR-6**: Handle conversion errors gracefully and provide meaningful error messages

## Non-Functional Requirements
- **NFR-1**: Conversion performance should be fast enough to handle typical music scores within 5 seconds
- **NFR-2**: The user interface should be intuitive and easy to use
- **NFR-3**: The application should be compatible with modern web browsers
- **NFR-4**: Error messages should be clear and helpful for debugging

## Constraints
- **Technical**: Must not use the music21 library for conversion
- **Dependencies**: May require external tools or libraries for specific format conversions
- **Platform**: Must run on the existing Flask-based infrastructure

## Assumptions
- The ABC+ notation is well-formed and follows the ABC+ specification
- The server environment has access to necessary tools for format conversion
- Users have basic knowledge of ABC+ notation

## Acceptance Criteria

### AC-1: MIDI Conversion
- **Given**: A user inputs valid ABC+ notation
- **When**: The user selects MIDI as the output format and clicks convert
- **Then**: The system generates a valid MIDI file
- **Verification**: `programmatic`
- **Notes**: The MIDI file should contain the musical notes, rhythm, and basic structure from the ABC+ notation

### AC-2: LilyPond Conversion
- **Given**: A user inputs valid ABC+ notation
- **When**: The user selects LilyPond as the output format and clicks convert
- **Then**: The system generates a valid LilyPond file
- **Verification**: `programmatic`
- **Notes**: The LilyPond file should accurately represent the musical structure from the ABC+ notation

### AC-3: MusicXML Conversion
- **Given**: A user inputs valid ABC+ notation
- **When**: The user selects MusicXML as the output format and clicks convert
- **Then**: The system generates a valid MusicXML file
- **Verification**: `programmatic`
- **Notes**: This functionality already exists and should be maintained

### AC-4: Convert to All Formats
- **Given**: A user inputs valid ABC+ notation
- **When**: The user clicks the "Convert to All Formats" button
- **Then**: The system generates all supported formats and packages them in a zip file
- **Verification**: `programmatic`
- **Notes**: The zip file should contain files in all supported formats

### AC-5: User Interface
- **Given**: A user accesses the ABC+ Converter web application
- **When**: The user views the interface
- **Then**: The interface includes a format selector dropdown and a "Convert to All Formats" button
- **Verification**: `human-judgment`
- **Notes**: The interface should be intuitive and easy to use

### AC-6: Error Handling
- **Given**: A user inputs invalid ABC+ notation
- **When**: The user attempts to convert the notation
- **Then**: The system displays a clear error message
- **Verification**: `human-judgment`
- **Notes**: Error messages should be helpful for debugging

## Open Questions
- [ ] What external tools or libraries should be used for MIDI and LilyPond conversion instead of music21?
- [ ] How to handle different versions of ABC+ notation?
- [ ] What are the specific requirements for each output format?