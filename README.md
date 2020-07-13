# savemetadata
Easy way to add your python script's source code as image metadata

# Usage
You write a plotting script (here [`test.py`](test.py)). Inside, do the following:

```python
from savemetadata import png_metadata

import matplotlib as mpl

# ... plotting code goes here ...

fig.figsave("figure.png", metadata=png_metadata())
```

Your code generates the file `figure.png`. Its PNG metadata now stores your original script filename and source. This can later be extracted by using `savemetadata.extract_metadata_png("figure.png")` which returns a dict with keys `'name'` and `'contents'`.

# TODO
- Add `pdf_metadata()`
- Store the date/time (anything else?) when the script was run
- Wrap things so the user doesn't have to use `png_` or `pdf_`
- Add a CLI to extract from the figure and write new script files
- Inject into mpl's `figsave`?
- Introspect to see if this figure is generated using *multiple* python files?
