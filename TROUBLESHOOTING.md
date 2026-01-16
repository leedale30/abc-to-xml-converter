# Fixing "ModuleNotFoundError: No module named 'pyparsing'" Error

## Problem

When running the ABC to MusicXML converter, conversions fail with:

```
ModuleNotFoundError: No module named 'pyparsing'
```

This happens even when `pyparsing` is installed in the virtual environment.

## Root Cause

The `app.py` was using a hardcoded `python3` command in the subprocess call:

```python
result = subprocess.run(
    ['python3', CONVERTER_SCRIPT, temp_abc_path],  # ❌ Uses system Python
    ...
)
```

This invokes the **system Python** instead of the **virtual environment's Python**, so packages installed in `.venv` (like `pyparsing`) are not available.

## Solution

Replace `'python3'` with `sys.executable`, which always points to the Python interpreter currently running the Flask app:

```python
result = subprocess.run(
    [sys.executable, CONVERTER_SCRIPT, temp_abc_path],  # ✅ Uses venv Python
    ...
)
```

## Quick Fix Steps

1. **Open `app.py`**
2. **Find line ~139** containing `['python3', CONVERTER_SCRIPT, ...]`
3. **Replace `'python3'` with `sys.executable`**
4. **Restart the Flask server**

## Verification

After applying the fix, conversions should complete successfully without the `pyparsing` import error.

---

*Fixed: 2026-01-16*
