# Graphics Final Project
### Name: Ryan Poon
### Class Period: 4
---
## New Graphics Engine Features
- Anti-aliasing
- Phong shading

---
## The Details
- Anti-aliasing:
    Use Xiaolin Wu's line drawing algorithm. Add new MDL command, "AA," with arguments "on" and "off." If "on," Xiaolin Wu's algorithm will be used. If the command is not present, or set to "off," then Bresenham's algorithm will be used.
- Phong shading:
    - implement shading MDL command to accept either "flat" or "phong" argument