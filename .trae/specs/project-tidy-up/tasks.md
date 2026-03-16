# Project Tidy-Up - Implementation Plan

## [x] Task 1: Identify and list all files to be removed
- **Priority**: P0
- **Depends On**: None
- **Description**:
  - Create a comprehensive list of all files in the root directory
  - Categorize files into: temporary, test, duplicate zip, old JS, and core
  - Verify which files are safe to remove
- **Acceptance Criteria Addressed**: All
- **Test Requirements**:
  - `programmatic` TR-1.1: List all files in root directory
  - `human-judgment` TR-1.2: Review and categorize files
  - `programmatic` TR-1.3: Verify core files are identified correctly
- **Notes**: Be careful not to mark any core files for removal

## [x] Task 2: Remove temporary files
- **Priority**: P0
- **Depends On**: Task 1
- **Description**:
  - Remove all tmp*.ly files
  - Remove output.midi
  - Remove showcase_output.mid
  - Remove test_request.json
- **Acceptance Criteria Addressed**: AC-1
- **Test Requirements**:
  - `programmatic` TR-2.1: Verify temporary files are removed
  - `programmatic` TR-2.2: Verify no core files were removed
- **Notes**: Double-check before deleting

## [x] Task 3: Remove test files
- **Priority**: P0
- **Depends On**: Task 1
- **Description**:
  - Remove all test_*.py files
  - Remove all test_*.abc files
  - Remove all test_*.ly files
  - Remove explore_music21_formats.py
  - Remove apply_fix.py
  - Remove check_mei.py
- **Acceptance Criteria Addressed**: AC-2
- **Test Requirements**:
  - `programmatic` TR-3.1: Verify test files are removed
  - `programmatic` TR-3.2: Verify no core files were removed
- **Notes**: Consider if any test files should be kept and moved to a test directory

## [x] Task 4: Remove duplicate zip files
- **Priority**: P0
- **Depends On**: Task 1
- **Description**:
  - Remove all all_formats_*.zip files
  - Optionally keep the latest one or remove all
- **Acceptance Criteria Addressed**: AC-3
- **Test Requirements**:
  - `programmatic` TR-4.1: Verify duplicate zip files are removed
  - `programmatic` TR-4.2: Verify no core files were removed
- **Notes**: These zip files were likely created during testing

## [x] Task 5: Remove old JS files
- **Priority**: P0
- **Depends On**: Task 1
- **Description**:
  - Remove abc_parse_music_FINAL.js
  - Remove abc_parse_music_FIX.js
  - Remove abc_parse_music_PUSH.js
  - Remove abc_parse_music_original.js
- **Acceptance Criteria Addressed**: AC-4
- **Test Requirements**:
  - `programmatic` TR-5.1: Verify old JS files are removed
  - `programmatic` TR-5.2: Verify no core files were removed
- **Notes**: These appear to be old versions of the parser that are no longer needed

## [x] Task 6: Verify core files remain
- **Priority**: P1
- **Depends On**: Tasks 2-5
- **Description**:
  - Verify app.py remains
  - Verify requirements.txt remains
  - Verify setup.py remains
  - Verify annotationguide.json remains
  - Verify all documentation files remain
  - Verify all directories remain (templates/, static/, examples/, etc.)
- **Acceptance Criteria Addressed**: AC-5
- **Test Requirements**:
  - `programmatic` TR-6.1: List all remaining files in root
  - `human-judgment` TR-6.2: Review remaining files to ensure completeness
- **Notes**: Compare against a list of expected core files

## [x] Task 7: Test the application
- **Priority**: P1
- **Depends On**: Task 6
- **Description**:
  - Start the application
  - Verify it loads correctly
  - Test basic conversion functionality
  - Test multi-format conversion
  - Verify all endpoints work
- **Acceptance Criteria Addressed**: AC-6
- **Test Requirements**:
  - `programmatic` TR-7.1: Verify application starts without errors
  - `programmatic` TR-7.2: Verify basic conversion works
  - `programmatic` TR-7.3: Verify all endpoints respond
- **Notes**: Test thoroughly to ensure nothing was broken

## [ ] Task 8: Optional - Create test directory (if needed)
- **Priority**: P2
- **Depends On**: Task 1
- **Description**:
  - If any test files are worth keeping, create a tests/ directory
  - Move selected test files to tests/ directory
  - Update documentation if needed
- **Acceptance Criteria Addressed**: None (optional)
- **Test Requirements**:
  - `human-judgment` TR-8.1: Review test files to keep
  - `programmatic` TR-8.2: Verify files are moved correctly
- **Notes**: Only do this if there are valuable test files to preserve
