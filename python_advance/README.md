# README.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

This is a Python learning repository focused on advanced Python concepts. Each file is numbered (17-25) and demonstrates a specific advanced Python topic with examples and exercises.

## Running Code

**Execute individual lesson files:**
```powershell
python <filename>.py
```

**Example:**
```powershell
python 25_decorators.py
python 24_argparse.py --number1 10 --number2 5 --operation add
```

**No test framework or build system is configured** - this is a learning/practice repository.

## Code Structure

The repository follows a consistent pattern:
- **Main lesson files**: `##_topic.py` - Core concept implementations
- **Exercise files**: `##_topic_ex.py` - Practice exercises for the same topic
- **IDLE session files**: `##_topic_IDLE.py` - Interactive Python session transcripts showing exploratory learning

### Topics Covered (by file number)

- **17**: Inheritance - Single inheritance with `isinstance()` and `issubclass()`
- **18**: Multiple inheritance - Method resolution order and calling parent methods
- **19**: Custom exceptions - Creating and raising custom exception classes
- **20**: Iterators - Implementing `__iter__()` and `__next__()` protocols
- **21**: Generators - Using `yield` for lazy evaluation and infinite sequences
- **22**: List/set/dict comprehensions - Compact syntax for collection creation
- **23**: Sets and frozensets (file placeholder - empty)
- **24**: Argparse - CLI argument parsing with named arguments and choices
- **25**: Decorators - Function wrappers for timing and behavior modification

## Key Patterns

**Custom Iterators**: Implement both `__iter__()` (returns self) and `__next__()` (raises `StopIteration` when done)

**Generators**: Prefer `yield` over building full lists when dealing with large or infinite sequences

**Multiple Inheritance**: First parent class in the inheritance list takes precedence in method resolution (see `18_multiple_inheritance.py`)

**Decorators**: Use the `@decorator_name` syntax above function definitions; decorators return wrapper functions that enhance behavior

## Development Environment

- **IDE**: PyCharm (based on `.idea/` directory and `main.py` comments)
- **Python Version**: 3.13.0 (based on IDLE transcripts)
- **OS**: Windows (PowerShell environment)
