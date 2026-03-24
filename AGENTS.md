# AGENTS.md

## Project Goals
This is a lightweight astronomy utility page for telescope users.
The code must remain simple, readable, and dependency-free.

## Coding Style
- Use plain HTML, CSS and vanilla JavaScript only
- Do NOT introduce frameworks (React, Vue, etc.)
- Keep everything in a single file unless explicitly requested
- Prefer clarity over cleverness
- Use descriptive variable names
- Add comments for non-obvious calculations (especially astronomy math)

## Rules
- DO NOT modify existing core functionality
- DO NOT change existing calculations unless fixing a bug
- DO NOT change UI layout drastically
- DO NOT refactor working code unless requested
- Add new features in isolated functions

## When Adding Features
- Keep functions small and independent
- Avoid global variables unless necessary
- Reuse existing styles
- Maintain current visual style
- Ensure dark mode compatibility

## JavaScript Guidelines
- Use simple DOM manipulation
- Avoid advanced patterns
- No build tools
- No transpilers
- No external libraries

## Comments
- Comment all astronomy-related formulas
- Comment time conversions
- Comment sidereal time logic

## UI Guidelines
- Maintain monospace font
- Keep centered layout
- Keep minimalistic look
- Ensure mobile compatibility

## Performance
- Avoid heavy computations
- Avoid loops inside 1s timers
- Do not block UI updates

## Priority
1. Stability
2. Simplicity
3. Readability
4. New features