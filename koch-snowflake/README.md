# Koch Curve Snowflake

This is a simple implementation in Python of a Koch Curve Snowflake in an image. The [pdf](https://github.com/the-other-mariana/code-journal/blob/master/koch-snowflake/CJ09_KochCurve.pdf) shows the algorithm followed. <br />

## Specifications

Python Version: `Python 3.6.2` <br />
Line Library: [line.py](https://github.com/the-other-mariana/code-journal/blob/master/koch-snowflake/line.py) <br />

## Custom Line File

To use the `line.py` file: <br />

```Python
import line as ln #line.py must be on same folder of koch.py
```

Now, the line can be painted on an image by:

```Python
ln.line([x0, y0], [x1, y1], thick, color, img)
```
*Note: the line.py file coordinates are sent in cartesian, not pixels. This is in order to accept negative coordinates (but still must be integers) and facilitate mathematical models*

## Usage

1. Download this repo and store it in your computer.
1. Go to this repo's directory and open Powershell.
1. Type `python koch.py` to run the code.

## Output

A sample Koch Snowflake was the following: <br />

![alt text](https://github.com/the-other-mariana/code-journal/blob/master/koch-snowflake/output/koch01.png?raw=true) <br />

Koch's curve is implemented to do a fractal with the base polygon being any type of odd-sided polygon, not only triangles. For a pentagon, the pentagonal Koch Curve looks as follows. <br />

![alt text](https://github.com/the-other-mariana/code-journal/blob/master/koch-snowflake/output/penttest05.png?raw=true) <br />

Koch Curve makes up a snowflake if the iterations increase. A small visualization of this would the as follows. <br />

![alt text](https://github.com/the-other-mariana/code-journal/blob/master/koch-snowflake/output/koch-gif.gif) <br />