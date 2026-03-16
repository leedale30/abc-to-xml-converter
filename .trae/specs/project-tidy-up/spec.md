# Project Tidy-Up - Product Requirement Document

## Overview
- **Summary**: Clean up and organize the project structure by removing temporary files, test files, and organizing the remaining files into appropriate directories.
- **Purpose**: To improve the project's maintainability, readability, and professionalism by removing clutter and organizing files properly.
- **Target Users**: Developers and maintainers of the ABC+ Converter project.

## Goals
- Remove temporary and test files from the root directory
- Organize remaining files into appropriate directories
- Maintain all necessary project files and functionality
- Improve git repository cleanliness
- Keep the project's core functionality intact

## Non-Goals (Out of Scope)
- Modifying any core source code files
- Changing the application's functionality
- Removing any important documentation
- Modifying the git history

## Background & Context
- The project root directory contains many temporary and test files that were created during development
- There are multiple duplicate zip files (all_formats*.zip)
- Old abc_parse_music_*.js files are present but no longer needed
- Temporary ly files (tmp*.ly) and other test files clutter the root
- The project has grown organically and needs organization

## Functional Requirements
- **FR-1**: Identify and remove all temporary files from the root directory
- **FR-2**: Identify and remove all test files from the root directory
- **FR-3**: Remove duplicate zip files (keep only the latest or none)
- **FR-4**: Organize any remaining loose files into appropriate directories
- **FR-5**: Verify that core functionality is not affected by the cleanup

## Non-Functional Requirements
- **NFR-1**: The cleanup should not break any existing functionality
- **NFR-2**: The project should still build and run correctly after cleanup
- **NFR-3**: The git repository should be cleaner and easier to navigate

## Constraints
- **Technical**: Must not remove any source code, documentation, or configuration files
- **Dependencies**: Must maintain all files required for the application to run
- **Backward Compatibility**: Must maintain all existing functionality

## Assumptions
- The temporary and test files are no longer needed
- The abc_parse_music_*.js files are not being used
- The duplicate zip files are not needed
- The core source files (app.py, templates/, static/, etc.) are all necessary

## Acceptance Criteria

### AC-1: Temporary Files Removed
- **Given**: The project root directory
- **When**: The cleanup is complete
- **Then**: All temporary files (tmp*.ly, output.midi, showcase_output.mid, etc.) are removed
- **Verification**: `programmatic`

### AC-2: Test Files Removed
- **Given**: The project root directory
- **When**: The cleanup is complete
- **Then**: All test files (test_*.py, test_*.abc, test_*.ly, etc.) are removed
- **Verification**: `programmatic`

### AC-3: Duplicate Zip Files Removed
- **Given**: The project root directory
- **When**: The cleanup is complete
- **Then**: All duplicate all_formats_*.zip files are removed
- **Verification**: `programmatic`

### AC-4: Old JS Files Removed
- **Given**: The project root directory
- **When**: The cleanup is complete
- **Then**: All abc_parse_music_*.js files are removed
- **Verification**: `programmatic`

### AC-5: Core Files Remain
- **Given**: The project root directory
- **When**: The cleanup is complete
- **Then**: All core source files, documentation, and configuration files remain
- **Verification**: `programmatic`

### AC-6: Application Still Runs
- **Given**: The cleaned-up project
- **When**: The application is started
- **Then**: The application runs normally and all functionality is available
- **Verification**: `programmatic`

## Open Questions
- [ ] Should we keep any of the test files for future reference?
- [ ] Should we create a dedicated test directory for any tests we want to keep?
- [ ] Should we archive the old files instead of deleting them?
