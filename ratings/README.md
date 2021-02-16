## User ratings

Load data with Python Pandas

```
import pandas as pd

df = pd.read_csv("./ca-ratings.csv.zip", compression="zip")

df.sample(5)
```

![user ratings](./pandas-ratings.png)

## See also
- Step-by-step tutorial: [How to build a climbing route recommendation engine](https://openbeta.substack.com/p/building-a-climbing-route-recommendation)
- [OpenBeta recommendation API](https://openbeta.io/api-ml)
