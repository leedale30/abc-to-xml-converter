# Multi-Format Music Converter - Product Requirement Document

## Overview
- **Summary**: Enhance the ABC+ Converter to support bidirectional conversion between a wide range of music file formats, allowing users to convert "any file type to any other file type" as much as possible.
- **Purpose**: To create a comprehensive music format conversion tool that leverages music21 and existing libraries to support the maximum possible number of music file formats.
- **Target Users**: Musicians, music educators, composers, and anyone who needs to convert between different music file formats.

## Goals
- Add support for file uploads (any supported format)
- Enable bidirectional conversion between as many formats as possible
- Maintain backward compatibility with existing ABC+ to MusicXML conversion
- Provide a user-friendly interface for selecting input and output formats
- Support both text-based and binary music formats

## Non-Goals (Out of Scope)
- Creating custom conversion logic from scratch (use existing libraries)
- Supporting every possible music format in existence
- Real-time format conversion during editing

## Background & Context
- The current ABC+ Converter supports converting ABC+ to MusicXML, MIDI, and LilyPond
- music21 library is already installed and supports many formats for both reading and writing
- Existing tools like abc2xml, abc2midi, abc2ly are available for ABC-specific conversions

## Functional Requirements
- **FR-1**: Allow users to upload music files in any supported format
- **FR-2**: Detect input file format automatically
- **FR-3**: Allow users to select target output format from available options
- **FR-4**: Convert files bidirectionally between supported formats
- **FR-5**: Maintain existing ABC+ text input functionality
- **FR-6**: Provide format conversion via both file upload and text input
- **FR-7**: Handle conversion errors gracefully

## Non-Functional Requirements
- **NFR-1**: Conversion should be fast and efficient
- **NFR-2**: User interface should be intuitive and responsive
- **NFR-3**: Support large music files where possible
- **NFR-4**: Clear error messages for unsupported formats or conversion failures

## Constraints
- **Technical**: Use music21 as the primary conversion engine
- **Dependencies**: Leverage existing libraries (music21, abcmidi, LilyPond, abc2xml)
- **Backward Compatibility**: Maintain all existing functionality

## Assumptions
- music21 will handle most conversion needs
- Some format combinations may not be possible
- Users will understand that not all format conversions are supported

## Acceptance Criteria

### AC-1: File Upload
- **Given**: User accesses the converter
- **When**: User uploads a music file
- **Then**: System accepts the file and detects its format
- **Verification**: `programmatic`

### AC-2: Format Detection
- **Given**: User uploads a music file
- **When**: File is uploaded
- **Then**: System automatically detects the input format
- **Verification**: `programmatic`

### AC-3: Target Format Selection
- **Given**: Input format is detected
- **When**: User selects target format
- **Then**: System shows only supported output formats for the given input
- **Verification**: `human-judgment`

### AC-4: Bidirectional Conversion
- **Given**: User has a file in format A
- **When**: User selects to convert to format B and back
- **Then**: Both conversions work (if supported)
- **Verification**: `programmatic`

### AC-5: Error Handling
- **Given**: User attempts to convert to/from an unsupported format
- **When**: Conversion is attempted
- **Then**: System shows clear error message
- **Verification**: `human-judgment`

### AC-6: Backward Compatibility
- **Given**: Existing ABC+ text input functionality
- **When**: User uses ABC+ text input
- **Then**: All existing conversion options still work
- **Verification**: `programmatic`

## Open Questions
- [ ] What priority should we give to different format combinations?
- [ ] Should we show all possible formats or only those supported by music21?
- [ ] How to handle very large music files?