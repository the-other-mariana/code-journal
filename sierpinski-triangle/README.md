# Sierpinski Triangle

This is a simple implementation in Python of how a Sierpinski Triangle can be painted on an image. <br />

## Specifications

Python Version: `Python 3.6.2` <br />
Line Library: [line.py](https://github.com/the-other-mariana/code-journal/blob/master/poly-spiral/line.py) <br />

## Custom Line File

To use the `line.py` file: <br />

```Python
import line as ln #line.py must be on same folder of sierpinski.py
```

Now, the line can be painted on an image by:

```Python
ln.line([x0, y0], [x1, y1], thick, color, img)
```
*Note: the line.py file coordinates are sent in cartesian, not pixels. This is in order to accept negative coordinates and facilitate mathematical models*

## Usage

1. Download this repo and store it in your computer.
1. Go to this repo's directory and open Powershell.
1. Type `python sierpinski.py` to run the code.

## Output

A sample Sierpinski Triangle was the following: <br />

![alt text](https://github.com/the-other-mariana/code-journal/blob/master/sierpinski-triangle/output/tri03.png) <br />
